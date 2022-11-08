.. _ldap_system:

LDAP system
-----------

The LDAP system contains the configuration needed to communicate with a
`LDAP <https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol>`_ system. It is used by
:ref:`LDAP sources <ldap_source>` to stream entities from LDAP catalogs.
Note that `Microsoft ActiveDirectory <https://en.wikipedia.org/wiki/Active_Directory>`_ is also supported
through its LDAP-compatible interface/API.

It supports the following properties:

Prototype
^^^^^^^^^

::

    {
        "host": "FQDN of LDAP host",
        "port": 389,
        "use_ssl": false,
        "verify_ssl": true,
        "username": "$ENV(username-variable)",
        "password": "$SECRET(password-variable)",
        "charset": "latin-1",
        "custom_ca_pem_chain": "-----BEGIN CERTIFICATE-----\nMIIGYTCCB[...]\n-----END CERTIFICATE-----\n",
        "connect_timeout": 60,
        "read_timeout": 1800
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

   * - ``host``
     - String
     - The fully qualified domain name (``FQDN``) of the LDAP host server. Note: do not use a URL on the form
       "ldap(s)://<host>:<port>" but use the ``host``, ``port`` and ``use_ssl`` properties separately instead.
     - "localhost"
     -

   * - ``port``
     - Integer
     - The TCP port of the LDAP service.
     - 389
     -

   * - ``use_ssl``
     - Boolean
     - Indicates to the client whether to use a secure socket layer (``SSL``) or not when communicating with the LDAP service
     - false
     -

   * - ``use_ssl``
     - Boolean
     - If ``use_ssl`` is set to ``true`` then this property controls if the certificate used for the connection should be verified.
     - true
     -

   * - ``custom_ca_pem_chain``
     - String
     - If ``use_ssl`` is set to ``true`` this property can hold a chain of certificates (in PEM format) that
       should be used to verify the SSL connection.
     -
     -

   * - ``username``
     - String
     - The user to authenticate as against the LDAP service. If not set, no authentication will be attempted.
     -
     -

   * - ``password``
     - String
     - The password to use for authenticating with the LDAP service. Required if ``username`` is set.
     -
     - Yes

   * - ``charset``
     - String
     - The charset used to encode strings in the LDAP database. Defaults to ``"latin-1"`` aka ``"ISO-8859-1"``,
       as ``"UTF-8"`` is usually not the default encoding in LDAP catalogs at the time of writing.
     - "latin-1"
     -

   * - ``connect_timeout``
     - Integer
     - Number of seconds to wait for connecting to the LDAP server before timing out.
     - ``60``
     -

   * - ``read_timeout``
     - Integer
     - Number of seconds to wait for the LDAP server to respond to a request before timing out.
     - ``1800``
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "example_ldap",
        "name": "Example LDAP server",
        "type": "system:ldap",
        "host": "ldap.example.org",
        "port": 389,
        "username": "$ENV(username-variable)",
        "password": "$SECRET(password-variable)"
    }
