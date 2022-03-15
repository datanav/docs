
.. _mssql_system:

Legacy Microsoft SQL system
---------------------------

The Legacy Microsoft SQL system represents a `Microsoft SQL Server <https://en.wikipedia.org/wiki/Microsoft_SQL_Server>`_ available over the network.

Note that this system is a legacy system that's based on open source drivers and has been superceded by the
:ref:`Microsoft SQL Server <mssql-sqlserver_system>` which uses official microsoft drivers.

See the :ref:`supported column types <sql_server_types>` list for a overview of which SQL Server column types
are supported and how they are mapped to :ref:`Sesam types <entity_data_types>`.

Prototype
^^^^^^^^^

::

    {
        "_id": "sql_system_id",
        "type": "system:mssql",
        "name": "Legacy Microsoft SQL Server Database",
        "username":"$ENV(username-variable)",
        "password":"$SECRET(password-variable)",
        "host":"fqdn-or-ip-address-here",
        "tds_version":"7.4",
        "instance": "named-instance",
        "port": 1433,
        "database": "database-name"
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

   * - ``username``
     - String
     - Username to use when connecting to the database.
     -
     - Yes

   * - ``password``
     - String
     - Password to use when connecting to the database.
     -
     - Yes

   * - ``host``
     - String
     - Host name or IP address to the database server. Must be DNS resolvable if non-numeric.
     -
     - Yes

   * - ``instance``
     - String
     - The name of the SQL Server "named instance", if applicable. Note that if ``instance`` is set, ``port`` will be
       ignored as SQL Server will assign a "named instance" a random port by default. Be aware that using such
       "port-less" named instances potentially has consequences for the configuration of firewall rules as well
       (i.e. for both TCP and UDP port ranges, please consult the SQL Server DBA or SQL Server manual for details).
     -
     -

   * - ``port``
     - Integer
     - Database IP port. Note: ignored if ``instance`` is set, see the previous section.
     - 1433
     -

   * - ``database``
     - String
     - Name/id of database to connect to.
     -
     - Yes

   * - ``tds_version``
     - String
     - Version of the `TDS protocol <https://en.wikipedia.org/wiki/Tabular_Data_Stream>`_ to use for the driver.
       Note that the default is ``null`` which means it's not set. This will tell the database driver to attempt to
       auto-detect the protocol version, which should work in most cases. However, if you experience unknown or general
       connection errors, you can try to specify the TDS protocol version string manually (typically on the
       form "7.0", "7.4" etc).
     -
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

Example MS SQL Server configuration:

::

    {
        "_id": "sqlserver_db",
        "name": "Legacy MS SQL Server test database",
        "type": "system:mssql",
        "username": "$ENV(username-variable)",
        "password": "$SECRET(password-variable)",
        "host": "localhost",
        "port": 1433,
        "database": "testdb"
    }
