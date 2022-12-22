.. _dtl-transforms:

Transform Functions
===================

A transform function is a function that has side-effects, typically
modifying the target entity, and has no return value.

.. _`dtl_transform-add`:

``add``
-------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   PROPERTY(string{1})
       |   VALUES(value-expression{1})
       |
       | Adds the PROPERTY field(s) to the target entity with the values returned
         by evaluating the VALUES expression.

       .. NOTE::

         This transform function is :ref:`namespaced identifiers <namespaces-feature>` aware.

         If namespaced identifiers are enabled,
         then the property will be prefixed by the current
         namespace. If the property is ``_id`` then the string values
         will be prefixed by the identity namespace. All other
         properties will have their name prefixed by the property
         namespace.

     - | ``["add", "age", 26]``
       |
       | Adds the ``age`` property with the value 26 to the target entity.
       |
       | ``["add", "upper_name", ["upper", "_S.name"]]``
       |
       | Adds the ``upper_name`` property to the target entity. The value is
         the uppercased version of the source entity's ``name`` property.
       |
       | ``["add",``
       |   ``["concat", "x-", "_S.key"], "_S.value"]``
       |
       | Adds the property returned by the ``concat`` function and assigns it the
         value returned by ``_S.value``.
       |
       | **With namespaced identifiers enabled:**
       |
       | ``{``
       |   ``"namespaced_identifiers": true,``
       |   ``"namespaces": {``
       |     ``"identity": "foo",``
       |     ``"property": "bar"``
       |   ``}``
       | ``}``
       |
       | *Source entity:* ``{}``
       |
       | ``["add", "age", 26]``
       |
       | Result: ``{"bar:age": 26}``. Adds the ``bar:age`` property with the value
         26 to the target entity.
       |
       | ``["add", "person:age", 26]``
       |
       | Result: ``{"person:age": 26}``. Adds the ``person:age`` property with the
         value 26 to the target entity.
       |
       | ``["add", "::age", 26]``
       |
       | Result: ``{"age": 26}``. Adds the ``age`` property with the value 26 to
         the target entity. Note
         that if the PROPERTY arguments starts with ``::`` it will be interpreted
         to mean add what ever is after the double colons. See
         :ref:`NI escape syntax <ni_escape_syntax>` for more details.
       |
       | ``["add", ":age", 26]``
       |
       | Result: ``{"bar:age": 26}``. Adds the ``bar:age`` property with the value
         26 to the target entity.
         Note that this example uses the :ref:`NI escape syntax <ni_escape_syntax>`
         to reference the current namespace.

.. _dtl_transform-case:

``case``
--------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   (VALUE(value-expression{1},
       |    THEN(transforms{1}))+,
       |   ELSE(transforms{0\|1})
       |
       | Evaluates the first THEN for which VALUE is true. If there is no
         match, then ELSE is evaluated. If there is no ELSE, then it is a no-op.

       .. NOTE::

          If you need to specify multiple transforms then wrap them in a list.

     - | ``["case",``
       |   ``["gte", "_S.age", 18], ["add", "group", "adult"],``
       |   ``["gte", "_S.age", 13], ["add", "group", "teenager"],``
       |   ``["gte", "_S.age", 2], ["add", "group", "toddler"],``
       |   ``["lt", "_S.age", 2], ["add", "group", "baby"],``
       |   ``["add", "group", "unknown"]]``
       |
       | Adds ``{"group": "adult"}`` if the value of ``_S.age`` is greater than or equal to ``18``,
       | or ``{"group": "teenager"}`` if the value of ``_S.age`` is greater than or equal to ``13``,
       | or ``{"group": "toddler"}`` if the value of ``_S.age`` is less than ``2``,
       | otherwise ``{"group": "unknown"}``.

.. _dtl_transform-case-eq:

``case-eq``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUE(value-expression{1}),
       |   (VALUE_N(value-expression{1},
       |    THEN(transforms{1}))+,
       |   ELSE(transforms{0\|1})
       |
       | Evaluates the first THEN for which VALUE is equal to VALUE_N. If there is no
         match, then ELSE is evaluated. If there is no ELSE, then it is a no-op.

       .. NOTE::

          If you need to specify multiple transforms then wrap them in a list.

     - | ``["case-eq", "_S.country",``
       |   ``"NO", ["add", "country", "Norway"],``
       |   ``"SE", ["add", "country", "Sweden"],``
       |   ``["add", "country", "Other"]]``
       |
       | Given then value of ``_S.country``, adds ``{"country": "Norway"}`` if the value is ``"NO"``
         and ``{"country": "Sweden"}`` if the value is ``"SE"``, otherwise ``{"country": "Other"}`` is added.
       |
       | ``["case-eq", "_S.dialing_code",``
       |   ``45, ["add", "country_code", "DK"],``
       |   ``46, ["add", "country_code", "SE"],``
       |   ``47, ["add", "country_code", "NO"]]``
       |
       | Given the value of ``_S.dialing_code``, adds ``{"country": "DK"}`` if the value is
         ``45`` and ``{"country": "SE"}`` if the value  is ``46`` and ``{"country": "NO"}`` if the value is ``47``,
         otherwise it is a no-op.

.. _`dtl_transform-comment`:

``comment``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   COMMENTS(value-expression{>=0})
       |
       | A transform that does nothing except hold comments. Useful for
         documenting the transforms, or just disabling transforms inside. Any
         expressions inside the comment will not be evaluated.
     - | ``["comment", "This is a comment"]``
       |
       | A single line comment.
       |
       | ``["comment",``
       |      ``"First line",``
       |      ``"Second line",``
       |      ``"Third line"]``
       |
       | A comment that spans multiple lines.

.. _`dtl_transform-copy`:

``copy``
--------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   INCLUDE_PROPERTIES(wildcard-string-list{1})
       |   EXCLUDE_PROPERTIES(wildcard-string-list{1})
       |
       | Copies properties in INCLUDE_PROPERTIES from the source entity to the
         target entity. Any properties matching any of the EXCLUDE_PROPERTIES
         patterns are not included. INCLUDE_PROPERTIES and EXCLUDE_PROPERTIES
         can be a single string or a list of strings, where the strings are
         patterns. ``*`` and ``?`` are valid pattern characters.

       .. NOTE::

         This transform function is :ref:`namespaced identifiers <namespaces-feature>` aware.

         The pattern in PROPERTY is namespace aware, so the last colon in the pattern
         is considered to be the separator between the namespace and the identifier.
     - | ``["copy", "age"]``
       |
       | Copies the ``age`` property from the source entity to the target entity.
       |
       | ``["copy", "a*", "ab*"]``
       |
       | Copies all properties starting with ``a`` from the source entity to the
         target entity, but not those starting with ``ab``.
       |
       | ``["copy",``
       |   ``["list", "a*", "b*"],``
       |   ``["list", "ab*", "ba*"]]``
       |
       | Copies all properties starting with ``a`` or ``b`` from the source entity
         to the target entity, but not those starting with ``ab`` or ``ba``.
       |
       | **With namespaced identifiers enabled:**
       |
       | ``{``
       |   ``"namespaced_identifiers": true,``
       |   ``"namespaces": {``
       |     ``"identity": "foo",``
       |     ``"property": "bar"``
       |   ``}``
       | ``}``
       |
       | *Source entity:*
       | ``{"age": 36,``
       |  ``"x:age": 36}``
       |  ``"xyz:age": 36}``
       |
       | ``["copy", "age"]``
       |
       | Result:
       | ``{ "age": 36.``
       |   ``"x:age": 36,``.
       |   ``"xyz:age": 36}``.
       | Copies the ``age`` property in all namespaces to the target entity.
       |
       | ``["copy", "x*:*e", "*y*:*e"]``
       |
       | Result: ``{ "x:age": 36 }``.
       | Copies the properties ending with ``e`` in all namespaces starting with ``x``,
         except those in a namespace that contains the character ``y``,
         to the target entity.

.. _dtl_transform-create:

``create``
----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | For each entity in VALUES emit them as new entities to the DTLs output
         pipeline.

       | Note that these new entities *must* have an ``_id`` string property.
         Values that are not entities will be ignored.

     - | ``["create", "_S.orders"]``
       |
       | Emit the orders in the source entity's ``orders`` field as new entities.
       |
       | ``["create", ["apply", "order", "_S.orders"]]``
       |
       | Emit the orders in the source entity's ``orders`` field as new entities,
         but apply the ``order`` transform to them first.

.. _dtl_transform-create-child:

``create-child``
----------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | For each entity in VALUES add it to the ``$children`` property on the
         target entity. Note that the entities *must* have an ``_id`` string property.
         Values that are not entities will be ignored.
       |
       | This function is almost equivalent to:
       |
       | ``["add", "$children",``
       |   ``["union", "_T.$children", ...]]``
       |
       | Note that the ``$children`` property is special. This function should
         really only be used when writing into a ``dataset`` sink.
       |
       | If an entity with a ``$children`` property is written to the ``dataset``
         sink then it will compare it against the value of the ``$children``
         property in the previous version of the entity. It will detect deleted
         entities and add them to the property before storing the entity.
       |
       | Note also that there is an :ref:`emit_children <emit_children_transform>`
         transform that can be used to expand the ``$children`` entities into
         standalone entities.

     - | ``["create-child", "_S.orders"]``
       |
       | Adds the orders in the source entity's ``orders`` field to the "$children" property
         on the target entity.

.. _`dtl_transform-default`:

``default``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   PROPERTY(string{1})
       |   VALUES(value-expression{1})
       |
       | Adds the PROPERTY field(s) to the target entity with the values returned
         by evaluating the VALUES expression, unless the property already exists.
         ``default`` behaves exactly like ``add``, except that it does not add
         the property if the property already exists on the target entity. If
         the property exists it does nothing.

       .. NOTE::

         This transform function is :ref:`namespaced identifiers <namespaces-feature>` aware.

         If namespaced identifiers are enabled,
         then the property will be prefixed by the current
         namespace. If the property is ``_id`` then the string values
         will be prefixed by the identity namespace. All other
         properties will have their name prefixed by the property
         namespace.
     - | ``["default", "age", 26]``
       |
       | Adds the ``age`` property with the value 26 to the target entity, if
         the property does not exists.
       |
       | ``["default", "upper_name", ["upper", "_S.name"]]``
       |
       | Adds the ``upper_name`` property to the target entity, if
         the property does not exists.. The value is
         the uppercased version of the source entity's ``name`` property.
       |
       | ``["default",``
       |   ``["concat", "x-", "_S.key"], "_S.value"]``
       |
       | Adds the property returned by the ``concat`` function and assigns it the
         value returned by ``_S.value``, if the property does not exists..
       |
       | **With namespaced identifiers enabled:**
       |
       | ``{``
       |   ``"namespaced_identifiers": true,``
       |   ``"namespaces": {``
       |     ``"identity": "foo",``
       |     ``"property": "bar"``
       |   ``}``
       | ``}``
       |
       | *Source entity:* ``{}``
       |
       | ``["default", "age", 26]``
       |
       | Result: ``{"bar:age": 26}``. If the target entity does not already have
         the ``bar:age`` property, then
         the ``bar:age`` property with the value 26 is added to the target entity.
       |
       | ``["default", "person:age", 26]``
       |
       | Result: ``{"person:age": 26}``. If the target entity does not already have
         the ``person:age`` property, then
         the ``person:age`` property with the value 26 is added to the target entity.
       |
       | ``["default", "::age", 26]``
       |
       | Result: ``{"age": 26}``. If the target entity does not already have the
         ``age`` property, then
       | the ``age`` property with the value 26 is added to the target entity. Note
         that if the PROPERTY arguments starts with ``::`` it will be interpreted
         to mean add what ever is after the double colons. See
         :ref:`NI escape syntax <ni_escape_syntax>` for more details.
       |
       | ``["default", ":age", 26]``
       |
       | Result: ``{"bar:age": 26}``. If the target entity does not already have the
         ``bar:age`` property, then
         the ``bar:age`` property with the value 26 is added to the target entity.
         Note that this example uses the :ref:`NI escape syntax <ni_escape_syntax>`
         to reference the current namespace.

.. _`dtl_transform-discard`:

``discard``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   UNLESS_CONDITION(boolean-expression{0|1})
       |
       | This transform is almost identical to ``filter``, but will drop the target
         entity on the floor. Use it with care as the discarded entity will not be
         deleted in the sink.
       |
       | If the evaluation of the UNLESS_CONDITION expression returns false, then stop
         applying transformations. In this case *no* target entity is emitted
         for the source entity. Note that any entities already emitted by
         ``create`` will not be stopped. If you want then make sure that you don't
         create them before the ``discard``.
       |
       | If the UNLESS_CONDITION argument is not given then the target entity will be discarded.

       .. WARNING::

          Only use this transform when you know that you've never sent an entity
          with the same ``_id`` to the sink before. The reason is that that the entity will
          then not be deleted in the sink. If you want it to be deleted then use the
          ``filter`` transform instead.

     - | ``["discard", ["gt", "_S.age", 42]]``
       |
       | Discard the target entity unless the source entity's age is greater than 42.
       |
       | ``["discard", ["eq", "_S.type", "person"]]``
       |
       | Discard the target entity unless the source entity's type is ``person``.
       |
       | ``["discard"]``
       |
       | Discard the target entity unconditionally.
       |

.. _`dtl_transform-filter`:

``filter``
----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   UNLESS_CONDITION(boolean-expression{0|1})
       |
       | If the evaluation of the UNLESS_CONDITION expression returns false, then stop
         applying transformations. In this case *no* target entity is emitted
         for the source entity. Note that any entities already emitted by
         ``create`` will not be stopped. If you want then make sure that you don't
         create them before the ``filter``.
       |
       | If the UNLESS_CONDITION argument is not given then the filter evaluates to
         false.

       .. NOTE::

          If used with a ``dataset`` sink then the ``filter`` function
          will set the ``_filtered`` property to ``true`` and emit the
          entity.

          The reason for this is so that the ``dataset`` sink can
          detect deleted entities even on incremental syncs, not just
          on full syncs. Entities with the ``_filtered`` property set to
          ``true`` will thus be deleted from the dataset if the entity
          already exists and it is not already deleted.

          The rationale for this behaviour is so that entities that
          have previous versions get deleted in the resulting dataset
          when they no longer pass the filter.

          If you have more than one transform then you may want to be
          careful about how you process ``_filtered`` entities in
          subsequent transforms.

          If you would like to control how deletions happen, then you
          should not use the ``filter`` function, but instead set the
          ``_deleted`` property.

     - | ``["filter", ["gt", "_S.age", 42]]``
       |
       | Continue processing only if the source entity's age is greater than 42.
       |
       | ``["filter", ["eq", "_S.type", "person"]]``
       |
       | Continue processing only if the source entity's type is ``person``.
       |
       | ``["filter"]``
       |
       | Stop processing.
       |

.. _`dtl_transform-if`:

``if``
------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   CONDITION(boolean-expression{1}),
       |   THEN(transforms{1}),
       |   ELSE(transforms{0|1})
       |
       | If CONDITION evaluates to *true* then apply the transforms in THEN,
       | otherwise apply the transforms in ELSE.

       | Note that the THEN and ELSE arguments can either be a single transform
         function or a list of transform functions. The list can be empty.

       .. NOTE::

          If you need to specify multiple transforms then wrap them in a list.

          | ``["if", ["gt", "_S.age", 18],``
          |      ``[["add", "type", "adult"],``
          |       ``["add", "is_adult", true]],``
          |      ``["add", "type", "child"]]``

     - | ``["if", ["eq", "_S.type", "person"], [``
       |      ``["add", "type", "person"],``
       |      ``["copy", ["list", "name", "age"]]]]``
       |
       | If the source entity's ``type`` field is equal ``person`` then apply
         the ``add`` and ``copy`` transforms. There is no else clause given,
         which is effectively the same as an empty list with no transforms.
       |
       | ``["if", ["gt", "_S.age", 18],``
       |      ``["add", "type", "adult"],``
       |      ``["add", "type", "child"]]``
       |
       | If the source entity's ``age`` is greater than 18 then add ``type``
         field with value ``adult``, if not add ``child``.

.. _`dtl_transform-make-ni`:

``make-ni``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   NAMESPACE(string{1})
       |   FROM_PROPERTY(string{1})
       |   TO_PROPERTY(string{0|1})
       |
       | Adds the FROM_PROPERTY field to the target entity's TO_PROPERTY with
         string values made into namespaced identifiers in the NAMESPACE namespace.
         If none of the values can be made into namespaced identifiers then nothing is added. If
         TO_PROPERTY is omitted then it defaults to FROM_PROPERTY + ``-ni``.

       .. NOTE::

         This transform function is :ref:`namespaced identifiers <namespaces-feature>` aware.

         If namespaced identifiers are enabled,
         then the property will be prefixed by the current
         namespace. If the property is ``_id`` then the string values
         will be prefixed by the identity namespace. All other
         properties will have their name prefixed by the property
         namespace.
     - | ``["make-ni", "soccer", "referee", "ref"]``
       |
       | If the source entity has ``{"referee": "john.doe"}`` then adds the ``ref``
         property with the value ``~:soccer:john.doe`` to the target entity.
       |
       | ``["make-ni", "hockey", "players"]``
       |
       | Adds the ``players-ni`` property to the target entity, if
         any namespaced identifiers were created.
       |
       | **With namespaced identifiers enabled:**
       |
       | ``{``
       |   ``"namespaced_identifiers": true,``
       |   ``"namespaces": {``
       |     ``"identity": "foo",``
       |     ``"property": "bar"``
       |   ``}``
       | ``}``
       |
       | *Source entity:*
       | ``{"referee": "john.doe",``
       |  ``"x:referee": "john.c.doe"}``
       |
       | ``["make-ni", "soccer", "referee"]``
       |
       | Result:
       | ``{ "referee-ni": "~:soccer:john.doe"``
       |   ``"x:referee-ni": "~:soccer:john.c.doe" }``.
       | Copies all ``referee`` properties in all namespaces from the source entity
         to the target entity. Note that the target properties are suffixed by ``-ni``.
         The values are converted into
         NIs by adding the ``soccer`` namespace. Any non-string values are ignored.
       |
       | ``["make-ni", "soccer", "referee", "ref"]``
       |
       | Result:
       | ``{ "ref": "~:soccer:john.doe"``
       |   ``"x:ref": "~:soccer:john.c.doe" }``.
       | Copies all ``referee`` properties in all namespaces from the source entity
         to the target entity. Note that the target properties are *not* suffixed by
         ``-ni``. The properties keep their namespaces, but the identifier
         part is replaced by ``ref``. The values are converted into
         NIs by adding the ``soccer`` namespace. Any non-string values are ignored.
       |
       | ``["make-ni", "soccer", "x:referee"]``
       |
       | Result:
       | ``{ "x:referee-ni": "~:soccer:john.c.doe" }``.
       | Copies the ``x:referee`` property as ``x:referee-ni`` from the source entity
         to the target entity. The values are converted into
         NIs by adding the ``soccer`` namespace. Any non-string values are ignored.
       |
       | ``["make-ni", "soccer", "x:referee", "ref"]``
       |
       | Result:
       | ``{ "x:ref": "~:soccer:john.c.doe" }``.
       | Copies the ``x:referee`` property as ``x:ref`` from the source entity
         to the target entity. The values are converted into
         NIs by adding the ``soccer`` namespace. Any non-string values are ignored.
       |
       | ``["make-ni", "soccer", "x:referee", "y:ref"]``
       |
       | Result:
       | ``{ "y:ref": "~:soccer:john.c.doe" }``.
       | Copies the ``x:referee`` property as ``y:ref`` from the source entity
         to the target entity. The values are converted into
         NIs by adding the ``soccer`` namespace. Any non-string values are ignored.

.. _`dtl_transform-merge`:

``merge``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | For each entity in VALUES copy all the properties of the value onto the
         target entity. If the property already exists, it will be overwritten. This means that
         properties from later value entities win over earlier  ones.
     - | ``["merge", "_S.orders"]``
       |
       | Copies the properties of the entities in ``_S.orders`` to the target.
       |
       | ``["merge", ["list", {"a": 1}, {"a": 2, "b": 3}]]``
       |
       | Add the properties ``a=2`` and ``b=3`` to the target entity. Note that
         ``a=1`` is not added because it gets overwritten with ``a=2`` later.

.. _`dtl_transform-merge-union`:

``merge-union``
---------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | For each entity in VALUES copy all the properties of the value onto the
         target entity. If the property already exists on the target entity, add
         the new values as a list of values.
     - | ``["merge-union", "_S.orders"]``
       |
       | Copies the properties of the entities in ``_S.orders`` to the target.
         Merge the property values if the property already exists.
       |
       | ``["merge-union",``
       |   ``["list", {"a": 1}, {"a": 2, "b": 3}]]``
       |
       | Add the properties ``a=[1, 2]`` and ``b=3`` to the target entity.

.. _`dtl_transform-remove`:

``remove``
----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   PROPERTY(wildcard-string{1})
       |
       | Removes the PROPERTY field from the target entity. The PROPERTY can
         be pattern with ``*`` and ``?`` characters in it. The pattern must match
         the full property names.

       .. NOTE::

         This transform function is :ref:`namespaced identifiers <namespaces-feature>` aware.

         The pattern in PROPERTY is namespace aware, so the last colon in the pattern
         is considered to be the separator between the namespace and the identifier.
     - | ``["remove", "age"]``
       |
       | Removes the ``age`` property from the target entity.
       |
       | ``["remove", "temp_*"]``
       |
       | Removes all properties matching the ``temp_*`` wildcard pattern from
         the target entity.
       |
       | **With namespaced identifiers enabled:**
       |
       | ``{``
       |   ``"namespaced_identifiers": true,``
       |   ``"namespaces": {``
       |     ``"identity": "foo",``
       |     ``"property": "bar"``
       |   ``}``
       | ``}``
       |
       | *Target entity:*
       | ``{"age": 36,``
       |  ``"x:age": 36}``
       |  ``"y:age": 36}``
       |
       | ``["remove", "age"]``
       |
       | Result: ``{}``.
       | Removes the ``age`` property in all namespaces from the target entity.
       |
       | ``["remove", "x*:age"]``
       |
       | Result: ``{"age": 36, "y:age": 36}``.
       | Removes the ``age`` property in all namespaces starting with ``x``
         from the target entity.
       |
       | ``["remove", "x:age"]``
       |
       | Result: ``{"age": 36, "y:age": 36}``.
       | Removes the ``x:age`` property from the target entity.

