=====================================
Wave Financial to Membercare Dataflow
=====================================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Membercare Companies
-------------------------------------
Every Wave Customer will be synchronized with a Membercare Companies.

Once a link between a Wave Customer and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Membercare Companies Property
     - Membercare Data Type
   * - name
     - companyName
     - "string"
   * - website
     - url
     - "string"


Wave Customer person to Membercare Persons
------------------------------------------
Every Wave Customer person will be synchronized with a Membercare Persons.

Once a link between a Wave Customer person and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Membercare Persons Property
     - Membercare Data Type
   * - address.city
     - addresses.postalCode.city
     - "string"
   * - address.country.code
     - addresses.country.id
     - "string"
   * - address.postalCode
     - addresses.postalCode.zipCode
     - "string"
   * - email
     - socialSecurityNumber.number (Dependant on having wd:Q1273217 in socialSecurityNumber.iso2Letter)
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
   * - name
     - name
     - "string"
   * - shippingDetails.address.city
     - addresses.postalCode.city
     - "string"
   * - shippingDetails.address.country.code
     - addresses.country.id
     - "string"
   * - shippingDetails.address.postalCode
     - addresses.postalCode.zipCode
     - "string"


Wave Invoice to Membercare Invoices
-----------------------------------
Every Wave Invoice will be synchronized with a Membercare Invoices.

Once a link between a Wave Invoice and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Membercare Invoices Property
     - Membercare Data Type
   * - dueDate
     - payDueDate
     - "string"
   * - items.description
     - invoiceItems.description
     - "string"
   * - items.price
     - invoiceItems.unitPrice
     - "string"
   * - items.quantity
     - invoiceItems.quantity
     - "string"


Wave Product to Membercare Products
-----------------------------------
Every Wave Product will be synchronized with a Membercare Products.

Once a link between a Wave Product and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Membercare Products Property
     - Membercare Data Type
   * - name
     - name
     - "string"


Wave Country to Membercare Countries
------------------------------------
Every Wave Country will be synchronized with a Membercare Countries.

Once a link between a Wave Country and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Country and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Wave Country Property
     - Membercare Countries Property
     - Membercare Data Type
   * - name
     - name
     - "string"

