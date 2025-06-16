
.. _mysql_system:

MySQL system
------------

The MySQL system represents a `MySQL database <https://en.wikipedia.org/wiki/MySQL>`_ available over the network:
See the :ref:`supported column types <mysql_types>` list for a overview of which MySQL column types are supported and
how they are mapped to :ref:`Sesam types <entity_data_types>`.

Prototype
^^^^^^^^^

.. code-block :: json

    {
        "_id": "sql_system_id",
        "type": "system:mysql",
        "name": "The MySQL Database",
        "username":"$ENV(username-variable)",
        "password":"$SECRET(password-variable)",
        "host":"fqdn-or-ip-address-here",
        "port": 3306,
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

   * - ``port``
     - Integer
     - Database IP port.
     - 3306
     -

   * - ``database``
     - String
     - Name/id of database to connect to.
     -
     - Yes

   * - ``sslmode``
     - String
     - The ssl mode to use. The value has to be one of "disabled", "preferred", or "required".
       Please consult the `MySQL documentation <https://dev.mysql.com/doc/refman/8.4/en/connection-options.html#option_general_ssl-mode>`_  for
       the full details of what these modes entail.
     - ``"preferred"``
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

Example MySQL configuration:

.. code-block :: json

    {
        "_id": "sqlserver_db",
        "name": "MySQL test database",
        "type": "system:mysql",
        "username": "$ENV(username-variable)",
        "password": "$SECRET(password-variable)",
        "host": "localhost",
        "port": 3306,
        "database": "testdb"
    }

