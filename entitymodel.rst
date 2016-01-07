=================
Entity Data Model
=================

Sesam uses an entity data model as the core representation of
data. Each entity is a dictionary of key-value pairs. Each key is a
string and the value can be either a literal value, a list or another
dictionary.

A Sesam entity has a few special keys that should not be messed
with. The following data prototype explains these special properties.

::

  {
  	"_id": "the identity of the entity",
  	"_updated": "a token indicating when this was modified",
  	"_deleted": "indicating if the entity should be treated as deleted",
        "_hash": "a hash string of the entity's content",
        "_previous": "the _updated token of the previous version",
        "_ts": "timestamp for when entity was registered in source"
  }

The entity data model supports a wide range of data types including,
string, integer, decimal, boolean, URI, bytes and datetime. Over the
wire both a binary and JSON representation is used.

Reserved fields
---------------

Entity fields starting with ``_`` are reserved. Any such fields will
be ignored when writing an entity to a dataset. Note that the fields
are only reserved at the root level, so child entities can have them.


.. list-table::
   :header-rows: 1
   :widths: 30, 50, 10

   * - Field
     - Description
     - Required

   * - ``_id``
     - This is the primary key of the entity. The value is always a
       string.
     - Yes

   * - ``_deleted``
     - If ``true`` then the entity is deleted. All other values are
       interpreted as if the entity is not deleted.
     -

   * - ``_updated``
     - The sequence of the entity. The value must be either a string
       or an integer value. The value is used to tell the order of the
       entities. The value is meant to be opaque, and should not be
       parsed or interpreted by other parties than the data source
       that produced it. The ``_updated`` value can be passed through
       to the ``since`` request parameter in HTTP endpoints.
     -

   * - ``_hash``
     - A string containing the hash of the entity's content. This value
       is used to decide when an entity has changed.

       *This field is used by entities stored in datasets.*
     -

   * - ``_previous``
     - A pointer back to the previous version of this entity. The
       value refers to the ``_updated`` field of the previous
       version. If the field is missing or the value is
       ``null``, then there exists no previous version.

       *This field is used by entities stored in datasets.*
     -

   * - ``_ts``
     - This the real-world timestamp for when the entity was added to
       the datasource. The value is an integer representing the number
       of seconds since epoch (January 1st 1970 UTC). This field is
       used only for informal purposes.

       *This field is used by entities stored in datasets.*
     -


Standard datatypes
------------------

Entities are mapped to and from JSON objects, so they support the same
datatypes as JSON does. Because JSON only supports a limited number of
datatypes there is also limited support for `Transit
<https://github.com/cognitect/transit-format>`_ datatypes.

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Type
     - Description
     - Example

   * - Entity (aka object)
     - Like a JSON object where keys are always strings.
     - ``{"a": 123}``

   * - List
     - A list of values. Values can be of any type.
     - ``["abc", 123, [4, 5], {"x": "y"}]``

   * - String
     - A string value. Maximum size is 4294967296 bytes.
     - ``"abc"``

   * - Integer
     - An integer value. The valid range is between ``-9223372036854775808``
       and ``9223372036854775807``.
     - ``123``

   * - Decimal
     - A decimal number. The valid range is the IEEE 754 binary 64 format,
       because we're currently storing the value as a double-precision
       floating-point number. Note that you may loose precision when using
       this datatype.
     - ``123.456``

   * - Boolean
     - A boolean value. Either ``true`` or ``false``.
     - ``true``

   * - Null
     - A null value. Typically used to represent a missing value.
     - ``null``

Extension types (Transit encoded)
----------------------------------

`Transit <https://github.com/cognitect/transit-format>`_ encoded
values are represented as strings in JSON. The value is prefixed by
"~" and tag character that indicates the type of the value. The
extension types below are currently the only ones supported. Transit
types that are not recognized will be treated as string values.

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Type
     - Description
     - Example

   * - URI
     - Uniform Resource Identifier (URI).
     - ``"~rhttp://www.sesam.io/"``

   * - Datetime
     - Date and time with up to nanoseconds precision. The valid range is
       from ``"~t1677-09-21T00:12:43.145224192Z"`` to
       ``"~t2262-04-11T23:47:16.854775807Z"``. The date and time parts
       of the string are mandatory. The fraction of a second is optional.
       The value must always be in UTC, so the ``Z`` at the end is mandatory.
     - ``"~t2015-01-02T03:04:05.123456789Z"``, ``"~t1973-01-22T23:11:54Z"``

   * - Bytes
     - A base64 encoded binary value.
     - ``"~bAAECAwQF"``
