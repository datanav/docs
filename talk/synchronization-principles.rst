.. _synchronization_principles:

==========================
Synchronization principles
==========================

Definitions
-----------

- ``Merge``: When two entities merge together to form one entity.
- ``Update``: When an entity in a merged set changes.
- ``Priority``: Used to define the sorting order in a conflict.
- ``Reference``: A link between entities in a system.
- ``Single value``: The data model defines that a field can hold one value.
	- Example: "Given name" (P735):

	  .. code-block:: json

	  	{
	  		"p:P735": "Alan"
	  	}
- ``Value set``: The data model defines that a field can hold a single set of multiple values.
	- Example: "Street address" (P6375):

		.. code-block:: json

			{
				"p:P6375": [
					{
						"ps:P6375": "Streetaddress 1",
						"ps:P8307": 0
					},
					{
						"ps:P6375": "Streetaddress 2",
						"ps:P8307": 1
					}
				]
			}

- ``Multi value``: The data model defines that a field can hold multiple values.
	- Example: "Participant" (P710):

		.. code-block:: json

			{
				"p:P710": [
					{
						"p:P735": "Alan",
						"p:P734": "Smithee"
					},
					{
						"p:P735": "John",
						"p:P734": "Doe"
					}
				]
			}
