.. _postgresql_system:

PostgreSQL system
-----------------

The PostgreSQL system represents a `PostgreSQL RDBMS <https://en.wikipedia.org/wiki/PostgreSQL>`_ available on the network.
See the :ref:`supported column types <postgresql_types>` list for a overview of which PostgreSQL column types are supported
and how they are mapped to :ref:`Sesam types <entity_data_types>`.

Prototype
^^^^^^^^^

::

    {
        "_id": "sql_system_id",
        "type": "system:postgresql,
        "name": "The PostgreSQL Database",
        "username":"$ENV(username-variable)",
        "password":"$SECRET(password-variable)",
        "host":"fqdn-or-ip-address-here",
        "port": 5432,
        "database": "database-name",
        "sslmode": "prefer"
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

   * - ``port``
     - Integer
     - Database IP port.
     - 5432
     -

   * - ``database``
     - String
     - Name/id of database to connect to.
     -
     - Yes

   * - ``sslmode``
     - String
     - The ssl mode to use. The value has to be one of "disable", "allow", "prefer", "require", "verify-ca" or "verify-full".
       Please consult the `PostgreSQL documentation <https://www.postgresql.org/docs/10/libpq-ssl.html>`_  for
       the full details of what these modes entail.
     - ``"prefer"``
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

Example PostgreSQL configuration:

::

    {
        "_id": "postgresql_db",
        "name": "PostgreSQL test database",
        "type": "system:postgresql",
        "username": "$ENV(username-variable)",
        "password": "$SECRET(password-variable)",
        "host": "test.postgresql.mydomain.com",
        "database": "test"
    }

