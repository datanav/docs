========================
Source datatype mappings
========================

Introduction
============

The Sesam :doc:`entity model <entitymodel>` defines a set of :ref:`supported data types <entity_data_types>` that any
external types need to be mapped to. The various data sources have different schemas, and which types are supported and
their current mappings to the Sesam types is listed in this document.

.. _sql_types:

SQL systems
===========

This section documents which native types are supported by the RDBMS systems and to what Sesam type they map to.
Any unsupported column type will have to be blacklisted in the source configuration, or you will have to write a
custom query that coerces the non-supported column to a supported type.

.. _sql_server_types:

SQL Server
----------

The following is the supported native types of Microsoft SQL server. We support SQL Server 2008, but most of these
column types should be both forwards and backwards compatible with older and future SQL Server versions.

.. list-table::
   :header-rows: 1
   :widths: 30, 30, 40

   * - Native type
     - Sesam type
     - Comment

   * - ``INT``
     - Integer
     -

   * - ``TINYINT``
     - Integer
     -

   * - ``BIGINT``
     - Decimal
     -

   * - ``NUMERIC``
     - Decimal
     -

   * - ``FLOAT``
     - Float
     -

   * - ``REAL``
     - Float
     -

   * - ``DECIMAL``
     - Decimal
     -

   * - ``CHAR``
     - String
     -

   * - ``BIT``
     - Boolean
     - ``0`` is ``false`` and ``1`` is ``true``

   * - ``VARCHAR``
     - String
     -

   * - ``NVARCHAR``
     - String
     -

   * - ``DATE``
     - Datetime
     - Values with timezone will be shifted into UTC timezone on import.

   * - ``DATETIME``
     - Datetime
     - Values with timezone will be shifted into UTC timezone on import.

   * - ``DATETIME2``
     - String
     - Converted by the driver to ``YYYY-MM-DD hh:mm:ss[.nnnnnnn] [+|-]tz:offset`` ISO format (0-padded year-month-day
       hour-minute-seconds components plus fraction of a second after the decimal marker and an optional timezone-offset
       at the end). You can use DTL ``datetime-parse`` to convert it to a native Datetime object.

   * - ``TIME``
     - String
     - Converted by the driver to ``hh:mm:ss[.nnnnnnn]`` format (0-padded hour-minute-seconds components plus fraction of
       a second after the decimal marker (which is optional))

   * - ``UNIQUEIDENTIFIER``
     - UUID
     -

   * - ``XML``
     - String
     -

.. _oracle_types:

Oracle
------

The following is the supported native types of Oracle RDBMS. The tested version of oracle is Oracle 11g, but most of
the supported column types should be compatible with both older and newer versions of Oracle.

.. list-table::
   :header-rows: 1
   :widths: 30, 30, 40

   * - Native type
     - Sesam type
     - Comment

   * - ``INTEGER``
     - Integer
     -

   * - ``NUMBER``
     - Float
     - Depending on the column definition

   * - ``BINARY_FLOAT``
     - Float
     -

   * - ``BINARY_DOUBLE``
     - Float
     -

   * - ``CHAR``
     - String
     -

   * - ``VARCHAR``
     - String
     -

   * - ``VARCHAR2``
     - String
     -

   * - ``DATE``
     - Datetime
     - The range of this datatype is unlimited to nanosecond precision.
       Values with timezone will be shifted into UTC timezone on import.

   * - ``TIMESTAMP``
     - Datetime
     - The range of this datatype is unlimited to nanosecond precision.
       Values with timezone will be shifted into UTC timezone on import.

   * - ``BLOB``
     - Bytes
     -

   * - ``CLOB``
     - String
     -

   * - ``NCLOB``
     - String
     -

   * - ``RAW``
     - Bytes
     -

   * - ``LONG RAW``
     - Bytes
     -

   * - ``XMLType``
     - String
     -

.. _mysql_types:

