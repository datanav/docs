===================
DTL Reference Guide
===================

.. contents:: Table of Contents


Variables
----------

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Variable
     - Description
     - Examples
       
   * - ``_S``
     - Refers to the source entity. This is the entity on which the
       DTL transform operate. Note that with the ``apply`` function
       you can apply nested transforms, where each of the values
       given to ``apply`` is made a source entity for that nested
       transform.
     - | ``["gt", "_S.age", 42]``
       |
       | The source entity's ``age`` field must have a value greater than 26.

   * - ``_T``
     - Refers to the target entity. This is the entity that is the
       primary target entity of transforming the source entity. Note
       that the ``create`` transform can be used to emit entities
       in addition to just the target entity.
     - | ``["length", "_T.description", 100]``
       |
       | The target entity's ``description`` field must have a length of
         more than 100 characters.

   * - ``_``
     - Refers to the current entity. This variable is only available
       inside a few functions that take an expression as an
       argument. Examples of such functions are ``filter``, ``sort``
       and ``coalesce``.
     - | ``["filter", ["gt", "_.amount", 100], "_S.orders"]]``
       |
       | Filters out the order entities that have an amount of less than
         100, i.e. the filter function returns only the orders that have
         an amount of greater than 100. As you can see the ``_`` variable
         refers to the individual order entities, one at a time.



Logical
---------------

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples
       
   * - ``and``
     - | *Arguments:* boolean-expression{>0}
       |
       | Takes at least one boolean expression argument.
         Returns true only if all arguments evaluate to true.
     - | ``["and",``
       |    ``["gt", "_S.age", 26],``
       |    ``["eq", "_S.gender", "male"]]``
       |
       | Age must be greater than 26 and the gender must be male.

   * - ``or``
     - | *Arguments:* boolean-expression{>=0}
       |
       | Takes at least one boolean expression argument.
         Returns true if any of the arguments evaluate to true.
     - | ``["or",``
       |   ``["eq", "_S.category", "A"],``
       |   ``["eq", "_S.category", "B"]]``
       |
       | The category field must contain "A" or "B".
       
   * - ``not``
     - | *Arguments:* boolean-expression{1}
       |
       | Takes a single boolean expression argument.
         Returns the inverse boolean value.
     - | ``["not",``
       |   ``["or",``
       |      ``["eq", "_S.category", "A"],``
       |      ``["eq", "_S.category", "B"]]]``
       |
       | The category must contain neither "A" nor "B".


A *boolean-expression* is any function that returns a boolean value.

Comparisons
--------------------

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples
       
   * - ``eq``
     - | *Arguments:* value-expression{2}
       |
       | Coerces the values returned from the value expressions into
         list and compares those lists. Returns *true* if the two
         arguments given are equal.
     - | ``["eq", "_S.age", 42]``
       |
       | The source entity's age field must have the value 42.
       
   * - ``neq``
     - | *Arguments:* value-expression{2}
       |
       | Coerces the values returned from the value expressions into
         list and compares those lists. Returns *false* if the two
         arguments given are equal.
     - | ``["neq", "_S.age", 42]``
       |
       | The source entity's age field must *not* have the value 42.
       
   * - ``gt``
     - | *Arguments:* value-expression{2}
       |
       | Compares the *first value* returned by the two value
         expressions. Returns *true* if the first argument is greater
         than the second argument.
     - | ``["gt", "_S.age", 42]``
       |
       | The source entity's ``age`` field must have a value greater
         than 42.
       
   * - ``gte``
     - | *Arguments:* value-expression{2}
       |
       | Compares the *first value* returned by the two value
         expressions. Returns *true* if the first argument is greater
         than or equal the second argument.
     - | ``["gte", "_S.age", 42]``
       |
       | The source entity's ``age`` field must have a value greater
         than or equal 42.
       
   * - ``lt``
     - | *Arguments:* value-expression{2}
       |
       | Compares the *first value* returned by the two value
         expressions. Returns *true* if the first argument is less than
         the second argument.
     - | ``["lt", "_S.age", 42]``
       |
       | The source entity's ``age`` field must have a value less
         than 42.
       
   * - ``lte``
     - | *Arguments:* value-expression{2}
       |
       | Compares the *first value* returned by the two value
         expressions. Returns *true* if the first argument is less than
         or equal the second argument.
     - | ``["lte", "_S.age", 42]``
       |
       | The source entity's ``age`` field must have a value less
         than or equal 42.
       
   * - ``empty``
     - | *Arguments:* value-expression{1}
       |
       | Coerces the values returned from the value expressions into
         list. Returns *true* if the number of elements in the first
         argument is 0.
     - | ``["empty", "_S.hobbies"]``
       |
       | Returns true of the source entity's ``hobbies`` field is
         empty (has no values).

       
   * - ``not-empty``
     - | *Arguments:* value-expression{1}
       |
       | Coerces the values returned from the value expressions into
         list. Returns *true* if the number of elements in the first
         argument is greater than 0.
     - | ``["not-empty", "_S.hobbies"]``
       |
       | Returns true of the source entity's ``hobbies`` field is not
         empty (has one or more values).


