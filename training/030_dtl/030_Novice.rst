.. _dtl-novice-3-2:

Novice
------

.. _copy-3-2:

"Copy"
~~~~~~

Copy is one of the most fundamental DTL functions you will be using in Sesam when transforming your source data to your target. The main reason for this is that it allows you to copy source data by the use of wildcards, i.e. asterisk (*). In the below example this has been implemented in order to copy all keys with the namespace "golden-object:" in them:

``["copy", "golden-object:*"]``

In addition, ``["copy"]`` is convenient in that you can whitelist and blacklist source data by providing arguments in the ``["copy"]`` function as follows:   

``["copy", "*", "_*"]``

The first argument in the above declaration copies everything from your source to your target by the use of asterisk, whilst the second argument with the "_" prefix before the asterisk blacklists all values whose keys start with "_". For declarative purposes, this could be written as ``["copy", "<whitelist>", "<blacklist>"].`` The following example has been drafted to visually present this effect.

Data entering the pipe mssql-accounts from the system "sesam-training":

.. code-block:: json

	{
	  "country": "DK",
	  "id": 40,
	  "phone": "1-894-115-3398",
	  "_position": "Engineer"
	}

Pipe config:

.. code-block:: json

	{
	  "_id": "mssql-accounts",
	  "type": "pipe",
	  "source": {
	    "type": "sql",
	    "system": "sesam-training",
	    "table": "accounts"
	  },
	  "transform": {
	    "type": "dtl",
	    "rules": {
	      "default": [
	        ["copy", "*", "_*"]
	      ]
	    }
	  }
	}

Data produced by the pipe DTL transformation:

.. code-block:: json

	{
	  "mssql-accounts:country": "DK",
	  "mssql-accounts:id": 40,
	  "mssql-accounts:phone": "1-894-115-3398"
	}

As can be seen from the above produced data, the property with the key "_position" has been filtered by the blacklist parameter "_*" in the ``["copy"]`` function.

.. seealso::

  TODO

.. _add-3-2:

"Add"
~~~~~

Explain the add, based on ref 3.1.4 above

.. seealso::

  TODO

.. _concat-concatination-3-2:

"Concat" - Concatination
~~~~~~~~~~~~~~~~~~~~~~~~

Concatenation of strings, examples etc

.. seealso::

  TODO

.. _rdf:type-3-2:

rdf:type
~~~~~~~~

Resource Description Framework (?) explain what it means in Sesam
context

.. seealso::

  TODO

.. _namespace-3-2:

Namespace
~~~~~~~~~

Explain namespace in \_id (value) and keys.

EXAMPLESSS

.. seealso::

  TODO

.. _make-ni-3-2:

"Make-ni"
~~~~~~~~~

Declaraiton of foreign key in Sesam, explain /reference Namespace

.. seealso::

  TODO

.. _eq-equality-3-2:

"Eq" - Equality
~~~~~~~~~~~~~~~

Equality for joins [n-n]

.. seealso::

  TODO

.. _merge-as-a-source-3-2:

Merge as a Source
~~~~~~~~~~~~~~~~~

Examples, steal from PP training, show in tables vs json, everything
coming in goes out.

-  Strategy

-  Identidy - \_id etter merge

-  datasets

   15. .. rubric:: Filter as a transform
          :name: filter-as-a-transform

Explain in the context of reading from global pipes

.. seealso::

  TODO

.. _coalesce-3-2:

Coalesce
~~~~~~~~

ref 1.2.19

.. seealso::

  TODO

.. _nested-dictionaries-3-2:

Nested dictionaries
~~~~~~~~~~~~~~~~~~~

As you can see in *Example 3.2.17A: Dotted Notation*, we can get
attributes inside dictionaries by using "."

Dotted notation

list of dicts can give you list of values from a single key.

A: [{"foo":1},{"foo":2}] -> \_S.A.foo = [1,2]

1. ["add", "some-nested-attribute",
   "_S.somedict.some-nested-attribute"] 

*Example 3.2.17A: Dotted Notation*,

.. seealso::

  TODO

