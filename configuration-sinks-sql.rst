
.. _sql_sink:

SQL sink
--------

The `SQL <https://en.wikipedia.org/wiki/SQL>`_  sink writes entities to a
`relational database <https://en.wikipedia.org/wiki/Relational_database>`_ `table <https://en.wikipedia.org/wiki/Table_(database)>`_.
You will have to configure and provide a :ref:`SQL system <sql_system>` id in the ``system`` property.

The expected form of an entity to be written to the sink is:

::

    {
        "columnname1": value,
        "columnname2": another_value,
    }

This sink supports :ref:`batching <pipe_batching>`.

Prototype
^^^^^^^^^

::

    {
        "type": "sql",
        "system": "id-of-sql-system"
        "primary_key": ["list","of","key","names"],
        "table": "name-of-table",
        "schema": "default-schema-name-if-included",
        "batch_size": 100,
        "use_bulk_operations": false,
        "keep_failed_bulk_operation_files": false,
        "bulk_operation_timeout": 600,
        "bulk_operation_queue_size": 3,
        "schema_definition": [],
        "skip_identity_columns": false,
        "create_table_if_missing": false,
        "timestamp": "name-of-collumn-to-add-timestamp-into",
        "truncate_table_on_first_run": false
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

   * - ``primary_key``
     - List<String> or String
     - The value of this property can be a single string with the name of the column
       that contains a ``unique key``, such as the primary key (PK) of the table, or a list of strings
       if it is a compound primary key. If the property is not set the component will
       attempt to use table metadata reflection to deduce the PK to use.
     -
     -

   * - ``schema``
     - String
     - If a specific schema within a database is needed, you must provide its name in this property.
       Do *not* use schema names in the ``table`` property.
     -
     -

   * - ``timestamp``
     - String
     - Defines a name of a property (column) that is added to each entity, containg a timestamp in UTC.
       If the corresponding column exist in the target table, the value will be written to that column.
     - ``sesam-timestamp``
     -

   * - ``use_bulk_operations``
     - Boolean
     - Some database types supports bulk upload of data. Bulk uploading is typically much faster than doing
       updates with ``INSERT`` and ``UPDATE`` SQL statements, but may not be feasible in all cases (some bulk
       operations requires Sesam to have extra permissions in the database, for instance). Only some
       sql systems supports bulk operations, see :ref:`the documentation of the SQL systems <sql_system>` for
       details.
     - ``false`` for now; will be changed to ``true`` at some future date.
     -

   * - ``keep_failed_bulk_operation_files``
     - Boolean
     - Bulk operations typically involve writing some temporary files to disk. These files are normally
       deleted when the bulk operation is finished, but while debugging a problem it can be useful to
       keep the files when the bulk operation failes. This option can be set to ``true`` to keep all the
       files that are relevant for the failing bulk operation. You have to have access to the server's
       harddisk in order to see the files (the location of the bulk-files is written in the node's log-file).
       Note: The files are written to a temporary folder, and are deleted the next time the node restarts.
     - ``false``
     -

   * - ``bulk_operation_timeout``
     - Integer
     - The maximum number of seconds to wait for a bulk operation to finish. This is only applicable if both
       ``truncate_table_on_first_run`` and ``use_bulk_operations`` is set to ``true`` (and the SQL system supports
       bulk operations). This value should be set to the maximum number of seconds a bulk operation is expected to
       use for a single batch. It will typically depend on both the size of the batches, the size of the data and the
       performance of the receiving RDBM system.
     - ``600``
     -

   * - ``bulk_operation_queue_size``
     - Integer
     - The maximum number of bulk operation batches to queue for upload at any given time. This shouldn't normally
       be changed from the default. Higher numbers will consume more disk space.
     - ``3``
     -

   * - ``bulk_operation_buffer_size``
     - Integer
     - The maximum number of bytes of the temporary bulk file to be held in memory before flushing it to disk.
       You should not normally change this value. A higher value will consume more memory. If it set too high, it might
       result in the system running out of memory. If it is set too low, it might slow down the writing of the temporary bulk
       file resulting in poor performance. The default is 50 Mb.
     - ``50000000``
     -

   * - ``batch_size``
     - Integer
     - The maximum number of rows to insert into the database table in one operation
     - ``1000`` or ``use_bulk_operations`` is ``true``, ``100`` otherwise.
     -

   * - ``truncate_table_on_first_run``
     - Boolean
     - A flag that indicates that the target table should be truncated/emptied the first time a pump runs
       (for example on the first run, or when its offset has been set to zero manually). Please note that
       the truncating operation is executed in a separate transaction, so if any subsequent inserts should fail
       the truncating operation will not be rolled back.

       Note: combining this option with ``use_bulk_operations`` enables the sink to do a direct bulk copy operation to the
       target table on first run, which is much faster than using a temporary table which is the default method.
     - ``false``
     -

   * - ``create_table_if_missing``
     - Boolean
     - A flag that indicates that the target table should be created if it is missing the first time a pump runs
       (for example on the first run, or when its offset has been set to zero manually). If this property is ``true``
       then a proper schema definition must be supplied in the ``schema_definition`` property. Note that this property
       requires that the user defined in the :ref:`SQL system <sql_system>` have the necessary privileges to create and drop
       tables in the target database/schema.
     - ``false``
     -

   * - ``recreate_table_on_first_run``
     - Boolean
     - If combined with ``create_table_if_missing`` this property will make the sink drop and then recreate the table
       on the first run, or if the pipe is reset (based on the information in ``schema_definition`` which must also be
       provided).
     - ``false``
     -

   * - ``schema_definition``
     - List<Object>
     - A list of column definitions that guides the sink when creating a new table when the ``create_table_if_missing``
       is set to ``true``. See :ref:`SQL sink schema definition format <sql_sink_schema_definition_format>` for more
       details on how this element works.
     -
     -

   * - ``skip_identity_columns`` (experimental)
     - Boolean
     - If this flag is set, the sink will skip any identity columns it can detect via table metadata reflection. Note
       that you still need to define one or more non-identity unique column(s) in the ``primary_key`` property (sesam
       does not support automatically generated primary keys if there are no other unique combination of column values
       for a row).
     - ``false``
     -

       .. _remove_pk_char_sql:
   * - ``remove_pk_char_trailing_spaces``
     - Boolean
     - If set, removes trailing spaces from primary key values if they are of type ``char`` or ``nchar``. SQL automatically pads strings with whitespace if the string is shorter than the predetermined length, but trailing spaces are disregarded when comparing values. This setting, when ``true``, ensures that the sink also disregards trailing spaces. If set to ``false``, you can run into issues with updating existing rows.
     - ``true``
     -

   * - ``whitelist``
     - List<String>
     - Deprecated. The names of the properties (columns) to include when inserting rows into the target table. If there is a
       ``blacklist`` also specified, the whitelist will be filtered against the contents of the blacklist.
     -
     -


   * - ``blacklist``
     - List<String>
     - Deprecated. The names of the properties (columns) to exclude from inserts into the target table. If you are looking
       for a way to filter out identity columns, see the ``skip_identity_columns`` property.
     -
     -


Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "sql",
            "system": "my-sql-system",
            "table": "customers"
        }
    }


