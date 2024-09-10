================================
Crmoffice to Membercare Dataflow
================================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Crmoffice to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Crmoffice Companies to Membercare Products
------------------------------------------
Every Crmoffice Companies will be synchronized with a Membercare Products.

Once a link between a Crmoffice Companies and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Crmoffice Companies and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - Crmoffice Companies Property
     - Membercare Products Property
     - Membercare Data Type


Crmoffice Contacts to Membercare Persons
----------------------------------------
Every Crmoffice Contacts will be synchronized with a Membercare Persons.

Once a link between a Crmoffice Contacts and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Crmoffice Contacts and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Crmoffice Contacts Property
     - Membercare Persons Property
     - Membercare Data Type
   * - familyName
     - lastname
     - "string"
   * - givenName
     - firstname
     - "string"


Crmoffice Activities to Membercare Countries
--------------------------------------------
Every Crmoffice Activities will be synchronized with a Membercare Countries.

Once a link between a Crmoffice Activities and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Crmoffice Activities and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Crmoffice Activities Property
     - Membercare Countries Property
     - Membercare Data Type
   * - address.country
     - name
     - "string"


Crmoffice Companies to Membercare Countries
-------------------------------------------
Every Crmoffice Companies will be synchronized with a Membercare Countries.

Once a link between a Crmoffice Companies and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Crmoffice Companies and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Crmoffice Companies Property
     - Membercare Countries Property
     - Membercare Data Type
   * - postAddress.country
     - name
     - "string"
   * - visitAddress.country
     - name
     - "string"

