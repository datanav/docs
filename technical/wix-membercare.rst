==============================
Wix.com to Membercare Dataflow
==============================

Generated: 2024-09-07 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Membercare Persons
--------------------------------------
Every Wix.com Contacts will be synchronized with a Membercare Persons.

Once a link between a Wix.com Contacts and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Membercare Persons Property
     - Membercare Data Type
   * - info.name.first
     - firstname
     - "string"
   * - info.name.last
     - lastname
     - "string"
   * - primaryInfo.email
     - socialSecurityNumber.number (Dependant on having wd:Q1273217 in socialSecurityNumber.iso2Letter)
     - "string"


Wix.com Products to Membercare Products
---------------------------------------
Every Wix.com Products will be synchronized with a Membercare Products.

Once a link between a Wix.com Products and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Membercare Products Property
     - Membercare Data Type
   * - name
     - name
     - "string"

