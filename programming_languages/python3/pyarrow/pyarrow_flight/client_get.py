#!/usr/bin/env python3

import pyarrow        as pa
import pyarrow.flight as fl

arrow_flight_client = fl.connect('grpc://localhost:5005')

arrow_flight_descriptor = pa.flight.FlightDescriptor.for_path('some/path')

arrow_flight_info = \
    arrow_flight_client.get_flight_info(arrow_flight_descriptor)

arrow_flight_reader = arrow_flight_client.do_get(
    arrow_flight_info.endpoints[0].ticket
)

input_dataframe = arrow_flight_reader.read_pandas()
