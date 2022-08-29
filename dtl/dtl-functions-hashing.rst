Hashing
=======

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
