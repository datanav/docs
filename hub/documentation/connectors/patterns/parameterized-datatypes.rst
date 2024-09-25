Parameterized datatypes
=======================

Some datatypes are driven by other datatypes. E.g. fetching ``orderlines`` for each ``order``. If this is the case, then ``orderlines`` are parameterized by ``orders``. This should be represented as two datatypes. It is up the client of the connector to decide if they want to synchronise one or both of the data types.
