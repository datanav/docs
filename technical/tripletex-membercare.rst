================================
Tripletex to Membercare Dataflow
================================

Generated: 2024-09-07 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to Membercare Persons
---------------------------------------
Every Tripletex Contact will be synchronized with a Membercare Persons.

Once a link between a Tripletex Contact and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Membercare Persons Property
     - Membercare Data Type
   * - email
     - socialSecurityNumber.number (Dependant on having wd:Q1273217 in socialSecurityNumber.iso2Letter)
     - "string"
   * - firstName
     - firstname
     - "string"
   * - lastName
     - lastname
     - "string"


Tripletex Customer to Membercare Companies
------------------------------------------
Every Tripletex Customer will be synchronized with a Membercare Companies.

Once a link between a Tripletex Customer and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Membercare Companies Property
     - Membercare Data Type
   * - name
     - companyName
     - "string"
   * - website
     - url
     - "string"


Tripletex Customer person to Membercare Persons
-----------------------------------------------
Every Tripletex Customer person will be synchronized with a Membercare Persons.

Once a link between a Tripletex Customer person and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Membercare Persons Property
     - Membercare Data Type
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


Tripletex Department to Membercare Companies
--------------------------------------------
Every Tripletex Department will be synchronized with a Membercare Companies.

Once a link between a Tripletex Department and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Membercare Companies Property
     - Membercare Data Type
   * - name
     - companyName
     - "string"


Tripletex Employee to Membercare Persons
----------------------------------------
Every Tripletex Employee will be synchronized with a Membercare Persons.

Once a link between a Tripletex Employee and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Membercare Persons Property
     - Membercare Data Type
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


Tripletex Order to Membercare Invoices
--------------------------------------
Every Tripletex Order will be synchronized with a Membercare Invoices.

Once a link between a Tripletex Order and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Membercare Invoices Property
     - Membercare Data Type


Tripletex Orderline to Membercare Invoices
------------------------------------------
Every Tripletex Orderline will be synchronized with a Membercare Invoices.

Once a link between a Tripletex Orderline and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Membercare Invoices Property
     - Membercare Data Type
   * - count
     - invoiceItems.quantity
     - "string"
   * - description
     - invoiceItems.description
     - "string"
   * - unitPriceExcludingVatCurrency
     - invoiceItems.unitPrice
     - "string"


Tripletex Product to Membercare Products
----------------------------------------
Every Tripletex Product will be synchronized with a Membercare Products.

Once a link between a Tripletex Product and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Membercare Products Property
     - Membercare Data Type
   * - name
     - name
     - "string"


Tripletex Country to Membercare Countries
-----------------------------------------
Every Tripletex Country will be synchronized with a Membercare Countries.

Once a link between a Tripletex Country and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Country and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Tripletex Country Property
     - Membercare Countries Property
     - Membercare Data Type
   * - isoAlpha2Code
     - iso2Letter
     - "string"
   * - isoAlpha3Code
     - iso3Letter
     - "string"
   * - name
     - name
     - "string"


Tripletex Invoice to Membercare Invoices
----------------------------------------
Every Tripletex Invoice will be synchronized with a Membercare Invoices.

Once a link between a Tripletex Invoice and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Invoice and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Tripletex Invoice Property
     - Membercare Invoices Property
     - Membercare Data Type
   * - invoiceDueDate
     - payDueDate
     - "string"

