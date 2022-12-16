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

   * - lastname
     - Last name
     - "Doe"

   * - email
     - Email
     - "john.doe@sesam.io"
     
   * - gender (Planned)
     - Gender [1]_
     - "Male"
     
.. [1] Maps to a controlled vocabulary.

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

Product model (Planned)
-----------------------
Sesam Talk has the following model for a product.

.. list-table::
   :header-rows: 1

   * - Property
     - Description
     - Example

   * - name
     - Name of the product
     - "SesamTron 3000"

Systems
-------
Sesam Talk can read and write data for several common cloud services.


.. list-table::
   :header-rows: 1

   * - System
     - Type of system
     - Organisation
     - Person
     - Product

   * - :ref:`wave`
     - Accounting
     - Yes
     - Yes (primary contact from companies)
     - Planned

   * - :ref:`hubspot`
     - CRM
     - Yes
     - Yes
     - Planned

   * - :ref:`freshteam`
     - CRM
     - Yes
     - Yes
     - No
     
   * - CRMOffice (Planned)
     - CRM
     - Yes
     - Yes
     - Planned

Enhancement systems
-------------------
Sesam Talk has support for systems that enhances your data.

.. list-table::
   :header-rows: 1

   * - System
     - Organisation
     - Person
     - Product

   * - :ref:`opensesam`
     - Yes
     - N/A
     - Planned

Analytic systems
----------------
Sesam Talk can write and keep all your data up-to-date in your analytic solution.

.. list-table::
   :header-rows: 1

   * - System
     - Organisation
     - Person
     - Product

   * - :ref:`bigquery`
     - Yes
     - Yes
     - Planned

