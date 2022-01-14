.. _dtl-novice-3-2:

Novice
------

.. _copy-3-2:

"Copy"
~~~~~~

.. sidebar:: Summary

  "Copy" is...

  - one of the most fundamental DTL functions you will be using in Sesam
  - capable of evaluating asterisk
  - convenient in that you can whitelist and blacklist data

Copy is one of the most fundamental DTL functions you will be using in Sesam when transforming your source data to your target. The main reason for this is that it allows you to copy source data by the use of wildcards, i.e. asterisk (*). In the below example this has been implemented in order to copy all keys with the namespace "golden-object:" in them:

``["copy", "golden-object:*"]``

In addition, ``["copy"]`` is convenient in that you can whitelist and blacklist data by providing arguments in the ``["copy"]`` function as follows:   

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

  :ref:`developer-guide` > :ref:`DTLReferenceGuide` > :ref:`dtl-transforms`

  :ref:`developer-guide` > :ref:`configuration` > :ref:`pipe_section` > :ref:`namespaces`

  :ref:`developer-guide` > :ref:`DTLReferenceGuide` > :ref:`expression_language` > :ref:`namespaced-identifiers`

.. _add-3-2:

"Add"
~~~~~

.. sidebar:: Summary

  "Add"...

  - lets you define new properties
  - does not necessarily rely upon the Source or Target

["add"] lets you define new properties. As such, it does not necessarily rely upon the Source or
Target. The following source data, pipe configuration and output exemplifies using ["add"].

Source data:

.. code-block:: json

  {
    "ID": "user007",
    "Email": "thisIs@google.com",
    "PostCode": 0461,
    "Country": "Norway"
  }

Pipe Configuration:

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
             ["copy", "*"],
             ["add", "fakeKey", "fakeValue"],
             ["add", "fakeKey2", "_T.fakeKey"],
             ["add", "newEmail", "_S.Email"]
          ]
       }
    }
  }

Which will produce the following output, when the pipe has completed a run:

.. code-block:: json

   {
      "mssql-accounts:Email": "thisIs@google.com",
      "mssql-accounts:fakeKey": "fakeValue",
      "mssql-accounts:fakeKey2": "fakeValue",
      "mssql-accounts:newEmail": "thisIs@google.com",
      "mssql-accounts:PostCode": 0461,
      "mssql-accounts:Country": "Norway"
   }

.. seealso::

  :ref:`developer-guide` > :ref:`DTLReferenceGuide` > :ref:`dtl-transforms`

  :ref:`developer-guide` > :ref:`configuration` > :ref:`pipe_section` > :ref:`namespaces`

  :ref:`developer-guide` > :ref:`DTLReferenceGuide` > :ref:`expression_language` > :ref:`namespaced-identifiers`

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

Namespaces
~~~~~~~~~~

.. sidebar:: Summary

  Namespaces...

  - are essential with regards to Sesam's semantic enrichment 
  - aid in data lineage and shaping of data
  - are applied automatically by default

Namespaces in Sesam are part of our semantic enrichment. Namespaces aid in data lineage and shaping of data with respect to multiple system representations of the same object. In addition, this happens automatically by default.

To show the usage of namespaces we will extend upon the previously introduced example in :ref:`copy-3-2`. As you might recall, data produced by the pipe DTL transformation produced the following:

.. code-block:: json

	{
	  "mssql-accounts:country": "DK",
	  "mssql-accounts:id": 40,
	  "mssql-accounts:phone": "1-894-115-3398"
	}

In the above output, everything you see on the properties prior to the first ":" is Sesam's namespace enrichment.
As such, the namespace ``mssql-accounts`` is applied as the namespace for all properties, including the ``_id`` that is transformed in your pipe configuration for ``mssql-accounts``.

This is fairly straightforward, albeit imagine if you have merged multiple pipe datasets in for example a global, what happens then? How can you distinquish which properties originate from which pipe configuration? and how do you pick specific namespaces after these are merged? These questions will now be introduced and answered.  

Global pipe config:

.. code-block:: json
  
  {
    "_id": "global-person",
    "type": "pipe",
    "source": {
      "type": "merge",
      "datasets": ["mssql-accounts pip1", "pymsql-person pip2", "oracle-person pip3"],
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
          ["add", "Email", ["coalesce", ["list", "_S.mssql-accounts:Email", "_S.pymsql-person:Postaddress", "_S.oracle-person:EmailAddress", "No Email provided"]]],
          ["add", "PostCode", ["coalesce", ["list", "_S.pymsql-person:AreaCode", ["string", "_S.oracle-person:PostNumber"], "_S.mssql-accounts:Postcode", "No PostCode provided"]]],
          ["add", "PrivateAddress", ["coalesce", ["list", "_S.pymsql-person:Address", "_S.oracle-person:Address", "_S.mssql-accounts:Address", "No PrivateAddress provided"]]],
          ["rename", "AreaCode", "Postcode"]
        ]
      }
    },
    "metadata": {
      "global": true,
      "tags": "person"
    }
  }

