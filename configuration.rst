
=============================
Component configuration guide
=============================


.. contents:: Table of Contents


General
=======

The datalake is configured using JSON structures, either on disk or by posting to the API (see the API section). The main
concepts to configure for a node is the external systems and the flow between them and the lake. Also flows within
the lake is configured the same way.

The node configuration is a JSON list of one or more external system configurations and one or more pipe configurations describing
the flows into, within and out of the lake from these external systems. These configuration entities are JSON dictionaries
on the general form:

::

    [
        {
            "_id": "some-node-wide-unique-id"
            "type": "component-type:component-subtype",
            "other-properties": "other values",
            ..
        },
        {
            "_id": "some-other-node-wide-unique-id"
            "type": "component-type:component-subtype",
            "other-properties": "other values",
        ..
        },
        ..
    ]


Flows
=====

A data flow is a set of pipes describing the flow of data entities from an external system, between datasets inside
the lake and finally out of the lake to a external system. At the sources of each individual pipe in such a flow,
optional transforms can be specified that transforms the entities streaming from the source to a another form
before arriving at the destination sink.

This transform is described using a domain specific language inspired by Lisp called 'DTL' (see the DTL section for
more detail). The transformed entities can be entirely or partially constructed from entities from other datasets,
like joins in SQL select statements, with the main difference that the result is persisted for each pipe in the flow.

The datalake keeps track of the dependencies between datasets through DTL transforms in such a way that only changes
are propagated along the flow based on what entities are changed at the ultimate source of the flows. This leads to
a very efficient handling of entity streams within the lake.

The Pipe
========

A pipe is a triple of a source, sink and data sync task. The task 'pumps' data in the form om entities from the source
to the sink at regular or scheduled intervals.

The configuration of a pipe has two forms; one 'complete' form and one short hand form. Let's describe the 'complete'
form first and revisit the shorthand form after describing the various sinks and sources availble in the datalake core:

::

    {
       "_id": "pipe-id",
       "type": "pipe",
       "source": {
         ..
       },
       "sink": {
         ..
       }
       "task":  {
         ..
       }
    }

Sources
=======

Sources provide streams of entities as input to the pipes which is the building blocks for the flows in the data lake. These entities can take
any shape (i.e. they can also be nested), and have a single required property: "_id". This "_id" field must be unique within a flow.
Sources can also support "since" monikers or markers which lets them pick up where the previous stream of entities left off, sort
of like a bookmark in the entitiy stream. The "since" marker is opaque to the rest of the data lake components, and is assumed
to be interpretable only by the source. Within an entity, the marker is carried in the "_updated" property if supported
by the source.

The data lake supports a diverse set of core data sources:

The dataset source
------------------

The dataset source is one of the most commmonly used datasources in a lake. It simply presents a stream of entities from a
dataset stored in a datalake node. Its configuration is very simple and looks like:

::

    {
       "_id": "id-of-source",
       "type": "source:dataset",
       "dataset": "id-of-dataset",
       "supports_since": true,
       "include_previous_versions": true,
    }

Only the ``dataset`` configuration property is mandatory (the ``_id`` field is always mandatory in all entities, including
the configuration entities).

The ``supports_since`` flag (default set to ``true``) indicates wether to use a ``since`` marker when reading from the dataset,
i.e. whether to start at the beginning each time or not.

If the ``include_previous_versions`` flag (default set to ``true``) is set to ``false``, the data source will only return the
latest version of any entity for any unique ``_id`` value in the dataset. The default behaviour is to return all entities
recorded in the dataset in-order without considering the contents of the ``_id`` property.

The union dataset source
------------------------

The union dataset source is similar to the dataset source, except it can process several datasets at once and keep
track of each one in its since marker handler:

::

    {
       "_id": "id-of-source",
       "type": "source:union_datasets",
       "datasets": ["a-id-of-dataset","another-id-of-another-dataset"],
       "supports_since": true,
       "include_previous_versions": true,
    }

The configuration of this source is identical to the ``dataset`` source, except ``datasets`` can be a list of datasets ``id``s.

The relational database source
------------------------------

The relational database source is one of the most commonly used data sources. It short, it presents database relations
(i.e. tables or queries) as entities to the data lake. It has several options, all of which are presented below with
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
       "batch_size": 1000,
       "schema": "default-schema-name-if-included"
    }

