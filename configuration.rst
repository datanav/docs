
=============================
Component configuration guide
=============================


.. contents:: Table of Contents


General
=======

The Sesam Node is configured using *JSON* structures, either on disk or by posting to the *API* (see the API section). The main
concepts to configure for a node is the external systems and the *flow* between them and the *Sesam Node*. Also flows within
the Sesam Node is configured the same way.

The node configuration is a *JSON list* of *external system* configurations and *pipe* configurations describing
the flows into, within and out of the Sesam Node from these external systems. These configuration entities are *JSON dictionaries*
on the general form:

::

    [
        {
            "_id": "some-node-wide-unique-id"
            "type": "component-type:component-subtype",
            "some-property": "some value",
            ...
        },
        {
            "_id": "some-other-node-wide-unique-id"
            "type": "component-type:component-subtype",
            "some-other-property": "some other value",
        ...
        },
        ...
    ]


Flows
=====

A *flow* is a set of *pipes* describing the flow of data *entities* from an external system, between *datasets* inside
the Sesam Node and finally out of the Sesam Node to a external system. At the sources of each individual pipe in such a flow,
optional *transforms* can be specified that transforms the entities streaming from the source to a another form
before arriving at the destination.

This transform is described using a domain specific language called *"DTL"* (see the DTL section for
more detail). The transformed entities can be entirely or partially constructed from entities from other datasets,
like joins in *SQL select* statements, with the main difference that the result is persisted for each pipe in the flow.

The Sesam Node keeps track of the dependencies between datasets through DTL transforms in such a way that only changes
are propagated along the flow based on what entities are changed at the ultimate source of the flows. This leads to
a very efficient handling of entity streams within the Sesam Node.

Pipes
=====

A pipe is a *triple* of a *source*, *sink* and *data sync task*. The task "pumps" data in the form of entities from the source
to the sink at regular or scheduled intervals.

The configuration of a pipe has two forms; one "complete" form and one *short hand* form. Let's describe the "complete"
form first and revisit the shorthand form after describing the various sinks and sources available in the Sesam Node core:

::

    {
       "_id": "pipe-id",
       "type": "pipe",
       "source": {
         ...
       },
       "sink": {
         ...
       },
       "task": {
         ...
       }
    }

Sources
=======

Sources provide *streams of entities* as input to the pipes which is the building blocks for the flows in the Sesam Node. These entities can take
*any* shape (i.e. they can also be nested), and have a single required property: **_id**. This ``_id`` field must be *unique within a flow* for
a specific logical entity. There may however exist multiple *versions* of this entity within a flow.
Sources can also support ``since`` monikers or markers which lets them pick up where the previous stream of entities left off, sort
of like a bookmark in the entitiy stream. The ``since`` marker is opaque to the rest of the Sesam Node components, and is assumed
to be interpretable *only by the source*. Within an entity, the marker is carried in the ``_updated`` property if supported
by the source.

The Sesam Node supports a diverse set of core data sources:

The dataset source
------------------

The dataset source is one of the most commonly used datasources in a Sesam Node. It simply presents a stream of entities from a
dataset stored in a Sesam Node. Its configuration is very simple and looks like:

::

    {
       "_id": "id-of-source",
       "type": "source:dataset",
       "dataset": "id-of-dataset",
       "supports_since": true,
       "include_previous_versions": false
    }

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

   * - ``supports_since``
     - Boolean
     - Flag to indicate whether to use a ``since`` marker when reading from the dataset, i.e. to start at
       the beginning each time or not.
     - true
     -

   * - ``include_previous_versions``
     - Boolean
     - If the ``include_previous_versions`` flag is set to ``false``, the data source will only return the latest
       version of any entity for any unique ``_id`` value in the dataset. This is the default behaviour.
     - false
     -

The union datasets source
-------------------------

The union datasets source is similar to the ``dataset source``, except
it can process several datasets at once and keep track of each one in
its ``since`` marker handler:

::

    {
       "_id": "id-of-source",
       "type": "source:union_datasets",
       "datasets": ["a-id-of-dataset","another-id-of-another-dataset"],
       "supports_since": true,
       "include_previous_versions": false
    }

The configuration of this source is identical to the ``dataset`` source, except ``datasets`` can be a list of datasets ids.

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``datasets``
     - List
     - A list of datasets ids (strings).
     -
     - Yes

   * - ``supports_since``
     - Boolean
     - Flag to indicate whether to use a ``since`` marker when reading from the dataset, i.e. to start
       at the beginning each time or not.
     - true
     -

   * - ``include_previous_versions``
     - Boolean
     - If the ``include_previous_versions`` flag is set to ``false``, the data source will only return the
       latest version of any entity for any unique ``_id`` value in the dataset. This is the default behaviour.
       the ``_id`` property.
     - false
     -

