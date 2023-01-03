
.. _oracle_tns_system:

Oracle TNS system
-----------------

The Oracle SQL system represents a Oracle RDBMS configured using a `TNS name <http://www.orafaq.com/wiki/Tnsnames.ora>`_
See the :ref:`supported column types <oracle_types>` list for a overview of which Oracle column types are supported
and how they are mapped to :ref:`Sesam types <entity_data_types>`.

Prototype
^^^^^^^^^

::

    {
        "_id": "sql_system_id",
        "type": "system:oracle_tns",
        "name": "The Oracle Database",
        "username":"$ENV(username-variable)",
        "password":"$SECRET(password-variable)",
        "tns_name": "tns-name-here",
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

   * - ``tns_name``
     - String
     - A fully qualified `Oracle TNS name <http://www.orafaq.com/wiki/Tnsnames.ora>`_
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

Example Oracle TNS configuration:

::

    {
        "_id": "oracle_db",
        "name": "Oracle test database",
        "type": "system:oracle_tns",
        "username": "$ENV(username-variable)",
        "password": "$SECRET(password-variable)",
        "tns_name": "(DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = foo)(PORT = 1521)) (CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = BAR)))"",
        "coerce_to_decimal": true
    }