SQL sink schema definition format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _sql_sink_schema_definition_format:

The schema definition format consists of a list of objects for each property that exists in the input entities. These
objects are in essence column definitions and correspond directly to columns in the target table. The initial schema
definition can be generated from analysing the entities produced by the pipe the sink belongs to by using the API or
in the management studio. After being generated it can then be manually edited or augmented.

If the entities in the source dataset changes shape, or you change the shape of the entities produced by the pipe
by adding (or editing existing) DTL transforms attached to it, you may need to regenerate (or manually update) the
schema definition accordingly.

If the schema definition does not match the shape or value ranges of the entities that the sink is attempting to
insert (or update) in the resulting table, the sink will generate run time errors in the pump execution log.

Each object is on the form:

::

    {
        "source_property": "name_of_property",
        "name": "name_of_column",
        "type": "string|integer|decimal|float|binary|datetime|date|time|uuid|boolean",
        "max_size|max_value": 1234,
        "min_size|min_value": 1234,
        "precision": 10,
        "scale": 2,
        "allow_null": true|false,
        "primary_key": true|false,
        "index": true|false,
        "default": "default-value"
    }


The ``name`` property must correspond to a column in the target table and the ``source_property`` is the corresponding
property in the entity. In the case of the ``primary_key`` set to ``true`` and/or ``allow_null`` set to ``false``,
the property must exist in all entities. Note that at least one column definition in the schema definition list must
have ``primary_key`` set to ``true``. If you edit the ``name`` property, you must take care that it is an exact,
case-sentitive match with the definiton in the schema for the table.

