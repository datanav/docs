===================================
WebCRM to Business Central Dataflow
===================================

Generated: 2024-09-13 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Organisations to Business Central Companies
--------------------------------------------------
Every WebCRM Organisations will be synchronized with a Business Central Companies.

Once a link between a WebCRM Organisations and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - Business Central Companies Property
     - Business Central Data Type


WebCRM Persons to Business Central Contacts person
--------------------------------------------------
Every WebCRM Persons will be synchronized with a Business Central Contacts person.

Once a link between a WebCRM Persons and a Business Central Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Persons and a Business Central Contacts person:

.. list-table::
   :header-rows: 1

   * - WebCRM Persons Property
     - Business Central Contacts person Property
     - Business Central Data Type
   * - PersonDirectPhone
     - phoneNumber
     - "string"
   * - PersonMobilePhone
     - mobilePhoneNumber
     - "string"
   * - PersonName
     - displayName
     - "string"


WebCRM Products to Business Central Items
-----------------------------------------
Every WebCRM Products will be synchronized with a Business Central Items.

Once a link between a WebCRM Products and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - Business Central Items Property
     - Business Central Data Type
   * - ProductCostPrice
     - unitCost
     - N/A
   * - ProductPrice
     - unitPrice
     - N/A


WebCRM Quotationline to Business Central Salesorderlines
--------------------------------------------------------
Every WebCRM Quotationline will be synchronized with a Business Central Salesorderlines.

Once a link between a WebCRM Quotationline and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - Business Central Salesorderlines Property
     - Business Central Data Type

