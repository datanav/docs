=============================
Component configuration guide
=============================

.. contents:: Table of Contents
   :depth: 2
   :local:

General
=======

The *Sesam Node* is configured using one or more *JSON* files located in the node folder when starting the *Sesam Node*.

For example:

::
  docker run .... -v $PWD:/sesam

Will look for a file called *nodeconfig.json* in the current directory.

Conceptually, the configuration files contains definitions for *Systems*, *Pipes* and *Clusters*. The cluser configuration is not required when running just a single *Sesam Node*.

The node configuration is a *JSON array* of :ref:`system <system_section>` and :ref:`pipe configurations <pipe_section>`. The configuration :doc:`entities <entitymodel>` are
*JSON objects* of the form:

It should be noted that all ``_id`` property values must be unique across across the solution. This means unique within the *nodeconfig.json* file but also across all files when a multiple file configuration is used.

::

    [
        {
            "_id": "some-solution-wide-unique-id",
            "name": "Name of component",
            "type": "component-type",
            "some-property": "some value"
        },
        {
            "_id": "some-other-solution-wide-unique-id",
            "name": "Name of other component",
            "type": "component-type",
            "some-other-property": "some other value"
        }
    ]

.. _pipe_section:

Pipes
=====

A pipe defines the flow of data from a *datasource* to a *sink* on some schedule as defined by the pump settings. Optionally, a pipe may define an ordered list of transforms that are applied to entities as they flow from the *datasource* to the *sink*. The pump "pumps" data in the form of entities from the source to the sink at regular or scheduled intervals. A chain of transforms can be placed in between the source and the sink, so that entities are transformed on their way to the sink.

The pipe configuration consists of a :ref:`source <source_section>`, :ref:`transform <transform_section>`, :ref:`sink <sink_section>` and a :ref:`pump <pump_section>`.

The configuration of a pipe has two forms; one *complete* form and one *short hand* form. The  *complete* form first is described first and :ref:`revisit <pipes_revisited>` describes the *short hand* form.

Prototype
---------
The following *json* snippet shows the general form of a pipe definition.

::

    {
        "_id": "pipe-id",
        "name": "Name of pipe",
        "type": "pipe",
        "short_config": "sql://system/table",
        "source": {
        },
        "transform": {
        },
        "sink": {
        },
        "pump": {
        }
    }


Note that if no ``name`` property is explicitly set for the source, sink or pump configurations one will be generated based on the ``name`` of the pipe (i.e. the contents of this property postfixed with "source", "sink" or "pump" respectively).

Properties
----------

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``_id``
     - String
     - The id of the pipe, this should be unique within a Sesam Node.
     -
     - Yes

   * - ``name``
     - String
     - A human readable name of the component.
     -
     - Yes

   * - ``type``
     - String
     - The type of the component, for pipes the only allowed value is "pipe"
     -
     - Yes

   * - ``short_config``
     - String
     - A connection string-like short form of the configuration, see the :ref:`pipes revisited <pipes_revisited>` for
       more information on the format of this property.
     -
     -

   * - ``batch_size``
     - Integer
     - The number of source entities to consume before writing to the sink. The batch size
       can be used to buffer up entities so that they can be written together to the sink in
       one go. The sink must support batch for the bulking to happen. This may increase the
       throughput of the pipe, at the cost of a little extra memory usage. If the batch fails,
       then entities will be retried individually. The pipe offset will be saved after each
       batch if the source supports this.
     - 100
     -

   * - ``source``
     - Object
     - A configuration object for the :ref:`source <source_section>` component of the pipe. It can be omitted if
       ``short_config`` is present and contains enough information to infer the source configuration. See the
       :ref:`pipes revisited <pipes_revisited>` for more information about how the source configuration is inferred in
       this case.
     -
     -

   * - ``transform``
     - Object/List
     - Zero or more configuration objects for the :ref:`transform <transform_section>` components of the pipe.
       The default is to do no transformation of the entities. If a list of more than one transform components is
       given, then they are chained together in the order given. This means that the output of the first transform
       is passed as the input of the second, and so on. The output of the last transform is then passed to the
       sink. The first transform gets its input from the source.
     -
     -

   * - ``sink``
     - Object
     - A configuration object for the :ref:`sink <sink_section>` component of the pipe. If omitted, it defaults to
       a :ref:`dataset sink <dataset_sink>` with its ``dataset`` property set to same as the pipe's ``_id`` property.
     -
     -

   * - ``pump``
     - Object
     - A configuration object for the :ref:`pump <pump_section>` component of the pipe. If omitted, it
       defaults to a ``datasync`` pump with its ``source`` and ``sink`` properties set to the
       respective ``_id`` properties of the source and sink respectively (possibly a computed value).
     -
     -


Example configuration
---------------------

The following example shows a pipe definition that exposes data from a SQL database table called ``customers``, and feeds it into a sink that writes the data into a dataset called ``Northwind:Customers```.

::

   {
       "_id": "northwind-customers",
       "name": "Northwind customers",
       "type": "pipe",
       "source": {
           "type": "sql",
           "system": "Northwind",
           "table": "Customers"
       },
       "sink": {
           "type": "dataset",
           "dataset": "Northwind:Customers"
       },
       "pump": {
           "type": "task:datasync",
           "schedule_interval": 30000
       }
   }

.. _source_section:

Sources
=======

Sources provide *streams* of :doc:`entities <entitymodel>` as input to the :ref:`pipes <pipe_section>` which is the
building blocks for the :ref:`flows <flow_section>` in the Sesam Node. These entities can take *any* shape (i.e. they
can also be nested), and have a single required property: **_id**. This ``_id`` field must be *unique within a flow* for
a specific logical entity. There may exist multiple *versions* of this entity within a flow, however.

Continuation support
--------------------

Sources can optionally support a ``since`` moniker or marker which lets them pick up where the previous stream of
entities left off - like a "bookmark" in the entity stream. The ``since`` marker is opaque to the rest of the
Sesam Node components and is assumed to be interpretable *only by the source*. Within an entity, the marker is carried
in the ``_updated`` property if supported by its source.

The Sesam Node supports a diverse set of core data sources:

Common properties
-----------------

All sources have certain properties in common. Some of these are omitted in the documentation of the individual types
of sources except if the source has different default values for this property (typically the ``supports_since`` property):

Protoype
^^^^^^^^

::

    {
        "name": "Name of source",
        "type": "type-of-source",
        "supports_since": false,
        "source_specific": "properties",
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``name``
     - String
     - A human redable name of the component. It may be omitted as part of a pipe
       configuration, in case it will be generated based on the pipe's ``name`` property with a "source" postfix.
     -
     -

   * - ``type``
     - String
     - The type of source, it is a enumeration with values from the list of supported sources. See the details in the
       documentation of each of the sources. If omitted from a pipe declaration, it is assumed to be a SQL
       source.
     - "sql"
     -

   * - ``supports_since``
     - Boolean
     - Flag to indicate whether to use a ``since`` marker when reading from the dataset, i.e. to start at
       the beginning each time or not.
     - false
     -

The dataset source
------------------

The dataset source is one of the most commonly used datasources in a Sesam Node. It simply presents a stream of entities from a
dataset stored in a Sesam Node. Its configuration is very simple and looks like:

Prototype
^^^^^^^^^

::

    {
        "name": "Name of source",
        "type": "dataset",
        "dataset": "id-of-dataset",
        "supports_since": true,
        "include_previous_versions": false
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``dataset``
     - String
     - | A dataset id
     -
     - Yes

   * - ``include_previous_versions``
     - Boolean
     - If set to ``false``, the data source will only return the latest
       version of any entity for any unique ``_id`` value in the dataset. This is the default behaviour.
     - false
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "dataset",
            "dataset": "northwind:customers",
            "supports_since": false,
            "include_previous_versions": true
        }
    }

The union datasets source
-------------------------

The union datasets source is similar to the ``dataset source``, except
it can process several datasets at once and keep track of each one in
its ``since`` marker handler. The union datasets source reads its
datasets in order, exhausting each one before moving to the next.

The entity ``_id`` property in entities is prefixed by the dataset
id separated by the ``:`` character. This is done to prevent unwanted
identity collisions. The entity id ``dave`` from the ``men`` dataset
will end up with the id ``men:dave``, and the entity id ``claire``
from the ``women`` dataset will end up with the id ``women:claire``.

Prototype
^^^^^^^^^

::

    {
        "name": "Name of source",
        "type": "union_datasets",
        "datasets": ["id-of-dataset1", "id-of-dataset2"],
        "supports_since": true,
        "include_previous_versions": false
    }

Properties
^^^^^^^^^^

The configuration of this source is identical to the ``dataset``
source, except ``datasets`` can be a list of datasets ids.

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``datasets``
     - List<String>
     - A list of datasets ids.
     -
     - Yes

   * - ``supports_since``
     - Boolean
     - Flag to indicate whether to use a ``since`` marker when reading
       from the dataset, i.e. to start at the beginning each time or not.
     - true
     -

   * - ``include_previous_versions``
     - Boolean
     - If set to ``false``, the
       data source will only return the latest version of any entity for
       any unique ``_id`` value in the dataset. This is the default behaviour.
     - false
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>`
configuration, which is omitted here for brevity:

::

    {
        "source": {
            "name": "Customers and orders",
            "type": "union_datasets",
            "datasets": ["northwind:customers", "northwind:orders"],
            "supports_since": true,
            "include_previous_versions": true
        }
    }

The merge datasets source
-------------------------

The merge datasets source is similar to the ``dataset source``, except
it can process several datasets at once and keep track of each one in
its ``since`` marker handler.

The merge datasets source reads its all of its datasets and returns
entities ordered by their ``_ts`` field. It knows how to deal with
identities, so that only the *latest* version of entities are returned.

Entity ids are not modified in any way.

Prototype
^^^^^^^^^

::

   {
       "name": "Name of source",
       "type": "merge_datasets",
       "datasets": ["id-of-dataset1", "id-of-dataset2"],
       "strategy": "latest",
       "supports_since": true
    }

Properties
^^^^^^^^^^

