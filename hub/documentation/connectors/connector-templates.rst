.. _connector_templates:

=======================
The connector templates
=======================

A template file in a Sesam connector describes the specific DTL configuration files for a specific datatype. 

This includes configurations for both the ``-collect`` pipes following the established :ref:`data synchronization collect patterns <data_synchronization_collect_patterns>` as well as the ``-share`` pipes following the established :ref:`data synchronization share patterns <data_synchronization_share_patterns>`.

It is recommended to make these configurations as generic as possible and let :ref:`the connector manifest <connector_manifest>` manage the datatype specific details.

Example for a *contact* template file:

::

  [
    {
        "_id": "{{@ system @}}-{{@ datatype @}}-all",
        "namespaced_identifiers": false,
        "source": {
          "operation": "{{@ datatype @}}-list",
          "system": "{{@ system @}}",
          "type": "rest"
        },
        "type": "pipe"
    },
    {
        "_id": "{{@ system @}}-{{@ datatype @}}-collect",
        "exclude_completeness": [
          "{{@ system @}}-{{@ datatype @}}-share"
        ],
        "namespaced_identifiers": false,
        "source": {
          "dataset": "{{@ system @}}-{{@ datatype @}}-all",
          "type": "dataset"
        },
        "transform": [
          {
          "properties": {
              "primary_key": "id",
              "share_dataset": "{{@ system @}}-{{@ datatype @}}-share"
          },
          "template": "transform-collect-rest",
          "type": "template"
          },
          {
          "rules": {
              "default": [
                [
                "copy",
                "*"
                ],
                [
                "add", 
                "$last-modified",
                [
                    "datetime-parse",
                    "<FORMATSTRING>",
                    "<last-modified-key>"
                ]
                ]
              ]
          },
          "type": "dtl"
          }
        ],
        "type": "pipe"
    },
    {
        "_id": "{{@ system @}}-{{@ datatype @}}-share",
        "batch_size": 1,
        "namespaced_identifiers": false,
        "sink": {
          "deletion_tracking": false,
          "set_initial_offset": "onload"
        },
        "source": {
          "dataset": "{{@ system @}}-{{@ datatype @}}-transform",
          "type": "dataset"
        },
        "transform": {
          "properties": {
          "operation_delete": "{{@ datatype @}}-delete",
          "operation_insert": "{{@ datatype @}}-insert",
          "operation_lookup": "{{@ datatype @}}-lookup",
          "operation_update": "{{@ datatype @}}-update",
          "primary_key": "id",
          "rest_system": "{{@ system @}}",
          "share_dataset": "{{@ system @}}-{{@ datatype @}}-share"
          },
          "template": "transform-share-rest",
          "type": "template"
        },
        "type": "pipe"
    }
  ]

The example above shows how a template file may look when using the collect template :ref:`collect template <template_transform_collect_rest>` and the :ref:`share template <template_transform_share_rest>`. 

Notice that even though the file is named *contact*, the system name and datatype name are not yet set. These are configurable in the *manifest file*.