.. _dtl-beginner-3-1:

DTL: Beginner
-------------

.. _pipes-where-dtl-executes-3-1:

Pipes, where DTL executes
~~~~~~~~~~~~~~~~~~~~~~~~~

(Repeting 1.1.5?)

Sesam consumes and produces streams of data in the form of lists of
entities.

Streams of entities flow through **pipes**. A pipe has an associated
**pump** that pull data entities from the **source**, push them through
any **transforms**, and send the results to the **sink**. All of this is
configured in the pipes configuration. As with water pipes, there is a
flow inside the single pipe (segment), and pipes connect to other pipes
and systems.

DTL (Data transformation Language) as the name implies is a
transformation. It is part of the internal flow of the pipe and an
entity enters and is transformed before the resulting entity is passed
to the next step in the flow. Usually the sink.

A pipe do not strictly have to have a DTL-transform, but most pipes have
one. DTL is not used outside pipes in Sesam.

**Source** and **Target** are two central concepts in DTL. Source is
data entering the flow and target is data exiting the flow. In some DTL
functions this is implicit, like copy and rename. For other DTL
functions you use built-in Variables "_S." (**S**\ ource) and "_T."
(**T**\ arget).

The simplest DTL transforms only copy or rename a subset of the fields
from the source (single) entity that flows from pipe-source into
DTL-transform. The source-concept is context based in pipes and DTL. You
will see examples of this.

Example: (need to line up with other examples and have a nice layout)

(*Link to short video*?)

(pipe with only embeded data?? Make the dataset)

(pipe with this datasett as source??)

This is the config for a pipe that gets data entities from the dataset
salesforce-lead and make new enteties from each entity and put them in

{

"_id": "dtl-test",

"type": "pipe",

"source": {

"type": "dataset",

"dataset": "salesforce-lead"

},

"transform": {

"type": "dtl",

"rules": {

"default": [

["copy",

["list", "_id", "Username"]

],

["rename","EmailAddress",":Contact-point"]

]

}

}

}

DTL is often more complex. E.g. it can pull and use data from other data
sets in your Sesam node or deal with nested structures in the source
entity.

DTL has many functions that you can use to transform data. You find an
overview in the DTL Reference Guide. You will use this much.

**What happens when a pipe runs?**

**What is the relationship of pipes and DTL?**

.. _entities-pipes-and-id-3-1:

Entities, pipes and \_id @Geir Atle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What is an \_id? Why do we need it? Is it used for the same thing
always? What is it good for? [STRIKEOUT:Absolutely nothing] quite a bit!

The reserved property \_id
^^^^^^^^^^^^^^^^^^^^^^^^^^

Everything in Sesam must have a unique identity, whether it is a system
configuration, a pipe configuration, a dataset, an entity within a
dataset, etc.

The reserved property named \_id is used as unique identity for
components in Sesam.

This unique identity allows for precise references between
configurations and precise connections between data entities.

See <ref to \_id restrictions> for more information on how to create
valid identifiers.

System \_id
^^^^^^^^^^^

The identity (_id) of a system must be unique within a Sesam node
instance.

Once a system configuration is saved, its identity cannot be changed. If
you need to change a system’s identity, you can Duplicate the system
configuration, save the duplicated configuration with the desired
identity, and then delete the original configuration.

Remember to also update any other configurations that were referencing
the original system to reference the new identity.

In the Sesam Management Studio, when you view the list of all systems in
the Systems menu, the System column will by default show you the
identity of all the defined systems in that Sesam node.

If the name property is also defined for a system configuration, then
the System column will show that value instead of the identity.

Regardless, if you need to reference a system configuration from another
configuration in Sesam, you reference the system’s identity.

See <ref to naming conventions> for more information on system naming
conventions.

See <ref to system config> for more information on how to define systems
in Sesam.

Pipe \_id
^^^^^^^^^

The identity (_id) of a pipe must be unique within a Sesam node
instance.

Once a pipe configuration is saved, its identity cannot be changed. If
you need to change a pipe’s identity, you can Duplicate the pipe
configuration, save the duplicated configuration with the desired
identity, and then delete the original configuration.

In the Sesam Management Studio, when you view the list of all pipes in
the Pipes menu, the Pipe column will by default show you the identity of
all the defined pipes in that Sesam node.

If the name property is also defined for a pipe configuration, then the
Pipe column will show that value instead of the identity.

Regardless, if you need to reference a pipe configuration from another
configuration in Sesam, you reference the pipe’s identity.

