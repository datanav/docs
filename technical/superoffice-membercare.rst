==================================
SuperOffice to MemberCare Dataflow
==================================

Generated: 2024-09-30 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to MemberCare Companies
-------------------------------------------
Every SuperOffice Contact will be synchronized with a MemberCare Companies.

Once a link between a SuperOffice Contact and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - Name
     - companyName
     - "string"
   * - Urls.Value
     - url
     - "string"


SuperOffice Person to MemberCare Persons
----------------------------------------
Every SuperOffice Person will be synchronized with a MemberCare Persons.

Once a link between a SuperOffice Person and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - Address.Street.City
     - addresses.postalCode.city
     - "string"
   * - Address.Street.Zipcode
     - addresses.postalCode.zipCode
     - "string"
   * - BirthDate
     - birthDate
     - "string"
   * - Country.CountryId
     - addresses.country.id
     - "string"
   * - Emails.Value
     - socialSecurityNumber.number (Dependant on having wd:Q1273217 in socialSecurityNumber.iso2Letter)
     - "string"
   * - Firstname
     - firstname
     - "string"
   * - Lastname
     - lastname
     - "string"
   * - PersonId
     - addresses.id
     - "string"


SuperOffice Product to MemberCare Products
------------------------------------------
Every SuperOffice Product will be synchronized with a MemberCare Products.

Once a link between a SuperOffice Product and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - MemberCare Products Property
     - MemberCare Data Type
   * - Name
     - name
     - "string"


SuperOffice Quotealternative to MemberCare Invoices
---------------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a MemberCare Invoices.

Once a link between a SuperOffice Quotealternative and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - MemberCare Invoices Property
     - MemberCare Data Type


SuperOffice Quoteline to MemberCare Invoices
--------------------------------------------
Every SuperOffice Quoteline will be synchronized with a MemberCare Invoices.

Once a link between a SuperOffice Quoteline and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - Description
     - invoiceItems.description
     - "string"
   * - Quantity
     - invoiceItems.quantity
     - "string"
   * - UnitListPrice
     - invoiceItems.unitPrice
     - "string"


SuperOffice Sale to MemberCare Invoices
---------------------------------------
Every SuperOffice Sale will be synchronized with a MemberCare Invoices.

Once a link between a SuperOffice Sale and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - MemberCare Invoices Property
     - MemberCare Data Type


SuperOffice Listcountryitems to MemberCare Countries
----------------------------------------------------
Every SuperOffice Listcountryitems will be synchronized with a MemberCare Countries.

Once a link between a SuperOffice Listcountryitems and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcountryitems and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcountryitems Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - Name
     - name
     - "string"
   * - ThreeLetterISOCountry
     - iso3Letter
     - "string"
   * - TwoLetterISOCountry
     - iso2Letter
     - "string"

