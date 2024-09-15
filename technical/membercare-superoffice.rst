==================================
MemberCare to SuperOffice Dataflow
==================================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Companies to SuperOffice Contact
-------------------------------------------
Every MemberCare Companies will be synchronized with a SuperOffice Contact.

Once a link between a MemberCare Companies and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companies and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - MemberCare Companies Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - companyName
     - Name
     - "string"
   * - url
     - Urls.Value
     - "string"


MemberCare Organizations to SuperOffice Contact
-----------------------------------------------
Every MemberCare Organizations will be synchronized with a SuperOffice Contact.

Once a link between a MemberCare Organizations and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Organizations and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - MemberCare Organizations Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - name
     - Name
     - "string"


MemberCare Persons to SuperOffice Person
----------------------------------------
Every MemberCare Persons will be synchronized with a SuperOffice Person.

Once a link between a MemberCare Persons and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Persons and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - MemberCare Persons Property
     - SuperOffice Person Property
     - SuperOffice Data Type
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


MemberCare Invoices to SuperOffice Quoteline
--------------------------------------------
Every MemberCare Invoices will be synchronized with a SuperOffice Quoteline.

Once a link between a MemberCare Invoices and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
   * - invoiceItems.description
     - Description
     - "string"
   * - invoiceItems.quantity
     - Quantity
     - N/A
   * - invoiceItems.unitPrice
     - UnitListPrice
     - N/A

