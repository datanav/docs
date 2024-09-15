===========================
Wave to MemberCare Dataflow
===========================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to MemberCare Companies
-------------------------------------
Every Wave Customer will be synchronized with a MemberCare Companies.

Once a link between a Wave Customer and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - name
     - companyName
     - "string"
   * - website
     - url
     - "string"


Wave Customer person to MemberCare Persons
------------------------------------------
Every Wave Customer person will be synchronized with a MemberCare Persons.

Once a link between a Wave Customer person and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - MemberCare Persons Property
     - MemberCare Data Type
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


Wave Invoice to MemberCare Invoices
-----------------------------------
Every Wave Invoice will be synchronized with a MemberCare Invoices.

Once a link between a Wave Invoice and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - MemberCare Invoices Property
     - MemberCare Data Type
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


Wave Product to MemberCare Products
-----------------------------------
Every Wave Product will be synchronized with a MemberCare Products.

Once a link between a Wave Product and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - MemberCare Products Property
     - MemberCare Data Type
   * - name
     - name
     - "string"


Wave Country to MemberCare Countries
------------------------------------
Every Wave Country will be synchronized with a MemberCare Countries.

Once a link between a Wave Country and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Country and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - Wave Country Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - name
     - name
     - "string"

