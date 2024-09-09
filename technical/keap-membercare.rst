===========================
Keap to Membercare Dataflow
===========================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Companies to Membercare Companies
--------------------------------------
Every Keap Companies will be synchronized with a Membercare Companies.

Once a link between a Keap Companies and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Companies and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Keap Companies Property
     - Membercare Companies Property
     - Membercare Data Type
   * - company_name
     - companyName
     - "string"


Keap Contacts to Membercare Persons
-----------------------------------
Every Keap Contacts will be synchronized with a Membercare Persons.

Once a link between a Keap Contacts and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Contacts and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Keap Contacts Property
     - Membercare Persons Property
     - Membercare Data Type
   * - birthday
     - birthDate
     - "string"
   * - family_name
     - firstname
     - "string"
   * - family_name
     - name
     - "string"
   * - given_name
     - firstname
     - "string"
   * - given_name
     - name
     - "string"


Keap Opportunity to Membercare Invoices
---------------------------------------
Every Keap Opportunity will be synchronized with a Membercare Invoices.

Once a link between a Keap Opportunity and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Opportunity and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Keap Opportunity Property
     - Membercare Invoices Property
     - Membercare Data Type


Keap Product to Membercare Products
-----------------------------------
Every Keap Product will be synchronized with a Membercare Products.

Once a link between a Keap Product and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Membercare Products Property
     - Membercare Data Type
   * - product_name
     - name
     - "string"

