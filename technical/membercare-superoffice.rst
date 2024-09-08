==================================
Membercare to Superoffice Dataflow
==================================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Membercare to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Membercare Companies to Superoffice Contact
-------------------------------------------
Every Membercare Companies will be synchronized with a Superoffice Contact.

Once a link between a Membercare Companies and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - companyName
     - Name
     - "string"
   * - url
     - Urls.Value
     - "string"


Membercare Organizations to Superoffice Contact
-----------------------------------------------
Every Membercare Organizations will be synchronized with a Superoffice Contact.

Once a link between a Membercare Organizations and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Organizations and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Membercare Organizations Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - name
     - Name
     - "string"


Membercare Persons to Superoffice Person
----------------------------------------
Every Membercare Persons will be synchronized with a Superoffice Person.

Once a link between a Membercare Persons and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Persons and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Membercare Persons Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - addresses.country.id
     - Country.CountryId
     - "integer"
   * - addresses.id
     - PersonId
     - "integer"
   * - addresses.postalCode.city
     - Address.Street.City
     - "string"
   * - addresses.postalCode.zipCode
     - Address.Street.Zipcode
     - "string"
   * - birthDate
     - BirthDate
     - N/A
   * - firstname
     - Firstname
     - "string"
   * - lastname
     - Lastname
     - "string"


Membercare Invoices to Superoffice Quoteline
--------------------------------------------
Every Membercare Invoices will be synchronized with a Superoffice Quoteline.

Once a link between a Membercare Invoices and a Superoffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Invoices and a Superoffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Membercare Invoices Property
     - Superoffice Quoteline Property
     - Superoffice Data Type
   * - invoiceItems.description
     - Description
     - "string"
   * - invoiceItems.quantity
     - Quantity
     - N/A
   * - invoiceItems.unitPrice
     - UnitListPrice
     - N/A