The configuration has two primary properties, ``datasets`` which must
be a list of datasets ids and ``strategy`` for choosing the merge
strategy.

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``datasets``
     - List<String>
     - A list of datasets ids.
     -
     - Yes

   * - ``strategy``
     - String
     - The name of the strategy to use to merge entities. Valid
       options are "``latest``" (the default) and "``all``".

       The "``latest``" strategy returns the version of the entity with
       the newest timestamp (as given in the ``_ts`` field). It will
       return the entity from the dataset that contains the latest
       version. This strategy is useful when only the latest version
       of an entity among the given datasets are of interest.

       The "``all``" strategy returns a merged version of the entity that
       contains all latest versions from all datasets. The individual
       dataset entities are keyed under the dataset id that they came
       from. The entities are ordered by the timestamp of the latest
       version of that entity. The returned entity contains all latest
       versions from all datasets where is appears. This strategy is
       useful when all datasets provide data for the resulting
       entity. In a lot of cases one may want to use it with a
       transform, so that only the entity can be shaped in a way that
       is more useful downstream.
     - "latest"
     -

   * - ``supports_since``
     - Boolean
     - Flag to indicate whether to use a ``since`` marker when reading
       from the dataset, i.e. to start at the beginning each time or not.
     - true
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>`
configuration, which is omitted here for brevity:

::

    {
        "source": {
            "name": "Products with metadata",
            "type": "merge_datasets",
            "datasets": ["products", "products-metadata"],
            "supports_since": true
        }
    }

.. _sql_source:

The SQL source
--------------

The SQL database source is one of the most commonly used data sources. In short, it presents database ``relations``
(i.e. ``tables``, ``views`` or ``queries``) as a entity stream to the Sesam Node. It has several options, all of which
are presented below with their default values:

Prototype
^^^^^^^^^

::

    {
        "name": "Name of source",
        "type": "sql",
        "system": "id-of-system",
        "table": "name-of-table",
        "primary_key": ["list","of","key","names"],
        "query": "SQL query string",
        "updated_query": "SQL query string for 'since' support in queries",
        "updated_column": "column-name-for-since-support-in-tables",
        "whitelist": ["columns","to","include"],
        "blacklist": ["columns","to","exclude"],
        "fetch_size": 1000,
        "schema": "default-schema-name-if-included"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 30, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - Must refer to a ``system`` component by ``id``. The role of this component is provide services like connection
       pooling and authentication for the data sources using it
     -
     - Yes

   * - ``table``
     - String
     - If ``table`` is given, it must refer to a fully qualified table name in the database system,
       not including schema, which if needed must be set separately. The ``table`` and ``query``
       properties are mutually exclusive with ``table`` used if both are present. TODO: are table names case sensitive?
     -
     - Yes

   * - ``primary_key``
     - List<String> or String
     - The value of this property can be a single string with the name of the column
       that contains the ``primary key`` (PK) of the table or query, or a list of strings
       if it is a compound primary key. If the property is not set and the ``table``
       property is used, the data source component will attempt to use table metadata
       to deduce the PK to use. In other words, you will have to set this property if
       the ``query`` property us used. The name(s) used in this propery are case sensitive and must
       match the underlying database naming.
     -
     -

   * - ``query``
     - String
     - Must be a valid query in the dialect of the ``RDBMS`` represented by the
       ``system`` property. You will also have to configure the primary key(s)
       of the query in the ``primary_key`` property. Note: mutually exclusive with the
       ``table`` property with ``table`` taking precedence. TODO: are queries case sensitive?
     -
     - Yes

   * - ``updated_column``
     - String
     - If the underlying relation contains information about updates, the data source is
       able to support ``since`` markers. You can provide the name of the column to use
       for such queries here. This must be a valid column name in the ``table`` or ``query``
       result sets and it must be of a data type that supports larger or equal (">=") tests
       for the ``table`` case.
     -
     -

   * - ``updated_query``
     - String
     - If the ``query`` property is set, the ``since`` support must be expressed by a
       full query including any test needed. A single variable binding
       ``:since`` must be included somewhere in the query string - for example
       "select * from view_name v where v.updates >= :since".
     -
     -

   * - ``schema``
     - String
     - If a specific schema within a database is needed, you must provide its name in this property.
       Do *not* use schema names in the ``table`` property. TODO: are these names case sensitive?
     -
     -

   * - ``whitelist``
     - List<String>
     - The names of the columns to include in the generated entities. If there is a ``blacklist`` also specified, the
       whitelist will be filtered against the contents of the blacklist.
     -
     -

   * - ``blacklist``
     - List<String>
     - The names of the columns to exclude from the generated entities. If there is a ``whitelist`` also specified, the
       blacklist operates on the values of the whitelist (and not the whole columnset).
     -
     -

   * - ``fetch_size``
     - Integer
     - The fetch size of the result sets (number of rows in a cursor fetch) to get from the database
     - 1000
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

Example with a single table:

::

    {
        "source": {
            "type": "sql",
            "system": "Northwind",
            "table": "Customers"
        }
    }

Example with a single table, where the primary key is in a column named ``table_id`` and the updated datestamp is
in a column called ``updated``. This enables us to switch on ``since`` support:

::

    {
        "source": {
            "type": "sql",
            "system": "my_system",
            "table": "my_table",
            "primary_key": "table_id",
            "updated_column": "updated",
            "supports_since": true
        }
    }

Example with custom query:

::

    {
        "source": {
            "type": "sql",
            "system": "Northwind",
            "query": "select * from Customers",
            "primary_key": "CustomerID"
        }
    }

Example with a custom query from a table called ``my_table`` where the primary key is in a column named ``table_id``
and the updated datestamp is in a column called ``updated``. This enables us to switch on ``since`` support:

::

    {
        "source": {
            "type": "sql",
            "system": "my_system",
            "query": "select * from my_table",
            "primary_key": "table_id",
            "updated_column": "updated",
            "updated_query": "select * from my_table where updated >= :since",
            "supports_since": true
        }
    }

The CSV source
--------------

The CSV data source translates the rows of files in ``CSV format`` to entities. The configuration options are:

Prototype
^^^^^^^^^

::

    {
       "name": "Name of source",
       "type": "csv",
       "url": "url-to-csv-file",
       "has_header": true,
       "field_names": ["mappings","from","columns","to","properties"],
       "auto_dialect": true,
       "dialect": "excel",
       "encoding": "utf-8",
       "decode_error_strategy": "strict-or-replace",
       "primary_key": ["list","of","column","names"],
       "whitelist": ["list","of","column","names","to","include"],
       "blacklist": ["list","of","column","names","to","exclude"],
       "delimiter": ","
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``url``
     - String
     - The URL of the ``CVS`` file to load.
     -
     - Yes

   * - ``has_header``
     - Boolean
     - Flag that indicates to the source that the first row in the ``CSV`` file contains the names of the columns.
       If this property is set to ``false``, you will have to provide a list of column names in the ``field_names``
       property.
     - true
     -

   * - ``field_names``
     - List
     - If set, specifies the names of the columns. It takes precedence over the header in the CSV file if present.
     -
     -

   * - ``auto_dialect``
     - Boolean
     - Flag that hints to the source that it should try to guess the dialect of the ``CSV`` file on its own.
     - true
     -

   * - ``dialect``
     - String
     - Encodes what type of CSV file the file is. This is basically presets of the other properties.
       The recognised values are ``"excel"``, ``"excel_tab"`` and ``"unix_dialect"``.
       TODO: explain what they mean.
     -
     -

   * - ``encoding``
     - String
     - The character set to used to encode the text in the CSV file
     - "UTF-8"
     -

   * - ``decode_error_strategy``
     - String
     - A enumeration of "strict" and "replace" that tells the character decoder how to deal with illegal characters
       in the input data. The default is "strict" which raises an error and stops processing. The "replace" option
       will log a warning and attempt to replace the offending character(s) with the unicode special character for
       "replacement character", see https://en.wikipedia.org/wiki/Specials_%28Unicode_block%29 for more details.
       Use the "replace" option with extreme care as it can lead to data loss if you're not absolutely sure of what
       you are doing. The preferred option should always be to try the fix the data at the source.
     - "strict"
     -

   * - ``primary_key``
     - List<String> or String
     - The name of the column(s) to use as ``_id`` in the generated entities. It can be either a list of strings
       (if the identity is a compound value) or a single column name (i.e. a string). The column name(s) are case
       sensitive and must match the contents of either ``field_names`` or the header of the CSV file.
     -
     - Yes

   * - ``whitelist``
     - List<String>
     - The names of the columns to include in the generated entities. If there is a ``blacklist`` also specified, the
       whitelist will be filtered against the contents of the blacklist.
     -
     -

   * - ``blacklist``
     - List<String>
     - The names of the columns to exclude from the generated entities. If there is a ``whitelist`` also specified, the
       blacklist operates on the values of the whitelist (and not the whole columnset).
     -
     -

   * - ``delimiter``
     - String
     - The character or string to use as the ``CSV`` field separator (delimiter)
     - ","
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "csv",
            "name": "Country names from CSV source",
            "url": "http://blog.plsoucy.com/wp-content/uploads/2012/04/countries-20140629.csv",
            "id_field": "Code",
            "encoding": "iso-8859-1"
        }
    }

The RDF source
--------------

The RDF data source is able to read data in ``RDF NTriples``,
``Turtle`` or ``RDF/XML`` format and turn this into entities.  It will
transform triples on the form ``<subject> <predicate> "value"`` into
entities on the form:

::

    {
        "_id": "subject",
        "<predicate>": "value"
    }

RDF blank nodes will be turned into child entities. The configuration
snippet for the RDF data source is:

Prototype
^^^^^^^^^

::

    {
       "name": "Name of source",
       "type": "rdf",
       "system": "url-system-id",
       "url": "url-to-rdf-file",
       "format": "nt-ttl-or-xml"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`url system <url_system>` component to use. If not present, a URL system
       with the ``_id`` set to the contents of the ``url`` property will be created automatically. Note that if the
       HTTP server requires authentication, you will have to create a URL system component explicitly.
     -
     -

   * - ``url``
     - String
     - The URL of the ``RDF`` file to load - it can contain multiple subjects
       (with ``blank node`` hierarchies) and each unique non-blank subject will
       result in a single root entity.
     -
     - Yes

   * - ``format``
     - String
     - The type of ``RDF`` file referenced by the ``url`` property. It is
       an enumeration that can take following recognized values: ``"nt"`` for
       ``NTriples``, ``"ttl"`` for ``Turtle`` form or ``"xml"`` for ``RDF/XML``
       files.
     - "nt"
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "rdf",
            "name": "Metadata about Elvis impersonators",
            "url": "http://www.snee.com/rdf/elvisimp.rdf",
            "format": "xml",
        }
    }

The SDShare source
------------------

The SDShare data source can read ``RDF`` from ``ATOM feeds`` after the
``SDShare specification`` (http://sdshare.org). It has the following
properties:

Prototype
^^^^^^^^^

::

    {
       "name": "Name of source",
       "type": "sdshare",
       "system": "url-system-id",
       "url": "url-to-sdshare-fragments-feed",
       "supports_since": false
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`URL system <url_system>` component to use. If not present, a URL system
       with the ``_id`` set to the contents of the ``url`` property will be created automatically. Note that if the
       HTTP server requires authentication, you will have to create a URL system component explicitly.
     -
     -

   * - ``url``
     - String
     - The URL of the SDShare fragments feed to consume.
     -
     - Yes

   * - ``supports_since``
     - Boolean
     - Flag to indicate whether to include ``since`` request parameter when
       reading from the fragments feed.
     - true
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "sdshare",
            "name": "Metadata about norwegian companies",
            "url": "https://open.sesam.io/sdshare/server/1/fragments/enhetsregisteret"
        }
    }

.. _ldap_source:

The LDAP source
---------------

The LDAP source provides entities from a ``LDAP catalog`` configured by a :ref:`LDAP system <ldap_system>`.
It supports the following properties:

Prototype
^^^^^^^^^

::

    {
        "name": "Name of source",
        "type": "ldap",
        "system": "ldap-system-id",
        "search_base": "*",
        "search_filter": "(objectClass=organizationalPerson)",
        "attributes": "*",
        "id_attribute": "cn",
        "page_size": 500,
        "attribute_blacklist": ["a","list","of","attributes","to","exclude"]
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - ID of the LDAP system component to use
     -
     - Yes

   * - ``search_base``
     - String
     - The base LDAP search expression to use when looking for records
     - "*"
     -

   * - ``search_filter``
     - String
     - LDAP filter expression to apply to all records found by the ``search_base`` expression
     - "(objectClass=organizationalPerson)"
     -

   * - ``attributes``
     - String
     - A wildcard expression specifying which attributes to include in the entity.
     - "*"
     -

   * - ``id_attribute``
     - String
     - Sets which of the LDAP attributes to use for the ``_id`` property of a entity.
     - "cn"
     -

   * - ``page_size``
     - Integer
     - The default number of records to read at a time from the LDAP service.
     - 500
     -

   * - ``attribute_blacklist``
     - List
     - A list of attribute names (as strings) to exclude from the record when constructing entities.
     - []
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "ldap",
            "name": "Bouvet LDAP server data",
            "system": "bouvet_ldap",
            "search_base": "ou=Bouvet,dc=bouvet,dc=no"
        }
    }

The JSON source
---------------


The `JSON`` source can read entities from a ``JSON`` file available either locally or over HTTP.

