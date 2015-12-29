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
==================

The dataset source is one of the most commmonly used datasources in a lake. It simply presents a stream of entities from a
dataset stored in a datalake node. Its configuration is very simple and looks like:

 ::

 {
   "_id": "id-of-source",
   "type": "source:dataset",
   "dataset": "id-of-dataset",
   "supports_since": True,
   "include_previous_versions": True,
 }

Only the 'dataset' configuration property is mandatory (the "_id" field is always mandatory in all entities, including
the configuration entities).

The 'supports_since' flag (default set to True) indicates wether to use a 'since' marker when reading from the dataset,
i.e. whether to start at the beginning each time or not.

If the 'include_previous_versions' flag (default set to True) is set to False, the data source will only return the
latest version of any entity for any unique '_id' value in the dataset. The default behaviour is to return all entities
recorded in the dataset in-order without considering the contents of the '_id' property.

The union dataset source
========================

The union dataset source is similar to the dataset source, except it can process several datasets at once and keep
track of each one in its since marker handler:

 ::

 {
   "_id": "id-of-source",
   "type": "source:union_datasets",
   "datasets": ["a-id-of-dataset","another-id-of-another-dataset"],
   "supports_since": True,
   "include_previous_versions": True,
 }

The configuration of this source is identical to the 'dataset' source, except 'datasets' can be a list of datasets ids.

The relational database source
==============================

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

The 'external_system' property is mandatory for this datasource and must refer to a 'external system' component by id.
The role of this component is to do connection pooling and provide authentication services for the data sources using it.

If 'table' is given, it must refer to a fully qualified table name in the database system (not including schema, which if
 needed must be set separately). The 'table' and 'query' properties are mutually exclusive with 'table' used if both are
 present.

The value of the 'primary_key' property can be a single string with the name of the
column that contains the primary key (PK) of the table or query, or a list of strings if it is a compound primary key. If
the property is not set and the 'table' property is used, the data source component will attempt to use table metadata
to deduce the PK to use. In other words, you will have to set this property if the 'query' property us used.

The 'query' property must be a valid query in the dialect of the RDBMS represented by the 'external_system' property.
You will also have to configure the primary key(s) of the query in the 'primary_key' property.

If the underlying relation contains information about updates, the data source is able to support 'since' markers. You
can provide the name of the column to use for such queries in 'updated_column'. This must be a valid column name in the
'table' or 'query' result sets and it must be of a data type that supports larger than (">") tests for the 'table' case.

For custom queries given in the 'query' property, the 'since' support must be expressed by a full query including any
test needed. A single variable substitution "{{ since }}" must be included somewhere in the query string - for example
"select * from view_name v where v.updates > '{{ since }}'".

The 'batch_size' property controls the default size of the result sets to get from the database, with 1000 rows being
the default.

If a specific schema within a database is needed, you must provide its name in 'schema'. Do not use schema names in
table names.


The CSV source
==============

The CSV data source translates the rows of files in CSV format to entities. The configuration options are:

 ::

 {
   "_id": "source-id-here",
   "type": "source:csv",
   "filename": "path-to-file",
   "has_header": True,
   "field_names": ["mappings","from","columns","to","properties"],
   "auto_dialect": True,
   "dialect": "excel",
   "encoding": "utf-8",
   "id_field": "what-column-name-to-use-as-id",
   "delimiter": ","
 }

The 'filename' property is mandatory and must refer to a file in CSV format that exists.

'has_header' (default to True) is a flag that indicates to the source that the first row in the CSV file contains the
 names of the columns.

The contents of 'field_names', if given, is the names of the columns. It takes precedence over the header in the CSV file
 if present.

'auto_dialect' is a flag that hints to the source that it should try to guess the dialect of the CSV file on its own.

'dialect' is a string property that encodes what type of CSV file the file is. This is basically presets of the other properties.
The recognised values are "excel", "escaped", "excel-tab" and "singlequote".

