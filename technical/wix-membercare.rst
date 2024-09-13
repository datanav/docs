==============================
Wix.com to MemberCare Dataflow
==============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to MemberCare Persons
--------------------------------------
Every Wix.com Contacts will be synchronized with a MemberCare Persons.

Once a link between a Wix.com Contacts and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - info.name.first
     - firstname
     - "string"
   * - info.name.last
     - lastname
     - "string"
   * - primaryInfo.email
     - socialSecurityNumber.number (Dependant on having wd:Q1273217 in socialSecurityNumber.iso2Letter)
     - "string"


Wix.com Products to MemberCare Products
---------------------------------------
Every Wix.com Products will be synchronized with a MemberCare Products.

Once a link between a Wix.com Products and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - MemberCare Products Property
     - MemberCare Data Type
   * - name
     - name
     - "string"