Conditionals
---------------------

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples
       
   * - ``if``
     - | *Arguments:*
       |   CONDITION(boolean-expression{1}),
       |   THEN(value-expression{1}),
       |   ELSE(value-expression{0\|1})
       |
       | If CONDITION evaluates to *true* then return the result of
         evaluating THEN. If CONDITION evaluates to *false* then return
         the result of evaluating ELSE.
     - | ``["if", ["gt", "_S.age", 42], 1, 2]``
       |
       | Return 1 if the source entity's ``age`` field is greater
         than 43, if not 2 is returned.

   * - ``coalesce``
     - | *Arguments:*
       |   FUNCTION(function-expression{0|1}),
       |   VALUES(value-expression{1})
       |
       | Returns the first value in VALUES that makes the FUNCTION expression
         return a non-null value. The FUNCTION expression argument is optional,
         so if it is not given the first non-null value in VALUES is returned.
     - | ``["coalesce", "_S.tags"]``
       |
       | Returns the first value in the source entity's ``tags``
         field that is not null.
       |
       | ``["coalesce",``
       |     ``["gt", "_.expenses", 1000], "_S.hobbies"]``
       |
       | Returns the first hobby that has expenses greater than 1000.


Nested transformations
----------------------

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples
       
   * - ``apply``
     - | *Arguments:*
       |   TRANSFORM_ID(string{1}),
       |   VALUES(value-expression{1})
       |
       | Applies the TRANSFORM_ID transform on the entities in VALUES.
         TRANSFORM_ID must be the id of a transform in the current DTL
         specification.
     - | ``["apply", "order", "_S.orders"]``
       |
       | This will transform the order entities in the source entity's
         ``orders`` field using the ``order`` transform. The output is
         the transformed order entities.


Paths
----------------------

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples
       
   * - ``path``
     - | *Arguments:*
       |   PROPERTY_PATH(string{1}),
       |   VALUES(value-expression{1})
       |
       | Traverses the PROPERTY_PATH path for each of the entities in
         VALUES. The result is a list of all the values at the end of
         the traversal. PROPERTY_PATH paths are separated by '``.``'
         (periods). Only properties on the entity can be traversed. If
         you want to traverse to other entities use ``hops`` instead.
     - | ``["path", "age", ["values", {"age": 23}, {"age": 24}]]``
       |
       | Traverses the ``age`` field of the VALUES entities.
         Returns ``[23, 24]``.
       |
       | ``["path", "order_lines.item_name", "_S.orders"]``
       |
       | This will travese from the source entity's orders to the
         order lines and their item names. The output is a list of
         product item names.


Hops
----------------------

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples
       
   * - ``hops``
     - | *Arguments:*
       |   HOPS_SPEC(dict{1})
       |
       | ...TODO...
     - |


