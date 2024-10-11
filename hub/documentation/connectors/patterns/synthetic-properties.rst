Synthetic properties
====================

In some cases we need to introduce custom (synthetic) properties in the ``-collect`` or ``-enrich`` pipes when source system are missing the required metadata. In that case we should prefix the property names with ``sesam_`` in order to keep track of which properties originate from the source system and which do not.

Example:

::

  {
    "_id": "<system>-<datatype>-all",
    "namespaced_identifiers": false,
    "source": {
      "dataset": "<system>-<parent-datatype>-collect",
      "type": "dataset"
    },
    "transform": {
      "rules": {
        "create-versions": [
          [
            "copy",
            "*"
          ],
          [
            "add",
            "_id",
            [
              "string",
              "_S.<child-primary-key>"
            ]
          ],
          [
            "add",
            "sesam_<parent-datatype-primary-key>",
            "_R._S.<parent-datatype-primary-key>"
          ]
        ],
        "default": [
          [
            "create-child",
            [
              "apply",
              "create-versions",
              "_S.<array-of-children>"
            ]
          ]
        ]
      },
      "type": "dtl"
    },
    "type": "pipe"
  }

The example above shows the beginning of a :ref:`parameterized input pattern <parameterized-datatypes>` in which we split out children from their parent. In this case we also add the relationship back to the parent as a synthetic property.

When using synthetic properties and the :ref:`rest template <template_transform_share_rest>` its important to take into account that the synthetic properties do not show when comparing data during :ref:`optimistic locking <optimistic_locking>` in the source system's ``-share`` pipe. These properties will have to be removed from all comparisons since they do not exist in the source system.