.. _connector_manifest:

======================
The connector manifest
======================

The manifest file allows you to configure which datatypes should use which templates. In many cases the data synchronization part are identical for many datatypes in a specific system, i.e. except for the naming of the datatypes the DTL pipe configurations are the same. 

Instead of creating several identical flows, one can simply re-use the same template for different datatypes whenever possible.

Example of a *manifest* file:

::

  {
    "auth": "<value>",
    "auth_variant": "<value>",
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
    "requires_service_api_access": true,
    "system-template": "templates/system.json"
  }

In this case, the ``contact``, ``product`` and ``project`` datatypes from this specific system all had the exact same configuration, which means we could re-use the contact template for all three. The ``country`` datatype however required its own template. 