Strings
----------------------

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples
       
   * - ``upper``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the uppercase version of its input strings.
         Non-string values are ignored.
     - | ``["upper", ["values", "a", "b", "c"]]``
       |
       | Returns ``["A", "B", "C"]``.
       |
       | ``["upper", "_S.name"]``
       |
       | Returns an uppercased version of the source entity's name.
       
   * - ``lower``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the lowercase version of its input strings.
         Non-string values are ignored.
     - | ``["lower", ["values", "A", "B", "C"]]``
       |
       | Returns ``["a", "b", "c"]``.
       |
       | ``["lower", "_S.name"]``
       |
       | Returns a lowercased version of the source entity's name.
       
   * - ``length``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the length (number of characters) of its input strings.
         Non-string values are ignored.
     - | ``["length", ["values", "", "a", "bb", "ccc"]]``
       |
       | Returns ``[0, 1, 2, 3]``.
       |
       | ``["length", "_S.name"]``
       |
       | Returns the length of the source entity's name.
       
   * - ``concat``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns a concatenated string of its input strings.
         Non-string values are ignored.
     - | ``["concat", ["values", "a", "b", "c"]]``
       |
       | Returns ``"abc"``.
       |
       | ``["concat", "_S.tags"]``
       |
       | Returns a concatenated version of the source entity's tags.


