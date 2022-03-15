.. _oracle_system:

Oracle system
-------------

The Oracle SQL system represents a `Oracle RDBMS <https://en.wikipedia.org/wiki/Oracle_Database>`_ available on the network.
See the :ref:`supported column types <oracle_types>` list for a overview of which Oracle column types are supported
and how they are mapped to :ref:`Sesam types <entity_data_types>`.

Prototype
^^^^^^^^^

::

    {
        "_id": "sql_system_id",
        "type": "system:oracle",
        "name": "The Oracle Database",
        "username":"$ENV(username-variable)",
        "password":"$SECRET(password-variable)",
        "host":"fqdn-or-ip-address-here",
        "port": 1521,
        "database": "database-name",
        "coerce_to_decimal": false
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
     - 1521
     -

   * - ``database``
     - String
     - Name/id of database to connect to.
     -
     - Yes

   * - ``coerce_to_decimal``
     - Boolean
     - If set to `true`, it will force the use of the decimal type for all "numeric" types (i.e. numbers with precision
       and scale information). What type the column data ends up as is not clearly defined by the current oracle
       backend driver so in some cases it may yield a float value instead of a decimal value. This property should
       always be set to `true` if your flows care if numeric values are floats or decimals. The default value is `false`.
     - ``false``
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

Example Oracle configuration:

::

    {
        "_id": "oracle_db",
        "name": "Oracle test database",
        "type": "system:oracle",
        "username": "$ENV(username-variable)",
        "password": "$SECRET(password-secret)",
        "host": "oracle",
        "database": "XE",
        "coerce_to_decimal": true
    }

