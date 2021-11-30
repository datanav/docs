============
Sharing data 
============

The main benefit of Sesam is its ability to share data by delivering it in the form that each target system asks for. Instead of changing the systems to fit the data, Sesam speaks the target's language.

The core principle of data management with Sesam is to bring data to any target systems in need. The targets will use their optimized data storage to store the new data.

Transport
---------
Sesam supports both push and publish mechanisms. Push has the advantage of making it possible for Data Managers to control the flow and know the state of the target system. Publish has an advantage that gives the target system control over their dataflow, but supports a limited array of data formats, such as JSON, CSV, XML, RDF, SD-SHARE and only supports HTTPS.
Sesam does not support ad hoc querying on published data. Sesam has a limited support for pre-defined query properties or data subsets.

Identifiers
-----------
When sending data to a target system, the main challenge is using the right identifiers for the object you update, and also the right identifiers for any references from that object to other objects in the same target system.
The correct ID for the necessary objects is available in the global datasets, and by hopping to them in the outgoing flow, the correct identifiers can be populated.

Completeness
------------
To ensure that any composed object is complete before sending it to a target system, the completeness feature(if set) will delay the transfer of incomplete objects to targets. If the completeness feature is not set, incomplete objects will be sent to targets. 

Generated identifiers
---------------------
In API-based systems the result of the insert or update call should feed back into the target input flow, to handle IDs and errors.

