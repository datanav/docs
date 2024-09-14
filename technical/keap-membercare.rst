===========================
Keap to MemberCare Dataflow
===========================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Companies to MemberCare Companies
--------------------------------------
Every Keap Companies will be synchronized with a MemberCare Companies.

Once a link between a Keap Companies and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Companies and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Keap Companies Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - company_name
     - companyName
     - "string"


Keap Contacts to MemberCare Persons
-----------------------------------
Every Keap Contacts will be synchronized with a MemberCare Persons.

Once a link between a Keap Contacts and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Contacts and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Keap Contacts Property
     - MemberCare Persons Property
     - MemberCare Data Type
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


Keap Opportunity to MemberCare Invoices
---------------------------------------
Every Keap Opportunity will be synchronized with a MemberCare Invoices.

Once a link between a Keap Opportunity and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Opportunity and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Keap Opportunity Property
     - MemberCare Invoices Property
     - MemberCare Data Type


Keap Product to MemberCare Products
-----------------------------------
Every Keap Product will be synchronized with a MemberCare Products.

Once a link between a Keap Product and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - MemberCare Products Property
     - MemberCare Data Type
   * - product_name
     - name
     - "string"