The ``type`` property is automatically mapped to the appropriate target RDBMS column type, based on the information
in the ``max_size``/``max_value`` and ``min_size``/``min_value`` properties. For example, an ``integer`` type may
translate to a ``bigint`` if the value range is outside +-2^31 (i.e larger than 32 bits) or a ``tinyint`` if it fits within
a unsigned byte range (0..255). The translation table for the currently supported systems is listed below.

If the ``index`` property for a column definition is set to ``true``, the table creation will add a default type
of index to the column for the particular target RDBMS system.

The ``precision`` and ``scale`` properties are valid only for ``decimal`` type columns and define the total number
of digits and the fractional digits respectively. I.e. the decimal number "10.3" would have a ``precision`` of "3"
and an ``scale`` of "1".

The optional ``default`` property contains what value to use if the property is not present in the entity. If a
default value for a particular column has been set in the table schema, this value should match the schema value.


Translation table for the :ref:`Microsoft SQL Server <mssql-sqlserver_system>` and :ref:`Legacy Microsoft SQL server <mssql_system>`:


.. list-table::
   :header-rows: 1
   :widths: 20, 20, 20, 30

   * - Type
     - Range/size
     - Column type
     - Comment

   * - ``string``
     - <= 8000
     - nvarchar(size)
     - Unicode

   * - ``string``
     - > 8000
     - nvarchar(MAX)
     - Unicode

   * - ``binary``
     - <= 8000
     - varbinary(size)
     -

   * - ``binary``
     - > 8000
     - varbinary(MAX)
     -

   * - ``integer``
     - -9223372036854775808 - 9223372036854775808
     - integer
     - 64 bit/8 bytes

   * - ``integer``
     - -2147483648 - 2147483647
     - int
     - 32 bit/4 bytes

   * - ``integer``
     - -32768 - 32768
     - smallint
     - 16 bit/1 word/2 bytes

   * - ``integer``
     - 0 - 255
     - tinyint
     - 8 bit/1 byte

   * - ``decimal``
     - Any
     - decimal(precision,scale)
     -

   * - ``float``
     - 53 bit precision
     - float
     - Double precision IEEE-754 number

   * - ``datetime``
     - 0001-01-01T00:00:00.000000Z - 9999-12-31T23:59:59.999999Z
     - datetime2
     -

   * - ``date``
     - 0001-01-01 - 9999-12-31
     - date
     - Coerced from ``datetime`` values or pre-formatted strings

   * - ``time``
     - 00:00:00.000000 - 23:59:59.999999
     - time
     - Coerced from ``datetime`` values or pre-formatted strings

   * - ``boolean``
     - true | false
     - bit
     - Coerced to ``0`` or ``1``

   * - ``uuid``
     - Any valid UUID
     - uniqueidentifier
     - Preformatted strings on the format ``xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`` can also be used

