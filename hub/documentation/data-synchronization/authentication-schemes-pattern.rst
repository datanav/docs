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

* Example of connectors using OAuth2: `Hubspot <https://github.com/sesam-io/hubspot-connector/blob/playground>`__, `Keap <https://github.com/sesam-io/keap-connector/blob/playground>`__, `Shopify <https://github.com/sesam-io/shopify-connector/blob/playground>`__, `Sage <https://github.com/sesam-io/sage-connector/blob/playground>`__, `ZohoCRM <https://github.com/sesam-io/zohocrm-connector/blob/playground>`__, `Wave <https://github.com/sesam-io/wave-connector/blob/playground>`__, `BusinessCentral <https://github.com/sesam-io/businesscentral-connector/blob/playground>`__, `Asana <https://github.com/sesam-io/asana-connector/blob/playground>`__
* A full connector example with Oauth2 authentication could be found in `Hubspot connector's playground branch <https://github.com/sesam-io/hubspot-connector/blob/playground>`__ in the `Manifest <https://github.com/sesam-io/hubspot-connector/blob/playground/manifest.json>`__ and `System <https://github.com/sesam-io/hubspot-connector/blob/playground/templates/system.json>`__.

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
* Example of connectors using API key: `PowerofficeGo <https://github.com/sesam-io/powerofficego-connector/blob/playground>`__, `WooCommerce <https://github.com/sesam-io/woocommerce-connector/blob/playground>`__, `Wix <https://github.com/sesam-io/wix-connector/blob/playground>`__
* A full connector example with API key authentication could be found in `WooCommerce connector's playground branch <https://github.com/sesam-io/woocommerce-connector/tree/playground>`__ in the `Manifest <https://github.com/sesam-io/woocommerce-connector/blob/playground/manifest.json>`__ and `System <https://github.com/sesam-io/woocommerce-connector/blob/playground/templates/system.json>`__.

Tripletex authentication
------------------------

This is a custom style of authentication used by the Tripletex connector. It requires the following secrets:

.. list-table::
   :widths: 20, 30
   :header-rows: 1

   * - Property
     - Description
   * - ``consumer_token``
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
   * - ``consumer_token``
     - The consumer key as provided in the connector configuration.
     - String
   * - ``employee_token``
     - The employee token as provided in the connector configuration.
     - String

* Tripletex has production and test environments. The production accounts use ``employee_token`` set by Sesam app while you have to set both tokens in the test accounts.
* A full connector example with custom Tripletex authentication could be found in `Tripletex connector's playground branch <https://github.com/sesam-io/tripletex-connector/tree/playground>`__ in the `Manifest <https://github.com/sesam-io/tripletex-connector/blob/playground/manifest.json>`__ and `System <https://github.com/sesam-io/tripletex-connector/blob/playground/templates/system.json>`__.

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

* A full connector example with custom Superoffice authentication could be found in `Superoffice connector's playground branch <https://github.com/sesam-io/superoffice-connector/tree/playground>`__ in the `Manifest <https://github.com/sesam-io/superoffice-connector/blob/playground/manifest.json>`__ and `System <https://github.com/sesam-io/superoffice-connector/blob/playground/templates/system.json>`__.

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

* Example of connectors using JWT: `webCRM <https://github.com/sesam-io/webcrm-connector/blob/playground>`__
* A full connector example with JWT authentication could be found in `webCRM connector's playground branch <https://github.com/sesam-io/webcrm-connector/tree/playground>`__ in the `Manifest <https://github.com/sesam-io/webcrm-connector/blob/playground/manifest.json>`__ and `System <https://github.com/sesam-io/webcrm-connector/blob/playground/templates/system.json>`__.