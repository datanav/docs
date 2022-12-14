How Sesam Talk works
====================

Sesam Talk synchronizes a limited set of core types with a limited set of properties between the various :doc:`supported system <systems/index>`.

Sesam Talk merges data from the different systems on certain criteria. People are merged if they have the same email, organisations are merged if they have the exact same name.

Person model
------------
Sesam Talk has the following model for a person.

.. list-table::
   :header-rows: 1

   * - Property
     - Description
     - Example

   * - firstname
     - First name
     - "John"

   * - laatname
     - Last name
     - "Doe"

   * - email
     - Email
     - "john.doe@sesam.io"

Organisation model
------------------
Sesam Talk has the following model for an organisation.

.. list-table::
   :header-rows: 1

   * - Property
     - Description
     - Example

   * - name
     - Name of the organisation
     - "Sesam.io AS"

   * - address
     - Adresse line
     - "Sørkedalsveien 8"

   * - address2
     - Adresse line 2
     - ""

   * - zip
     - Zipcode
     - "7435"

   * - country
     - Country [1]_
     - "Norway"

   * - domain
     - Top level domain
     - "sesam.io"

.. [1] Maps to a controlled vocabulary.

Systems
-------
Sesam Talk can read and write data for several common cloud services.


.. list-table::
   :header-rows: 1

   * - System
     - Type of system
     - Organisation
     - Person

   * - :ref:`wave`
     - Accounting
     - Yes
     - Yes (primary contact from companies)

   * - :ref:`hubspot`
     - CRM
     - Yes
     - Yes

   * - :ref:`freshteam`
     - CRM
     - Yes
     - Yes

Enhancement systems
-------------------
Sesam Talk has support for systems that enhances your data.

.. list-table::
   :header-rows: 1

   * - System
     - Organisation
     - Person

   * - :ref:`opensesam`
     - Yes
     - N/A

Analytic systems
----------------
Sesam Talk can write and keep all your data up-to-date in your analytic solution.

.. list-table::
   :header-rows: 1

   * - System
     - Organisation
     - Person

   * - :ref:`bigquery`
     - Yes
     - Yes