The ``external_system`` property is mandatory for this datasource and must refer to a ``external system`` component by id.
The role of this component is to do connection pooling and provide authentication services for the data sources using it.

If ``table`` is given, it must refer to a fully qualified table name in the database system (not including schema, which if
needed must be set separately). The ``table`` and ``query`` properties are mutually exclusive with ``table`` used if both are
present.

The value of the ``primary_key`` property can be a single string with the name of the
column that contains the primary key (PK) of the table or query, or a list of strings if it is a compound primary key. If
the property is not set and the ``table`` property is used, the data source component will attempt to use table metadata
to deduce the PK to use. In other words, you will have to set this property if the ``query`` property us used.

The ``query`` property must be a valid query in the dialect of the RDBMS represented by the ``external_system`` property.
You will also have to configure the primary key(s) of the query in the ``primary_key`` property.

If the underlying relation contains information about updates, the data source is able to support ``since`` markers. You
can provide the name of the column to use for such queries in ``updated_column``. This must be a valid column name in the
``table`` or ``query`` result sets and it must be of a data type that supports larger than (">") tests for the ``table`` case.

For custom queries given in the ``query`` property, the ``since`` support must be expressed by a full query including any
test needed. A single variable substitution ``{{ since }}`` must be included somewhere in the query string - for example
``select * from view_name v where v.updates > '{{ since }}'``.

The ``batch_size`` property controls the default size of the result sets to get from the database, with 1000 rows being
the default.

If a specific schema within a database is needed, you must provide its name in ``schema``. Do not use schema names in
table names.


The CSV source
--------------

The CSV data source translates the rows of files in CSV format to entities. The configuration options are:

::

    {
       "_id": "source-id-here",
       "type": "source:csv",
       "filename": "path-to-file",
       "has_header": true,
       "field_names": ["mappings","from","columns","to","properties"],
       "auto_dialect": true,
       "dialect": "excel",
       "encoding": "utf-8",
       "id_field": "what-column-name-to-use-as-id",
       "delimiter": ","
    }

The ``filename`` property is mandatory and must refer to a file in CSV format that exists.

``has_header`` (default ``true``) is a flag that indicates to the source that the first row in the CSV file contains the
names of the columns.

The contents of ``field_names``, if given, is the names of the columns. It takes precedence over the header in the CSV file
if present.

``auto_dialect`` is a flag that hints to the source that it should try to guess the dialect of the CSV file on its own.

``dialect`` is a string property that encodes what type of CSV file the file is. This is basically presets of the other properties.
The recognised values are ``"excel"``, ``"escaped"``, ``"excel-tab"`` and ``"singlequote"``. TODO: explain what they mean.

``id_field`` is a string property containing the name of the column to use as ``_id`` in the generated entities.

``delimiter`` is a string property with the character to use as the CSV delimiter (comma i.e. ``","`` by default)

The RDF source
--------------

The RDF data source is able to read data in RDF NTriples, Turtle or RDF/XML format and turn this into entities.
It will transform triples on the form <subject> <predicate> "value" into entities on the form:

::

    {
        "_id": "<subject>",
        "<predicate>": "value",
        ..
    }

The configuration snippet for the RDF data source is:

::

    {
        "_id": "source-id-here",
        "type": "source:rdf",
        "filename": "path-to-file-here",
        "format": "nt-ttl-or-xml"
    }

``filename`` is the full path to a RDF file to load - it can contain multiple subjects (with blank node hierarchies) and
each unique non-blank subject will result in a single root entity.

``format`` is a string property with the following recongnised values: ``"nt"`` for NTriples, ``"ttl"`` for Turtle form or ``"xml"``
for RDF/XML files.

The SDShare source
------------------