If the ``supports_since`` property is set to *true*, then the
``since`` request parameter is added to the URL to signal that we want
only changes that happened after the since marker.

Prototype
^^^^^^^^^

::

    {
       "name": "Name of source",
       "system": "url-system-id",
       "type": "json",
       "url": "url-to-json-file"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`URL system <url_system>` component to use. If not present, a URL system
       with the ``_id`` set to the contents of the ``url`` property will be created automatically. Note that if the
       HTTP server requires authentication, you will have to create a URL system component explicitly.
     -
     -

   * - ``url``
     - String
     - The URL of the ``JSON`` file to load.
     -
     - Yes

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "json",
            "name": "Test JSON source via HTTP",
            "url": "https://server.com/sesam/data/test.json",
        }
    }

An example with a local file:

::

    {
        "source": {
            "type": "json",
            "name": "Test JSON source via the local FS",
            "url": "/sesam/data/test.json",
        }
    }


The metrics source
------------------

The metrics data source provides the ``internal metrics`` (i.e. counters and statistics) of the Sesam Node as a list
of ``JSON`` entities. It has no specific configuration:

Prototype
^^^^^^^^^

::

    {
        "name": "Name of source",
        "type": "metrics"
    }

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "source": {
            "name": "Sesam Node Metrics"
            "type": "metrics"
        }
    }

The empty source
----------------

Sometimes it is useful for debugging or development purposes to have a data source that doesn't produce any entities:

Prototype
^^^^^^^^^

::

    {
        "name": "Name of source",
        "type": "empty"
    }

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "empty",
            "name": "An empty source",
        }
    }


.. _http_endpoint_source:

The HTTP endpoint source
------------------------

This is a special data source that registers an HTTP endpoint that one
can ``POST`` entities to. Entities posted here will be written to the
pipe's sink. Both individual entities and lists of entities can be
posted.

The ``POST`` endpoint will be available at the same location
as where you can ``GET`` pipe entities. By using the ``HTTP endpoint``
source you enable ``POST`` support at this endpoint.

The protocol is described in additional detail in the :doc:`JSON Push
Protocol <json-push>` document. The serialisation of entities as JSON
is described in more detail :doc:`here <entitymodel>`.

This source is compatible with :ref:`The JSON push sink
<json_push_sink>`.

Accepted Content types
^^^^^^^^^^^^^^^^^^^^^^

The HTTP endpoint supports POSTs of both single JSON objects and lists of JSON objects. The requests ``content-type``
header element must be set to ``application/json`` in this case.

The endpoint also supports receiving RDF in NTriples form after the
`SDShare Push specification <https://github.com/SesamResearch/sdshare-push/blob/master/spec.md>`_. In this case
the URL parameters have to include at least one ``resource`` parameter describing which resources the NTriples
payload contains statements about. If you include a ``resource`` parameter that there are no statements about in the
NTriples body, an empty entity is generated with its ``_deleted`` flag set to ``true``. Note that the ``graph``
parameter of the protocol is ignored - the destination of the entities generated from the NTriples payload must be
configured in the pipe's ``sink`` section. This type of request expects the ``content-type``
to be ``application/n-triples`` or ``text/plain``.

::

   http://localhost:9042/pipes/mypipe/entities

A pipe that references the ``HTTP endpoint`` source will not pump any entities,
in practice this means that a ``datasync`` pump is not configured for the
pipe; the only way for entities to flow through the pipe is by posting them
the HTTP endpoint.


Prototype
^^^^^^^^^

::

    {
        "name": "Name of source",
        "type": "http_endpoint"
    }

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>`
configuration, which is omitted here for brevity:

::

    {
        "source": {
            "name": "Endpoint - events",
            "type": "http_endpoint"
        },
    }


.. _fake_source:

The fake source
---------------

This is a utility data source intended to be used to quickly mock up syntetic data for testing purposes.
It uses the `Fake Factory <http://fake-factory.readthedocs.org/en/latest/>`_ Python package in conjunction with a entity
template to produce custom entities that can be consumed by a sink. Fake sources intended to be interconnected can be
realised by using the *shared id pools* of the related :ref:`Fake System <fake_system>` component.

Prototype
^^^^^^^^^

::

    {
        "name": "Name of source",
        "type": "fake",
        "entities": 1234,
        "system": "fake-system-id",
        "template": {
            "_id": "system:some_id_pool",
            "some_property": "fake_factory_method_name"
        }
    }


Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of a :ref:`Fake System <fake_system>` component. It is only required if the ``template`` property contain
       fields using a "system:<pool_id>" value to generate id fields from a predefined population (i.e. so datasets can be
       linked).
     -
     -

   * - ``entities``
     - Integer
     - The number of entities to generate. Note that the shared ids in the :ref:`Fake System <fake_system>` component
       should take this into account. If the pool size is less than the number of entities to generate, an error will
       be raised.
     -
     - Yes

   * - ``template``
     - Object
     - A entity template for the generation. It needs to contain at least a ``_id`` property for the entity to be valid.
       Se the example configurations for more details on how this template works.
     -
     - Yes

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>`
configuration, which is omitted here for brevity.

A source that generates a typical person entity via various `Fake Factory providers <http://fake-factory.readthedocs.org/en/latest/providers/faker.providers.person.html>`_.

::

    {
        "source": {
            "name": "Fake people",
            "type": "fake",
            "entities": 100,
            "template": {
                "_id": "uuid4",
                "last_name": "last_name",
                "first_name": "first_name",
                "address": "address",
                "telephone": "phone_number",
                "email": "email",
                "employer": "company"
            }
        },
    }

The general form of a template property is

::

    "property_name": "fake_factory_provider_name"

For generating id properties from a fixed set (to be able to link entities from different sources together using
:ref:`DTL transforms <dtl_transform>`), a special syntax for the value part is used:

::

    "shared_id_propery": "system:<pool_id_from_fake_system_component>".

These shared *id pools* are configured as part of the :ref:`Fake System <fake_system>` component, and you have to include
its id in the ``system`` property. Here's an example of two pipes with sources for fake employee- and employer (company)
entities using a shared pool of ids for the employer id:

.. _fake_system_example:

::

    [
        {
            "_id": "employers_employees",
            "type": "system:fake",
            "name": "Employees and employers system",
            "id_pools": {
                "employers": {
                    "seed": 1234,
                    "min": 1,
                    "max": 1000
                }
            }
        },
        {
            "_id": "employees",
            "name": "Employees",
            "type": "pipe",
            "source": {
                "name": "Fake employees source",
                "type": "fake",
                "system": "employers_employees",
                "entities": 100,
                "template": {
                    "_id": "uuid4",
                    "last_name": "last_name",
                    "first_name": "first_name",
                    "address": "address",
                    "telephone": "phone_number",
                    "email": "email",
                    "employer": "system:employers"
                }
            }
        },
        {
            "_id": "employers",
            "name": "Employers",
            "type": "pipe",
            "source": {
                "name": "Fake employers source",
                "type": "fake",
                "system": "employers_employees",
                "entities": 100,
                "template": {
                    "_id": "system:employers",
                    "name": "company",
                    "address": "address",
                    "email": "company_email",
                    "home_page": "uri"
                }
            }
        }
    ]

.. _sparql_source:

The SPARQL source
-----------------

The SPARQL source fetches data about subjects from a triplestore exposing a SPARQL complient endpoint. The endpoint of
the source is configured either directly or implicitly by a :ref:`URL system <url_system>`. The source uses
two SPARQL queries to construct entities; the fragment query is a SPARQL ``SELECT`` query that gets a list of subjects
to get data for and their modification times and a fragment query, which is a SPARQL ``CONSTRUCT`` query that
gathers all relevant statements about a particular subject. The latter is then used to generate the stream of entities.

Prototype
^^^^^^^^^

