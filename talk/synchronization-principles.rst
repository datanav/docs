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

General rule of data synchronization
------------------------------------

Data should never be of lesser quality after synchronization.

Merge: Single value + set. Conflict: Different time
---------------------------------------------------

.. list-table::
   :widths: 150, 30, 150

   * - Start

       .. code-block:: text
       		:dedent:

		    Entity A
		    P = 100
		    A.X = M.Z
		    X = "V1"
		    T = 1

		    Entity B
		    P = 10
		    B.Y = M.Z
		    Y = "V2"
		    T = 2

     -
     - Target

       .. code-block:: text
       		:emphasize-lines: 4,5
       		:dedent:

		    Entity A
		    P = 100
		    A.X = M.Z
		    X = "V2"
		    T = 3
		                                    
		    Entity B
		    P = 10
		    B.Y = M.Z
		    X = "V2"
		    T = 2

Merge: Single value + set. Conflict: Same time priority
-------------------------------------------------------

.. list-table::
   :widths: 150, 30, 150

   * - Start

       .. code-block:: text
       		:dedent:

		    Entity A
		    P = 100
		    A.X = M.Z
		    X = "V1"
		    T = 1

		    Entity B
		    P = 10
		    B.Y = M.Z
		    Y = "V2"
		    T = 2

     -
     - Target

       .. code-block:: text
       		:emphasize-lines: 10,11
       		:dedent:

		    Entity A
		    P = 100
		    A.X = M.Z
		    X = "V1"
		    T = 1
		                                    
		    Entity B
		    P = 10
		    B.Y = M.Z
		    Y = "V1"
		    T = 2

Merge: Single value + set. Empty property
-----------------------------------------

.. list-table::
   :widths: 150, 30, 150

   * - Start

       .. code-block:: text
       		:dedent:

		    Entity A
		    P = 100
		    A.X = M.Z
		    X = ""
		    T = 1

		    Entity B
		    P = 10
		    B.Y = M.Z
		    Y = "V2"
		    T = 2

     -
     - Target

       .. code-block:: text
       		:emphasize-lines: 4,5
       		:dedent:

		    Entity A
		    P = 100
		    A.X = M.Z
		    X = "V2"
		    T = 2
		                                    
		    Entity B
		    P = 10
		    B.Y = M.Z
		    Y = "V2"
		    T = 1

Update: Single value + set
--------------------------

.. list-table::
   :widths: 150, 30, 150

   * - Start

       .. code-block:: text
       		:emphasize-lines: 9
       		:dedent:

		    Entity A
		    P = 100
		    A.X = M.Z
		    X = ""
		    T = 1

		    Entity B
		    P = 10
		    B.Y = M.Z
		    Y = "V2" -> ""
		    T = 2

     -
     - Target

       .. code-block:: text
       		:emphasize-lines: 4,5
       		:dedent:

		    Entity A
		    P = 100
		    A.X = M.Z
		    X = ""
		    T = 3
		                                    
		    Entity B
		    P = 10
		    B.Y = M.Z
		    Y = ""
		    T = 2

Merge: Multi value. Conflict
----------------------------

.. list-table::
   :widths: 150, 30, 150

   * - Start

       .. code-block:: text
       		:dedent:

		    Entity A
		    P = 100
		    A.X = M.Z
		    X = "V1"
		    T = 1

		    Entity B
		    P = 10
		    B.Y = M.Z
		    Y = "V2"
		    T = 2

     -
     - Target

       .. code-block:: text
       		:emphasize-lines: 4
       		:dedent:

		    Entity A
		    P = 100
		    A.X = M.Z
		    X = { "V1", "V2" }
		    T = 1
		                                    
		    Entity B
		    P = 10
		    B.Y = M.Z
		    Y = "V2"
		    T = 2

Merge: Multi value. Empty property
----------------------------------

.. list-table::
   :widths: 150, 30, 150

   * - Start

       .. code-block:: text
       		:dedent:

		    Entity A
		    P = 100
		    A.X = M.Z
		    X = ""
		    T = 1

		    Entity B
		    P = 10
		    B.Y = M.Z
		    Y = "V2"
		    T = 2

     -
     - Target

       .. code-block:: text
       		:emphasize-lines: 4,5
       		:dedent:

		    Entity A
		    P = 100
		    A.X = M.Z
		    X = "V2"
		    T = 2
		                                    
		    Entity B
		    P = 10
		    B.Y = M.Z
		    Y = "V2"
		    T = 1

Update: Multi value
-------------------

.. list-table::
   :widths: 150, 30, 150

   * - Start

       .. code-block:: text
       		:emphasize-lines: 10
       		:dedent:

		    Entity A
		    P = 100
		    A.X = M.Z
		    X = "V2"
		    T = 1

		    Entity B
		    P = 10
		    B.Y = M.Z
		    Y = "V2" -> ""
		    T = 2

     -
     - Target

       .. code-block:: text
       		:emphasize-lines: 4,5
       		:dedent:

		    Entity A
		    P = 100
		    A.X = M.Z
		    X = ""
		    T = 3
		                                    
		    Entity B
		    P = 10
		    B.Y = M.Z
		    Y = ""
		    T = 2

References. Merge: Single value + set. Conflict: Different time
---------------------------------------------------------------

.. list-table::
   :widths: 150, 10, 150, 30, 150, 10, 150

   * - Start

       .. code-block:: text
       		:emphasize-lines: 10
       		:dedent:
       		:class: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2 custom-card

		    Entity A
		    P = 100
		    A.X = M.Z
		    X = "V2"
		    T = 1

		    Entity B
		    P = 10
		    B.Y = M.Z
		    Y = "V2" -> ""
		    T = 2

	 -
	 -

       .. code-block:: text
       		:emphasize-lines: 10
       		:dedent:

		    Entity A
		    P = 100
		    A.X = M.Z
		    X = "V2"
		    T = 1

		    Entity B
		    P = 10
		    B.Y = M.Z
		    Y = "V2" -> ""
		    T = 2

     -
     - Target

       .. code-block:: text
       		:emphasize-lines: 4,5
       		:dedent:

		    Entity A
		    P = 100
		    A.X = M.Z
		    X = ""
		    T = 3
		                                    
		    Entity B
		    P = 10
		    B.Y = M.Z
		    Y = ""
		    T = 2

     -
     -

        .. code-block:: text
       		:emphasize-lines: 4,5
       		:dedent:

		    Entity A
		    P = 100
		    A.X = M.Z
		    X = ""
		    T = 3
		                                    
		    Entity B
		    P = 10
		    B.Y = M.Z
		    Y = ""
		    T = 2
