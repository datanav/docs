=======================================
Powerofficego to PowerOfficeGo Dataflow
=======================================

Generated: 2023-08-14 09:28:53

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Supplier to PowerOfficeGo Address
-----------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Supplier and a PowerOfficeGo Address must be established.

A Powerofficego Supplier will merge with a PowerOfficeGo Address if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGo Address Property
   * - MailAddress.Id
     - id

Once a link between a Powerofficego Supplier and a PowerOfficeGo Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Supplier and a PowerOfficeGo Address:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGo Address Property
     - PowerOfficeGo Data Type


Powerofficego Contactperson to PowerOfficeGo Address
----------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a PowerOfficeGo Address.

Once a link between a Powerofficego Contactperson and a PowerOfficeGo Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a PowerOfficeGo Address:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - PowerOfficeGo Address Property
     - PowerOfficeGo Data Type
   * - address1
     - address1
     - "string"
   * - address2
     - address2
     - "string"
   * - city
     - city
     - "string"
   * - residenceCountryCode
     - countryCode
     - "string"
   * - zipCode
     - zipCode
     - "string"


Powerofficego Contactperson to PowerOfficeGo Customer
-----------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a PowerOfficeGo Customer.

Once a link between a Powerofficego Contactperson and a PowerOfficeGo Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a PowerOfficeGo Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - PowerOfficeGo Customer Property
     - PowerOfficeGo Data Type
   * - address1
     - mailAddress.address1
     - "string"
   * - address2
     - mailAddress.address2
     - "string"
   * - city
     - mailAddress.city
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - "string"
   * - emailAddress
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "string"
   * - lastChanged
     - lastChanged
     - "string"
   * - lastName
     - LastName
     - "string"
   * - residenceCountryCode
     - mailAddress.countryCode
     - "string"
   * - zipCode
     - mailAddress.zipCode
     - "string"


Powerofficego Contactperson to PowerOfficeGo Customers
------------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a PowerOfficeGo Customers.

Once a link between a Powerofficego Contactperson and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - dateOfBirth
     - dateOfBirth
     - "string"
   * - emailAddress
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - LastName
     - "string"


Powerofficego Customer to PowerOfficeGo Contactperson
-----------------------------------------------------
Every Powerofficego Customer will be synchronized with a PowerOfficeGo Contactperson.

Once a link between a Powerofficego Customer and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type
   * - LastName
     - lastName
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - "string"
   * - emailAddress
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "integer"
   * - lastChanged
     - lastChanged
     - "string"
   * - mailAddress.address1
     - address1
     - "string"
   * - mailAddress.address2
     - address2
     - "string"
   * - mailAddress.city
     - city
     - "string"
   * - mailAddress.countryCode
     - residenceCountryCode
     - "string"
   * - mailAddress.zipCode
     - zipCode
     - "string"


Powerofficego Customers to PowerOfficeGo Contactperson
------------------------------------------------------
Every Powerofficego Customers will be synchronized with a PowerOfficeGo Contactperson.

Once a link between a Powerofficego Customers and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type
   * - LastName
     - lastName
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - "string"
   * - emailAddress
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"

