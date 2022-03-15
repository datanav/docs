
.. _conditional_transform:

Conditional transform
---------------------

The conditional transform selects an active transform based on a key typically controlled by an environment variable.
It is typically used in devops to be able to use the same configuration in different type of environments (i.e. development,
staging, production). The actual transform to use is resolved at runtime when the parent pipe is created.

The configuration options are:

Prototype
^^^^^^^^^

::

    {
       "type": "conditional",
       "condition": "$ENV(current-environment)",
       "alternatives": {
           "dev": {
               "type": "dtl",
               ..
           },
           "test": {
               "type": "dtl",
               ..
              },
           "prod": {
               "type": "dtl",
               ..
           }
       }
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``condition``
     - String
     - The key to look up in ``alternatives`` for the actual transform to use at runtime. Typically an environment variable.
       Note that all possible enumerations of this value need to exist in ``alternatives``.
     -
     - Yes

   * - ``alternatives``
     - Object
     - A dictionary of actual transform configurations keyed by the enumerated value of ``condition``.
     -
     - Yes