::

    {
        "name": "Name of source",
        "type": "sparql",
        "system": "url-system-id",
        "url": "sparql-endpoint",
        "fragments_query": "SPARQL select query",
        "fragment_query": "SPARQL construct query"
        "since_default": "0001-01-01T00:00:00Z"
    }


Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of a :ref:`URL System <url_system>` component. If not specified, one will be automatically generated using
       the base of the ``url`` property as the system's ``base_url``.
     -
     -

   * - ``fragments_query``
     - List<String> or String
     - A SPARQL ``SELECT`` query that should return exactly two bound variables: ``id`` which should contain a unique subject
       and ``updated`` which should contain its modification time in ISO UTC format (or "0001-01-01T00:00:00Z" if not
       available in the data). If the ``supports_since`` is set to true, you must include a filter based on the
       ``updated`` content compared to the current since moniker. You must use a variable expansion "${since}" for this
       purpose. The query result set should always be ordered by the "?updated" variable. If a list of strings is given,
       they will be converted to a single string by concatenation with the newline character.
     -
     - Yes

   * - ``fragment_query``
     - List<String> or String
     - A SPARQL ``CONSTRUCT`` query that should return all the relevant statements for a particular subject selected
       by the ``fragments_query`` query. The query should use the expansion variable "${uri}" to filter or select
       the correct subject to construct the statements to return.  If a list of strings is given, they will be
       converted to a single string by concatenation with the newline character.
     -
     - Yes

   * - ``since_default``
     - String
     - A string literal to use when querying the triplestore the first time.
     - "0001-01-01T00:00:00Z"
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>`
configuration, which is omitted here for brevity.

::

    {
        "source": {
            "name": "SPARQL example",
            "type": "sparql",
            "url": "http://localhost:8890/sparql",
            "fragments_query": [
                "PREFIX sdshare: <http://www.sdshare.org/2012/extension/>",
                "SELECT DISTINCT ?id ?updated WHERE {",
                 "    ?id sdshare:lastmodified ?updated",
                 "} FILTER (?updated >= \"${since}\"^^xsd:dateTime) ORDER BY ?updated",
            ],
            "fragment_query": [
                "CONSTRUCT { ?subject ?property ?value } WHERE {",
                "  ?subject ?property ?value .",
                "} FILTER (?subject = <${uri}>)",
            ]
        },
    }

.. _transform_section:

Transforms
==========

Transforms sit between the source and the sink. Entities passed from a
source to a sink, can optionally be passed through a chain of
transforms before they are passed on to the sink. This makes it
possible to reshape the entities on their way to the sink. Transforms
can also be used to filter entities and construct new entities.

Transforms can be configured on a pipe by specifying the
"``transform``" property. The field is optional, and can contain
either a transform configuration object or a list of them.

::

   {
       "_id": "mypipe",
       "name": "Name of pipe",
       "type": "pipe",
       ...
       "source": {
          ...
       },
       ..
       "transform": {
           ...the transform configuration goes here...
       }
    }}

.. _dtl_transform:

The DTL transform
-----------------

This is a transform that lets you apply Data Transformation Language
transformations on the entities stream produced by the data source.

See :doc:`DTLReferenceGuide` for more details on the transformation
language itself.

Example configuration
^^^^^^^^^^^^^^^^^^^^^

Pipe configuration that reads entities from the
``Northwind:Customers`` dataset and transforms them using the Data
Transformation Language before writing them to the
``customer-with-orders`` dataset.

::

   {
       "_id": "customer-with-orders",
       "name": "Customers with orders",
       "type": "pipe",
       "source": {
          "type": "dataset",
          "dataset": "Northwind:Customers"
       },
       "transform": {
           "type": "dtl",
           "name": "Join customers with their orders",
           "dataset": "Northwind:Customers",
           "transforms": {
               "default": [
                   ["copy", "_id"],
                   ["add", "name", "_S.ContactName"],
                   ["add", "orders", ["apply", "order", ["hops", {
                       "datasets": ["Northwind:Orders o"],
                       "where": [
                           ["eq", "_S._id", "o.CustomerID"]
                       ]
                   }]]]
               ],
               "order": [
                   ["add", "order_id", "_S.OrderID"],
                   ["add", "order_date", "_S.OrderDate"]
               ]
           }
       }
   }


The JSON Schema validation transform
------------------------------------

A transform that validates entities against a ``JSON Schema``
(http://json-schema.org/) document. If the document is valid then the
field referenced by ``key_valid`` will be set to true, otherwise
false. Any validation error messages will be added to the field
referenced by ``key_errors``.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 3, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``schema``
     - Object
     - The JSON schema to validate entities against.
     -
     - Yes

   * - ``key_valid``
     - String
     - The field to store the validation result. This is a boolean value,
       which is true if the entity is valid, otherwise false.
     - ``valid``
     -

   * - ``key_errors``
     - String
     - The field to store the validation error messages. The error messages
       is a list of strings. The field is only added if the entity is invalid.
     - ``errors``
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

   {
       "_id": "men-validated",
       "type": "pipe",
       "source": {
           "type": "dataset",
           "dataset": "men"
       },
       "transform": {
           "type": "json_schema",
           "schema": {
               "type" : "object",
               "properties" : {
                   "name" : {"type" : "string"},
                   "born" : {"type" : "string"}
               },
               "required": ["name", "born"]
           }
       }
   }

If the following entities where pushed through the pipe:

::

   [
    {"_id": "3",
     "name": "Jim"},
    {"_id": "5",
     "name": "Bob",
     "born": "1972-03-12"}
   ]

then these would come out:

::

   [
    {"_id": "3",
     "valid": false,
     "errors": [
       "'born' is a required property"
     ],
     "name": "Jim"},
    {"_id": "5",
     "valid": true,
     "name": "Bob",
     "born": "1972-03-12"}
   ]

The HTTP transform
------------------

This transform POSTs entities to an HTTP endpoint, which transforms
them and then returns them in the response. The HTTP endpoint must
accept ``application/json`` and the response must be
``application/json``. The endpoint must support lists of entities
only, i.e. it should expect to receive a JSON array and it should
always return a JSON array. If the endpoint returns a 4xx or 5xx HTTP
response, then the transform will raise an exception.

The endpoint is free to decide how the entitites are
transformed. It'll just have to produce a list of zero or more
entities from the entities it was posted. This means that entities can
be transformed, filtered out or new ones created.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 3, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``url``
     - Object
     - The URL to HTTP POST entities to.
     -
     - Yes

   * - ``batch_size``
     - Integer
     - The maximum number of entities to POST in each request. If there are
       more entities than this then they'll be split across multiple HTTP
       requests.
     - 100
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

  {
      "_id": "deduplicated-men",
      "type": "pipe",
      "source": {
          "type": "dataset",
          "dataset": "men"
      },
      "transform": {
          "type": "http",
          "url": "http://localhost:8080/transforms/deduplicate",
          "batch_size": 5
      }


The properties to CURIEs transform
----------------------------------

This transform can transform entity properties to `RDF curies <https://www.w3.org/TR/curie/>`_ (a superset of XML QNames)
based on wildcard patterns. It is used primarily when dealing with or preparing to output RDF data.

Prototype
^^^^^^^^^

