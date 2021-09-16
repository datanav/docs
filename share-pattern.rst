Sharing data 
============	
The main purpose of a Sesam is its ability to share data by delivering data in the form that each target system needs.

Transport
---------
Sesam supports both push and pull mechanisms. Push is prefered as it makes it possible for Data Managers to controll the flow and know the status of the target system.

Schema
------
Sesam supports any data schema, and transforms the data from the global datasets into the target schema before offering it to the target schema. 

Data format
-----------
Sesam has native connectors to transform its internal Json format into the most common data formats. Like XML, Jsn, SQL, CSV, Excel etc. Any format not supported can be buildt with a microservice.

Identifiers
-----------
When sending data to a terget system, a main challinge is using the right identifiers for the object you update, and for any refferences from that object to other objects in the same target system.
The corect ID for the nessessary objects are available in the global datasets, and by hoping to them in the outgoing flow, the correct identifiers can be poppulated.

Completenes
-----------
To ensure that any composed object is complete before sending it to a terget system. The completenes features dalays the trensfer of incpmpleate objects.

Feedback loop
-------------
In API based systems the result of the insert or update call scuold feed back into the target input flow, to handle Ids and errors.