See <ref to naming conventions> for more information on pipe naming
conventions.

See <ref to system config> for more information on how to define pipes
in Sesam.

Dataset \_id
^^^^^^^^^^^^

The identity (_id) of a dataset must be unique within a Sesam node
instance.

By default, a dataset will have the same identity as the pipe it is
generated from.

You can override the default dataset identity by defining the dataset
property in the pipe’s sink configuration. (reference to sink config).

Once a dataset is generated, its identity cannot be changed. If you need
to change a dataset’s identity, you can edit the dataset property in the
pipe’s sink configuration, delete the sink dataset, and restart the
pipe. This will generate a new dataset with the new identity.

Remember to also update any other configurations that were referencing
the original dataset to reference the new identity.

In the Sesam Management Studio, when you view the list of all datasets
in the Datasets menu, the Dataset column will show you the identity of
all the datasets in that Sesam node.

If you need to reference a dataset from another configuration in Sesam,
you reference the dataset’s identity.

Entity \_id
^^^^^^^^^^^

The identity (_id) of an entity must be unique within the dataset in
which it resides. The identity of an entity is similar to a primary key
in a database table.

What makes an entity unique is usually dictated by the source system the
entity is imported from. This can typically be the primary key(s) of a
database table.

This means that you usually define the identity for entities in inbound
pipes.

If the source system has multiple properties that combined makes the
entity unique, you must combine all these properties into the \_id
property to ensure that uniqueness is preserved in Sesam.

In some cases, you can handle this in the source configuration part of
the inbound pipe. SQL sources, for example, allows you to specify
multiple columns from the source database as primary keys. Sesam will
then combine these columns automatically into the \_id during import.

In other cases, you may have to explicitly add the \_id property with
DTL in a transform step in the inbound pipe. This may be relevant when
the source configuration does not support specifying multiple properties
as primary keys.

Entity \_id and namespaces
^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, the pipe identity of the pipe where the entity originates is
used as namespace for both the entity’s identifier and the entity’s
properties.

Note that there is a slight, but significant, difference in the
placement of the namespace for the entity’s \_id property compared to
its other properties.

For the \_id property, the namespace prefixes the property **value**:

“_id”: ”\ **<namespace>**:<value>”

For other properties, the namespace prefixes the property **name**:

“\ **<namespace>**:property1”: ”<value>”

The reason the namespace is put into the value of the \_id is to ensure
that all entities are unique across all source systems.

Example:

An entity imported from a system called “crm” with a “user” table
consisting of a primary key “userId” with value “123”, and a column
“email” with value “john.doe@foo.no” would look something like this:

{

“_id”: “\ **crm-user**:123”,

“\ **crm-user**:userId”: “123”,

“\ **crm-user**:email”: “john.doe@foo.com”

}

Now imagine you have another source where one of the entities are also
identified by “123”.

Unless the namespace is part of the property value of \_id, both
entities would have the same \_id, namely “123”. So by prefixing this
value with a namespace we ensure that these entities do not come into
conflict with each other.

See <namespace ref> for more info on namespaces.

See <make-ni ref> for more info on namespaced identifiers and connecting
data in Sesam.

The autogenerated property $ids
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Should probably write something sensible about the connection between
\_id and $ids somewhere. Maybe related to merge pipes? – ‘Yea, or maybe
add it to the \_ Properties chapter’ -G

.. _entity-data-model-data-types-3-1:

Entity Data model – Data Types @Gabriell
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Entities, Dictionaries and \_id
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sesams Entity Data model is based on JSON – JavaScript Object notation –
and supports both the most common datatypes literally and the uncommon
ones as strings. It is a dictionary built up by key-value pairs. The key
is a string but the value can either be a literal value, a list or
another dictionary.

There is however one crucial difference between JSON dictionaries and
the Sesam Entity Data model; our entity model requires a primary key
‘_id’ as you have learned about in the previous topic. The value of the
key “_id” must always be a string. In the dataset view it can be found
in the list on the left hand side, on the top bar when viewing any
entity or shown inside the entity dictionary by checking the box “Show
System Attributes”.

An entity is therefore defined as a dictionary with the key “_id” as
shown in *Example 3.1.3A: Entity*

