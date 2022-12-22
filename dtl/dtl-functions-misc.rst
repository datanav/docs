Misc
====

.. _fail_dtl_function:

``fail!``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   MESSAGE(string{1})
       |
       | A function that makes the pump fail. It can be used to conditionally fail the pump. A string error message can be specified in the first argument.
     - | ``["fail!", "Processing stopped because of invalid input. Please review."]``
       |
       | Causes the pump to fail. The error message is reported in the `pump-failed` event in the pump execution dataset.

.. _hash128_dtl_function:

``hash128``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   ALGORITM("murmur3")
       |   SEED(integer-expression{0|1})
       |   VALUES(value-expression{1})
       |
       | Generates 128 bit integer hashes from bytes and strings. Values of
         other types are ignored. This function can be used to generate
         content hashes. The only supported algoritm is "murmur3"
         (`MurmurHash3 <https://en.wikipedia.org/wiki/MurmurHash>`_).

       | The function takes an optional seed argument. The seed
         can be used to randomize the hash function.

     - | ``["hash128", "murmur3", "abc"]``
       |
       | Returns ``79267961763742113019008347020647561319``.
       |
       | ``["hash128", "murmur3", ["combine", "abc", 123, "def"]]``
       |
       | Returns ``[[79267961763742113019008347020647561319,``
       |           ``114697464648834432121201791580882983835]]``.

.. _is_changed_dtl_function:

``is-changed``
--------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   FUNCTION(function-expression{1}),
       |
       | Returns true if the results of evaluating the FUNCTION expression on the current
         version and the previous version of the source entity are different.
       |
       | If the previous version does not exist then the ``is-changed``
       | function returns ``null``. This means that we don't know if it has changed.
       |
       | If either the current or the previous version of the entity
       | has ``_deleted`` set to ``true`` then the ``is-changed``
       | function returns ``true``.

       .. NOTE::

          If the source is not a ``dataset`` source then the
          ``is-changed`` function will always return ``null``.

       .. NOTE::

          Do not use the ``is-changed`` function to track state
          changes in the sink. This does not work as the pipe may not
          actually have seen the previous version of the source
          entity. This is particularly likely if the dataset source
          reads the latest versions only. Compaction in the source
          dataset may also prevent the pipe from actually seeing all
          versions.

          If you need to do track state changes in the dataset sink
          then do ``hops`` to the sink dataset. In that case you have
          to set ``"batch_size": 1`` on the pipe and
          ``"set_initial_offset": "onload"`` on the dataset sink. The
          former so that the pipe can see its own writes and the
          latter so that the pipe don't have to wait for the sink
          dataset to be populated (something that will never happen as
          the pipe won't be allowed to run).


     - | ``["is-changed", "_.name"]``
       |
       | Returns true if the source entity's ``name`` property changed.
       |
       | ``["is-changed", ["list", "_.height", "_.width"]]``
       |
       | Returns true if the source entity's ``height`` or ``width`` properties changed.
       |
       | ``["is-changed", ["-", "_.end", "_.start"]]``
       |
       | Returns true if the source entity's distance between ``start`` and ``end`` changed.

.. _literal_dtl_function:

``literal``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   MESSAGE(value{1})
       |
       | A function that returns its argument. The argument is not evaluated and is returned as-is. This function is used to avoid side-effects from value expression evaluation.
     - | ``["literal", "_S.foo"]``
       |
       | Returns the string ``_S.foo``, and not the value of the source entity's foo property.

.. _tuples_dtl_function:

``tuples``
----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{>0})
       |
       | Constructs a list of tuples, the product of the values given in the
         arguments. The tuple length is equal to the number
         of function arguments. ``null`` values are ignored.
       |
       | This function is a good choice when you need to do joins on
         composite keys.
     - | ``["tuples"]``
       |
       | Returns ``[]``.
       |
       | ``["tuples", "a", "b", "c"]``
       |
       | Returns ``[["a", "b", "c"]]``.
       |
       | ``["tuples", ["list", 1, 2], 3]``
       |
       | Returns ``[[1, 3], [2, 3]]``.
       |
       | ``["tuples",``
       |   ``["list", 1, 2], ["list", 3, null, 4, 5]]``
       |
       | Returns ``[[1, 3], [1, 4], [1, 5],``
       |         ``[2, 3], [2, 4], [2, 5]]``. The ``null`` value was ignored.
