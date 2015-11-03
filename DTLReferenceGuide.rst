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