As can be seen from the above pipe configuration, we merge the datasets ``mssql-accounts``, ``pymsql-person`` and ``oracle-person``.
In addition, we add the properties ``Email``, ``PostCode``, ``PrivateAddress``, and ``rename`` the property ``AreaCode`` to be ``Postcode``.
With regards to namespaces the aforementioned properties will take the namespace ``global-person``, albeit the ``rename`` property will not.
This is because the ``rename`` function retains the initally applied namespace for the property you are renaming, which is a bit unique and in this case this will be ``pymsql-person``.

With regards to picking the individual datasets that are merged in our pipe ``global-person``, this is exemplified for the properties ``Email``, ``PostCode`` and ``PrivateAddress``.
These properties are prioritized in a list and to pick spesific properties from datasets you must use the entire namespace to ensure Sesam understands which specific properties you refer to.

To show how the above pipe configuration evaluates, look at the below result:

.. code-block:: json
	
	{
	  "mssql-accounts:Email": "christian89@hotmail.com",
	  "mssql-accounts:Postcode": "6400",
	  "mssql-accounts:Address": "Rojumvej 66",
	  "oracle-person:EmailAddress": "hansMajestæt@gmail.com",
	  "oracle-person:PostNumber": 6400,
	  "oracle-person:Address": "Rojumvej 66",
	  "pymsql-person:Postaddress": "hansMajestæt@gmail.com",
	  "pymsql-person:AreaCode": "6851",
	  "pymsql-person:Postcode": "6851",
	  "pymsql-person:Address": "Danmarksgate 7",
	  "global-person:Email": "christian89@hotmail.com",
	  "global-person:Postcode": "6851",
	  "global-person:PrivateAddress": "Danmarksgate 7"
	}

As can be seen from the above example, namespaces allow for investigating and understanding where properties come from, are changed or first introduced. In addition, namespaces ensure that Sesam's MDM can be carried out. 

.. seealso::

  :ref:`concepts` > :ref:`concepts-features` > :ref:`concepts-namespaces`

  :ref:`concepts` > :ref:`concepts-features` > :ref:`concepts-global-datasets`

  :ref:`concepts` > :ref:`concepts-features` > :ref:`concepts-merging`

  :ref:`developer-guide` > :ref:`configuration` > :ref:`pipe_section` > :ref:`namespaces`

.. _make-ni-3-2:

"Make-ni"
~~~~~~~~~

.. sidebar:: Summary

  "Make-ni"...

  - creates namespaced identfiers (NIs) by using the ``["make-ni"]`` function
  - in Sesam is a complete Uniform Resource Identifier (URI)
  - is used to declare foreign keys as you would in a relational database management system (RDBMS)

The ``["make-ni"]`` DTL function allows for defining `namespaced identifiers <https://docs.sesam.io/concepts.html?highlight=namespaced%20identifiers#namespaces>`_ (NIs). A NI in Sesam is a complete Uniform Resource Identifier (URI). As such, it is used to investigate how data is semantically linked in a Sesam node. In addition, it is also used to declare foreign keys as you would in a relational database management system (RDBMS), albeit in Sesam the references will naturally be between pipes.

As a NI is produced, after a pipe has completed its run, it will be prefixed with ``~:`` followed by the namespace and its value. To exemplify, look at the below example:

.. code-block:: json

	{
	  "_id": "salesforce-accounts",
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
	        ["copy", "*"],
	        ["add", "rdf:type",
	          ["ni", "salesforce", "Account"]
	        ],
	        ["make-ni", "salesforce-contacts", "phone"]
	      ]
	    }
	  }
	}

The above pipe configuration will produce the following output:

.. code-block:: json

	{
	  "salesforce-accounts:country": "DK",
	  "salesforce-accounts:id": 40,
	  "salesforce-accounts:phone": "1-894-115-3398",
	  "salesforce-accounts:phone-ni": "~:salesforce-contacts:1-894-115-3398",
	  "salesforce-accounts:position": "CEO",
	  "rdf:type": "~:salesforce:Account"
	}

