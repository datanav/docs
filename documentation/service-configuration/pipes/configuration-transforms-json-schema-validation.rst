
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
     - Yes

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
