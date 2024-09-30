Connector asymmetry
===================

Some endpoints are asymmetric, e.g. the data model exposed in collect pipeline might differ from the data model required in share pipes. Or the system might expose a datatype for collect, but actually requires that datatype to be updated through an other datatype's API. This asymmetry should be managed by the connector such that data coming out of collect pipeline is symmetric with the data coming into the share pipes. Both of these scenarios, with some variantion will be covered in this section. 

Data model asymmetry
--------------------

In the case of a data model asymmetry, i.e. the system exposes one data model for GET requests but an other for POST requests, the solution is relatively straight foreward. It's recommended to adapt the share model to match the collect model as one can then start building the collect part of a connector first and start using that without breaking backwards compatibility.

HTTP method asymmetry
---------------------

HTTP method asymmetry covers cases where a datatype is exposed by its own API in either GET or POST requests, but not both. There are different variations of this scenario as described below:

GET for datatype A but POST for datatype B
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This often occurs when datatype A is actually a part of datatype B in some way. It could be an association (HubSpot) or an invoice line connected to an invoice (Wave).
If possible the easiest solution for these cases is to have the POST requests for datatype A use the URL for datatype B, but still use datatype A specific system operation. Often however you require datatype B to be present in the payload. In many cases that means that datatype A is actually present in the GET request for datatype B, even though datatype A also has its own GET API. If so, regarding themas the same datatype in the connector might be the best solution, and let the enrich pipes split them up in individual datatypes if required.

GET and update (POST/PATCH/PUT) for datatype A but INSERT for datatype B
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This might also occur when datatype B in some way depends on datatype A, often through a required relationship. In these cases we need to view the datatypes as separate, but add an additional share pipe to the datatype B flow which only deals with inserts of datatype A. This logic should either be managed in the share pipe before the share template, or in an additional ``-preshare`` pipe before the share pipe. Datatype B's share pipe will also require it's insert capabilities removed as this is now managed by datatype A. In addition the colelct template for datatype B will now have to look for *$generated_id* in datatype A's share dataset.

Datatype dependencies
^^^^^^^^^^^^^^^^^^^^^

Every system have a different way of structuring their data model, and some times they do not scale well with your central model. E.g. they might have split up datatypes in hierarchies which makes sence for that specific system, but not for any other system. Even though these hierarchies have no real interest to your central model they might be required in order to correctly share this datatype back to the system. In this case you might also have to introduce multiple share pipes for your datatype in order to create the correct hierarcial structure in the target system.  

Hops required asymmetry
-----------------------

When required connector pipes may perform hops to other connector datasets to achieve symmetry or to satisfy required data dependencies, but not to datasets outside the connector. This should however be performed with caution as you might introduce loops or additional dependencies. An example of this might be if the API does not expose relationships through the GET request (but rather implicitly through the rewuest URL. We can introduce these in the connector by performing hops to the required collect pipe. 


