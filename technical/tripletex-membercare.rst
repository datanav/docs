================================
Tripletex to MemberCare Dataflow
================================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to MemberCare Persons
---------------------------------------
Every Tripletex Contact will be synchronized with a MemberCare Persons.

Once a link between a Tripletex Contact and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - email
     - socialSecurityNumber.number (Dependant on having wd:Q1273217 in socialSecurityNumber.iso2Letter)
     - "string"
   * - firstName
     - firstname
     - "string"
   * - lastName
     - lastname
     - "string"


Tripletex Customer to MemberCare Companies
------------------------------------------
Every Tripletex Customer will be synchronized with a MemberCare Companies.

Once a link between a Tripletex Customer and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - name
     - companyName
     - "string"
   * - website
     - url
     - "string"


Tripletex Customer person to MemberCare Persons
-----------------------------------------------
Every Tripletex Customer person will be synchronized with a MemberCare Persons.

Once a link between a Tripletex Customer person and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - deliveryAddress.city
     - addresses.postalCode.city
     - "string"
   * - deliveryAddress.country.id
     - addresses.country.id
     - "string"
   * - deliveryAddress.postalCode
     - addresses.postalCode.zipCode
     - "string"
   * - email
     - socialSecurityNumber.number (Dependant on having wd:Q1273217 in socialSecurityNumber.iso2Letter)
     - "string"
   * - id
     - addresses.id
     - "string"
   * - name
     - name
     - "string"
   * - physicalAddress.city
     - addresses.postalCode.city
     - "string"
   * - physicalAddress.country.id
     - addresses.country.id
     - "string"
   * - physicalAddress.postalCode
     - addresses.postalCode.zipCode
     - "string"
   * - postalAddress.city
     - addresses.postalCode.city
     - "string"
   * - postalAddress.country.id
     - addresses.country.id
     - "string"
   * - postalAddress.postalCode
     - addresses.postalCode.zipCode
     - "string"


Tripletex Department to MemberCare Companies
--------------------------------------------
Every Tripletex Department will be synchronized with a MemberCare Companies.

Once a link between a Tripletex Department and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - name
     - companyName
     - "string"


Tripletex Employee to MemberCare Persons
----------------------------------------
Every Tripletex Employee will be synchronized with a MemberCare Persons.

Once a link between a Tripletex Employee and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - address.city
     - addresses.postalCode.city
     - "string"
   * - address.country.id
     - addresses.country.id
     - "string"
   * - address.postalCode
     - addresses.postalCode.zipCode
     - "string"
   * - dateOfBirth
     - birthDate
     - "string"
   * - email
     - socialSecurityNumber.number (Dependant on having wd:Q1273217 in socialSecurityNumber.iso2Letter)
     - "string"
   * - employeeNumber
     - socialSecurityNumber.number (Dependant on having wd:Q36218176 in socialSecurityNumber.iso2Letter)
     - "string"
   * - firstName
     - firstname
     - "string"
   * - id
     - addresses.id
     - "string"
   * - lastName
     - lastname
     - "string"
   * - nationalIdentityNumber
     - socialSecurityNumber.number (Dependant on having wd:Q1140371 in socialSecurityNumber.iso2Letter)
     - "string"


Tripletex Order to MemberCare Invoices
--------------------------------------
Every Tripletex Order will be synchronized with a MemberCare Invoices.

Once a link between a Tripletex Order and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - MemberCare Invoices Property
     - MemberCare Data Type


Tripletex Orderline to MemberCare Invoices
------------------------------------------
Every Tripletex Orderline will be synchronized with a MemberCare Invoices.

Once a link between a Tripletex Orderline and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - count
     - invoiceItems.quantity
     - "string"
   * - description
     - invoiceItems.description
     - "string"
   * - unitPriceExcludingVatCurrency
     - invoiceItems.unitPrice
     - "string"


Tripletex Product to MemberCare Products
----------------------------------------
Every Tripletex Product will be synchronized with a MemberCare Products.

Once a link between a Tripletex Product and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - MemberCare Products Property
     - MemberCare Data Type
   * - name
     - name
     - "string"


Tripletex Country to MemberCare Countries
-----------------------------------------
Every Tripletex Country will be synchronized with a MemberCare Countries.

Once a link between a Tripletex Country and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Country and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - Tripletex Country Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - isoAlpha2Code
     - iso2Letter
     - "string"
   * - isoAlpha3Code
     - iso3Letter
     - "string"
   * - name
     - name
     - "string"


Tripletex Invoice to MemberCare Invoices
----------------------------------------
Every Tripletex Invoice will be synchronized with a MemberCare Invoices.

Once a link between a Tripletex Invoice and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Invoice and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Tripletex Invoice Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - invoiceDueDate
     - payDueDate
     - "string"

