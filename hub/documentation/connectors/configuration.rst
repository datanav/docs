=======================
Connector Configuration
=======================

In a particular environment, connectors can be configured using a ``config.json`` file. This file has a property called ``connector_config`` whose value is the configuration of an embedded pipe with the same name. By editing the entities in the embedded source, the various connectors can be configured.


Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10

   * - Property
     - Type
     - Description
     - Required?

   * - ``_id``
     - String
     - The id of the connector. This id will be used throughout the various components
     - Yes

   * - ``type``
     - String
     - Must always be equal to ``connector``
     - Yes

   * - ``visible``
     - Boolean
     - Specifies if this connector should be visible in the UI at all. Default is true.
     - No

   * - ``additional-properties``
     - Object
     - Dictionary of objects that specifies values that we need from the user and what they should be called. The key specifies the identifier of the property
     - No

   * - ``additional-properties.<property>.name``
     - String
     - Display name for the property for the user - becomes the label for the text field.
     - No

   * - ``additional-properties.<property>.description``
     - String
     - Description of the property for the user that explains what it is.
     - No

   * - ``account_selection``
     - Object
     - Dictionary for configuring the account selection feature. This can be used if the system supports multiple accounts per user and there is a way for us to get that list and present it to the user to choose between.
     - No

   * - ``account_selection.endpoint``
     - String
     - The endpoint in the external system that the backend should POST to in order to retrieve the list of accounts.
     - No

   * - ``account_selection.payload_property``
     - String | Array<String>
     - Optional, can be a string, or a list of strings, and defines how to traverse the obtained response from the system.
     - No

   * - ``account_selection.id_property``
     - String | Array<String>
     - Tells which property to use for obtaining the account, after (optionally) traversing the obtained response using payload_property.
     - No

   * - ``account_selection.label_property``
     - String | Array<String>
     - Tells which property in the response to use for labeling the account, after (optionally) traversing the obtained response using payload_property.
     - No

   * - ``auth``
     - Object
     - Configuration options related to the authorization scheme for the particular system. The properties under this object are shown below.
     - Yes

   * - ``description``
     - String
     - The text shown below the title in the connector card on the dashboard in Management Console.
     - Yes

   * - ``docs_url``
     - String
     - A link to our own docs on this specific connector.
     - Yes

   * - ``logo``
     - String
     - A URL that holds the logo for the system this connector is made for. This property should point to a bigger version of the logo, with the name if the system included.
     - Yes


   * - ``logo``
     - String
     - A URL that holds the logo for the system this connector is made for. This property should point to a bigger version of the logo, with the name if the system included.
     - Yes

   * - ``logo_symbol``
     - String
     -  A URL that holds the logo for the system this connector is made for. This property should point to a smaller version of the logo, an icon without text, if available.
     - Yes

   * - ``hidden_entity_types``
     - Array
     - A list of entity types that should be hidden from the UI for this connector. The values here must reference the ids of the entity types as defined in the manifest.
     - No

   * - ``multi-tenant``
     - Boolean
     - This property tells us if this connector is something that every tenant can use. With the exception of "shared" connectors like ``difi`` or ``wikidata``, this is always ``true``.
     -

   * - ``favicon``
     - String
     - Favicon used for this connector.
     - No

   * - ``title``
     - String
     - The title shown on the connector card on the dashboard in Management Console.
     - Yes

   * - ``category``
     - String
     - Which category of system this is, such as ERP, CRM. Unused in the UI currently.
     - Yes

   * - ``stage``
     - String
     - Which stage of development this connector is in. Unused in the UI currently.
     - Yes

   * - ``url``
     - String
     - Important property as this points towards the raw URL for which connector repository to use, including the branch (or commit hash). Ex: https://raw.githubusercontent.com/sesam-io/wave-connector/playground
     - Yes

   * - ``parameter_values``
     - Object
     - A dictionary of parameters that should overwrite those specified in the connector manifest. E.g. if there is a ``base_url`` in the manifest, the value can be manually specified here.
     - No

   * - ``connect_flow``
     - Object
     - Properties that can be used to configure the connection flow for this connector.
     - No

   * - ``connect_flow.custom_sections``
     - Array
     - With this you can specify custom sections of text in the connect flow as such:
     - No

   * - ``connect_flow.custom_sections.[].order``
     - Integer
     - Specifies the ordering of the section
     - No

   * - ``connect_flow.custom_sections.[].title``
     - String
     - Title of the section
     - No

   * - ``connect_flow.custom_sections.[].content``
     - String
     - The actual body of text for the section
     - No

   * - ``vendor``
     - Object
     - Parameters that determine the styling of the dashboard when this connector is chosen as the vendor (i.e. the first connector).
     - Yes

   * - ``vendor.banner``
     - String
     - The name of the "product" that corresponds to when this connector is used as the vendor (primary/first system), e.g. `Making Freshteam Talk`
     - Yes

   * - ``vendor.description``
     - String
     - The text used in the dashboard when this system is used as the vendor, e.g. `Connect to these services to synchronize your data with SuperOffice.`.
     - Yes

   * - ``vendor.title``
     - String
     - The display title used for the system this connector connects to, e.g. SuperOffice.
     - Yes

   * - ``vendor.supported_connectors``
     - Array
     - A list of connectors that can be connected to when this system is the vendor. This filters the connectors that can be seen in the dashboard after the first connection. The entries in the list need to correspond to the _ids of the other connectors.
     - No

   * - ``vendor.hidden_entity_type_options``
     - Array
     - List of entity type options that should be hiddne from the UI for all connectors, when we are using this vendor. Example values are ``fullsync`` and ``share_enabled``.
     - No

   * - ``vendor.homepageLogo``
     - Object
     - Properties for the logo of the homepage for this vendor
     - No

   * - ``vendor.homepageLogo.logo``
     - String
     - URL for the logo used for the homepage link.
     - No

   * - ``vendor.homepageLogo.homepageUrl``
     - String
     - URL of the corresponding marketplace for this vendor, e.g. ``https://wave.sesam.io``.
     - No