::

    {
        "type": "properties_to_curies",
        "id_prefix": "id_prefix",
        "prefixes": [
          "some_prefix", ["some_pattern"]
        ]
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``id_prefix``
     - String
     - The prefix to use for ``_id`` properties
     -
     - Yes

   * - ``prefixes``
     - List<(String, List<String>)>
     - A list of String,List pairs that make up the rules for which properties should be assigned which prefixes.
       See the example section below for a fuller explanation of this property.
     -
     - Yes

Example
^^^^^^^

The "prefixes" property is a object with contains a list of string+list pairs, where the first item is the prefix
to add and the second is the path expression that is used to match against. The number of elements in the list must
be even.

Path expressions are evaluated in order and the first matching path expression will win, so if a path expression
matches the prefix will be assigned to the matching key.

A path expression is a list of strings. The right-most string value is the most specific. "**" can be used to denote
nestedness at an arbitrary depth. "*" can be used as a wildcard in the string values themselves.

Given the configuration:

::

    {
        "transform": [
           {
             "type": "properties_to_curies",
             "id_prefix": "x",
             "prefixes": [
                  "c", ["status", "code"],
                  "_", ["status"],
                  "t", ["t_*"],
                  "m", ["status", "**", "m*"],
                  "s", ["status", "**"],
                  "x", ["**"]
             ]
           }
        ]
    }

And the input entity:

::

    {
        "_id": "2",
        "name": "John",
        "born": "1980-01-23",
        "code": "AB32",
        "t_a": "A",
        "status": {
            "married": True,
            "spouse": "Pam",
            "code": 123,
            "t_b": {
                "t_c": "C",
                "hello": "world",
                "<s:hi>": "bye"
            }
        }
    }

The transform will output the following transformed entity:

::

    {
        "_id": "<x:2>",
        "<x:name>": "John",
        "<x:born>": "1980-01-23",
        "<x:code>": "AB32",
        "<t:t_a>": "A",
        "<_:status>": {
            "<m:married>": True,
            "<s:spouse>": "Pam",
            "<c:code>": 123,
            "<t:t_b>": {
                "<t:t_c>": "C",
                "<s:hello>": "world",
                "<s:hi>": "bye"
            }
        }
    }

The URIs to CURIEs transform
----------------------------

This transform can transform entity properties containing URIs in the keys and/or the values to a more compact form
using `RDF curies <https://www.w3.org/TR/curie/>`_ (a superset of XML QNames). It is used primarily when dealing with
or reading RDF data.

Prototype
^^^^^^^^^

::

    {
        "type": "properties_to_curies",
        "prefixes": {
          "some_prefix": "some_uri"
        }
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``prefixes``
     - Object
     - A mapping of RDF prefixes (curies) to URIs. This is used to compress URI keys or properties to the form
       "<foo:key_or_value>" or "~rfoo:key_or_value". The common RDF prefixes are built-in
       and you don't have to provide the mapping for it. If no prefix mappings are given, the built-in and node-wide
       prefixes are used instead.
     -
     -

Example
^^^^^^^

Given the configuration:

::

    {
        "transform": [
           {
             "type": "uris_to_curies",
             "prefixes": {
                 "test": "http://psi.test.com/",
                 "foo": "http://psi.foo.com/"
             }
           }
        ]
    }

And the input entity:

::

    {
        "_id": "http://psi.test.com/2",
        "http://psi.test.com/name": "John",
        "born": "1980-01-23",
        "http://psi.test.com/code": "AB32",
        "status": {
            "http://psi.foo.com/married": True,
            "spouse": "Pam",
            "url1": "~rhttp://www.foo.com",
            "url2": "~rhttp://psi.foo.com/url2",
            "code": 123,
            "child": {
                "t_c": "C",
                "http://psi.test.com/hello": "http://psi.foo.com/world",
                "http://psi.tests.com/s": "bye"
            }
        }
    }

The transform will output the following compact/"compressed" transformed entity:

::

    {
        "_id": "<test:2>",
        "<test:name>": "John",
        "born": "1980-01-23",
        "<test:code>": "AB32",
        "status": {
            "<foo:married>": True,
            "spouse": "Pam",
            "code": 123,
            "url1": "~rhttp://www.foo.com",
            "url2": "~rfoo:url2",
            "child": {
                "t_c": "C",
                "<test:hello>": "<foo:world>",
                "http://psi.tests.com/s": "bye"
            }
        }
    }

The undirected graph transform
------------------------------

The undirected graph transform transforms a list of properties representing nodes in a graph into all its
possible sets of edges, forming a complete graph. The transform will generate all possible edges in the
graph, which will be twice the number of entities as there are values in the aggregate of the list of properties given.
See the example section for an example.

Prototype
^^^^^^^^^

::

    {
        "type": "undirected_graph",
        "nodes": ["_id", "sameAs"],
        "from": "from-property",
        "to": "to-property"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``nodes``
     - List<String>
     - A list of entity property names that should be used to pick the nodes of the graph. The properties must refer
       to a value that is either a string or a URI, or a list of strings or URIs. No other value types are allowed in
       the transform.
     - ["_id", "sameAs"]
     -

   * - ``from``
     - String
     - The name of the property to use as "from" point in the generated entity for an edge in the graph.
     - "from"
     -

   * - ``to``
     - String
     - The name of the property to use as the "to" point in the generated entity for an edge in the graph.
     - "to"
     -

Example
^^^^^^^

Given the configuration:

::

    {
        "transform": [
           {
             "type": "undirected_graph",
             "nodes": ["_id", "map"],
             "from": "from",
             "to": "to"
           }
        ]
    }

And the input entity:

::

    {
       "_id": "foo",
       "map": ["bar", "zoo"]
    }

The transform will output the following edges of the graph as entities on its output stream:

::

   {
       "_id": "foo.bar",
       "from": "foo",
       "to": "bar"
   }

   {
       "_id": "foo.zoo",
       "from": "foo",
       "to": "zoo"
   }

   {
       "_id": "bar.foo",
       "from": "bar",
       "to": "foo"
   }

   {
       "_id": "bar.zoo",
       "from": "bar",
       "to": "zoo"
   }

   {
       "_id": "zoo.foo",
       "from": "zoo",
       "to": "foo"
   }

   {
       "_id": "zoo.bar",
       "from": "zoo",
       "to": "bar"
   }

.. _sink_section:

Sinks
=====

Sinks are at the receiving end of pipes and are responsible for writing entities into a internal dataset or a target system.
Sinks can support batching by implementing specific methods and accumulating entites in a buffer before writing the batch.

.. _dataset_sink:

The dataset sink
----------------

The dataset sink writes the entities it is given to an identified dataset. The configuration looks like:

Prototype
^^^^^^^^^

::

    {
        "name": "Name of sink",
        "type": "dataset",
        "dataset": "id-of-dataset"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``dataset``
     - String
     - The id of the dataset to write entities into. Note: if it doesn't exist before
       entities are written to the sink, it will be created on the fly.
     -
     - Yes

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "dataset",
            "name": "Northwind Customer dataset sink",
            "dataset": "Northwind:Customer",
        }
    }

.. _databrowser_sink:

The databrowser sink
--------------------

The databrowser sink writes the entities it is given to a Solr index to be displayed by the Sesam Databrowser
application. The input entitities are transformed to special Databrowser JSON documents before being sent off for
indexing.

The configuration looks like:

Prototype
^^^^^^^^^

::

    {
        "name": "Name of sink",
        "type": "databrowser",
        "system": "url-system-id",
        "prefixes": {
          "prefix": "http://expansionsion.com/foo",
          "other_prefix": "http://other.expansionsion.com/bar"
        }
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`Solr system <solr_system>` component to use.
     -
     - Yes

   * - ``prefixes``
     - Dictionary
     - A dictionary mapping prefix to their URI expansions. This prefix mapping
       will be used to expand CURIES into full URIs.
     -
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "databrowser",
            "name": "Index the Northwind customers",
            "url": "http://localhost:8893/solr/my_index",
        }
    }

The InfluxDB sink
-----------------

The InfluxDB sink is able to write entities representing measurement values over time to the InfluxDB time series database https://influxdata.com/.
A typical source for the entities written to it is the metrics data source, but any properly constructed entity can be
written to it. You will have to configure and provide a :ref:`InfluxDB system <influxdb_system>` id in the ``system`` property.


The expected form of an entity to be written to the sink is:

::

    {
        "_id": "toplevel/sublevel/parent/measurement",
        "property": value,
        "another_property": another_value,
    }

The ``_id`` property is expected to be a path-style composite value consisting of a top level node, a sublevel node, a parent node
and finally a measurement, for example "lake_node/sinks/test-sink/some-metric". The path components are used as ``tags``
in the influxdb database so metrics can be easily searched for in for example Grafana http://grafana.org/.

The rest of the properties on the entity should be on the form ``'string-key: numeric-value'``. There can be more than one
measurement per metric, for example a histogram of multiple sliding window values.

Prototype
^^^^^^^^^

::

    {
        "name": "Name of sink",
        "type": "influxdb",
        "system": "id-of-influxdb-system"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`InfluxDB system <influxdb_system>` component to use.
     -
     - Yes

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "influxdb",
            "name": "InfluxDB sink",
            "system": "my-influxdb-system"
        }
    }

.. _json_push_sink:

The JSON push sink
------------------

The JSON push sink implements a simple HTTP based protocol where
individual entities or lists of entities are ``POSTed`` as JSON data
to an :ref:`HTTP endpoint <url_system>`.

The protocol is described in additional detail in the :doc:`JSON Push
Protocol <json-push>` document. The serialisation of entities as JSON
is described in more detail :doc:`here <entitymodel>`.

This sink is compatible with :ref:`The HTTP endpoint source
<http_endpoint_source>`.

Prototype
^^^^^^^^^

::

    {
        "name": "Name of sink",
        "type": "json_push",
        "system": "url-system-id",
        "url": "url-to-http-endpoint"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`URL system <url_system>` component to use. If not present, a URL system
       with the ``_id`` set to the contents of the ``url`` property will be created automatically. Note that if the
       HTTP server requires authentication, you will have to create a URL system component explicitly.
     -
     -

   * - ``url``
     - String
     - The full URL to HTTP service implementing the ``JSON push protocol`` described.
     -
     - Yes

   * - ``batch_size``
     - Integer
     - The maximum number of entities to POST in each request. If there are
       more entities than this then they'll be split across multiple HTTP
       requests.
     - 100
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "json_push",
            "name": "Local JSON push service sink",
            "url": "http://localhost:9042/pipes/foo/entities"
        }
    }

.. _sdshare_push_sink:

The SDShare push sink
---------------------

The SDShare push sink is similar to the :ref:`JSON push sink <json_push_sink>`, but instead of posting JSON it
translates the inbound entities to ``RDF`` and ``POSTs`` them in ``NTriples`` form to a :ref:`HTTP endpoint <url_system>`
implementing the ``SDShare push protocol``.

Prototype
^^^^^^^^^

::

    {
        "name": "Name of sink",
        "type": "sdshare_push",
        "system":"url-system-id",
        "url": "url-to-http-endpoint",
        "graph": "uri-of-graph-to-post-to",
        "prefixes": {
            "a-prefix": "the-expansion"
        }
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`URL system <url_system>` component to use. If not present, a URL system
       with the ``_id`` set to the contents of the ``url`` property will be created automatically. Note that if the
       endpoint requires authentication, you will have to create a URL system component explicitly.
     -
     -

   * - ``url``
     - String
     - The full URL to HTTP service implementing the ``SDShare push protocol``.
     -
     - Yes

   * - ``graph``
     - String
     - A URI representing a graph to post the ``RDF ntriples`` to
     -
     - Yes

   * - ``prefixes``
     - Dictionary
     - A dictionary mapping prefix to their URI expansions. This prefix mapping
       will be used to expand CURIES into full URIs.
     -
     - Yes

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "sdshare_push",
            "name": "Local SDShare push service sink",
            "url": "http://localhost:8001/sdshare_push_service",
            "prefixes": {
                "dc": "http://purl.org/dc/elements/1.1/",
                "foaf": "http://xmlns.com/foaf/0.1/",
                "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#"
            }
        }
    }

.. _smsmessage_sink:

The SMS message sink
--------------------

