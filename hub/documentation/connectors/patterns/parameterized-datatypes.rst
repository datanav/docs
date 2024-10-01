Parameterized datatypes
=======================

In some cases you might have to fetch a datatype's full content based on subset of the data. These scenarios can occur be when:

- The system API's do not cover a ``-list`` APi, i.e. an API where we can fetch all entities from a datatype. In these cases we need to fetch all the primary keys from an other API (i.e. a datatype with the primary keys as references) followed by an other API call for each primary.    
- The system's ``-list`` do not yield the full entity but a subset of it. When possible we should do the full import from the ``-list`` API followed by an other API call where we can fetch the full entities based on the ``-list`` API primary keys. 

In both these scenarios the setup looks similar. 

If the system does not provide a ``-list`` API we first need to release the primary keys as new entities in order to mimic a ``-list`` API.

The steps are as follows:

1. A ``-all`` pipe using the collect dataset of the datatype containing the primary keys as a source. This pipe should use :ref:`create-child <dtl_transform-create-child>` with the primary key as both ``_id`` and the key name of the datatypes primary key as value.

2. A ``-all2`` pipe using the ``-all`` dataset as a source. This pipe only releases the children created in the ``-all`` pipe.

3. A ``-collect`` pipe with the ``-all2`` dataset as a source. This pipes should use the newly released entitites from step 2 and potentially apply a filter removing ``"_deleted": true`` entities if required. This pipes should then use the newly released entitites and collect the full version of the entities from a ``-lookup`` API. In the next transform this pipe should contain the :ref:`collect-template <template_transform_collect_rest>` as if it were a normal ``-collect`` pipe.

If the system does have a ``-list`` API but only yield a subset of the entity data step 1 and 2 should be replaced by a ``-all`` collecting the data that can be collected through the ``-list`` API. Step 3 now uses this ``-all`` dataset as a source and follows step 3 above collecting entities from the ``-lookup`` API.   


Below follows a stripped down example on how this could look if the system lacks a ``-list`` API. In this case the datatype lies withing an other datatype:


|start-h3| ``-all`` pipe |end-h3|

::

    {
      "_id": "<system>-<datatype>-all",
      "namespaced_identifiers": false,
      "source": {
        "dataset": "<system>-<sourceDatatype>-collect",
        "type": "dataset"
      },
      "transform": [
        {
          "rules": {
          "create_rows": [
            [
              "add",
              "_id", 
              [
                "string",
                "_S.id"
              ]
            ],
            [
              "add",
              "id",
              "_S.id"
            ],
            [
              "add",
              "$original_id",
              "_R._S._id"
            ]
          ],
          "default": [
            [
              "create-child",
                [
                  "apply",
                  "create_rows",
                  "_S.<property>"
                ]
            ]
          ]
        },
        "type": "dtl"
      }
    ],
    "type": "pipe"
    }
  }

|start-h3| ``-all2`` pipe |end-h3|

::

    {
      "_id": "<system>-<datatype>-all2",
      "namespaced_identifiers": false,
      "source": {
        "dataset": "<system>-<datatype>-all",
        "type": "dataset"
      },
      "transform": [
        {
          "type": "emit_children"
        }
      ],
      "type": "pipe"
    }

|start-h3| ``-collect`` pipe |end-h3|

::

  {
  "_id": "<system>-<datatype>-collect",
  "exclude_completeness": [
      "<system>-<datatype>-share"
  ],
  "namespaced_identifiers": false,
  "source": {
      "dataset": "<system>-<datatype>-all2",
      "type": "dataset"
  },
  "transform": [
      {
      "rules": {
          "default": [
          [
              "filter",
              [
              "neq",
              "_S._deleted",
              true
              ]
          ],
          [
              "copy",
              "*"
          ]
          ]
      },
      "type": "dtl"
      },
      {
      "operation": "<datatype>-lookup",
      "id_expression": "<idProperty>",
      "replace_entity": true,
      "side_effects": false,
      "payload_property": "response",
      "system": "<system>",
      "type": "rest"
      },
      {
      "rules": {
          "default": [
          [
              "merge",
              "_S.response"
          ],
          [
              "add",
              [
              "$last-modified",
              [
                  "datetime-parse",
                  "<FORMATSTRING>",
                  "_S.response.<datetimeProperty>"
              ]
              
              ]
          ]
          ]
      },
      "type": "dtl"
      },
      {
      "properties": {
          "primary_key": "id",
          "operation_lookup_delete": "<datatype>-lookup",
          "share_dataset": "<system>-<datatype>-share"
      },
      "template": "transform-collect-rest",
      "type": "template"
      }
  ],
  "type": "pipe"
  }

.. |start-h3| raw:: html

     <h3>

.. |end-h3| raw:: html

     </h3>