.. _apply-custom-functions-3-2:

Apply - Custom Functions
~~~~~~~~~~~~~~~~~~~~~~~~

Basic, bare bruk på data fra \_S, forklar det uten å bruke hops

.. seealso::

  TODO

.. _merge-as-a-function-3-2:

Merge as a function
~~~~~~~~~~~~~~~~~~~

Source type Merge VS Transformation Merge

Merging dictionaries up to the root level of entities.

.. seealso::

  TODO

.. _hops-3-2:

Hops
~~~~

.. sidebar:: Summary

  Hops...

  - can be used to perform joins across two or more namespaces
  - allows you to enrich your data beyond what is readily available from the source you are working on


Hops can be used to perform joins across two or more namespaces. In essence, hops allows you to enrich your data beyond what is readily available from the source you are working on. To exemplify, the below example shows how data from ``"salesforce-person"`` and ``"erp-company``"" are joined:

Data from ``"salesforce-person``:

.. code-block:: json

	{
	  "salesforce-person:_id": 40,
	  "salesforce-person:country": "DK",
	  "salesforce-person:id": 40,
	  "salesforce-person:age": 32,
	  "salesforce-person:departmentID": 3
	}

Data from ``"erp-company``:

.. code-block:: json

	{
		"erp-company:_id": 3,
	  "erp-company:department": 3,
	  "erp-company:position": "Engineer",
	  "erp-company:positionStatus": "On leave",
	  "erp-company:departmentManager": "Danmark Tordenskjold"
	}

Pipe configuration:

.. code-block:: json

	{
	  "_id": "salesforce-erp-preparation",
	  "type": "pipe",
	  "source": {
	    "type": "dataset",
	    "dataset": "global-person"
	  },
	  "transform": {
	    "type": "dtl",
	    "rules": {
	      "default": [
	        ["copy",
	          ["list", "salesforce-person:country", "salesforce-person:id", "salesforce-person:departmentID"]
	        ],
	        ["if",
          	["eq", "_S.departmentID", null],
          	["filter"]
        	],
	        ["merge",
	          ["hops", {
	            "datasets": ["erp-company ec"],
	            "where": [
	              ["eq", "_S.salesforce-person:departmentID", "ec.department"]
	            ]
	          }]
	        ],
	        ["remove", ["list", "departmentID", "department"]]
	      ]
	    }
	  }
	}

As can be seen from the above pipe configuration ``"salesforce-erp-preparation"``, the ``["merge"]`` function is used to wrap the result from the ``["hops"]`` function. In the ``["hops"]`` function you can see how two namespaces are joined in the ``["eq"]`` statement, namely ``"salesforce-person"``and the abbreviated form ``"ec"``. When this pipe completes its run, the following output will be produced: 

.. code-block:: json

	{
	  "salesforce-person:_id": 40,
	  "salesforce-person:country": "DK",
	  "salesforce-person:id": 40,
	  "erp-company:position": "Engineer",
	  "erp-company:positionStatus": "On leave",
	  "erp-company:departmentManager": "Danmark Tordenskjold"
	}

From the above output you should now recognize how ``["hops"]`` can be used to enrich your data beyond what is readily available from its source.

.. seealso::

  :ref:`developer-guide` > :ref:`DTLReferenceGuide` > :ref:`path_expressions_and_hops`

.. _underline-properties-3-2:

\_ Properties
~~~~~~~~~~~~~

(_deleted, filtered, \_id, \_previous, \_updated, *\_hash? REF 1.2.24*)

.. seealso::

  TODO

.. _type-examples-3-2:

Type examples
~~~~~~~~~~~~~

Type eksempler:

• Datettime

• Dict {}

• List

○ First

○ Unique/Distinct

○ Last

○ Count

○ nth

• String

• Integer

• Decimal

• Float

• Boolean

○ And

○ Or

○ Not

○ In

○ Eq

○ If-null

○ Is-empty

.. seealso::

  TODO

.. _tasks-for-dtl-novice-3-2:

Tasks for DTL: Novice
~~~~~~~~~~~~~~~~~~~~~
