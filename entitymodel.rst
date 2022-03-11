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
string, integer, decimal, boolean, namespaced identifier, URI, bytes
and datetime. Over the wire both a binary and JSON representation is
used.

Reserved fields
---------------

Entity fields starting with ``_`` are reserved. Any such fields,
except ``_id`` and ``_deleted``, will be ignored when writing an entity
to a dataset. Note that the fields are only reserved at the root
level, so child entities can have them.


.. list-table::
   :header-rows: 1
   :widths: 30, 50, 10

   * - Field
     - Description
     - Required

       .. _id_field:
   * - ``_id``
     - This is the primary key of the entity. The value is always a
       string.
     - Yes

   * - ``_deleted``
     - If ``true``, then the entity is deleted. All other values are
       interpreted as if the entity is not deleted.
     -

   * - ``_updated``
     - The sequence of the entity. The value must be either a string
       or an integer value. The value is used to tell the order of the
       entities. The value is meant to be opaque, and should not be
       parsed or interpreted by other parties than the source
       that produced it. The ``_updated`` value can be passed through
       to the ``since`` request parameter in HTTP endpoints.
     -

   * - ``_hash``
     - A string containing the hash of the entity's content. This value
       is used to decide when an entity has changed. Of the reserved
       fields, only ``_id`` and ``_deleted`` contribute to the hash value.

       *This field is generated automatically when writing an entity to a dataset.*
     -

   * - ``_previous``
     - A pointer back to the previous version of this entity. The
       value refers to the ``_updated`` field of the previous version
       of the entity. If the field is missing or the value is
       ``null``, then there exists no previous version. Note that the
       previous version may not actually exist anymore as dataset compaction
       may have reclaimed it.

       *This field is generated automatically when writing an entity to a dataset.*
     -

   * - ``_ts``
     - This the real-world timestamp for when the entity was added to
       the dataset. The value is an integer representing the number
       of microseconds since epoch (January 1st 1970 UTC). This field is
       used only for informal purposes.

       *This field is generated automatically when writing an entity to a dataset.*
     -

   * - ``_tracked``
     - If ``true`` then the entity was added to the dataset by
       `dependency tracking <concepts.html#dependency-tracking>`_.

       *This field is generated automatically by the dependency tracking.*
     -

Special fields
---------------

Entity fields starting with ``$`` are semi-reserved. They have special
meaning and will sometimes be produced and consumed by built-in
components. These fields are normal fields that will be hashed and
stored as part of the entity.


.. list-table::
   :header-rows: 1
   :widths: 30, 50, 10

   * - Field
     - Description
     - Required

       .. _dollar_ids_field:
   * - ``$ids``
     - This field can be used to hold all the identities of an entity. An entity
       may have multiple identities, i.e. in addition to the one in ``_id``. The value type
       is always :ref:`NI <ni_data_type>`. The :ref:`merge <merge_source>` source
       will collect all the merged identities in this field.
     -

       .. _dollar_children:
   * - ``$children``
     - The :ref:`create-child <dtl_transform-create-child>` DTL transform function
       will add the created child entity as a value in the ``$children`` property of the
       target entity. The :ref:`emit_children <emit_children_transform>` transform can
       then later be used to expand the ``$children`` entities into standalone entities.
     -

       .. _dollar_replaced:
   * - ``$replaced``
     - The :ref:`merge <merge_source>` source will set the ``$replaced`` field
       to ``true`` if the output entity is being replaced with a new entity that has a
       different entity id. This typically happens when the entity is being merged
       with another entity where the id of the other entity takes precedence over
       the current one.
     -

.. _entity_data_types:

Standard types
--------------

Entities are mapped to and from JSON objects, so they support the same
data types as JSON does. Because JSON only supports a limited number of
data types there is also limited support for `Transit
<https://github.com/cognitect/transit-format>`_ data types.

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Type
     - Description
     - Example

   * - Dict
     - Like a JSON object where keys are always strings. This type is not *orderable*.
     - ``{"a": 123}``

   * - Entity
     - Like a Dict, but with an ``_id`` property. The ``_id`` property must
       be a string.
     - ``{"_id", "person1", "a": 123}``

   * - List
     - A list of values. Values can be of any type.  This type is not *orderable*.
     - ``["abc", 123, [4, 5], {"x": "y"}]``

   * - String
     - A string value. Maximum length is 4294967296 bytes.
     - ``"abc"``

   * - Integer
     - An integer value. The range of this data type is unlimited, i.e. it can store
       any positive or negative integer value.
     - ``123``

   * - Decimal
     - A decimal number. This data type has arbitrary precision. Use it instead of
       ``Float`` when/if keeping precision is important to your application.
     - ``123.456``

   * - Float
     - A `double-precision floating point number <https://en.wikipedia.org/wiki/Double-precision_floating-point_format>`_.
       The valid range is the IEEE 754 binary 64 format,
       because we're internally storing the value as a double-precision
       floating-point number. Note that you may loose precision when using
       this data type.
     - ``123.456``

   * - Boolean
     - A boolean value. Either ``true`` or ``false``.
     - ``true``

   * - Null
     - A null value. Typically used to represent a missing value. This type is not *orderable*.
     - ``null``

.. _extension-types:

Extension types
---------------

`Transit <https://github.com/cognitect/transit-format>`_ encoded
values are represented as strings in JSON. The value is prefixed by
"~" and tag character that indicates the type of the value. The
extension types below are currently the only ones supported. Transit
types that are not recognized will be treated as string values.

Note that there's currently no support for escaping string literals
that start with a "~" character.

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Type
     - Description
     - Example

       .. _ni_data_type:
   * - NI
     - Namespaced Identifier (NI)
     - ``"~:mynamespace:123"``

   * - URI
     - Uniform Resource Identifier (URI)
     - ``"~rhttp://www.sesam.io/"``

   * - Date
     - A date value. The valid range is from ``"~t0001-01-01"`` to
       ``"~t9999-12-31"``.
     - ``"~t2015-12-31"``

   * - Datetime
     - Date and time with up to nanoseconds precision. The valid range is
       from ``"~t0001-01-01T00:00:00Z"`` to
       ``"~t9999-12-31T23:59:59.123456789Z"``. The date and time parts
       of the string are mandatory. The fraction of a second is optional.
       The value must always be in UTC, so the ``Z`` at the end is mandatory.
     - ``"~t2015-01-02T03:04:05.123456789Z"``, ``"~t1973-01-22T23:11:54Z"``

   * - Bytes
     - A base64 encoded binary value.
     - ``"~bAAECAwQF"``

   * - UUID
     - A Universally unique identifier formatted as hexadecimal text.
     - ``"~u531a379e-31bb-4ce1-8690-158dceb64be6"``

   * - Decimal
     - A decimal number with arbitrary precision.
     - ``"~f12345678901234567890.1234567890"``

.. _mixed_type_ordering:

Mixed type ordering
-------------------

In situations where lists of values of multiple types have to be
ordered then the following ordering is used:

* Null

* Boolean

* Integer, Float, Decimal

* Date, Datetime

* UUID

* Namespaced identifier (NI)

* URI

* String

* Dict

* Tuple

* Bytes

Types under the same bullet point are compatible and internally
orderable. Values of incompatible types are sorted not by value but by
the rank of their type (see the list above).

Example: ``["sorted", ["list", 1.5, "b", 1, "a", 2]]`` returns ``[1, 1.5, 2, "a", "b"]``
because the strings and integers are not compatible types. The
integers are ordered before the strings. Decimals and integers are compatible,
so they are sorted together.

Note that values of the Dict type are ordered by sorting their keys
and then comparing each key+value pair.