| \``\`
| *Example 3.1.3A: Entity*
| {“_id”: “primary-key-as-String”}.

\``\`

| *Example 3.1.3B: Dictionary* is not an entity, because it is missing
  \_id.
| \``\`
| *Example 3.1.3B: Dictionary*
| {}
| \``\`

Data types
^^^^^^^^^^

Sesam has many built in data types. I will list and explain them simply
here and refer you to the documentation
https://docs.sesam.io/entitymodel.html for further information.

Dictionary: \`{“key”: value}\`

Entity \`{“_id”: “primary-key-as-String”}`.

List: \`[“supports”, “different”, “types”,0, 0.01, true, null, {}, [],
]\`

String: \`“”\`

Integer: \`0\`

Decimal, \`0.01\`

Float: \`“~f123.456”\`

Boolean: \`true/false\`

Null: \`null\`

.. _syntax-3-1:

Syntax
~~~~~~

-

   -

      -
      -

   -

      -

-

   -

Within IT, syntax can be defined as: “the structure of statements in a
computer language”.

Expanding upon your current knowledge of JSON, and how it is used in
Sesam, a typical JSON syntax consists of the following:

[“<function>”, “<key>”, “<value>”]

i.e:

[“rename”, “EmailAddress”, “:Contact-point”], as shown in 3.1.1

Additionally, you will frequently be shaping JSON as data flows through
Sesam. Typically, when shaping JSON, you will be working with the Source
or Target that exists in a given pipe’s flow of data, as mentioned in
3.1.1.

In this sub-chapter, we will go through the functions [“copy”] and
[“rename”], as also introduced earlier in this section, in addition to
the [“add”] function.

[“copy”] lets you copy properties existing in your Source data, and the
most typical way of using [“copy”] is to copy everything in the Source.
To denote that you want to copy everything, you can use asterisk (*).
Asterisk works like a wildcard, and therefore copies everything in the
Source. This can look like the following:

{

"_id": "dtl-test",

"type": "pipe",

"source": {

"type": "dataset",

"dataset": "salesforce-lead"

},

"transform": {

"type": "dtl",

"rules": {

"default": [

["copy", "*"]

]

}

}

}

[“rename”] lets you define a new key for a given key in your Source. As
such, let’s say we have:

{

“EmailAddress”: “thisIs@google.com”,

“PostCode”: 0461,

“Country”: “Norway”

}

In our Source, albeit you don’t want the key to be “EmailAddress” rather
just “Email”, you could do the following in your pipe config:

{

"_id": "dtl-test",

"type": "pipe",

"source": {

"type": "dataset",

"dataset": "salesforce-lead"

},

"transform": {

"type": "dtl",

"rules": {

"default": [

["copy", "*"],

["rename", "EmailAddress", "Email"]

]

}

}

}

Which will produce the following dataset, when the pipe has completed a
run:

{

“Email”: “thisIs@google.com”,

“PostCode”: 0461,

“Country”: “Norway”

}

Continuing on to the [“add”] function. [“add”] lets you define a new key
and/or value. As such, it does not necessarily rely upon the Source or
Target. The following pipe config lists such definitions by using
[“add”].

{

"_id": "dtl-test",

"type": "pipe",

"source": {

"type": "dataset",

"dataset": "salesforce-lead"

},

"transform": {

"type": "dtl",

"rules": {

"default": [

["copy", "*"],

["add", "fakeKey", "fakeValue"],

["add", "fakeKey2", "_T. fakeKey "],

["add", "newEmail", "_S.Email"]

]

}

}

}

Which will produce the following dataset, when the pipe has completed a
run:

{

“fakeKey”: “fakeValue”,

“fakeKey2”: “fakeValue”,

“newEmail”: “thisIs@google.com”,

“PostCode”: 0461,

“Country”: “Norway”

}

Having covered the above functions, you should now be able to do some
basic shaping of your data as it flows into and out of a pipe. Albeit
you will quickly experience the need to do more advanced shaping of your
data. In order for you to do just that, you will now learn about the
functions: [“string”], [“concat”], [“plus”] and [“minus”].

These functions work like expressions, i.e., you can add or subtract
from an integer value by using [“plus”] and/or [“minus”]. The following
Source data, pipe config and result after a run shows simple use cases
of all of these functions.

Source data:

{

“favouriteSeries”: “Breaking Bad”,

“secondFavouriteSeries”: “Game of Thrones”,

“favouriteNumber”: 7,

“newEmail”: “thisIs@google.com”,

“PostCode”: 0461,

“Country”: “Norway”

}

Pipe config:

{

"_id": "dtl-test",

"type": "pipe",

"source": {

"type": "dataset",

"dataset": "salesforce-lead"

},

"transform": {

"type": "dtl",

"rules": {

"default": [

["copy", "*"],

["add", "postalCode", ["string", "_S.PostCode"]],

["add", "numberPlussed", ["plus", 1, "_S. favouriteNumber"]],

["add", "numberMinussed", ["minus", 1, "_S. favouriteNumber"]],

["add", "series", ["concat", "_S. favouriteSeries ", " and ", "_S.
secondFavouriteSeries",]]

]

}

}

}

Result after run:

{

“favouriteSeries”: “Breaking Bad”,

“secondFavouriteSeries”: “Game of Thrones”,

“series”: “Breaking Bad and Game of Thrones”,

“favouriteNumber”: 7,

“newEmail”: “thisIs@google.com”,

“numberPlussed”: 8,

“numberMinussed”: 6,

“postalCode”: “0461”,

“PostCode”: 0461,

“Country”: “Norway”

}

.. _dtl-in-practice-3-1:

DTL in practice
~~~~~~~~~~~~~~~

In this section you will learn how to:

- create a pipe from scratch
- view the output of a pipe
- write a greeting to the world with DTL

Create a new pipe
^^^^^^^^^^^^^^^^^

Let us start by creating a new pipe from scratch called ``practice``.
In the Sesam Management Studio, navigate to the **Pipes** view and follow these steps:

- Click the **New pipe** button
- Type in `practice` as the pipe's ``_id``
- In the **Templates** panel:

  - Choose Source Sytem: ``system:sesam-node``
  - Choose Source Provider: ``embedded prototype``
  - Click the **Replace** button to put the chosen Source configuration into the pipe configuration area.
  - Click the **Add DTL transform** button to get a nice starting point to write DTL.

- Lastly, add some test data:

  .. code-block:: json

    "entities": [{
      "_id": "1",
      "data": "One"
    }, {
      "_id": "2",
      "data": "Two"
    }]

You should now have the following pipe config:

.. _practice-pipe-config-initial:
.. code-block:: json
  :caption: Practice pipe config - initial
  :linenos:

  {
    "_id": "practice",
    "type": "pipe",
    "source": {
      "type": "embedded",
      "entities": [{
        "_id": "1",
        "data": "One"
      }, {
        "_id": "2",
        "data": "Two"
      }]
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "_id"]
        ]
      }
    }
  }

Save and run the pipe by clicking the **Save** button and then the **Start** button.

In the next section you learn how to view the result of a pipe run.

Pipe output
^^^^^^^^^^^

To view the result of a pipe run, switch to the pipe's **Output** tab.
Here you will see two entities:

::

  practice:1
  practice:2

But they are both empty:

.. code-block:: json
  :linenos:

  {
  }

This is because we only copy the ``_id`` so far.

In the next section you will learn to write your first piece of DTL to make the output a bit more interesting.

Greet the world!
^^^^^^^^^^^^^^^^

Switch back to the **Config** tab.

First, change the ``copy`` so that all source properties are included.
Then add a property called ``greeting`` with the value `Hello, World!`:

.. code-block:: json

  ["copy", "*"],
  ["add", "greeting", "Hello, World!"]

Save and start the pipe again.

Switch to the **Output** tab to view the new results.

Now you will see that the output has changed:

.. code-block:: json
  :caption: ``practice:1``
  :linenos:

  {
    "practice:data": "One",
    "practice:greeting": "Hello, World!"
  }

.. code-block:: json
  :caption: ``practice:2``
  :linenos:

  {
    "practice:data": "Two",
    "practice:greeting": "Hello, World!"
  }

You have now learned how to create a new pipe from scratch using templates, write and edit DTL functions,
run a pipe and view it's output.

.. _practice-pipe-config-final:
.. code-block:: json
  :caption: Practice pipe config - final
  :linenos:

  {
    "_id": "practice",
    "type": "pipe",
    "source": {
      "type": "embedded",
      "entities": [{
        "_id": "1",
        "data": "One"
      }, {
        "_id": "2",
        "data": "Two"
      }]
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*"],
          ["add", "greeting", "Hello, World!"]
        ]
      }
    }
  }


.. _pipe-shortcuts-3-1:

Pipe shortcuts
~~~~~~~~~~~~~~

Preview, Ctrl + Enter

Formatering alt + .

Save ctrl + s

Find/replace

Ctrl+space = Search/autocomplete


.. _tasks-for-dtl-beginner-3-1:

Tasks for DTL: Beginner
~~~~~~~~~~~~~~~~~~~~~~~
