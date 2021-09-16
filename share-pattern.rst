Sharing data 
============	
The main purpose of a Sesam is its ability to share data by delivering data in the form that each target system needs. Instead of changing the system to adjust to data. Sesam utilize their own language.

The core principle of Sesam data management is that any target systems needing data, will sync their designated optimized data store.

Transport
---------
Sesam supports both push and publish mechanisms. Push is having the advantage of making it possible for Data Managers to control the flow and know the state of the target system. Publish has an advantage that gives the target system control over their data flow, but a limited support for data formats, JSON, CSV, XML, RDF, SD-SHARE, and only supports HTTPS.
Sesam does not support ad hoc querying on published data but has a limited support pre-defined query properties or data subsets.

Schema
------
Sesam supports any data schema and transforms the data from the global datasets into the target schema before offering it to the target system. 

Data format
-----------
Sesam has native connectors to transform its internal JSON format into the most common data formats. Like XML, JSON, SQL, CSV, Excel etc. Any format not supported can be delivered using push through a microservice.

Identifiers
-----------
When sending data to a target system, a main challenge is using the right identifiers for the object you update, and for any references from that object to other objects in the same target system.
The correct ID for the necessary objects is available in the global datasets, and by hoping to them in the outgoing flow, the correct identifiers can be populated.

Completeness
-----------
To ensure that any composed object is complete before sending it to a target system. The completeness features delay the transfer of incomplete objects.

Feedback loop
-------------
In API based systems the result of the insert or update call should feed back into the target input flow, to handle Ids and errors.

