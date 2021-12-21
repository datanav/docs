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

Basics, uten apply

.. seealso::

  TODO

.. _underline-properties-3-2:

\_ Properties
~~~~~~~~~~~~~

.. sidebar:: Summary

  ``"_"`` Properties...

  - in Sesam are categorized as `reserved fields <https://docs.sesam.io/entitymodel.html#reserved-fields>`_
  - provide different functionality for Sesam with regards to how entities are treated

``_`` properties in Sesam are categorized as `reserved fields <https://docs.sesam.io/entitymodel.html#reserved-fields>`_. These fields provide different functionality for Sesam with regards to how entities are treated, as these move through a Sesam dataflow. Only the ``"_id"`` and ``"_deleted"``, will be ignored when writing an entity to a dataset. Additionally, these fields are *only* reserved at the root level, so nested entities can have them.

Below, a complete list of these fields is provided:

 - ``"_deleted"`` - if ``true`` the entity is treated as deleted
 - ``"_filtered"`` - if ``true`` the entity is filtered
 - ``"_hash"`` -  determines if an entity has changed over time and enables `change tracking <https://docs.sesam.io/concepts.html#change-tracking>`_
 - ``"_id"`` - a string value that is the identity of the entity
 - ``"_previous"`` - the previous version of the latest ``"_updated"`` value
 - ``"_tracked"`` - if ``true``, the entity was added by `dependency tracking <https://docs.sesam.io/concepts.html#dependency-tracking>`_
 - ``"_ts"`` - a real-world timestamp for when the entity was added to the dataset
 - ``"_updated"`` - determines when the entity was modified and the value must either be a string or an integer value

In general, reserved fields are used in order to make Sesam perform as intended and so they will largely affect the performance of a Sesam node without you even knowing. Albeit, you will immediately get to know ``"_deleted"``, ``"_filtered"`` and ``"_id"`` when creating dataflows in Sesam. An entity cannot exist without an ``"_id"``, so it is a given that you will get acquainted with that field immediately. With regards to the ``"_filtered"`` field this allows for you to evaluate and modify whether your DTL logic should transform specific states of an entity and will in general become more apparent as data moves towards exposure in a Sesam dataflow. Finally, the ``"_deleted"`` field is usually used as a filter in your endpoint pipes, as you have to ensure that no deleted entities are exposed to the outside world.

To show how this could look like in a pipe configuration, the following example has been drafted:

.. code-block:: json

	{
	  "_id": "transform-salesforce-person",
	  "type": "pipe",
	  "source": {
	    "type": "dataset",
	    "dataset": "global-person"
	  },
	  "transform": {
	    "type": "dtl",
	    "rules": {
	      "default": [
	        ["if",
	          ["eq", "_S.position", "Employee"],
	          ["copy", "*"],
	          ["filter"]
	        ]
	      ]
	    }
	  }
	}

As this pipe runs, entities will be filtered if they do not have a ``"position"`` of ``"Employee"`` and so the ``"_filtered"`` field will be ``true``. This exemplifies how you can utilize the ``"_filtered"`` field to make sure your DTL logic behaves as intended.      

.. seealso::

	:ref:`developer-guide` > :ref:`DTLReferenceGuide` > :ref:`dtl-transforms`

	:ref:`developer-guide` > :ref:`entity_data_model` > :ref:`reserved-fields`

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
