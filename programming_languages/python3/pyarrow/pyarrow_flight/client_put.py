#!/usr/bin/env python3

import pyarrow.flight as fl
import pyarrow        as pa

pyarrow_schema = pa.Schema.from_pandas(pandas_dataframe)

pyarrow_table = pa.Table.from_pandas(
    pandas_dataframe,
    schema=pyarrow_schema,
    preserve_index=False
)

arrow_flight_client = fl.connect('grpc://localhost:5005')

try:
    upload_descriptor = pa.flight.FlightDescriptor.for_path('some/path')

    writer, _ = arrow_flight_client.do_put(
        upload_descriptor,
        pyarrow_table.schema
    )

    writer.write_table(pyarrow_table)
    writer.close()
except pa._flight.FlightUnavailableError:
    pass