The SMS message sink is capable of sending ``SMS`` messages based on the entities it receives. The message to send can be
constructed either by inline templates or from templates read from disk. These templates are assumed to be ``Jinja``
templates (http://jinja.pocoo.org/) with the entities properties available to the templating context. The template file
name can either be inlined in the configuration or embedded in the input entity. The SMS service to use must be
configured separately as a :ref:`system <system_section>` and its ``_id`` property given in the ``system`` property.
Currently, only the :ref:`Twilio provider <twilio_system>` is supported.

Prototype
^^^^^^^^^

::

    {
        "name": "Name of sink",
        "type": "sms",
        "system": "sms-system-id",
        "body_template": "static jinja template as a string",
        "body_template_property": "id-of-property-for-body-template",
        "body_template_file": "/static/full/file-name/to/jinja-template/on-disk",
        "body_template_file_property": "id-of-property-for-template-file-name",
        "recipients": "static,comma,separated,list,of,international,phonenumbers",
        "recipients_property": "id-of-property-to-get-recipients-from",
        "from_number": "static-international-phone-number-to-use-as-from-number",
    }

Properties
^^^^^^^^^^

The configuration must contain at most one of ``body_template``, ``body_template_property``, ``body_template_file`` or
``body_template_file_property``:

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`Twilio provider <twilio_system>` component to use.
     -
     - Yes

   * - ``body_template``
     - String
     - Should contain a ``Jinja template`` to use for constructing messages. The template will have access to all entity properties by name.
     -
     - Yes

   * - ``body_template_property``
     - String
     - Should contain a ``id`` of a property of the incoming entity to use for looking up the ``Jinja template``
       (i.e for inlining the templates in the entities). It should not be used at the same time as ``body_template``
       or ``body_template_file*``
     -
     -

   * - ``body_template_file``
     - String
     - Should refer to a text file on disk containing the ``Jinja template`` to use for constructing the body message
       from the incoming entity. It is mutually exclusive with the other ways of specifying a body template.
     -
     -

   * - ``body_template_file_property``
     - String
     - The ``id`` of a property in the incoming entity to use for looking up the file name of the ``Jinja template``
       on disk (i.e. inlining the body template filename in the entity). As with the other body template options,
       it is mutually exclusive in use.
     -
     -

   * - ``recipients``
     - String
     - Should contain a comma-separated list of internationalised phone-numbers to send the message constructed to.
       If this is not inlined in the entities via ``recipients_property`` (see below) the property is required.
     -
     - Yes

   * - ``recipients_property``
     - String
     - Should contain the id of the property to look up the recipients from the entity itself (i.e for inlining the
       recpients). If ``recipients`` (see abowe) is not specified, this property is mandatory and the propery
       referenced by it must exists and be valid for all entities.
     -
     - Yes

   * - ``from_number``
     - String
     - An international phone number to use as the sender of all messages
     -
     - Yes

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity. The
examples assume a :ref:`system component <system_section>` (i.e. a :ref:`Twilio service <twilio_system>`) has been
configured earlier:

::

    {
        "sink": {
            "type": "sms",
            "name": "Send SMS messages",
            "system": "twilio_service",
            "body_template": "SMS message: {{ message_prop_id }}",
            "recipients": "+4799887766,+4788776655",
            "from_number": "+4766554433"
        }
    }

In the above example the entities sent to the sink should have at least a single property ``message_prop_id``, i.e.:

::

    {
        "_id": "message_id",
        "message_prop_id": "This is the message to send",
        "some_other_property": "Some other value"
    }

An example where the template to use is included in the entity written to the sink:

::

    {
        "sink": {
            "type": "sms",
            "name": "Send SMS messages",
            "system": "twilio_service",
            "body_template_property": "body_template_property_id",
            "recipients": "+4799887766,+4788776655",
            "from_number": "+4766554433"
        }
    }

For the example above the entities sent to the sink should have at least a single property ``body_template_property_id``
and it also needs to have the properties references in the embedded template:

::

    {
        "_id": "message_id",
        "body_template_property_id": "SMS message: {{ message_prop_id }}",
        "message_prop_id": "This is the message to send",
        "some_other_property": "Some other value"
    }

You can also store the Jinja templates on disk and reference them in the same way via filenames instead of embedding
the templates in config or the entities themselves.


.. _solr_sink:

The Solr sink
-------------

The Solr sink writes the entities it is given to a Solr index. The input entity is converted to a JSON document and its
``_id`` property is converted to a JSON ``id`` property automatically. If you include your own ``id`` propery, it will
overwrite this generated property before being sent off for indexing.

Limitations
^^^^^^^^^^^

Due to the limited JSON datastructure allowed by Solr, there are some restrictions on the form of the entities accepted
by the sink:

* only "flat" entities are allowed - any child entities must be removed or merged into the root entity before
being sent to the sink.
* Lists properties are supported, but they can only contain a single type of property.
* Lists cannot contain other lists or entities.

Any properties not adhering to these rules are ignored (this is logged as a warning).

The configuration looks like:

Prototype
^^^^^^^^^

::

    {
        "name": "Name of sink",
        "type": "databrowser",
        "system": "url-system-id",
        "prefixes": {
          "prefix": "http://expansionsion.com/foo",
          "other_prefix": "http://other.expansionsion.com/bar"
        }
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`Solr system <solr_system>` component to use.
     -
     - Yes

   * - ``prefixes``
     - Dictionary
     - A dictionary mapping prefix to their URI expansions. This prefix mapping
       will be used to expand CURIES into full URIs.
     -
     -

.. _sparql_sink:

The SPARQL sink
---------------

The SPARQL sink converts entities to RDF statements and writes them to a graph in a triplestore via a SPARQL compatible
endpoint.

Prototype
^^^^^^^^^

::

    {
        "name": "Name of sink",
        "type": "sparql",
        "system": "id-of-url-system"
        "graph": "http://uri.of/graph",
        "do_diff": false,
        "write_sdshare_updated": true,
        "prefixes": {
            "some_prefix" : "http://some/uri/",
            "other_prefix" : "http://another.uri/schema/"
        }
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``url``
     - String
     - The URL of the SPARQL endpoint to use.
     -
     - Yes

   * - ``system``
     - String
     - The id of a :ref:`URL system <url_system>` component to use. If not given, one will be automatically generated
       based on the ``url`` propery. Note that if the SPARQL endpoint uses authentication, you will have to create
       a URL system to use.
     -
     -

   * - ``graph``
     - String
     - A full URI for the graph to write the entities into.
     -
     - Yes

   * - ``do_diff``
     - Boolean
     - Tell the sink to compute the difference between the target graph RDF statements and the RDF statements generated
       by converting the input entity to RDF. This ensures the minimum number of write operations to the endpoint.
       This does however come with the cost of (many) more read operations. Use this option if your entities are large
       and/or there is large amounts of changes flowing through the sink on average.
     -
     - false

   * - ``write_sdshare_updated``
     - Boolean
     - Tell the sink to automatically insert SDShare updated predicates with the generated RDF statements written to
       the endpoint. Note that the local UTC time is currently used for this timestamp.
     -
     - true

   * - ``prefixes``
     - Object
     - A mapping of RDF prefixes (curies) to URIs. This is used to expand properties on the form "<foo:property>" to
       its full URI predicate ("http://example.com/foo/propery" for example). The common RDF prefixes are built-in
       and you don't have to provide the mapping for it. If no prefix mappings are given, the built-in and node-wide
       prefixes are used instead.
     -
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "name": "Sink for inserting Fylke data into a remove triplestore",
            "type": "sparql",
            "url": "http://virtuoso-itest.cloudapp.net:8890/sparql",
            "graph": "http://example.com/fylketest",
            "do_diff": true,
            "write_sdshare_updated": true,
            "prefixes": {
                "geo_fylke" : "http://psi.datanav.info/difi/geo/fylke/",
                "geo" : "http://psi.datanav.info/difi/geo/schema/"
            }
    }


The SQL sink
------------

The SQL sink writes entities to a SQL database table. You will have to configure and provide a :ref:`SQL system <sql_system>` id in the ``system`` property.

The expected form of an entity to be written to the sink is:

::

    {
        "columnname1": value,
        "columnname2": another_value,
    }


Prototype
^^^^^^^^^

::

    {
        "name": "Name of sink",
        "type": "sql",
        "system": "id-of-sql-system"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`SQL system <sql_system>` component to use.
     -
     - Yes

   * - ``table``
     - String
     - Refers to a fully qualified table name in the database system, not including schema, which if needed must be
       set separately.
     -
     - Yes

   * - ``schema``
     - String
     - If a specific schema within a database is needed, you must provide its name in this property.
       Do *not* use schema names in the ``table`` property.
     -
     -


Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "sql",
            "name": "SQL sink",
            "system": "my-sql-system",
            "table": "customers"
        }
    }



.. _mail_message_sink:

The mail message sink
---------------------

The mail message sink is capable of sending mail messages based on the entities it receives. The message to send can be
constructed either by inline templates or from templates read from disk. These templates are assumed to be ``Jinja
templates`` (http://jinja.pocoo.org/) with the entities properties available to the templating context. The template file
name can either be embedded in the configuration or in the input entity. The mail server settings have to
be registered in a :ref:`SMTP system <smtp_system>` component in advance and its ``_id`` put in the ``system``
property of the sink.

Prototype
^^^^^^^^^

::

    {
        "name": "Name of sink",
        "type": "mail",
        "system": "smtp-system-id",
        "body_template": "static jinja template as a string",
        "body_template_property": "id-of-property-to-get-as-a-body-template",
        "body_template_file": "/static/full/file-name/to/jinja-template/on-disk",
        "body_template_file_property": "id-of-property-for-body-template-filename",
        "subject_template": "static jinja template as a string",
        "subject_template_property": "id-of-property-to-get-as-a-subject-template",
        "subject_template_file": "/static/full/file-name/to/jinja-template/on-disk",
        "subject_template_file_property": "id-of-property-for-subject-template-filename",
        "recipients": "static,comma,separated,list,of,email,addresses",
        "recipients_property": "id-of-property-to-get-recipients-from",
        "mail_from": "static@email.address"
    }

Properties
^^^^^^^^^^

The configuration must contain at most one of ``body_template``, ``body_template_property``, ``body_template_file`` or
``body_template_file_property``. The same applies to ``subject_template``.

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`SMTP system <smtp_system>` to use.
     -
     - Yes

   * - ``body_template``
     - String
     - Should contain a ``Jinja template`` to use for constructing messages. The template will have access to all entity properties by name.
     -
     - Yes

   * - ``body_template_property``
     - String
     - Should contain a ``id`` of a property of the incoming entity to use for looking up the ``Jinja template``
       (i.e for inlining the templates in the entities). It should not be used at the same time as ``body_template``
       or ``body_template_file*``
     -
     -

   * - ``body_template_file``
     - String
     - Should refer to a text file on disk containing the ``Jinja template`` to use for constructing the body message
       from the incoming entity. It is mutually exclusive with the other ways of specifying a body template.
     -
     -

   * - ``body_template_file_property``
     - String
     - The ``id`` of a property in the incoming entity to use for looking up the file name of the ``Jinja template``
       on disk (i.e. inlining the body template filename in the entity). As with the other body template options,
       it is mutually exclusive in use.
     -
     -

   * - ``subject_template``
     - String
     - Should contain a ``Jinja template`` to use for constructing subjects for the email messages. The template
       will have access to all entity properties by name
     -
     - Yes

   * - ``subject_template_property``
     - String
     - Should contain a ``id`` of a property of the incoming entity to use for looking up the ``Jinja template``
       (i.e for inlining the templates in the entities). It should not be used at the same time as ``subject_template``
       or ``subject_template_file*``
     -
     -

   * - ``subject_template_file``
     - String
     - Should refer to a text file on disk containing the ``Jinja template`` to use for constructing the message subject
       from the incoming entity. It is mutually exclusive with the other ways of specifying a body template.
     -
     -

   * - ``subject_template_file_property``
     - String
     - The ``id`` of a property in the incoming entity to use for looking up the file name of the ``Jinja template``
       on disk (i.e. inlining the subject template filename in the entity). As with the other subject template options,
       it is mutually exclusive in use.
     -
     -

   * - ``recipients``
     - String
     - Should contain a comma-separated list of email addresses to send the message constructed to. If this is not
       inlined in the entities via ``recipients_property`` (see below) this property is mandatory.
     -
     - Yes

   * - ``recipients_property``
     - String
     - Should contain the id of the property to look up the recpients from the entity itself (i.e for inlining the
       recpients). If ``recipients`` (see abowe) is not specified, this property is mandatory and the propery
       referenced by it must exists and be valid for all entities.
     -
     -

   * - ``mail_from``
     - String
     - An email address to use as the sender of all messages
     -
     - Yes

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "mail",
            "name": "Send mail messages",
            "system": "our-smtp-server",
            "body_template": "Mail message body: {{ message_prop_id }}",
            "subject_template": "Subject: {{ subject_prop_id }}",
            "recipients": "foo@bar.com,info@example.com",
            "mail_from": "all@of.us"
        }
    }

In the above example the entities sent to the sink should have at least a single property ``message_prop_id``, i.e.:

::

    {
        "_id": "message_id",
        "message_prop_id": "This is the message to send",
        "subject_prop_id": "This is the subject of the message to send",
        "some_other_property": "Some other value"
    }

As for the :ref:`SMS sink <smsmessage_sink>`, you can either supply a subject or body template embedded in the entities you
write to the sink. You can also reference filenames either in the config or embedded in the entities.

Example of filenames referenced in the config:

::

    {
        "sink": {
            "type": "mail",
            "name": "Send mail messages",
            "system": "our-smtp-server",
            "body_template_file": "/path/to/file/bodytemplate.jinja",
            "subject_template_file": "/path/to/file/subjecttemplate.jinja",
            "recipients": "foo@bar.com,info@example.com",
            "mail_from": "all@of.us"
        }
    }

The null sink
-------------

The null sink is the equivalent of the empty data source; it will discard any entities written to it and do nothing (it
never raises an error):

Prototype
^^^^^^^^^

::

    {
        "name": "Name of sink",
        "type": "null"
    }

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "null",
            "name": "Sink that doesn't do anything",
        }
    }

.. _system_section:

Systems
=======

A system component represents a computer system that can provide data entities. Its task is to provide common properties
and services that can be used by several data sources, such as connection pooling, authentication settings,
communication protocol settings and so on.

.. _sql_system:

The SQL system
--------------

The SQL system component represents a RDBMS and contains the necessary information to establish a connection
to the RDBMS and manage these connections among the sources that read from it. The configuration of the sql
system should be made available before any sources that use it. It can also provide source configurations for reading
from all tables it can introspect from the RDBMS schema.

Prototype
^^^^^^^^^

::

    {
        "_id": "sql_system_id",
        "type": "system:sql",
        "name": "The Foo Database",
        "connection_string": "foo://database/SID",
        "timezone": "UTC",
        "pool_size": 10,
        "pool_timeout": 30,
        "pool_max_overflow": 10
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``connection_string``
     - String
     - Contains a SQLAlchemy connection URL used for establishing a connection to the RDBMS. See
       http://docs.sqlalchemy.org/en/latest/core/engines.html for details of the formatting of this string for the
       various databases supported. A Sesam Node currently supports SQLite, Oracle, MS SQL Server, MySQL and Postgresql
       drivers.
     -
     - Yes

   * - ``timezone``
     - String
     - The local timezone for the database server. It is used for any date(time) objects returned that doesn't have any
       timezone information. The default is the UTC timezone. All the official timezone names are supported,
       i.e. "UTC", "GMT", "EST" etc. You can also use the indirect "Continent/City" format, for example "Europe/Oslo"
       (see `the complete list <http://twiki.org/cgi-bin/xtra/tzdatepick.html>`_ for which cities are supported).
     - "UTC"
     -

   * - ``pool_size``
     - Integer
     - The target maximum number of concurrent connections to the database
     - 10
     -

   * - ``pool_timeout``
     - Integer
     - The number of seconds to wait before a idle connection is terminated
     - 30
     -

   * - ``pool_max_overflow``
     - Integer
     - How many connections over the ``pool_size`` are allowed before refusing to establish a incoming connection. This
       means that the absolute hard limit of connections in a connection pool is ``pool_size`` + ``pool_max_overflow``.
     - 10
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

Example SQL Lite configuration:

::

    {
        "_id": "northwind_db",
        "name": "Northwind example database",
        "type": "system:sql",
        "connection_string": "sqlite:///lake/exampledata/Northwind.db"
    }

Example Oracle configuration:

::

    {
        "_id": "oracle_db",
        "name": "Oracle test database",
        "type": "system:sql",
        "connection_string": "oracle://system:oracle@oracle:1521/XE?charset=utf8"
    }

Example MS SQL Server configuration:

::

    {
        "_id": "sqlserver_db",
        "name": "MS SQL Server test database",
        "type": "system:sql",
        "connection_string": "mssql+pymssql://user:password@localhost:1433/testdb?charset=utf8"
    }

.. _fake_system:

The fake system
---------------

The fake component represents a generic fake data source. It is meant to be used in conjunction with the :ref:`fake source <fake_source>`
to produce test data, and is responsible for providing fixed sets of ids so "fake" entities from different fake sources
can be linked.

Prototype
^^^^^^^^^

::

    {
        "_id": "fake_system_id",
        "type": "system:fake",
        "name": "The Fake System",
        "id_pools": {
            "pool1": {
               "seed": 1234,
               "min": 1,
               "max": 10
            },
            "pool2": {
               "seed": 1234,
               "min": 100,
               "max": 10000
            }
        }
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``id_pools``
     - Object
     - Contains a mapping of names pool objects that can be used by a :ref:`fake source <fake_source>` to draw
       id values from. The values are integers (which is cast to a string for ``_id`` properties) and the maximum number
       of entries in the set is given by ``max``-``min``. The number of ``entities`` of a fake source must not exceed
       this number, or an error will be raised (i.e. it should be equal or less).
     -
     - Yes

   * - ``seed``
     - Integer
     - A random seed to be used with the pool.
     - 1234
     -

   * - ``min``
     - Integer
     - The minimum value in the pool set
     - 0
     -

   * - ``max``
     - Integer
     - The maximum value in the pool set
     - 100000000
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

See the :ref:`example configuration <fake_system_example>` in the fake source section.

.. _influxdb_system:

The InfluxDB system
-------------------

The InfluxDB system represents a InfluxDB system and all the information needed to connect and write to it.
It is used in conjunction with the :ref:`InfluxDB sink <influxdb_sink>` to write entities to a InfluxDB time series
database.

Prototype
^^^^^^^^^

::

    {
        "_id": "influxdb-system-id",
        "name": "Name of InfluxDB system",
        "type": "system:influxdb",
        "host": "localhost",
        "port": 8086,
        "username": "root",
        "password": "root",
        "database": "Sesam Node",
        "ssl": false,
        "verify_ssl": false,
        "timeout": None,
        "use_udp": false,
        "udp_port": 4444
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``host``
     - String
     - The ``FQDN`` of the InfluxDB server
     - "localhost"
     -

   * - ``port``
     - Integer
     - The TCP port of the InfluxDB service
     - 8086
     -

   * - ``username``
     - String
     - The user to authenticate as against the InfluxDB service
     - "root"
     -

   * - ``password``
     - String
     - The password to use for authenticating with the InfluxDB service
     - "root"
     -

   * - ``database``
     - String
     - The name of the database to create and write into. Note that it will be created automatically
       if it doesn't exist.
     - "sesam_node"
     -

   * - ``verify_ssl``
     - Boolean
     - Flag to indicate that the client hould verify the server's ssl certificate before initiating
       communication with it
     - false
     -

   * - ``timeout``
     - Integer
     - If set, sets the timeout to a specified number of seconds. Default is not set and indicates
       no timeout (i.e. infitite wait). Note that this can result in hanging services if the server is not reachable.
     -
     -

   * - ``use_udp``
     - Boolean
     - Indicate to the client to use the UDP protocol rather than TCP when talking to the InfluxDB server.
       The default is ``false`` which means ``use TCP``. UDP can in certain high-volume scenarios be more efficient
       than TCP due to its simplicity
     - false
     -

   * - ``udp_port``
     - Integer
     - The ``UDP`` port to use if ``use_udp`` is set to ``true``.
     - 4444
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "my_influxdb_system",
        "type": "system:influxdb",
        "name": "My InfluxDB database",
        "host": "localhost",
        "port": 8086,
        "username": "root",
        "password": "root",
        "database": "my_database",
    }

.. _ldap_system:

The LDAP system
---------------

The LDAP system contains the configuration needed to communicate with a LDAP system. It is used by
:ref:`LDAP sources <ldap_source>` to stream entities from LDAP catalogs.

It supports the following properties:

Prototype
^^^^^^^^^

::

    {
        "host": "FQDN of LDAP host",
        "port": 389,
        "use_ssl": false,
        "username": "authentication-username-here",
        "password": "authentication-password-here",
        "charset": "latin-1"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``host``
     - String
     - The fully qualified domain name (``FQDN``) of the LDAP host server
     - "localhost"
     -

   * - ``port``
     - Integer
     - The TCP port of the LDAP service.
     - 389
     -

   * - ``use_ssl``
     - Boolean
     - Indicates to the client whether to use a secure socket layer (``SSL``) or not when communicating with the LDAP service
     - false
     -

   * - ``username``
     - String
     - The user to authenticate as against the LDAP service. If not set, no authentication will be attempted.
     -
     -

   * - ``password``
     - String
     - The password to use for authenticating with the LDAP service. Required if ``username`` is set.
     -
     - Yes

   * - ``charset``
     - String
     - The charset used to encode strings in the LDAP database. Defaults to ``"latin-1"`` aka ``"ISO-8859-1"``,
       as ``"UTF-8"`` is usually not the default encoding in LDAP catalogs at the time of writing.
     - "latin-1"
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "bouvet_ldap",
        "name": "Bouvet LDAP server",
        "type": "system:ldap",
        "host": "dc1.bouvet.no",
        "port": 389,
        "username": "bouvet\\some-user",
        "password": "********"
    }


.. _smtp_system:

The SMTP system
---------------

The SMTP system represents the information needed to connect to a SMTP server for sending emails. It is used in
conjunction with the :ref:`mail message sink <mail_message_sink>` to construct and send emails based on the entities it
receives.

Prototype
^^^^^^^^^

::

    {
        "_id": "id-of-system",
        "name": "Name of system",
        "type": "system:smtp",
        "smtp_server": "localhost",
        "smtp_port": 25,
        "smtp_username": None,
        "smtp_password": None,
        "use_tls": false,
        "max_per_hour": 1000
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``smtp_server``
     - String
     - Contains a ``FQDN`` of the ``SMTP service`` to use
     - "localhost"
     -

   * - ``smtp_port``
     - Integer
     - The TCP port to use when talking to the ``SMTP service``
     - 25
     -

   * - ``smtp_username``
     - String
     - The username to use when authenticating with the ``SMTP service``. If not set, no authentication is attempted.
     -
     -

   * - ``smtp_password``
     - String
     - The password to use if ``smtp_username`` is set. It is mandatory if the ``smtp_username`` is provided.
     -
     - Yes

   * - ``use_tls``
     - Boolean
     - Indicating to the client to use ``TLS encryption`` when communicating with the ``SMTP service``.
     - false
     -

   * - ``max_per_hour``
     - Integer
     - The maximum number of messages to send for any hour. It is used for stopping run-away message sending in
       development or testing. Note that any message not sent will be logged but discarded.
     - 1000
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "our-smtp-server",
        "type": "system:smtp",
        "name": "Our SMTP Server",
        "smtp_server": "localhost",
        "smtp_port": 25,
        "smtp_username": "some-user",
        "smtp_password": "*********",
        "max_per_hour": 100000
    }

.. _solr_system:

The Solr system
---------------

The Solr system represents the information needed to connect to a Solr server for indexing JSON documents. It is used in
conjunction with the :ref:`solr sink <solr_sink>` or the :ref:`databrowser sink <databrowser_sink>` simks.

Prototype
^^^^^^^^^

::

    {
        "_id": "id-of-system",
        "name": "Name of system",
        "type": "system:solr",
        "url": "http://localhost:8983/solr/",
        "commit_within": null,
        "timeout": 30,
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``url``
     - String
     - Contains a full URL to the Solr dataset to read/write documents from
     - "http://localhost:8983/solr/"
     -

   * - ``commit_within``
     - Integer
     - The number of milliseconds to wait until committing (default is to autocommit once per document). This is used
       to set up commit batching. The default is null (i.e. not set) which means commit for each document.
     - null
     -

   * - ``timeout``
     - Integer
     - The number of seconds to wait for a response from the Solr server when adding/committing data
     - 30
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "our-solr-server",
        "type": "system:solr",
        "name": "Our Solr Server",
        "smtp_server": "http://localhost:8983/solr/ourdata/",
        "commit_within": 3000,
        "timeout": 60
    }

.. _twilio_system:

The Twilio system
-----------------

The Twilio system is a ``SMS system`` used with :ref:`SMS message sinks <smsmessage_sink>` to construct
and send SMS messages from entities. It has the following properties:

Prototype
^^^^^^^^^

::

    {
        "_id": "system-id",
        "name": "Service name",
        "type": "system:twilio",
        "account": "twilio-account-number",
        "token": "twilio-api-token",
        "max_per_hour": 1000
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``account``
     - String
     - The ``Twilio`` account number
     -
     - Yes

   * - ``token``
     - String
     - The ``Twilio`` API token
     -
     - Yes

   * - ``max_per_hour``
     - Integer
     - The maximum number of messages to send for any hour. It is used for stopping run-away message sending in
       development or testing. Note that any message not sent will be logged but discarded.
     - 1000
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
         "_id": "twilio_service",
         "type": "system:twilio",
         "name": "Twilio Service",
         "account": "12334567890",
         "token": "ABCD-ADEF-FAA1-1234",
         "max_per_hour": 100000
    }

.. _url_system:

The URL system
--------------

The URL system represents a HTTP server serving requests from a base url. It can also represent local files
either by just passing in a local path in its ``base_url`` property or using a ``file://`` protocol in the URL.
It provides session handling, connection pooling and authentication services to sources and sinks which need to
communicate with a HTTP server.

Prototype
^^^^^^^^^

::

    {
        "_id": "id-of-system",
        "name": "Name of system",
        "type": "system:url",
        "base_url": "http://host:port/path",
        "username": None,
        "password": None,
        "verify_ssl": false,
        "authentication": "basic"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``base_url``
     - String
     - The full URL of the base url of the HTTP server.
     -
     - Yes

   * - ``username``
     - String
     - The username to use when authenticating with the ``HTTP server``. If not set, no authentication is attempted.
     -
     -

   * - ``password``
     - String
     - The password to use if ``username`` is set. It is mandatory if the ``username`` is provided.
     -
     - Yes

   * - ``verify_ssl``
     - Boolean
     - Indicate to the client if it should attempt to verify the SSL certificate when communicating with the
       ``HTTP server`` over SSL/TLS.
     - false
     -

   * - ``authentication``
     - String
     - What kind of authentication protocol to use when ``username`` is set. The default is basic authentication.
     - "basic"
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "our-http-server",
        "type": "system:url",
        "name": "Our HTTP Server",
        "base_url": "http://our.domain.com/files"
    }

.. _pump_section:

Pumps
=====

Pumps are responsible for "pumping" data through the :ref:`pipe <pipe_section>` by reading :doc:`entities <entitymodel>`
from a :ref:`source <source_section>` and writing them into a :ref:`sink <sink_section>`. The pump is also responsible
for retrying failed writes of entities and logging its activity. It can also log ultimately failed entities to a "dead letter"
dataset for manual inspection. Pumps log their :doc:`execution history <pump-execution>` in a internal dataset with
the id "system:pump_execution:<pump_id>". See the :doc:`chapter on the pump execution dataset <pump-execution>` for more
details about the contents of this dataset.

Prototype
---------

::

    {
        "_id": "pump_id",
        "type": "datasync",
        "name": "My Pipe pump",
        "schedule_interval": 15000,
        "cron_expression": "* * * * * *",
        "rescan_run_count": 10,
        "rescan_cron_expression": "* * * * * *",
        "run_at_startup": false,
        "max_read_retries": 0,
        "max_retries_per_entity": 5,
        "max_consecutive_write_errors": 1,
        "max_write_errors_in_retry_dataset": 0,
        "dead_letter_dataset": "dead-letter-dataset-id"
    }

Properties
----------

A note on the required properties: a pump configuration needs to have either a ``schedule_interval`` *or* a
``cron_expression`` property to govern when the pump should be run. They are mutually exclusive with the
``cron_expression`` taking precedence if both are present.

If you are unfamiliar with `cron expressions <https://en.wikipedia.org/wiki/Cron>`_, you can read more of how
they are formatted in the :doc:`Cron Expressions <cron-expressions>` document.

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``schedule_interval``
     - Integer
     - The number of milliseconds between runs. It is a required field if no ``cron_expression`` is present. It is
       mutually exclusive with the ``cron_expression`` property.
     -
     - Yes

   * - ``cron_expression``
     - String
     - A cron expression that indicates when the pump should run. It is a required field if no ``schedule_interval`` is
       specified. It is mutually exclusive with the ``schedule_interval`` property.
     -
     - Yes

   * - ``rescan_run_count``
     - Integer
     - How many times the pump should run before scheduling a complete rescan of the source of the pipe that the pump
       is part of. It is mutually exclusive with the ``rescan_cron_expression`` property.
     -
     -

   * - ``rescan_cron_expression``
     - String
     - A cron expression that indicates when the pump should schedule a full rescan of the source of the pipe the pump
       is part of. It is mutually exclusive with the ``rescan_run_count`` property.
     -
     -

   * - ``run_at_startup``
     - Boolean
     - A flag that indicates if the pump should run when the Sesam Node starts up, in addition to the normal schedule
       specified by the ``schedule_interval`` or ``cron_expression`` properties.
     - false
     -

   * - ``max_read_retries``
     - Integer
     - A counter that indicates to the pump how many times it should retry when failing to read a entity from a source.
       The default (0) means that it should not retry but log an error immediately when encountering read errors.
     - 0
     -

   * - ``max_retries_per_entity``
     - Integer
     - A counter that indicates to the pump how many times it should retry a failing entity when writing to a sink before
       giving up on it, which in case it can optionally write it to a ``dead_letter_dataset`` (if specified).
     - 5
     -

   * - ``max_consecutive_write_errors``
     - Integer
     - A counter that indicates to the pump how many consecutive write errors it tolerates before terminating the
       current run. The default (1) means it will terminate after the first write error it encounters.
     - 1
     -

   * - ``max_write_errors_in_retry_dataset``
     - Integer
     - A counter that indicates to the pump how many write errors it accepts in its execution history dataset. If the number of
       retryable and not "dead" failed entities in the dataset exceeds this number, the pump will refuse to
       write any more failed entities to the execution dataset and terminate, even if the ``max_retries_per_entity`` or
       ``max_retries_per_entity`` is not reached at that point. This purpose of this property is to limit the size of the
       pump execution dataset in the case where a target system is unrechable (or misconfigured). The default value (0) effectively
       disables retries for write errors.
     - 0
     -

Example configuration
---------------------

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

A scheduled pump running every 30 seconds, no retries or dead letter dataset:

::

    {
        "pump": {
           "type": "datasync",
           "name": "My Pipe pump",
           "schedule_interval": 30000
       }
    }

A cron pump running every day at midnight with max 5 retries, maximum 100 retries in the execution log and a dead letter
dataset. Also max ten consecutive write failures allowed:

::

    {
        "pump": {
           "type": "datasync",
           "name": "My Pipe pump",
           "cron_expression": "0 0 0 * * *",
           "max_retries_per_entity": 5,
           "max_consecutive_write_errors": 10,
           "max_write_errors_in_retry_dataset": 100,
           "dead_letter_dataset": "pump-dead-letters"
       }
    }

A scheduled pump running every 30 seconds but do a full rescan of the source every full hour. No retries or dead letter
datasets:

::

    {
        "pump": {
           "type": "datasync",
           "name": "My Pipe pump",
           "schedule_interval": 30000,
           "rescan_cron_expression": "0 0 * * * *"
       }
    }

A scheduled pump running every 5 minutes from 14:00 and ending at 14:55, AND fire every 5 minutes starting at
18:00 and ending at 18:55, every day. No retries or dead letter datasets:

::

    {
        "pump": {
           "type": "datasync",
           "name": "My Pipe pump",
           "cron_expression": "0 0/5 14,18 * * ?"
       }
    }


.. _pipes_revisited:

Pipes revisited
===============

As mentioned earlier, in the :ref:`pipe section <pipe_section>`, there is a special "short hand" configuration for
one of the most used pipes; pipes pumping entities from RDBMS tables to an internal dataset. Since this is an often
encountered usecase, we have condensed the information needed into a single url-style form:

::

    [
        {
           "_id": "Northwind",
           "type": "system:sql",
           "name": "Northwind SQLite database",
           "connection_string": "sqlite:///lake/exampledata/Northwind.db"
        },
        {
           "_id": "Northwind:Orders",
           "type": "pipe",
           "name": "Orders from northwind",
           "short_config": "sql://Northwind/Orders"
        }
    ]

Currently, only the :ref:`sql system <sql_system>` and :ref:`source <sql_source>` is supported
though other short forms may be added at a later time. The above example using the ``short_config`` form is equivalent
to this fully expanded pipe configuration:

::

    [
        {
           "_id": "Northwind",
           "type": "system:sql",
           "connection_string": "sqlite:///lake/exampledata/Northwind.db"
        },
        {
           "_id": "Northwind:Orders",
           "type": "pipe",
           "source": {
               "name": "Orders from northwind - source",
               "type": "sql",
               "system": "Northwind",
               "table": "Orders"
           },
           "sink": {
               "name": "Orders from northwind - sink",
               "type": "dataset",
               "dataset": "Northwind:Orders"
           },
           "pump": {
               "name": "Orders from northwind - pump",
               "schedule_interval": 15000
           }
        }
    ]

You can combine the short form with properties from the :ref:`dataset sink <dataset_sink>`, :ref:`sql source <sql_source>`
and specific :ref:`pump <pump_section>` properties, as long as the ``_id`` and ``type`` properties aren't overridden, for example
changing the pump schedule and startup flag:

::

    [
        {
           "_id": "Northwind",
           "type": "system:sql",
           "name": "Northwind SQLite database",
           "connection_string": "sqlite:///lake/exampledata/Northwind.db"
        },
        {
           "_id": "Northwind:Orders",
           "type": "pipe",
           "name": "Orders from northwind",
           "short_config": "sql://Northwind/Orders",
           "pump": {
               "schedule_interval": 60000,
               "run_at_startup": true
           }
        }
    ]