'id_field' is a string property containing the name of the column to use as "_id" in the generated entities.

'delimiter' is a string property with the character to use as the CSV delimiter (comma i.e. "," by default)

The RDF source
==============

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

'filename' is the full path to a RDF file to load - it can contain multiple subjects (with blank node hierarchies) and
each unique non-blank subject will result in a single root entity.

'format' is a string property with the following recongnised values: "nt" for NTriples, "ttl" for Turtle form or "xml"
for RDF/XML files.

The SDShare source
==================

The SDShare data source can read RDF from ATOM feeds after the SDShare specification (http://sdshare.org). It has
the following properties:

 ::

 {
   "_id": "data-source-id",
    "type": "source:sdshare",
    "sdshare_server": "url-to-sdshare-http-server",
    "provider_id": "the-id-of-the-sdshare-provider",
    "inline_feed": False,
    "updated_predicate": "URI-for-updated-value-predicate",
 }

'sdshare_server' is mandatory and must contain the URL to a http SDShare server

'provider_id' is also mandatory and is a string property with the id of the sdshare provider to read from

'inline_feed' is a optional flag that indicates whether to read the inline RDF (if it exists) or read a RDF fragment
by following the links.

'updated_predicate' is the predicate URI to look for to set the "_updated" property in the generated entities to be able
to support since markers.

The LDAP source
===============

The LDAP source provides entities from a LDAP catalog. It supports the following properties:

  ::

  {
    "_id": "id-of-source",
    "type": "source:ldap",
    "host": "FQDN of LDAP host",
    "port": 389,
    "use_ssl": False,
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

'host' is mandatory and must contain the fully qualified domain name of the LDAP host server

'port' is a optional integer property which defaults to 389. It must be set to the port of the LDAP service.

'use_ssl' is a flag that indicates to use SSL or not when communicating with the LDAP service (optional)

'username' is a string property containing the user name to use when authenticating with the LDAP service

'password' is a string property with the password to use when authenticating

'search_base' is the base LDAP search expression to use when looking for records (optional)

'search_filter' is a filter expression to apply to all records found by the 'search_base' expression (optional)

'attributes' is a wildcard specifying which attributes to include in the entity (optional)

'id_attribute' which of the LDAP attributes to use for the "_id" property of a entity (optional)

'charset' the charset used to encode strings in the LDAP database (optional)

'page_size' the default number of records to read at a time from the LDAP service (optional)

'attribute_blacklist' is a list of attribute names (as strings) to exclude from the record when constructing entities

The external system source
==========================

The external system source [TODO]

The JSON sources
================

There are several JSON datasources in the core lake:

JSON file source
================

The JSON file source can read entities from one or more a JSON file(s).

 ::

 {
   "_id": "source-id"
   "type": "source:json_file",
   "filepath": "path-to-json-file(s)",
   "notify_read_errors": True
 }

'filepath' is mandatory and can be either a full path to a JSON file, or a path to a directory containing ".json" files.

'notify_read_errors" is a optional boolean flag (True by default) that indicates if the source should throw exceptions on
parse errors, or produce special inline error-entities instead (these can be interpreted by a datasync task without
stopping the process). The flag is useful for reading configuration files from disk, for example.

Remote JSON source
==================

The remote JSON source can read entities from a JSON file available over HTTP.

 ::

 {
   "_id": "source-id"
   "type": "source:json_remote",
   "fileurl": "URL-to-json-file",
 }

'fileurl' is a mandatory string propery containing the full URL to a JSON file to download and parse.

The metrics source
==================

The metrics data source provides the internal metrics of the lake as a list of JSON entities. It has no configuration:


 ::

 {
   "_id": "source-id"
   "type": "source:metrics",
 }

Sinks
=====

The dataset sink
================

The dataset sink writes the entities it is given to a identified dataset

The InfluxDB sink
=================

The JSON push sink
==================

The SDShare push sink
=====================

The SMS message sink
====================

The mail message sink
=====================

