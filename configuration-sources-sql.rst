.. _sql_source:

SQL source
----------

The `SQL <https://en.wikipedia.org/wiki/SQL>`_ database source is one of the most commonly used data sources.
In short, it presents `database relations <https://en.wikipedia.org/wiki/Relation_(database)>`_ (i.e. ``tables``,
``views`` or ``queries``) as a entity stream to Sesam.

The SQL source has several options, all of which are presented below with their default values:

Prototype
^^^^^^^^^

::

    {
        "system": "id-of-system",
        "table": "name-of-table",
        "primary_key": ["list","of","key","names"],
        "query": "SQL query string",
        "updated_query": "SQL query string for 'since' support in queries",
        "updated_column": "column-name-for-since-support-in-tables",
        "whitelist": ["columns","to","include"],
        "blacklist": ["columns","to","exclude"],
        "fetch_size": 1000,
        "preserve_null_values": false,
        "schema": "default-schema-name-if-included"
    }


Column types
^^^^^^^^^^^^

See the :ref:`supported column types <sql_types>` list for a overview of which RDBMS column types
are supported and how they are mapped to :ref:`Sesam types <entity_data_types>`. Note that if your ``table`` or
``query`` property refer to relations with unsupported column types, you will either have to use the ``blacklist``
configuration property to ignore them, or write a custom ``query`` that coerces the non-supported column to a
supported type.

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
     - Must refer to a :ref:`SQL system <sql_system>` component by ``id``. The role of this component is provide
       services like connection pooling and authentication for the data sources using it
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
       the ``query`` property us used. Note that this property might be case sensitive.
     -
     -

   * - ``query``
     - List<String> or String
     - Must be a valid query in the dialect of the ``RDBMS`` represented by the
       ``system`` property. You will also have to configure the primary key(s)
       of the query in the ``primary_key`` property. Note: mutually exclusive with the
       ``table`` property with ``table`` taking precedence. If a list of strings is given, they will be
       converted to a single string by concatenation with the newline character.
     -
     - Yes

   * - ``updated_column``
     - String
     - If the underlying relation contains information about updates, the data source is
       able to support ``since`` markers. You can provide the name of the column to use
       for such queries here. This must be a valid column name in the ``table`` or ``query``
       result sets and it must be of a data type that supports larger or equal (">=") tests
       for the ``table`` case. Note that this property might be case sensitive.
     -
     -

   * - ``updated_query``
     - List<String> or String
     - If the ``query`` property is set, the ``since`` support must be expressed by a
       full query including any test needed. A single variable binding
       ``:since`` must be included somewhere in the query string - for example
       "select * from view_name v where v.updates >= :since". If a list of strings is given, they will be
       converted to a single string by concatenation with the newline character.

       .. WARNING::

          The ``updated_query`` must cover the exact same ids as the
          ``update`` query. If not you run the risk of a full sync
          failing and then completing in incremental mode, which would
          mean that the full sync is not covering all ids and thus end
          up deleting ids not seen. Consider setting
          ``is_chronological_full`` to ``false`` on pipes to prevent
          the pipe offset from being set during a full sync.

     -
     -

   * - ``schema``
     - String
     - If a specific schema within a database is needed, you must provide its name in this property.
       Do *not* use schema names in the ``table`` property.
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

   * - ``preserve_null_values``
     - Boolean
     - If set to ``true`` will include null values in the entities produces by this source. By default they are omitted.
     - False
     -

   * - ``fetch_size``
     - Integer
     - The fetch size of the result sets (number of rows in a cursor fetch) to get from the database
     - 1000
     -

   * - ``if_source_empty``
     - Enum<String>
     - Determines the behaviour of the pipe when the SQL source does not return any entities. Normally, any previously synced
       entities will be deleted even if the pipe does not receive any entities from its source.
       If set to ``"fail"``, the pipe will automatically fail if the source returns no entities. This means that any
       previous entities in the pipe's dataset are not deleted.
       If set to ``"accept"``, the pipe will *not* fail and any previously synced entities will be deleted.

       The global default ``global_defaults.if_source_empty`` can be set for all pipes in the
       :ref:`service metadata <service_metadata_section>`.
     - ``"accept"``
     -

Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``false`` (Dynamic: ``true`` if ``updated_column`` set)

   * - ``is_since_comparable``
     - ``true`` (Default)

   * - ``is_chronological``
     - ``false`` (Dynamic: if ``table`` and ``updated_column`` set then defaults to ``true``, if ``query`` then it can be set explicitly)

   * - ``is_chronological_full``
     - ``false`` (Dynamic: ``true`` if ``is_chronological`` is effectively ``true`` and this property is not explicity set to ``false``)

       If this property is set to ``false`` then a full run will not
       consider the source to be chronological even though it is
       chronological in incremental runs.

       .. NOTE::

          In practice this avoids doing an order by when doing full runs,
          but at the cost of not saving pipe offsets and supporting
          incremental deletion tracking if it fails to complete.

          We have seen SQL tables where only the latest rows have
          an value in the updated column. In that case it is not that
          useful to use order by and to save pipe offsets
          incrementally.


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
            "updated_column": "updated"
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
            "updated_query": "select * from my_table where updated >= :since"
        }
    }