Values / collections
----------------------

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples
       
   * - ``first``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the first value in VALUES. If VALUES is not a sequence
         of values, then VALUES is returned. If VALUES is empty, then
         null is returned.
     - | ``["first", ["values", "a", "b", "c"]]``
       |
       | Returns ``"A"``.
       |
       | ``["first", "_S.tags"]``
       |
       | Returns the first tag in the source entity's ``tags`` field.
       
   * - ``values``
     - | *Arguments:*
       |   VALUES(value-expression{>0})
       |
       | Constructs a list of the values in VALUES.
     - | ``["values"]``
       |
       | Returns ``[]``.
       |
       | ``["values", "a", "b", "c"]``
       |
       | Returns ``["a", "b", "c"]``.
       |
       | ``["values", "a", ["values", "b"], "c"]``
       |
       | Returns ``["a", ["b"], "c"]``.
       
   * - ``flatten``
     - | *Arguments:*
       |   VALUES(value-expression{>0})
       |
       | Flattens its input values in VALUES. Note that it does *not* do so
         recursively. Constructs a new list.
     - | ``["flatten", ["values", 1, 2], ["values", 3, 4]]``
       |
       | Returns ``[1, 2, 3, 4]``.
       |
       | ``["flatten", ["values", 1, 2], ["values", 3, ["values", 4]]]``
       |
       | Returns ``[1, 2, 3, [4]]``.
       |
       | ``["flatten", ["values", 1, 2], ["values", 3, ["values", 4]], 5]``
       |
       | Returns ``[1, 2, 3, [4], 5]``.
       
   * - ``filter``
     - | *Arguments:*
       |   FILTER(boolean-expression(1}
       |   VALUES(value-expression{1})
       |
       | Filters out the the values in VALUES for which the FILTER expression
         does *not* evaluate to *true*.
     - | ``["filter", ["gt", "_.age", 42],``
       |     ``["values", {"age": 30}, {"age": 50}, {"age": 40}]]``
       |
       | Returns ``[{"age": 50}]``.
       |
       | ``["filter", ["gt", "_.amount", 100], "_S.orders"]]``
       |
       | Returns the order entities that have an amount of more than 100.
       
   * - ``min``
     - | *Arguments:*
       |   FUNCTION(value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Returns the minimum value in VALUES. If FUNCTION is given, the
         function is evaluated for each value in VALUES to, and the return
         value is used to for ordering to figure out what is the minimal value.
         Note that even though FUNCTION is given it is the value in VALUES that
         is returned.
     - | ``["min", ["values", 4, 2, 5, 3]]``
       |
       | Returns ``2``.
       |
       | ``["min", "_.amount", "_S.orders"]]``
       |
       | Returns the order with the lowest amount.
       
   * - ``max``
     - | *Arguments:*
       |   FUNCTION(value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Returns the maximum value in VALUES. If FUNCTION is given, the
         function is evaluated for each value in VALUES to, and the return
         value is used to for ordering to figure out what is the maximal value.
         Note that even though FUNCTION is given it is the value in VALUES that
         is returned.
     - | ``["max", ["values", 4, 2, 5, 3]]``
       |
       | Returns ``5``.
       |
       | ``["max", "_.amount", "_S.orders"]]``
       |
       | Returns the order with the highest amount.

   * - ``count``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the number of elements in VALUES.
     - | ``["count", ["values", 2, 4, 6]]``
       |
       | Returns ``3``.
       |
       | ``["count", ["gt", "_.amount", 100], "_S.orders"]]``
       |
       | Returns the the number of order entities that have an amount of
         more than 100.
       
   * - ``distinct``
     - | *Arguments:*
       |   FUNCTION(value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Returns a list of distinct values in VALUES, i.e. it returns a list
         where duplicates have been removed from VALUES. If FUNCTION is given, then
         function is evaluated for each value in VALUES, and the return
         value is used to check for duplicates. Note that even though FUNCTION is
         given it is the value in VALUES that is returned.
     - | ``["distinct", ["values", 4, 2, 5, 4, 3]]``
       |
       | Returns ``[4, 2, 5, 3]``.
       |
       | ``["distinct", "_S.tags"]]``
       |
       | Returns a deduplicated list of tags.
       |
       | ``["distinct", "_.ean", "_S.orders.line_item"]]``
       |
       | Returns a list of order lines, but only one per unique EAN, i.e. product
         number.
       
   * - ``sorted``
     - | *Arguments:*
       |   FUNCTION(value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Returns a list of sorted values in VALUES. If FUNCTION is given, then
         function is evaluated for each value in VALUES, and the return
         value is used as the sort key. Note that even though FUNCTION is
         given it is the value in VALUES that is returned. Note that this function
         does *not* remove duplicates. Use ``distinct`` to do that.
     - | ``["sorted", ["values", 4, 2, 5, 4, 3]]``
       |
       | Returns ``[2, 3, 4, 4, 5]``.
       |
       | ``["sorted", ["values", {"age": 30}, {"age": 50}, {"age": 20}]]``
       |
       | Returns ``[{"age": 20}, {"age": 30}, {"age": 50}]``.
       |
       | ``["sorted", "_S.tags"]]``
       |
       | Returns a sorted list of tags.
       
   * - ``map``
     - | *Arguments:*
       |   FUNCTION(value-expression(1}
       |   VALUES(value-expression{1})
       |
       | For each value in VALUES apply the FUNCTION function and construct a new
         list of the return values.
     - | ``["map", ["lower", "_."], ["values", "A", "B", "C"]]``
       |
       | Returns ``["a", "b", "c"]``.
       |
       | ``["map", ["distinct", "_."], ["values", ["values", "A", "A"], ["values", "B", "C"]]]``
       |
       | Returns ``[["A"], ["B", "C"]]``.


Sets
----------------------

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples
       
   * - ``union``
     - | *Arguments:*
       |   SET1(value-expression{1})
       |   SET2(value-expression{1})
       |
       | Returns the union of the two sets SET1 and SET2. The two arguments
         do not have to be real sets, but will be coerced into sets before
         applying the union operator.
     - | ``["union", ["values", "A", "B"], ["values", "B", "C"]]``
       |
       | Returns ``["A", "B", "C"]``.
       |
       | ``["union", "A", ["values", "B", "C"]]``
       |
       | Returns ``["A", "B", "C"]``.
       
   * - ``intersection``
     - | *Arguments:*
       |   SET1(value-expression{1})
       |   SET2(value-expression{1})
       |
       | Returns the intersection of the two sets SET1 and SET2. The two arguments
         do not have to be real sets, but will be coerced into sets before
         applying the intersection operator.
     - | ``["intersection", ["values", "A", "B"], ["values", "B", "C"]]``
       |
       | Returns ``["B"]``.
       |
       | ``["intersection", "B", ["values", "B", "C"]]``
       |
       | Returns ``["B"]``.
       |
       | ``["intersection", "A", ["values", "B", "C"]]``
       |
       | Returns ``["A"]``.
       
   * - ``difference``
     - | *Arguments:*
       |   SET1(value-expression{1})
       |   SET2(value-expression{1})
       |
       | Returns the difference of the two sets SET1 and SET2. The two arguments
         do not have to be real sets, but will be coerced into sets before
         applying the difference operator.
     - | ``["difference", ["values", "A", "B"], ["values", "B"]]``
       |
       | Returns ``["A"]``.
       |
       | ``["difference", "A", ["values", "B", "C"]]``
       |
       | Returns ``["A"]``.
       |
       | ``["difference", ["values", "A", "B", "C", "D"], ["values", "A", "B", "E"]]``
       |
       | Returns ``["C", "D"]``.
