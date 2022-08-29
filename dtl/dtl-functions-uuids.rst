UUIDs
=====

.. _uuid_dtl_function:

``uuid``
--------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{0|1})
       |
       | Create a new UUID object (version 4 ). It can optionally cast a single string or list of string UUID representations to
         UUID objects. Any input that can't be cast to a UUID object will be ignored.
       |
     - | ``["uuid"]``
       |
       | Returns a new random UUID object on the form "~u9f598f65-eea5-4906-a8f5-82f6d8e69726".
       |
       | ``["uuid", "abc98f65-ddf5-1234-a8f5-82f6d8e69726"]``
       |
       | Returns a new UUID object cast from the input argument: "~uabc98f65-ddf5-1234-a8f5-82f6d8e69726".
       |
       | ``["uuid", ["list", "abc98f65-ddf5-1234-a8f5-82f6d8e601a8", 2, "9f598f65-eea5-4906-a8f5-82f6d8e69726"]]``
       |
       | Returns two UUID objects: ["~uabc98f65-ddf5-1234-a8f5-82f6d8e69726", "~u9f598f65-eea5-4906-a8f5-82f6d8e69726"]
       | Note that the mismatched input argument ``2`` is ignored.

       .. WARNING::

          This function is non-deterministic and will return a
          different value every time it is evaluated. Be aware that if
          the pipe is rewound or reset then it will produce a
          different output. Dependency tracking will also have a
          similar effect as to produce a different value when entities
          are reprocessed.

          *Use this function with care and make sure
          that you are aware of the consequences of reprocessing
          entities.*

.. _is_uuid_dtl_function:

``is-uuid``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a UUID literal or value or if
         it is a list, that the first element in the list is a UUID type value or literal
       |
     - | ``["is-uuid", ["uuid"]]``
       |
       | Returns true.
       |
       | ``["is-uuid", "~u9f598f65-eea5-4906-a8f5-82f6d8e69726"]``
       |
       | Returns true.
       |
       | ``["is-uuid", "some-string"]``
       |
       | Returns false.
       |
       | ``["is-uuid", ["list", ["uuid"], "12345"]]``
       |
       | Returns true.
       |
       | ``["is-uuid", ["list", "12345", ["uuid"]]]]``
       |
       | Returns false.
       |
