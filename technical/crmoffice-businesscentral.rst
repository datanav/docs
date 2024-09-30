======================================
CRMOffice to Business Central Dataflow
======================================

Generated: 2024-09-30 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CRMOffice to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CRMOffice Companies to Business Central Customers (classification data)
-----------------------------------------------------------------------
Every CRMOffice Companies will be synchronized with a Business Central Customers (classification data).

Once a link between a CRMOffice Companies and a Business Central Customers (classification data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Companies and a Business Central Customers (classification data):

.. list-table::
   :header-rows: 1

   * - CRMOffice Companies Property
     - Business Central Customers (classification data) Property
     - Business Central Data Type


CRMOffice Contacts to Business Central Contacts (human data)
------------------------------------------------------------
Every CRMOffice Contacts will be synchronized with a Business Central Contacts (human data).

Once a link between a CRMOffice Contacts and a Business Central Contacts (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Contacts and a Business Central Contacts (human data):

.. list-table::
   :header-rows: 1

   * - CRMOffice Contacts Property
     - Business Central Contacts (human data) Property
     - Business Central Data Type
   * - directPhone
     - phoneNumber
     - "string"
   * - mobilePhone
     - mobilePhoneNumber
     - "string"

