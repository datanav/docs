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

.. sidebar:: Summary

  Merge...

  - as a source will join multiple datasets
  - in Sesam can be compared to a full outer join in a database
  - should use the properties ``version``, ``strategy`` and ``identity`` to work effectively
  - as a source is typically used in global pipes

Using merge as a source will join multiple datasets. Merging in Sesam can be compared to a full outer join in a database. In practice this means that everything that originates from each dataset being merged, will be retained in the merged entity representation. 

For merging to work effectively, the properties ``version``, ``strategy`` and ``identity`` should be used.

- ``version`` - can be set to either ``1`` or ``2``. Use ``2`` to ensure the merge source is up to date.

- ``strategy`` - can be set to either ``"defalt"`` or ``"compact"``. 

- ``identity`` - can be set to either ``"first"`` or ``"composite"``.

Merging is typically done in global pipes and in the following example, this is also your point of reference.

.. code-block:: json

	{
	  "_id": "global-person",
	  "type": "pipe",
	  "source": {
	    "type": "merge",
	    "datasets": ["salesforce-person pip1", "salesforce-contacts pip2", "salesforce-accounts pip3"],
	    "equality": [
	      ["eq", "pip2.phone", "pip3.phone"]
	    ],
	    "identity": "first",
	    "strategy": "default",
	    "version": 2
	  },
	  "metadata": {
	    "global": true,
	    "tags": ["person"]
	  }
	}

As can be seen from the above pipe configuration ``"global-person"`` you will recognize the aformentioned properties. ``version`` being set to ``2``, ``strategy`` to ``"default"`` and ``identity`` to ``"first"``.

The ``strategy`` property changes how the resulting entities look as these are merged in the ``equality`` property. In this particular example we are merging on the property ``phone`` for the namespaces ``"salesforce-contacts"`` and ``"salesforce-accounts"`` and the ``["eq"]`` function is now used as a join expression. As namespaces are being merged, the ``"default"`` value in the ``strategy`` property unions all the values and duplicates are not removed. In comparison, if the ``"compact"`` value is used, the pipe will try to compact property values, i.e: duplicate values are removed and empty lists are removed.

With regards to the ``identity`` property, this property determines how the ``_id`` will look, as entities are merged in your merge source. If the ``identity`` property is set to ``"first"`` the ``_id`` will be picked from the first dataset in the datasets list involved in the merge. As an example see the below, which shows the shape of an entity having been run through the above shown pipe configuration in ``"global-person"``:

.. code-block:: json

	{
    "$ids": [
      "~:salesforce-contacts:40",
      "~:salesforce-accounts:40"
    ],
    "_id": "salesforce-contacts:40",
    "_updated": 239,
    "salesforce-accounts:country": "DK",
    "salesforce-accounts:id": 40,
    "salesforce-accounts:phone": "1-894-115-3398",
    "salesforce-accounts:phone-ni": "~:salesforce-contacts:1-894-115-3398",
    "salesforce-accounts:position": "CTO",
    "salesforce-contacts:id": 40,
    "salesforce-contacts:name": "Bolton, Aladdin T.",
    "salesforce-contacts:phone": "1-894-115-3398",
    "rdf:type": [
      "~:salesforce:Contact",
      "~:salesforce:Account"
    ]
  }

As you can see from the above merged result, the ``_id`` turned out as ``"salesforce-contacts:40"`` as this is the entity that is placed at index null in the ``$ids`` array, which tells us which namespaces got merged based on our defined equality rules. If you were to change the ``identity`` to ``"composite"`` the ``_id`` would have turned out as ``"1|salesforce-contacts:40|2|salesforce-accounts:40"``.

.. seealso::

	:ref:`developer-guide` > :ref:`configuration` > :ref:`source_section` > :ref:`merge_source`

  :ref:`concepts` > :ref:`concepts-features` > :ref:`concepts-merging`

  :ref:`concepts` > :ref:`concepts-features` > :ref:`concepts-namespaces`

  :ref:`concepts` > :ref:`concepts-features` > :ref:`concepts-global-datasets`

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
