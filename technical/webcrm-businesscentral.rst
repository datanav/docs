===================================
WebCRM to Business Central Dataflow
===================================

Generated: 2024-09-11 07:53:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Organisations to Businesscentral Companies
-------------------------------------------------
Every Webcrm Organisations will be synchronized with a Businesscentral Companies.

Once a link between a Webcrm Organisations and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Organisations and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Webcrm Organisations Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


WebCRM Persons to Business Contacts person
------------------------------------------
Every WebCRM Persons will be synchronized with a Business Contacts person.

Once a link between a WebCRM Persons and a Business Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Persons and a Business Contacts person:

.. list-table::
   :header-rows: 1

   * - WebCRM Persons Property
     - Business Contacts person Property
     - Business Data Type
   * - PersonDirectPhone
     - phoneNumber
     - "string"
   * - PersonMobilePhone
     - mobilePhoneNumber
     - "string"
   * - PersonName
     - displayName
     - "string"


WebCRM Products to Business Items
---------------------------------
Every WebCRM Products will be synchronized with a Business Items.

Once a link between a WebCRM Products and a Business Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a Business Items:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - Business Items Property
     - Business Data Type
   * - ProductCostPrice
     - unitCost
     - N/A
   * - ProductPrice
     - unitPrice
     - N/A


WebCRM Quotationline to Business Salesorderlines
------------------------------------------------
Every WebCRM Quotationline will be synchronized with a Business Salesorderlines.

Once a link between a WebCRM Quotationline and a Business Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a Business Salesorderlines:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - Business Salesorderlines Property
     - Business Data Type