.. _`dtl_transform-rename`:

``rename``
----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   PROPERTY1(string{1})
       |   PROPERTY2(string{1})
       |
       | Copies the PROPERTY1 field from the source entity to the PROPERTY2 field
         on the target entity. This is effectively a way to copy and rename
         properties from the source entity to the target entity. No wildcard
         patterns are supported.

       .. NOTE::

         This transform function is :ref:`namespaced identifiers <namespaces-feature>` aware.

         If namespaced identifiers are enabled,
         then the renaming makes sure that any namespaces on the target entity either
         keep their original namespaces or all values are collected into a single
         property on the target.
     - | ``["rename", "age", "current_age"]``
       |
       | Copies the ``age`` field from the source entity and adds it as
         ``current_age`` on the target entity.
       |
       | ``["rename",``
       |   ``["concat", "in-", "_S.key"],``
       |   ``["concat", "out-", "_S.key"]]``
       |
       | Copies the value of the property returned by the first ``concat`` function
         and assigns it to the property returned by the second ``concat`` function.
       |
       | **With namespaced identifiers enabled:**
       |
       | ``{``
       |   ``"namespaced_identifiers": true,``
       |   ``"namespaces": {``
       |     ``"identity": "foo",``
       |     ``"property": "bar"``
       |   ``}``
       | ``}``
       |
       | *Source entity:*
       | ``{"a": 1,``
       |  ``"x:a": 2}``
       |  ``"xyz:a": 3}``
       |
       | ``["rename", "a", "b"]``
       |
       | Result:
       | ``{ "b": 1.``
       |   ``"x:b": 2,``.
       |   ``"xyz:b": 3}``.
       | Renames the ``a`` property in all namespaces to ``b`` in the same namespace.
         In practice this renames the identifier part of the namespaced identifiers
         from ``a`` to ``b``. If PROPERTY2 only contains the identifier part of
         namespaced identifier, then the identifier part of PROPERTY1 will be renamed to this.
       |
       | ``["rename", "a", "z:b"]``
       |
       | Result:
       | ``{"z:b": [1, 2, 3]}``.
       | Collects all the values in the ``a`` property in all namespaces into
         the ``z:b`` property. If PROPERTY2 contains a fully qualified namespaced
         identifier then all values in PROPERTY1 will be collected into this property.
       |
       | ``["rename", "x:a", "x:b"]``
       |
       | Result:
       | ``{"x:b": 2}``.
       | Renames the ``x:a`` property to ``x:b``.