The SDShare data source can read RDF from ATOM feeds after the SDShare specification (http://sdshare.org). It has
the following properties:

::

    {
       "_id": "data-source-id",
        "type": "source:sdshare",
        "sdshare_server": "url-to-sdshare-http-server",
        "provider_id": "the-id-of-the-sdshare-provider",
        "inline_feed": false,
        "updated_predicate": "URI-for-updated-value-predicate",
    }

``sdshare_server`` is mandatory and must contain the URL to a http SDShare server

``provider_id`` is also mandatory and is a string property with the id of the sdshare provider to read from

``inline_feed`` is a optional flag that indicates whether to read the inline RDF (if it exists) or read a RDF fragment
by following the links.

``updated_predicate`` is the predicate URI to look for to set the ``_updated`` property in the generated entities to be able
to support since markers.

The LDAP source
---------------

The LDAP source provides entities from a LDAP catalog. It supports the following properties:

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

``host`` is mandatory and must contain the fully qualified domain name of the LDAP host server

``port`` is a optional integer property which defaults to 389. It must be set to the port of the LDAP service.

``use_ssl`` is a flag that indicates to use SSL or not when communicating with the LDAP service (optional)

``username`` is a string property containing the user name to use when authenticating with the LDAP service

``password`` is a string property with the password to use when authenticating

``search_base`` is the base LDAP search expression to use when looking for records (optional)

``search_filter`` is a filter expression to apply to all records found by the 'search_base' expression (optional)

``attributes`` is a wildcard specifying which attributes to include in the entity (optional)

``id_attribute`` which of the LDAP attributes to use for the ``_id`` property of a entity (optional)

``charset`` the charset used to encode strings in the LDAP database (optional, defaults to ``"latin-1"`` aka ``"ISO-8859-1"``,
as ``"UTF-8"`` is usually not the default encoding in LDAP catalogs at the time of writing)

``page_size`` the default number of records to read at a time from the LDAP service (optional)

``attribute_blacklist`` is a list of attribute names (as strings) to exclude from the record when constructing entities

The external system source
--------------------------

The external system source [TODO]

The JSON sources
----------------

There are several ``JSON`` datasources in the core lake:

JSON file source
----------------

The ``JSON`` file source can read entities from one or more a ``JSON`` file(s).

::

    {
       "_id": "source-id"
       "type": "source:json_file",
       "filepath": "path-to-json-file(s)",
       "notify_read_errors": true
    }

``filepath`` is mandatory and can be either a full path to a ``JSON`` file, or a path to a directory containing ``.json`` files.

``notify_read_errors`` is a optional boolean flag (``true`` by default) that indicates if the source should throw exceptions on
parse errors, or produce special inline error-entities instead (these can be interpreted by a datasync task without
stopping the process). The flag is useful for reading configuration files from disk, for example.

Remote JSON source
------------------

The remote ``JSON`` source can read entities from a ``JSON`` file available over HTTP.

::

    {
       "_id": "source-id"
       "type": "source:json_remote",
       "fileurl": "URL-to-json-file",
    }

``fileurl`` is a mandatory string propery containing the full URL to a ``JSON`` file to download and parse.

The metrics source
------------------

The metrics data source provides the internal metrics of the lake as a list of ``JSON`` entities. It has no configuration:

::

    {
       "_id": "source-id"
       "type": "source:metrics",
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

Sinks are at the receiving end of pipes and are responsible for writing entities into a internal dataset or a external
system. Sinks can support batching by implementing specific methods and accumulating entites in a buffer before writing the batch.

The dataset sink
----------------

The dataset sink writes the entities it is given to a identified dataset. The configuration looks like:

::

    {
       "_id": "id-of-sink",
       "type": "sink:dataset",
       "dataset": "id-of-dataset"
    }

``dataset`` is mandatory and contain the id of the dataset to write entities into. Note: if it doesn't exist before
entities are written to the sink, it will be created on the fly.

The InfluxDB sink
-----------------

The InfluxDB sink is able to write entities representing measurement values over time to the InfluxDB time series database (https://influxdata.com/).
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
in the influxdb database so metrics can be easily searched for in for example Grafana (http://grafana.org/).

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
       "database": "lake",
       "ssl": false,
       "verify_ssl": false,
       "timeout": None,
       "use_udp": false,
       "udp_port": 4444
    }

The ``host`` property is the ``FQDN`` of the InfluxDB server, default is ``"localhost"``.

``port`` is the port of the InfluxDB service, the default is ``8086``

``username`` is the user to authenticate as against the InfluxDB service, default is ``"root"``

``password`` is the password to use for authenticating with the InfluxDB service, default is ``"root"``.

``database`` is the name of the database to create and write into. Default is ``"lake"``. Note that it will be created automatically
if it doesn't exist.

``ssl`` is a boolean flag that indicates whether to use ssl in communications with InfluxDB or not. Default is ``false``.

``verify_ssl`` is a boolean flag that tells the client to verify the server's ssl certificate before initiating communication with it.
The default is ``false``.

``timeout`` is a integer property that, if set, sets the timeout to a specified number of seconds. Default is not set and indicates
no timeout (i.e. infitite wait). Note that this can result in hanging services if the server is not reachable.

``use_udp`` is a optional boolean flag to indicate to the client to use the UDP protocol rather than TCP when talking to the InfluxDB server.
Default is ``false`` (i.e. use TCP). UDP can in certain high-volume scenarios be more efficient than TCP due to its simplicity.

``udp_port`` optional integer property for the port to use if ``use_udp`` is set to ``true``. The default is ``4444``.

The JSON push sink
------------------

The JSON push sink implements a simple HTTP based protocol where entities or lists of entities are ``POST``ed as ``JSON``
lists of dictionaries to a HTTP endpoint. The protocol is described in additional detail here: [TODO]. The serialisation
of entities as JSON is described in more detail here: [TODO].

The configuration is:

::

    {
       "_id": "some-unique-id",
       "type": "sink:json_push",
       "endpoint": "url-to-http-endpoint',
       "batch_size": 1500,
    }

``endpoint`` is a mandatory string property that must contain a full URL to HTTP service implementing the JSON push
protocol described.

``batch_size`` is a optional integer property for the maximum number of entities to accumulate before posting. Note that the remainder
of the internal buffer is flushed and posted at the end of a pipe task even if the number of entities is less than this number.

The SDShare push sink
---------------------

The SDShare push sink is similar to the ``JSON push sink``, but instead of posting ``JSON`` it translates the inbound entities
to ``RDF`` and ``POST``s the converted result in ``NTriples`` form to the HTTP endpoint.

::

    {
       "_id": "some-unique-sink-id-here",
       "type": "sink:sdshare_push",
       "endpoint": "url-to-http-endpoint",
       "graph": "uri-for-graph-to-post-to",
       "default_subject_prefix": "default-prefix-for-subjects',
       "default_predicate_prefix": "default-prefix-for-predicates"
    }

``endpoint`` is a mandatory string property that must contain a full URL to HTTP service implementing the ``SDShare push
protocol``.

``graph`` is a mandatory string property containing a URI to a graph to post the ``RDF ntriples`` to

``default_subject_prefix`` is a optional string property with a prefix to use for subjects if no prefix manager is found

``default_predicate_prefix`` is a optional string property with a prefix to use for predicates if no prefix manager is found

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
        "body_template_property": "id-of-property-to-get-as-a-body-template",
        "body_template_file": "/static/full/file-name/to/jinja-template/on-disk"
        "body_template_file_property": "id-of-property-to-get-as-a-body-template-file-name",
        "recipients": "static,comma,separated,list,of,fully,international,+xyz,phonenumbers",
        "recipients_property": "id-of-property-to-get-recipients-from",
        "from_number": "static-international-phone-number-to-use-as-from-number",
        "account": "twilio-account-number",
        "token": "twilio-api-token"
        "max_per_hour": 1000
    }

The configuration must contain at most one of ``body_template``, ``body_template_property``, ``body_template_file`` or
``body_template_file_property``.

``body_template`` is a string property that should contain a ``Jinja template`` to use for constructing messages. The template
will have access to all entity properties by name.

``body_template_property`` is a string property that should contain a id of a property of the incoming entity to use for
looking up the ``Jinja template`` (i.e for inlining the templates in the entities). It should not be used at the same time
as ``body_template`` or ``body_template_file*``.

``body_template_file`` is a string property that should refer to a text file on disk containing the ``Jinja template`` to use
for constructing the SMS body message from the incoming entity. It is mutually exclusive with the other ways of specifying
a body template.

``body_template_file_propery`` is a string property with a ``id`` of a property in the incoming entity to use for looking up
the file name of the ``Jinja template`` on disk (i.e. inlining the bodu template filename in the entity). As with the other
body template options, it is mutually exclusive in use.

``recipients`` is a string propery that should contain a comma-separated list of internationalised phone-numbers to send
the message constructed to. If this is not inlined in the entities via ``recipients_property`` (see below) this property
is mandatory.

``recipients_property`` is a string property that should contain the id of the property to look up the recpients from the
entity itself (i.e for inlining the recpients). If ``recipients`` (see abowe) is not specified, this property is mandatory
and the propery referenced by it must exists and be valid for all entities.

``from_number`` is a mandatory string propery containing a internartional phone number to use as the sender of all messages.

``account`` is a string propery with the ``Twilio`` account number (mandatory)

``token`` is a string property with the ``Twilio`` API token (mandatory)

``max_per_hour`` is a optional integer propery indicating the maximum number of messages to send for any hour. It is
used for stopping run-away message sending in development or testing. Note that any message not sent will be logged but
discarded.

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
        "body_template_file": "/static/full/file-name/to/jinja-template/on-disk"
        "body_template_file_property": "id-of-property-to-get-as-a-body-template-file-name",
        "subject_template": "static jinja template as a string",
        "subject_template_property": "id-of-property-to-get-as-a-subject-template",
        "subject_template_file": "/static/full/file-name/to/jinja-template/on-disk"
        "subject_template_file_property": "id-of-property-to-get-as-a-subject-template-file-name",
        "recipients": "static,comma,separated,list,of,fully,international,+xyz,phonenumbers",
        "recipients_property": "id-of-property-to-get-recipients-from",
        "mail_from": "static@email.address",
        "max_per_hour": 1000
    }

``smtp_server`` is a string propery containing a ``FQDN`` of the ``SMTP service`` to use. The default is ``"localhost"``.

``smtp_port`` is a integer property for the TCP port to use when talking to the ``SMTP service``. The default is ``25``.

``smtp_username`` is a optional string property containing the username to use when authenticating with the ``SMTP service``. If
not set, no authentication is attempted.

``smtp_password`` is string property containing the password to use if ``smtp_username`` is set. It is mandatory if the
``smtp_username`` is provided.

``use_tls`` is a optional boolean flag indicating to the client to use ``TLS encryption`` when communicating with the
``SMTP service``. The default is ``false``.

The configuration must contain at most one of ``body_template``, ``body_template_property``, ``body_template_file`` or
``body_template_file_property``. The same applies to ``subject_template``.

``body_template`` is a string property that should contain a ``Jinja template`` to use for constructing messages. The template
will have access to all entity properties by name.

``body_template_property`` is a string property that should contain a ``id`` of a property of the incoming entity to use for
looking up the ``Jinja template`` (i.e for inlining the templates in the entities). It should not be used at the same time
as ``body_template`` or ``body_template_file*``.

``body_template_file`` is a string property that should refer to a text file on disk containing the ``Jinja template`` to use
for constructing the SMS body message from the incoming entity. It is mutually exclusive with the other ways of specifying
a body template.

``body_template_file_propery`` is a string property with a ``id`` of a property in the incoming entity to use for looking up
the file name of the ``Jinja template`` on disk (i.e. inlining the bodu template filename in the entity). As with the other
body template options, it is mutually exclusive in use.

``subject_template`` is a string property that should contain a ``Jinja template`` to use for constructing subjects for the email
messages. The template will have access to all entity properties by name.

``subject_template_property`` is a string property that should contain a id of a property of the incoming entity to use for
looking up the ``Jinja template`` (i.e for inlining the templates in the entities). It should not be used at the same time
as ``subject_template`` or ``subject_template_file*``.

``subject_template_file`` is a string property that should refer to a text file on disk containing the ``Jinja template`` to use
for constructing the mail subject from the incoming entity. It is mutually exclusive with the other ways of specifying
a subject template.

``subject_template_file_propery`` is a string property with a id of a property in the incoming entity to use for looking up
the file name of the ``Jinja template`` on disk (i.e. inlining the bodu template filename in the entity). As with the other
subject template options, it is mutually exclusive in use.

``recipients`` is a string propery that should contain a comma-separated list of email addresses to send
the message constructed to. If this is not inlined in the entities via ``recipients_property`` (see below) this property
is mandatory.

``recipients_property`` is a string property that should contain the id of the property to look up the recpients from the
entity itself (i.e for inlining the recpients). If ``recipients`` (see abowe) is not specified, this property is mandatory
and the propery referenced by it must exists and be valid for all entities.

``mail_from`` is a mandatory string propery containing an email address to use as the sender of all messages.

``max_per_hour`` is a optional integer propery indicating the maximum number of messages to send for any hour. It is
used for stopping run-away message sending in development or testing. Note that any message not sent will be logged but
discarded.

The null sink
-------------

The null sink is the equivalent of the empty data source; it will discard any entities written to it and do nothing (it
never raises an error):

::

    {
       "_id": "id-of-sink",
       "type": "sink:null"
    }

