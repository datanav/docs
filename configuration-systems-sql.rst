
.. _sql_system:

SQL systems
-----------

The SQL system components represents a `RDBMS <https://en.wikipedia.org/wiki/Relational_database_management_system>`_
and contains the necessary information to establish a connection to the RDBMS and manage these connections among the
sources that read from it. It can also provide source configurations for reading from all tables it can introspect
from the RDBMS `schema <https://en.wikipedia.org/wiki/Database_schema>`_.

The common properties for all SQL systems are:

Prototype
^^^^^^^^^

::

    {
        "_id": "sql_system_id",
        "type": "system:oracle|oracle_tns|mssql|mysql",
        "name": "The Foo Database",
        "db-type-specific-property":"some-value",
        "timezone": "UTC",
        "pool_size": 10,
        "pool_timeout": 30,
        "pool_max_overflow": 10,
        "pool_recycle": 1800
    }

Column type mapping
^^^^^^^^^^^^^^^^^^^

See the :ref:`supported column types <sql_types>` section for a overview of which column types are supported
for each RDBMS system and how they are mapped to :ref:`Sesam types <entity_data_types>`.

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

   * - ``timezone``
     - String
     - The local timezone for the database server. It is used for any date(time) objects returned that doesn't have any
       timezone information. The default is the UTC timezone. All the official timezone names are supported,
       i.e. "UTC", "GMT", "EST" etc. You can also use the indirect "Continent/City" format, for example "Europe/Oslo"
       (see `the complete list <https://twiki.org/cgi-bin/xtra/tzdatepick.html>`_ for which cities are supported).

       .. WARNING::

          Non-timezone datetime values that are read from  a ``sql``
          source that uses the system will be shifted from the specified
          timezone to UTC. Note that the ``_updated`` property will
          not be shifted.

          Also note that Sesam relies on tabulated historical data for daylight
          saving information for the various timezones. This data gets corrected or
          supplemented from time to time which means that the result of a timezone
          conversion operation can change over time.

     - "UTC"
     -

   * - ``pool_size``
     - Integer
     - The target maximum number of concurrent connections to the database
     - 10
     -

   * - ``pool_timeout``
     - Integer
     - The number of seconds to wait before giving up on getting a connection from the connection pool.
     - 30
     -

   * - ``pool_max_overflow``
     - Integer
     - How many connections over the ``pool_size`` are allowed before refusing to establish a incoming connection. This
       means that the absolute hard limit of connections in a connection pool is ``pool_size`` + ``pool_max_overflow``.
     - 10
     -

   * - ``pool_recycle``
     - Integer
     - This configuration option prevents the pool from using a particular connection that has passed a certain age,
       and is appropriate for database backends such as MySQL that automatically close connections that have been stale
       after a particular period of time. Note that this doesn't affect any open/active connections.
     - 1800
     -
