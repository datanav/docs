Continuation
============

Continuation (also known as incremental loading) involves extracting only the data that has changed (excluding deletions) since the last extraction cycle.

Implementing continuation in a connector
----------------------------------------

See the section on :ref:`continuation support <continuation_support>`.


Example: system config with continuation
----------------------------------------

::

   "<datatype>-list": {
      "properties": {
      "base_url": "<datatype>",
      "primary_key": "<primary_key>",
      "updated_param": "<updated_param>"
      },
      "method": "GET",
      "page_size": 100,
      "url": "https://api.example.com/v1/data",
      "since_property_name": "<since_property_name>",
      "since_property_location": "<since_property_location>",
      "updated_expression": "<update_expression>"
    }


Example: pipe config with continuation
---------------------------------------

::

   {
      "_id": "<system>-<datatype>-all",
      "metadata": {
        "supports_since": true
      },
      "namespaced_identifiers": false,
      "pump": {
          "schedule_interval": 30,
          "rescan_cron_expression": "0 * * * *"
      },
      "source": {
        "operation": "list",
        "initial_since_value": "<initial_since_value>",
        "supports_since": true,
        "system": "<system>",
        "type": "rest",
      },
      "type": "pipe"
    }

A full connector example of continuation support could be found in `Superoffice connector's playground branch  <https://github.com/sesam-io/superoffice-connector/tree/playground>`_ in the `Contact template <https://github.com/sesam-io/superoffice-connector/blob/playground/templates/contact.json>`_.