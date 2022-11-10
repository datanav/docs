Late schema binding
-------------------
Ensure that transformations are done in accordance to the target schema. Bidirectional sync might not support patching, and you need the original object when sharing. When mapping, only use the namespace of the target system or the global namespace. Hops should be done on global properties. Use identifiers from the target system.

.. warning::

    We advice against referencing other namespaces, as this practice is a system to system integration.

When removing namespaces you need to rewrite the _id as it includes colons that will be removed.

Example snippet to fix _id when removing namespaces:

.. code-block::

        ["add", "_id",
          ["replace", ":", "-", "_S._id"]
        ]
        ..
      "remove_namespaces": true
