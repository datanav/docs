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

.. sidebar:: Summary

  Apply...

  - is an `expression language function <https://docs.sesam.io/DTLReferenceGuide.html?#expression-language>`_
  - is categorized as a `nested transformation function <https://docs.sesam.io/DTLReferenceGuide.html?#nested-transformations>`_
  - is suitable for transforming nested data structures

The ``["apply"]`` is an expression language function.
An expression language function has no side-effects and returns a single value or a list of values.
The ``["apply"]`` is categorized as a nested transformation and can be used to transform nested elements.

To exemplify, the following example is used:

Source dataset:

.. code-block:: json

  {
    "My_list": [
      {
        "sensor_id": 1,
        "temp": "50 degrees"
      },
      {
        "sensor_id": 2
      }
    ],
    "id": 1
  }

Pipe transform statement:

.. code-block:: json

  "transform": {
    "type": "dtl",
    "rules": {
      "default": [
        ["copy", "*"],
        ["add", "rdf:type",
          ["ni", "arcgis-grid-measure", "grid-measure"]
        ],
        ["merge",
          ["apply", "custom_function", "_S.My_list"]
        ]
      ],
      "custom_function": [
        ["add", "lastSensorID", "_S.sensor_id"],
        ["if",
          ["neq", "_S.temp", null],
          ["add", "newTemperature", "_S.temp"]
        ]
      ]
    }
  }

Output:

.. code-block:: json

  {
    "_id": "arcgis-grid-measure:1",
    "arcgis-grid-measure:id": 1,
    "arcgis-grid-measure:newTemperature": "50 degrees",
    "arcgis-grid-measure:lastSensorID": 2
  }

Starting from the top, the source dataset ``"My_list"`` is a list with nested dictionaries. Such a data object is an ideal candidate for use in a nested transformation, such as an ``["apply"]`` function, shown in the "Pipe transform statement". As you should recognize, the ``["apply"]`` is used to access the nested elements in the source property ``"My_list"``. In addition, the function called ``"custom_function"`` is referenced and then applied when the ``["apply"]`` funcion evaluates. In order for the result to become part of the dataset, you will need to also merge the result to the default rule, which is why we need the ``["merge"]`` wrapper.

Going into detail with respect to what happens in our ``"custom_function"``, you could state, that applying it is like using a for loop, in a programming language, to send in entries from a list to a function. As such, our ``"custom_function"`` will be called for each index in the list that we pass onto it. This is also why ``"lastSensorID"`` evaluates to ``2``, since the last entry we pass onto it equals ``{"foo": 2}``. The if statement that is applied in our ``"custom_function"`` is an example of how the logic can disregard list indexes and rather evaluate property values. This is a useful strategy you can apply to further making use of the ``["apply"]`` function, in addition to extending your transform capabilities.

.. seealso::

  :ref:`developer-guide` > :ref:`DTLReferenceGuide` > :ref:`expression_language` > :ref:`nested_transformations`

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