MySQL
-----

The following is the supported native types of MySQL. The tested version is 5.6, but most of
the supported column types should be compatible with both older and newer versions of MySQL.

.. list-table::
   :header-rows: 1
   :widths: 30, 30, 40

   * - Native type
     - Sesam type
     - Comment

   * - ``INT``
     - Integer
     -

   * - ``TINYINT``
     - Integer
     -

   * - ``BIGINT``
     - Integer
     -

   * - ``NUMERIC``
     - Decimal
     -

   * - ``FLOAT``
     - Float
     -

   * - ``REAL``
     - Decimal
     -

   * - ``DOUBLE``
     - Decimal
     -

   * - ``DECIMAL``
     - Decimal
     -

   * - ``BIT``
     - Integer
     - ``0`` or ``1``

   * - ``BOOLEAN``
     - Integer
     - ``0`` or ``1``

   * - ``CHAR``
     - String
     -

   * - ``BINARY``
     - Bytes
     -

   * - ``VARCHAR``
     - String
     -

   * - ``VARBINARY``
     - Bytes
     -

   * - ``TEXT``
     - String
     -

   * - ``TINYTEXT``
     - String
     -

   * - ``DATETIME``
     - Datetime
     - The range of this datatype is unlimited to nanosecond precision.
       Values with timezone will be shifted into UTC timezone on import.

   * - ``DATE``
     - Datetime
     - The time part of the Datetime object is set to midnight (i.e. ``00:00:00.00000``)

   * - ``YEAR``
     - Integer
     - Range is ``1901``to ``2155``

   * - ``TIME``
     - String
     - Converted by the driver to ``hh:mm:ss[.nnnnnnn]`` format (0-padded hour-minute-seconds components plus fraction of
       a second after the decimal marker (which is optional))

   * - ``TIMESTAMP``
     - Datetime
     -

   * - ``TINYBLOB``
     - Bytes
     -

   * - ``MEDIUMBLOB``
     - Bytes
     -

   * - ``BLOB``
     - Bytes
     -

   * - ``LONGBLOB``
     - Bytes
     -

   * - ``ENUM``
     - Varying
     - Based on enum type

   * - ``SET``
     - Varying
     - List of values, based on set type


.. _postgresql_types:

PostgreSQL
----------

The following is the supported native types of PostgreSQL. The tested version is 9.5, but most of
the supported column types should be compatible with both older and newer versions of PostgreSQL.

.. list-table::
   :header-rows: 1
   :widths: 30, 30, 40

   * - Native type
     - Sesam type
     - Comment

   * - ``INTEGER``
     - Integer
     -

   * - ``SMALLINT``
     - Integer
     -

   * - ``BIGINT``
     - Integer
     -

   * - ``NUMERIC``
     - Decimal
     -

   * - ``REAL``
     - Float
     -

   * - ``DOUBLE``
     - Float
     -

   * - ``DECIMAL``
     - Decimal
     -

   * - ``BOOLEAN``
     - Boolean
     -

   * - ``CHAR``
     - String
     -

   * - ``VARCHAR``
     - String
     -

   * - ``TEXT``
     - String
     -

   * - ``TIMESTAMP``
     - Datetime
     - The range of this datatype is unlimited to nanosecond precision.
       Values with timezone will be shifted into UTC timezone on import.

   * - ``DATE``
     - String
     - Converted to ``YYYY-MM-DD`` format (0-padded year-month-day components)

   * - ``TIME``
     - String
     - Converted by the driver to ``hh:mm:ss[.nnnnnnn][+|-tz:offset]`` ISO format (0-padded hour-minute-seconds
       components plus fraction of a second after the decimal marker and a timezone-offset
       at the end).

   * - ``BYTEA``
     - Bytes
     -

   * - ``ENUM``
     - Varying
     - Based on enum type

   * - ``UUID``
     - String
     -

   * - ``XML``
     - String
     -
