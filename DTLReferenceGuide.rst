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



Logical
---------------

.. list-table:: 
   :header-rows: 1
   :widths: 10, 20, 30, 50

   * - Function
     - Arguments
     - Description
     - Examples
       
   * - ``and``
     - boolean-expression{0\|1}
     - Returns *false* if no arguments given.
     - | ``["and", ["gt", "_S.age", 26], ["eq", "_S.gender", "male"]]``
       |
       | Age must be greater than 26 and the gender must be male.

   * - ``or``
     - boolean-expression{0\|1}
     - Returns *true* if no arguments given.
     - | ``["or", ["eq", "_S.category", "A"], ["eq", "_S.category", "B"]]``
       |
       | The category field must contain "A" or "B".
       
   * - ``not``
     - boolean-expression{1}
     - Takes a single argument and returns the inverse boolean value.
     - | ``["not", ["or", ["eq", "_S.category", "A"], ["eq", "_S.category", "B"]]]``
       |
       | The category must *not* contain "A" or "B".


A *boolean-expression* is any function that returns a boolean value.

Comparisons
--------------------

.. list-table:: 
   :header-rows: 1

   * - Function
     - Arguments
     - Description
   * - ``eq``
     - value-expression{2}
     - Coerces the values returned from the value expressions into
       list and compares those lists. Returns *true* if the two
       arguments given are equal.
   * - ``neq``
     - value-expression{2}
     - Coerces the values returned from the value expressions into
       list and compares those lists. Returns *false* if the two
       arguments given are equal.
   * - ``gt``
     - value-expression{2}
     - Compares the *first value* returned by the two value
       expressions. Returns *true* if the first argument is greater
       than the second argument.
   * - ``gte``
     - value-expression{2}
     - Compares the *first value* returned by the two value
       expressions. Returns *true* if the first argument is greater
       than or equal the second argument.
   * - ``lt``
     - value-expression{2}
     - Compares the *first value* returned by the two value
       expressions. Returns *true* if the first argument is less than
       the second argument.
   * - ``lte``
     - value-expression{2}
     - Compares the *first value* returned by the two value
       expressions. Returns *true* if the first argument is less than
       or equal the second argument.
   * - ``empty``
     - value-expression{1}
     - Coerces the values returned from the value expressions into
       list. Returns *true* if the number of elements in the first
       argument is 0.
   * - ``not-empty``
     - value-expression{1}
     - Coerces the values returned from the value expressions into
       list. Returns *true* if the number of elements in the first
       argument is greater than 0.
     

Conditionals
---------------------

.. list-table:: 
   :header-rows: 1

   * - Function
     - Arguments
     - Description
   * - ``if``
     - CONDITION(boolean-expression{1}), THEN(value-expression{1}),
       ELSE(value-expression{0\|1})
     - If CONDITION evaluates to *true* then return THEN. If CONDITION
       evaluates to *false* then return ELSE.