Properties in the ``auth`` object for API key based connectors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10

   * - Property
     - Type
     - Description
     - Required?

   * - ``auth.type``
     - String
     - Specifies the type of authorization - either ``oauth2`` for when connectors support the OAuth protocol or `api_key` for other approaches based on manually providing api_keys, tokens and similar.
     - Yes

   * - ``auth.api_base_url``
     - String
     - This will replace the ``{{@ base_url @}}`` expression in templates. The endpoints in the connector's API can vary from environment to environment (e.g. using a test environment in Playground, prod environment in Prod), so we configure this per branch.
     - Yes

   * - ``auth.label``
     - String
     - Human-readable label for the API key field. Without it, the field is just called "API Key". Only relevant for api key based connectors.
     - Yes



Properties in the ``auth`` object for OAuth2 based connectors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10

   * - Property
     - Type
     - Description
     - Required?

   * - ``auth.type``
     - "api_key" | "oauth2"
     - Specifies the type of authorization - either ``oauth2`` for when connectors support the OAuth protocol or `api_key` for other approaches based on manually providing api_keys, tokens and similar.
     - Yes

   * - ``auth.api_base_url``
     - String
     - Similar to the config for the API key type authentication, the connector-deployer uses this for the ``{{@ base_url @}}`` value. In the Management console it is only needed for the Tripletex connector.
     - Yes

   * - ``auth.access_token_url``
     - String
     - The endpoint that the Management Console should use when requesting an access token. The access token is used in API requests towards the connector's systems.
     - Yes
      
   * - ``auth.authorize_scopes``
     - String
     - The scopes that represent which permissions the user must grant to our OAuth2 application. In the case of Hubspot, the scopes must be a subset of the scopes that we have set in the application configuration - this might vary from connector to connector. Some OAuth2 connectors don't require any scopes at all. It is recommended to use the openid scope if the provider supports it, since that allows us to extract the identity of the user that is connecting.
     - Yes
     
   * - ``auth.identity_url``
     - String
     - Currently only HubSpot uses this. This is an endpoint that provides user identity information given an existing access token. In this case it is required for determining the account ID of the tenant.
     - Yes
     
   * - ``auth.login_url``
     - Object
     - This is the URL that we should send the tenant to when they want to connect this connector. Generally, this is the page where the tenant will select their account on the external site. Sometimes it's called the "authorize" URL, and often ends with ``/authorize``.
     - Yes
     
   * - ``auth.tenant_id_expression``
     - String | Array
     - A bit of a misleading name, since this property is used for pointing to which property in the response from the external system that should be used as the account_id (not tenant_id). This property is taken from the token response when authorizing. As en example, the response from HubSpot (after calling the identity endpoint) returns properties where one of them is called ``hub_id``. The value of that is what we want to use as the account id. This can either be a string where it's just a name of the property to use, or it can be a list of string specifying the path to get to the property.
     - Yes
