#!/usr/bin/env python3.8

import argparse
import ast
from datetime import datetime
import threading
import time

import pyarrow
import pyarrow.flight

import pyarrow as pa


class FlightServer(pyarrow.flight.FlightServerBase):
    def __init__(
        self,
        host='localhost',
        location=None,
        tls_certificates=None,
        verify_client=False,
        root_certificates=None,
        auth_handler=None
    ):
        super(FlightServer, self).__init__(
            location,
            auth_handler, 
            tls_certificates,
            verify_client,
            root_certificates
        )

        self.flights = {}
        self.host = host
        self.tls_certificates = tls_certificates

    @classmethod
    def descriptor_to_key(self, descriptor):
        return (
            descriptor.descriptor_type.value,
            descriptor.command,
            tuple(descriptor.path or tuple())
        )

    def _make_flight_info(self, key, descriptor, table):
        if self.tls_certificates:
            location = pyarrow.flight.Location.for_grpc_tls(
                self.host,
                self.port
            )
        else:
            location = pyarrow.flight.Location.for_grpc_tcp(
                self.host,
                self.port
            )

        endpoints = [
            pyarrow.flight.FlightEndpoint(
                repr(key),
                [location]
            )
        ]

        mock_sink = pyarrow.MockOutputStream()

        stream_writer = pyarrow.RecordBatchStreamWriter(
            mock_sink,
            table.schema
        )

        stream_writer.write_table(table)
        stream_writer.close()
        data_size = mock_sink.size()

        return pyarrow.flight.FlightInfo(
            table.schema,
            descriptor,
            endpoints,
            table.num_rows,
            data_size
        )

    def list_flights(self, context, criteria):
        for key, table in self.flights.items():
            if key[1] is not None:
                descriptor = \
                    pyarrow.flight.FlightDescriptor.for_command(key[1])
            else:
                descriptor = pyarrow.flight.FlightDescriptor.for_path(*key[2])

            yield self._make_flight_info(key, descriptor, table)

    def get_flight_info(self, context, descriptor):
        key = FlightServer.descriptor_to_key(descriptor)

        if key in self.flights:
            table = self.flights[key]
            return self._make_flight_info(key, descriptor, table)
        raise KeyError('Flight not found.')

    def do_put(self, context, descriptor, reader, writer):
        print(descriptor.path[0].decode('utf-8'))

        key = FlightServer.descriptor_to_key(descriptor)
        self.flights[key] = reader.read_all()

    def do_get(self, context, ticket):
        key = ast.literal_eval(ticket.ticket.decode())

        if key not in self.flights:
            return None

        return pyarrow.flight.RecordBatchStream(self.flights[key])

    def do_action(self, context, action):
        if action.type == 'healthcheck':
            pass
        else:
            raise KeyError('Unknown action {!r}'.format(action.type))

    def _shutdown(self):
        '''Shut down after a delay.'''

        print('Server is shutting down...')

        time.sleep(2)
        self.shutdown()


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--host',
        type=str,
        default='localhost',
        help='Address or hostname to listen on'
    )

    parser.add_argument(
        '--port',
        type=int,
        default=5005,
        help='Port number to listen on'
    )

    parser.add_argument(
        '--tls',
        nargs=2,
        default=None,
        metavar=('CERTFILE', 'KEYFILE'),
        help='Enable transport-level security'
    )

    parser.add_argument(
        '--verify_client',
        type=bool,
        default=False,
        help='enable mutual TLS and verify the client if True'
    )

    args = parser.parse_args()

    tls_certificates = []
    scheme = 'grpc+tcp'

    if args.tls:
        scheme = 'grpc+tls'

        with open(args.tls[0], 'rb') as cert_file:
            tls_cert_chain = cert_file.read()

        with open(args.tls[1], 'rb') as key_file:
            tls_private_key = key_file.read()

        tls_certificates.append((tls_cert_chain, tls_private_key))

    location = '{}://{}:{}'.format(scheme, args.host, args.port)

    server = FlightServer(
        args.host,
        location,
        tls_certificates=tls_certificates,
        verify_client=args.verify_client
    )

    print('Serving on', location)

    try:
        server.serve()
    except (KeyboardInterrupt, SystemExit):
        print('\n')

        # Shut down on background thread
        # to avoid blocking current request:
        threading.Thread(target=server._shutdown).start()


if __name__ == '__main__':
    main()
