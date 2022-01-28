=========
Transform
=========

Schema
------
Sesam supports any data schema and transforms the data from the global datasets into the target schema before offering it to the target system.
Inbound from sources and within Sesam, Sesam operates schemaless. 
Sesam does not offer automatic schema validation nor business rules validation. Such validation has to be developed outside Sesam. 

Data format
-----------
Sesam has native connectors to transform its internal JSON format into the most common data formats, like XML, JSON, SQL, CSV, Excel etc. Any format not supported can be delivered using the push mechanism through a microservice. Sesam has a library of microservices (connectors), but in some cases a new microservice has to be developed if Sesam needs to connect to an unfamiliar or special system. This can be necessary because of special data format or security requirements of the targets (and even sources).