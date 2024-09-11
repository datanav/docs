===========================
Membercare to Keap Dataflow
===========================

Generated: 2024-09-11 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Membercare to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Membercare Companies to Keap Companies
--------------------------------------
Every Membercare Companies will be synchronized with a Keap Companies.

Once a link between a Membercare Companies and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
     - Keap Companies Property
     - Keap Data Type
   * - companyName
     - company_name
     - "string"


Membercare Organizations to Keap Companies
------------------------------------------
Every Membercare Organizations will be synchronized with a Keap Companies.

Once a link between a Membercare Organizations and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Organizations and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Membercare Organizations Property
     - Keap Companies Property
     - Keap Data Type
   * - name
     - company_name
     - "string"


Membercare Persons to Keap Contacts
-----------------------------------
Every Membercare Persons will be synchronized with a Keap Contacts.

Once a link between a Membercare Persons and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Persons and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Membercare Persons Property
     - Keap Contacts Property
     - Keap Data Type
   * - birthDate
     - birthday
     - "string"
   * - firstname
     - family_name
     - "string"
   * - firstname
     - given_name
     - "string"
   * - name
     - family_name
     - "string"
   * - name
     - given_name
     - "string"

