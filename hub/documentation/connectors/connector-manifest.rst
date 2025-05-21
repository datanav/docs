.. _connector_manifest:

======================
The connector manifest
======================

The manifest file allows you to configure which datatypes should use which templates. In many cases the data synchronization part are identical for many datatypes in a specific system, i.e. except for the naming of the datatypes the DTL pipe configurations are the same. 

Instead of creating several identical flows, one can simply re-use the same template for different datatypes whenever possible.

Example of a *manifest* file:

.. code-block:: json

  {
    "auth": "<value>",
    "datatypes": {
      "contact": {
        "template": "templates/contact.json"
      },
      "product": {
        "template": "templates/contact.json"
      },
      "project": {
        "template": "templates/contact.json"
      },
      "country": {
        "template": "templates/country.json"
      }
    },
    "system-template": "templates/system.json"
  }

In this case, the ``contact``, ``product`` and ``project`` datatypes from this specific system all had the exact same configuration, which means we could re-use the contact template for all three. The ``country`` datatype however required its own template. 

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10

   * - Property
     - Type
     - Description
     - Required?
     
   * - ``auth``
     - String
     - Specifies the type of authorization - either ``oauth2`` for when connectors support the OAuth protocol or ``api_key`` for other approaches based on manually providing api_keys, tokens and similar. 
     - Yes
     
   * - ``auth_variant``
     - String
     - If the auth flow has a specific auth variations that is not standard. Currently supports the values ``superoffice-ticket`` for ``oauth2`` auth and ``jwt``, ``tripletex`` and ``service_account`` for ``api_key`` auth.    
     - No
     
   * - ``oauth2.login_url``
     - ObjectString
     - If ``oauth2`` value in the ``auth`` property, the ``login_url`` (authorization URL).  
     - No     

   * - ``oauth2.scopes``
     - ArrayString | Array<String>
     - If ``oauth2`` value in the ``auth`` property, the required ``scopes``.  
     - No     

   * - ``oauth2.token_url``
     - String
     - If ``oauth2`` value in the ``auth`` property, the ``token_url``.  
     - No     

   * - ``datatypes``
     - Object
     - A dictionary of dictionaries with the datatype names as key. The key will be injected to all ``{{@ datatype @}}`` occurrences in the template file it points to. The properties under each datatype object are shown below. 
     - Yes

   * - ``system_template``
     - String
     - The location of the system template file for this system. Typically ``/templates/system.json``.
     - Yes

   * - ``use_webhook_secret``
     - Boolean
     - Set to ``true`` to generate a secret ``webhook_secret`` for validating incoming requests from the external system. This is intended to be used with the ``validation_expression`` in the :ref:`HTTP endpoint source <http_endpoint_source>`.
     - No



Properties in the ``datatypes`` object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10

   * - Property
     - Type
     - Description
     - Required?

   * - ``label``
     - String
     - A human-readable label for the datatype.
     - No
     
   * - ``parameters``
     - Object
     - A dictionary of parameters to be accessed by jinja syntax in the templates.  
     - No
     
   * - ``parent``
     - String
     - The parent datatype name when e.g. using the parameterized input pattern to collect children. To be used as the source dataset datatype name in the ``-all`` pipe.   
     - No
     
   * - ``sync_frequency``
     - String
     - The frequency of the pump for the ``-all`` pipe. Currently supports ``slow`` (only run the pipe at midnight) and ``weekly`` (run at 00:00 on Monday).     
     - No 

   * - ``template``
     - String
     - The location of the template file for this datatype. Typically ``/templates/<template-file>``.    
     - Yes 

   * - ``webhook``
     - Boolean
     - Set to ``true`` if the datatype has webhooks connected.
     - No