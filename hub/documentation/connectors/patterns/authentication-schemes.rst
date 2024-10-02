Authentication schemes
======================

We support the following authentication schemes:

OAuth2
------

For connectors that use ``oauth2`` authentication, the following secrets are required:

.. list-table::
   :widths: 20, 30
   :header-rows: 1

   * - Property
     - Description
   * - ``client_id``
     - Public identifier for the client.
   * - ``client_secret``
     - The confidential key assigned to the client application.

and the following secrets will be injected into the system:

.. list-table::
   :widths: 20, 30, 10
   :header-rows: 1

   * - Property
     - Description
     - Type
   * - ``oauth_access_token``
     - The initial token used to authenticate the client (obtained during onboarding).
     - String
   * - ``oauth_client_id``
     - The client id as provided in the connector configuration.
     - String
   * - ``oauth_client_secret``
     - The client secret as provided in the connector configuration.
     - String
   * - ``oauth_refresh_token``
     - The token used to refresh the access token (obtained during onboarding).
     - String

API key
-------

For connectors that use ``api_key`` authentication, the following secrets are required:

.. list-table::
   :widths: 20, 30
   :header-rows: 1

   * - Property
     - Description
   * - ``api_key``
     - The key used to authenticate the client.

and the following secrets will be injected into the system:

.. list-table::
   :widths: 20, 30, 10
   :header-rows: 1

   * - Property
     - Description
     - Type
   * - ``api_key``
     - The api key as provided in the connector configuration.
     - String

* Api key is generally less secure than OAuth2, as it is a simple key that can be easily compromised. It is recommended to use OAuth2 whenever possible (some connectors support both schemes).

Tripletex authentication
------------------------

This is a custom style of authentication used by the Tripletex connector. It requires the following secrets:

.. list-table::
   :widths: 20, 30
   :header-rows: 1

   * - Property
     - Description
   * - ``consumer_key``
     - The unique key to create an integration with Tripletex.
   * - ``employee_token``
     - The token created by the administrator of the Tripletex account.

and the following secrets will be injected into the system:

.. list-table::
   :widths: 20, 30, 10
   :header-rows: 1

   * - Property
     - Description
     - Type
   * - ``consumer_key``
     - The consumer key as provided in the connector configuration.
     - String
   * - ``employee_token``
     - The employee token as provided in the connector configuration.
     - String

* Tripletex has production and test accounts. The production accounts use ``employee_token`` set by Sesam app while you have to set both tokens in the test accounts.

SuperOffice authentication
--------------------------

This is a custom style of authentication used by the SuperOffice connector. It is a regular Oauth2 authentication but injects an additional secret named ``so_ticket`` into the system. It requires the following secrets:

.. list-table::
   :widths: 20, 30
   :header-rows: 1

   * - Property
     - Description
   * - ``client_id``
     - Public identifier for the client.
   * - ``client_secret``
     - The confidential key assigned to the client application.

and the following secrets will be injected into the system:

.. list-table::
   :widths: 20, 30, 10
   :header-rows: 1

   * - Property
     - Description
     - Type
   * - ``so_ticket``
     - The ticket used to authenticate the client.
     - String
   * - ``SO-Apptoken``
     - The client secret as provided in the connector configuration.
     - String

JWT authentication
------------------

For connectors that use ``jwt`` authentication, the following secrets are required:

.. list-table::
   :widths: 20, 30
   :header-rows: 1

   * - Property
     - Description
   * - ``api_key``
     - The application token used to request the JWT access token. The token includes a set of access rights.

and the following secrets will be injected into the system:

.. list-table::
   :widths: 20, 30, 10
   :header-rows: 1

   * - Property
     - Description
     - Type
   * - ``jwt_access_token``
     - The JWT token used to authenticate the client (obtained during onboarding).
     - String
   * - ``jwt_refresh_token``
     - The token used to refresh the access token (obtained during onboarding).
     - String