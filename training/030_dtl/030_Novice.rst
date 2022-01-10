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

.. _coalesce-3-2:

"Coalesce"
~~~~~~~~~~

.. sidebar:: Summary

  "Coalesce"...

  - is one of Sesam's core Master Data Management (MDM) capabilities
  - lets you define a list of prioritized properties

Coalesce is one of Sesam's core Master Data Management (MDM) capabilities. ``["coalesce"]`` lets you define a list of prioritized properties that will be evaluated so that you can make sure the first property that does not return ``null`` becomes the value of the property you are working on. An example has been drafted below to exemplify the use of ``["coalesce"]``.

Source data:

.. code-block:: json

  {
    "mssql-person:Email": "christian89@hotmail.com",
    "mssql-person:Postcode": "6400",
    "mssql-person:Address": "Rojumvej 66"
  }

  {
    "oracle-person:EmailAddress": "hansMajestæt@gmail.com",
    "oracle-person:PostNumber": 6400,
    "oracle-person:Address": "Rojumvej 66"
  }

  {
    "pymsql-person:Postaddress": "hansMajestæt@gmail.com",
    "pymsql-person:AreaCode": "6851",
    "pymsql-person:Address": "Danmarksgate 7"
  }

Pipe configuration:

.. code-block:: json

  {
    "_id": "global-person",
    "type": "pipe",
    "source": {
      "type": "merge",
      "datasets": ["mssql-person pip1", "pymsql-person pip2", "oracle-person pip3"],
      "equality_sets": [
        ["pip1.Email", "pip2.Postaddress", "pip3.EmailAddress"]
      ],
      "identity": "first",
      "strategy": "default",
      "version": 2
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*"],
          ["comment", "*** Adding global properties ***"],
          ["add", "Email", ["coalesce", ["list", "_S.mssql-person:Email", "_S.pymsql-person:Postaddress", "_S.oracle-person:EmailAddress", "No Email provided"]]],
          ["add", "PostCode", ["coalesce", ["list", "_S.pymsql-person:AreaCode", "_S.oracle-person:PostNumber", "_S.mssql-person:Postcode", "No PostCode provided"]]],
          ["add", "PrivateAddress", ["coalesce", ["list", "_S.pymsql-person:Address", "_S.oracle-person:Address", "_S.mssql-person:Address", "No PrivateAddress provided"]]]
        ]
      }
    },
    "metadata": {
      "global": true,
      "tags": "person"
    }
  }

When the above pipe runs, the following output will be produced:

.. code-block:: json

	{
	  "mssql-person:Email": "christian89@hotmail.com",
	  "mssql-person:Postcode": "6400",
	  "mssql-person:Address": "Rojumvej 66",
	  "oracle-person:EmailAddress": "hansMajestæt@gmail.com",
	  "oracle-person:PostNumber": 6400,
	  "oracle-person:Address": "Rojumvej 66",
	  "pymsql-person:Postaddress": "hansMajestæt@gmail.com",
	  "pymsql-person:AreaCode": "6851",
	  "pymsql-person:Address": "Danmarksgate 7",
	  "global-person:Email": "christian89@hotmail.com",
	  "global-person:PostCode": "6851",
	  "global-person:PrivateAddress": "Danmarksgate 7"
	}

As can be seen from the above dataset, you should recognize the properties with the namespace "global-person", as these properties are our added global properties in the above pipe configuration. This example is in practice Sesam's core MDM transform capability. 

.. seealso::

  :ref:`concepts` > :ref:`concepts-features` > :ref:`concepts-namespaces`

  :ref:`concepts` > :ref:`concepts-features` > :ref:`concepts-global-datasets`

  :ref:`concepts` > :ref:`concepts-features` > :ref:`concepts-merging`

  :ref:`developer-guide` > :ref:`configuration` > :ref:`pipe_section` > :ref:`namespaces`

  :ref:`developer-guide` > :ref:`DTLReferenceGuide` > :ref:`dtl-transforms`

  :ref:`developer-guide` > :ref:`DTLReferenceGuide` > :ref:`expression_language` > :ref:`namespaced-identifiers`

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

.. _concat-concatination-3-2:

"Concat" - concatenation
~~~~~~~~~~~~~~~~~~~~~~~~

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

Basics, uten apply

.. seealso::

  TODO

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