As can be seen from the above output, the property ``"salesforce-accounts:phone-ni"`` is the namespace that tells you that this is your recently created NI. The value of your NI is in practice your foreign key and tells you that the value of "phone" is a reference to the pipe named ``"salesforce-contacts"``.

Finally, as mentioned initially, the NI is in reality a URI, and as such you can press your NIs and navigate your Sesam node with respect to how data is semantically linked in your node.

.. seealso::

  :ref:`concepts` > :ref:`concepts-features` > :ref:`concepts-namespaces`

  :ref:`developer-guide` > :ref:`DTLReferenceGuide` > :ref:`dtl-transforms`

  :ref:`developer-guide` > :ref:`DTLReferenceGuide` > :ref:`expression_language` > :ref:`namespaced-identifiers`

.. _eq-equality-3-2:

"Eq" - Equality
~~~~~~~~~~~~~~~

.. sidebar:: Summary

  Equality...

  - is part of Sesam's `conditional DTL functions <https://docs.sesam.io/quick-reference.html#dtl-functions>`_
  - can be used both for join expressions as well as equality comparisons
  - is a boolean evaluator, meaning comparisons are returned as either ``true`` or ``false``

Equality is part of Sesam's `conditional DTL functions <https://docs.sesam.io/quick-reference.html#dtl-functions>`_.
In terms of functionality however, it serves a dual purpose. The ``["eq"]`` function can be used both for join expressions as well as equality comparisons.
Regardless, the ``["eq"]`` function is a boolean evaluator, meaning comparisons are returned as either ``true`` or ``false``. 

Join expressions evaluates intersection whereas the equality comparison evaluates exact matches.

In this section the equality comparison will be explained in detail, as the join expression is part of the section :ref:`merge-as-a-source-3-2`.

To exemplify usage of the equality comparison, look to the below:

``["eq", "_S.age", 42]``

Which will return ``true`` if the source entity's age field equals 42.

``["eq", "_S.hobbies", ["list", "soccer", "tennis"]]``

Will return ``true`` if the hobbies are exactly equal to ``["soccer", "tennis"]``.

Often times you will be using the equality comparison in conjunction with the ``if`` evaluator. An example is shown below:

``["if", ["eq", "_S.age", 42], ["add", "Old", true]]]``

The above logic will add the property ``"Old": true``, if your source entity's ``age`` field equals 42.

.. seealso::

	:ref:`developer-guide` > :ref:`DTLReferenceGuide` > :ref:`expression_language`

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

  :ref:`concepts` > :ref:`concepts-features` > :ref:`concepts-merging`

  :ref:`concepts` > :ref:`concepts-features` > :ref:`concepts-namespaces`

  :ref:`concepts` > :ref:`concepts-features` > :ref:`concepts-global-datasets`

  :ref:`developer-guide` > :ref:`configuration` > :ref:`source_section` > :ref:`merge_source`

.. _concat-concatination-3-2:

"Concat" - concatenation
~~~~~~~~~~~~~~~~~~~~~~~~

ref 1.2.19

.. seealso::

  TODO

.. _nested-data-structures-3-2:

Nested data structures
~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  Nested data structures...

  - can be accessed in Sesam by using dot notation (".")

Nested data structures can be accessed in Sesam by using dot notation ("."). Dot notation ensures that you can access properties within an object, such as a list with nested dictionaries. To exemplify, the following example is used:

``"My_list": [{"foo": 1}, {"foo": 2}]``

Accessing the ``"foo"`` element in ``"My_list"`` via Sesam dot notation:

``["add", "My_foo", "_S.My_list.foo"]``

Will return:

``"My_foo": [1,2]``

.. seealso::

  :ref:`developer-guide` > :ref:`DTLReferenceGuide` > :ref:`variables`

  :ref:`developer-guide` > :ref:`DTLReferenceGuide` > :ref:`dtl-transforms`

.. _apply-custom-rules-3-2:

Apply - Custom Rules
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
          ["apply", "custom_rule", "_S.My_list"]
        ]
      ],
      "custom_rule": [
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

Starting from the top, the source dataset ``My_list`` is a list where each element is a dictionary. Such a data object is an ideal candidate for use in a nested transformation, such as an ``["apply"]`` function, shown in the "Pipe transform statement". As you might recognize, the ``["apply"]`` is used to access elements in ``My_list``. In addition, the rule called ``"custom_rule"`` is referenced and then applied when the ``["apply"]`` funcion evaluates. In order for the result to become part of the dataset, you will need to also merge the result to the default rule, which is why we need the ``["merge"]`` wrapper.

Going into detail with respect to what happens in our ``"custom_rule"``, you could state, that applying it is like using a for loop, in a programming language, to send in entries from a list to a function. As such, our ``"custom_rule"`` will be called for each element in the list that we pass onto it. This is also why ``"lastSensorID"`` evaluates to ``2``, since the last entry we pass onto it equals ``{"sensor_id": 2}``. The if statement that is applied in our ``"custom_rule"`` is an example of how the logic can disregard list elements and rather evaluate property values. This is a useful strategy you can apply to further making use of the ``["apply"]`` function, in addition to extending your transform capabilities.

.. seealso::

  :ref:`developer-guide` > :ref:`DTLReferenceGuide` > :ref:`expression_language` > :ref:`nested_transformations`

.. _merge-as-a-function-3-2:

Merge as a function
~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  Merge as a function...

  - can be used both as ``["merge"]`` or ``["merge-union"]``
  - are what we call `transform functions <https://docs.sesam.io/DTLReferenceGuide.html#transforms>`_
  - will incur side-effects, typically modifying your target entity
  - ``["merge"]`` will **not** preserve duplicate values, keeping only the last
  - ``["merge-union"]`` will preserve duplicate values

As outlined in the example from :ref:`apply-custom-rules-3-2` on using the ``["merge"]`` function you will now learn more about the ``["merge"]`` function in addition to the ``["merge-union"]`` function.
``["merge"]`` and ``["merge-union"]`` are `transform functions <https://docs.sesam.io/DTLReferenceGuide.html#transforms>`_.
As such, these functions will incur side-effects, typically modifying your target entity.

The ``["merge"]`` function will copy all the properties from your target object onto your target entity.
If the property already exists, it will be overwritten.
This means that properties from later entries in for example a list, will win over earlier ones.
In comparison, the ``["merge-union"]`` function will add all entries regardless of whether or not the property already exists on your target entity.
To show the difference and implementation of these functions, look at the below example:

``["merge", ["list", {"a": 1}, {"a": 2, "b": 3}]]``

Which will produce the following result: ``{"a":2, "b":3}``, whereas the below:

``["merge-union", ["list", {"a": 1}, {"a": 2, "b": 3}]]``

will produce the following result: ``{"a":[1,2], "b":3}``

.. seealso::

  :ref:`concepts` > :ref:`concepts-features` > :ref:`concepts-namespaces`

  :ref:`developer-guide` > :ref:`configuration` > :ref:`pipe_section` > :ref:`namespaces`

  :ref:`developer-guide` > :ref:`DTLReferenceGuide` > :ref:`dtl-transforms`

.. _hops-3-2:

Hops
~~~~

.. sidebar:: Summary

  Hops...

  - can be used to perform joins across two or more namespaces
  - allows you to enrich your data beyond what is readily available from the source you are working on


Hops can be used to perform joins across two or more namespaces.
In essence, hops allows you to enrich your data beyond what is readily available from the source you are working on.
To exemplify, the below example shows how data from ``"salesforce-person"`` and ``"erp-company``"" are joined:

Data from ``salesforce-person``:

.. code-block:: json

  {
    "salesforce-person:_id": 40,
    "salesforce-person:country": "DK",
    "salesforce-person:id": 40,
    "salesforce-person:age": 32,
    "salesforce-person:departmentID": 3
  }

Data from ``erp-company``:

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
    "_id": "person-salesforce",
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
                ["eq", "_S.salesforce-person:departmentID", "ec.erp-company:department"]
              ]
            }]
          ],
          ["remove", ["list", "departmentID", "department"]]
        ]
      }
    }
  }

As can be seen from the above pipe configuration ``"person-salesforce"``, the ``["merge"]`` function is used to wrap the result from the ``["hops"]`` function. The ``["merge"]`` function ensures that the result from the ``["hops"]`` is added to the root level of the target entity.

In the ``["hops"]`` function you can see how two namespaces are joined in the ``["eq"]`` statement, namely ``"salesforce-person"`` and the abbreviated form ``"ec"``. As such, when ``departmentID`` from ``"salesforce-person"`` equals ``department`` from ``"erp-company"``, we can enrich our data beyond what is readily available from the source.

When this pipe completes its run, the following output will be produced: 

.. code-block:: json

  {
    "salesforce-person:_id": 40,
    "salesforce-person:country": "DK",
    "salesforce-person:id": 40,
    "erp-company:position": "Engineer",
    "erp-company:positionStatus": "On leave",
    "erp-company:departmentManager": "Danmark Tordenskjold"
  }

From the above output you should now recognize how ``["hops"]`` can be used to enrich your data.

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
