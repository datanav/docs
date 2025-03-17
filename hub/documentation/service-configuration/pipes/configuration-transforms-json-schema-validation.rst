
.. _json_schema_transform:

JSON Schema validation transform
--------------------------------

A transform that validates entities against a `JSON Schema <http://json-schema.org/>`_ document.
If the document is valid then the field referenced by ``key_valid`` will be set to true, otherwise
false. Any validation error messages will be added to the field
referenced by ``key_errors``.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 3, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``schema``
     - Object
     - The JSON schema to validate entities against.
     -
     - Yes, unless ``schema_url`` is specified

   * - ``schema_url``
     - String
     - URL that points to an externally stored JSON schema. Requires the ``system`` property to also be set. The
       retrieved schema will be stored in the effective config of the pipe under ``schema``.
     -
     - Yes, unless ``schema`` is specified

   * - ``system``
     - String
     - If using ``schema_url``, the ``system`` property needs to point to a valid :ref:`URL system <url_system>`.
     -
     - Yes, if ``schema_url`` is specified

   * - ``key_valid``
     - String
     - The field to store the validation result. This is a boolean value,
       which is true if the entity is valid, otherwise false.
     - ``"valid"``
     -

   * - ``key_errors``
     - String
     - The field to store the validation error messages. The error messages
       is a list of strings. The field is only added if the entity is invalid.
     - ``"errors"``
     -

   * - ``trigger_on``
     - Object
     - A dictionary with two properties: ``"key"`` (optional, defaults to ``"_trigger"``) and ``"value"``. The ``"key"``
       should point to a property in the entity (it supports path notation) and ``"value"`` should contain a value that
       this property should have to be passed into the transform. The ``"value"`` supports wildcards ("*") for substring
       matching. If the ``"key"`` doesn't exist or the ``"value"`` does not match the corresponding value in the entity,
       the entity will be passed through without being transformed. Note that this property is experimental and may
       be changed or removed.
     -
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

   {
       "_id": "men-validated",
       "type": "pipe",
       "source": {
           "type": "dataset",
           "dataset": "men"
       },
       "transform": {
           "type": "json_schema",
           "trigger_on": {
                "key":"_trigger",
                "value": "some-value*"
            },
           "schema": {
               "type" : "object",
               "properties" : {
                   "name" : {"type" : "string"},
                   "born" : {"type" : "string"}
               },
               "required": ["name", "born"]
           }
       }
   }

If the following entities where pushed through the pipe:

::

   [
    {"_id": "3",
     "name": "Jim"},
    {"_id": "5",
     "name": "Bob",
     "born": "1972-03-12"}
   ]

then these would come out:

::

   [
    {"_id": "3",
     "valid": false,
     "errors": [
       "'born' is a required property"
     ],
     "name": "Jim"},
    {"_id": "5",
     "valid": true,
     "name": "Bob",
     "born": "1972-03-12"}
   ]