The relational database source
------------------------------

The relational database source is one of the most commonly used data sources. In short, it presents database ``relations``
(i.e. ``tables``, ``views`` or ``queries``) as a entitiy stream to the Sesam Node. It has several options, all of which are presented below with
their default values:

::

    {
       "_id": "id-of-source",
       "type": "source:relational",
       "external_system": "id-of-external-system",
       "table": "name-of-table",
       "primary_key": ["list","of","key","names"],
       "query": "SQL query string",
       "updated_query": "SQL query string for 'since' support in queries",
       "updated_column": "column-name-for-since-support-in-tables',
       "column_blacklist": ["columns","to","not","include"],
       "batch_size": 1000,
       "schema": "default-schema-name-if-included"
    }

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 30, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``external_system``
     - String
     - Must refer to an ``external system`` component by ``id``. The role of this component is provide services like connection
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
     - List
     - The value of this property can be a single string with the name of the column
       that contains the ``primary key`` (PK) of the table or query, or a list of strings
       if it is a compound primary key. If the property is not set and the ``table``
       property is used, the data source component will attempt to use table metadata
       to deduce the PK to use. In other words, you will have to set this property if
       the ``query`` property us used. TODO: are these names case sensitive?
     -
     -

   * - ``query``
     - String
     - Must be a valid query in the dialect of the ``RDBMS`` represented by the
       ``external_system`` property. You will also have to configure the primary key(s)
       of the query in the ``primary_key`` property. Note: mutually exclusive with the
       ``table`` property with ``table`` taking precedence. TODO: are queries case sensitive?
     -
     - Yes

   * - ``updated_column``
     - String
     - If the underlying relation contains information about updates, the data source is
       able to support ``since`` markers. You can provide the name of the column to use
       for such queries here. This must be a valid column name in the ``table`` or ``query``
       result sets and it must be of a data type that supports larger than (">") and larger or equal (">=") tests
       for the ``table`` case. TODO: are these names case sensitive?
     -
     -

   * - ``updated_query``
     - String
     - If the ``query`` property is set, the ``since`` support must be expressed by a
       full query including any test needed. A single variable substitution
       ``{{ since }}`` must be included somewhere in the query string - for example
       "select * from view_name v where v.updates > '{{ since }}'".  TODO: are queries case sensitive?
     -
     -

   * - ``schema``
     - String
     - If a specific schema within a database is needed, you must provide its name in this property.
       Do *not* use schema names in the ``table`` property. TODO: are these names case sensitive?
     -
     -

   * - ``column_blacklist``
     - List
     - A list of column names to exclude from the generated entity. TODO: are these names case sensitive?
     -
     -

   * - ``batch_size``
     - Integer
     - The default size of the result sets (number of rows in a cursor fetch) to get from the database
     - 1000
     -

The CSV source
--------------

The CSV data source translates the rows of files in ``CSV format`` to entities. The configuration options are:

::

    {
       "_id": "source-id-here",
       "type": "source:csv",
       "url": "url-to-csv-file",
       "has_header": true,
       "field_names": ["mappings","from","columns","to","properties"],
       "auto_dialect": true,
       "dialect": "excel",
       "encoding": "utf-8",
       "id_field": "what-column-name-to-use-as-id",
       "delimiter": ","
    }

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
       The recognised values are ``"excel"``, ``"escaped"``, ``"excel-tab"`` and ``"singlequote"``.
       TODO: explain what they mean.
     -
     -

   * - ``encoding``
     - String
     - | The character set to used to encode the text in the CSV file
     - "UTF-8"
     -

   * - ``id_field``
     - String
     - | The name of the column to use as ``_id`` in the generated entities.
     -
     - Yes

   * - ``delimiter``
     - String
     - The character or string to use as the ``CSV`` field separator (delimiter)
     - ","
     -

The RDF source
--------------

The RDF data source is able to read data in ``RDF NTriples``,
``Turtle`` or ``RDF/XML`` format and turn this into entities.  It will
transform triples on the form ``<subject> <predicate> "value"`` into
entities on the form:

::

    {
        "_id": "<subject>",
        "<predicate>": "value"
        ...
    }

RDF blank nodes will be turned into child entities. The configuration
snippet for the RDF data source is:

::

    {
        "_id": "source-id-here",
        "type": "source:rdf",
        "url": "url-to-rdf-file",
        "format": "nt-ttl-or-xml"
    }

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
     - ``nt``
     - 


The SDShare source
------------------

The SDShare data source can read ``RDF`` from ``ATOM feeds`` after the
``SDShare specification`` (http://sdshare.org). It has the following
properties:

::

    {
       "_id": "data-source-id",
        "type": "source:sdshare",
        "url": "url-to-sdshare-fragments-feed",
        "supports_since": false
    }

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
     - The URL of the SDShare fragments feed to consume.
     -
     - Yes

   * - ``supports_since``
     - Boolean
     - Flag to indicate whether to include ``since`` request parameter when
       reading from the fragments feed.
     - true
     -


The LDAP source
---------------

The LDAP source provides entities from a ``LDAP catalog``. It supports the following properties:

::

    {
        "_id": "id-of-source",
        "type": "source:ldap",
        "host": "FQDN of LDAP host",
        "port": 389,
        "use_ssl": false,
        "username": "authentication-username-here",
        "password": "authentication-password-here",
        "search_base": "*",
        "search_filter": "(objectClass=organizationalPerson)",
        "attributes": "*",
        "id_attribute": "cn",
        "charset": "latin-1",
        "page_size": 500,
        "attribute_blacklist": ["a","list","of","attributes","to","exclude"]
    }

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

   * - ``charset``
     - String
     - The charset used to encode strings in the LDAP database. Defaults to ``"latin-1"`` aka ``"ISO-8859-1"``,
       as ``"UTF-8"`` is usually not the default encoding in LDAP catalogs at the time of writing.
     - "latin-1"
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

The external system source
--------------------------

The external system source [TODO]

The JSON sources
----------------

There are several ``JSON`` datasources in the core Sesam Node:

JSON file source
^^^^^^^^^^^^^^^^

The ``JSON`` file source can read entities from one or more ``JSON`` file(s).

::

    {
       "_id": "source-id",
       "type": "source:json_file",
       "filepath": "path-to-json-file(s)",
       "notify_read_errors": true
    }

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``filepath``
     - String
     - A full path to a ``JSON`` file, or a path to a directory containing ``.json`` files
     -
     - Yes

   * - ``notify_read_errors``
     - Boolean
     - Indicates if the source should throw exceptions or parse errors, or produce special inline error-entities
       instead (these can be interpreted by a datasync task without stopping the process). The flag is useful for
       reading configuration files from disk, for example.
     - true
     -

Remote JSON source
^^^^^^^^^^^^^^^^^^

The remote ``JSON`` source can read entities from a ``JSON`` file available over HTTP.

::

    {
       "_id": "source-id",
       "type": "source:json_remote",
       "url": "url-to-json-file"
    }

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
     - The URL of the ``JSON`` file to load.
     -
     - Yes

The metrics source
------------------

The metrics data source provides the ``internal metrics`` (i.e. counters and statistics) of the Sesam Node as a list of ``JSON`` entities. It has no configuration:

::

    {
       "_id": "source-id",
       "type": "source:metrics"
    }

The empty source
----------------

Sometimes it is useful for debugging or development purposes to have a data source that doesn't produce any entities:

::

    {
       "_id": "the-id-of-the-source",
       "type": "source:empty"
    }

Sinks
=====

Sinks are at the receiving end of pipes and are responsible for writing entities into a internal dataset or an external
system. Sinks can support batching by implementing specific methods and accumulating entites in a buffer before writing the batch.

The dataset sink
----------------

The dataset sink writes the entities it is given to an identified dataset. The configuration looks like:

::

    {
       "_id": "id-of-sink",
       "type": "sink:dataset",
       "dataset": "id-of-dataset"
    }

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

The InfluxDB sink
-----------------

The InfluxDB sink is able to write entities representing measurement values over time to the InfluxDB time series database https://influxdata.com/.
A typical source for the entities written to it is the metrics data source, but any properly constructed entity can be
written to it. The expected form of an entity to be written to the sink is:

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

The sink has a configuration that looks like:

::

    {
       "_id": "id-of-sink",
       "type": "sink:influxdb",
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

The JSON push sink
------------------

The JSON push sink implements a simple HTTP based protocol where entities or lists of entities are ``POST``ed as ``JSON``
lists of objects to a HTTP endpoint. The protocol is described in additional detail here: [TODO]. The serialisation
of entities as JSON is described in more detail here: [TODO].

The configuration is:

::

    {
       "_id": "some-unique-id",
       "type": "sink:json_push",
       "endpoint": "url-to-http-endpoint",
       "batch_size": 1500
    }

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``endpoint``
     - String
     - The full URL to HTTP service implementing the ``JSON push protocol`` described.
     -
     - Yes

   * - ``batch_size``
     - Integer
     - The maximum number of entities to accumulate before posting. Note that the remainder of the internal buffe
       is flushed and posted at the end of a pipe task even if the number of entities is less than this number.
     - 1000
     -

The SDShare push sink
---------------------

The SDShare push sink is similar to the ``JSON push sink``, but
instead of posting ``JSON`` it translates the inbound entities to
``RDF`` and ``POST``s them in ``NTriples`` form to the ``SDShare push
protocol`` HTTP endpoint.

::

    {
       "_id": "some-unique-sink-id-here",
       "type": "sink:sdshare_push",
       "endpoint": "url-to-http-endpoint",
       "graph": "uri-of-graph-to-post-to",
       "prefixes": {
          "a-prefix": "the-expansion"
       }
    }

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``endpoint``
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


The SMS message sink
--------------------

The SMS message sink is capable of sending ``SMS`` messages based on the entities it receives. The message to send can be
constructed either by inline templates or from templates read from disk. These templates are assumed to be ``Jinja``
templates (http://jinja.pocoo.org/) with the entities properties available to the templating context. The template file
name can either be fixed in the configuration or given as part of the input entity. Note that the only service supported
by the sink is ``Twilio``.

::

    {
        "_id": "some-id",
        "type": "sink:sms",
        "body_template": "static jinja template as a string",
        "body_template_property": "id-of-property-for-body-template",
        "body_template_file": "/static/full/file-name/to/jinja-template/on-disk",
        "body_template_file_property": "id-of-property-for-template-file-name",
        "recipients": "static,comma,separated,list,of,international,phonenumbers",
        "recipients_property": "id-of-property-to-get-recipients-from",
        "from_number": "static-international-phone-number-to-use-as-from-number",
        "account": "twilio-account-number",
        "token": "twilio-api-token",
        "max_per_hour": 1000
    }

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

The mail message sink
---------------------

The mail message sink is capable of sending mail messages based on the entities it receives. The message to send can be
constructed either by inline templates or from templates read from disk. These templates are assumed to be ``Jinja
templates`` (http://jinja.pocoo.org/) with the entities properties available to the templating context. The template file
name can either be fixed in the configuration or given as part of the input entity.

::

    {
        "_id": "some-id",
        "type": "sink:mail",
        "smtp_server": "localhost",
        "smtp_port": 25,
        "smtp_username": None,
        "smtp_password": None,
        "use_tls": false,
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
        "mail_from": "static@email.address",
        "max_per_hour": 1000
    }

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

   * - ``max_per_hour``
     - Integer
     - The maximum number of messages to send for any hour. It is used for stopping run-away message sending in
       development or testing. Note that any message not sent will be logged but discarded.
     - 1000
     -


The null sink
-------------

The null sink is the equivalent of the empty data source; it will discard any entities written to it and do nothing (it
never raises an error):

::

    {
       "_id": "id-of-sink",
       "type": "sink:null"
    }

External system
===============


Task
====


Pipes revisited
===============


Transforms
==========

Transforms can be configured on a pipe by specifying the "``transform``" property:

::
   
   {"_id": "mypipe",
    "type": "pipe",
    ...
    "source": {
       ...
    }.
    "transform": ...the transform configuration goes here...
    }}


The DTL transform
-----------------

This transform lets you apply Data Transformation Language transformations
on the entities stream produced by the data source.

See :doc:`DTLReferenceGuide` for more details on the transformation
language itself.

**Example:** Pipe configuration that reads entities from the
``Northwind:Customers`` dataset and transforms them using the DTL
transform specified in the "``transform``" key on the source. The
transformed entities are then written to the ``customer-with-orders``
dataset.

::
   
   {"_id": "customer-with-orders",
    "type": "pipe",
    "source": {
      "type": "source:dataset",
      "dataset": "Northwind:Customers"
    },
    "transform": {
        "type": "transform:dtl",
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
    }}


The properties transform
------------------------

The properties transform has the following capabilities:

* Add CURIE prefixes to properties
* Rename properties
* Collapse URIs into CURIEs

TODO: Add detailed docs plus examples.


The remote transform
--------------------

TODO: This is not yet implemented, but the idea is that entities are
posted to an HTTP endpoint, transformed by the service, and then
returned.
