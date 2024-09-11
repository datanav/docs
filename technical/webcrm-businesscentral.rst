==================================
WebCRM to BusinessCentral Dataflow
==================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to BusinessCentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Organisations to Business Companies
------------------------------------------
Every WebCRM Organisations will be synchronized with a Business Companies.

Once a link between a WebCRM Organisations and a Business Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a Business Companies:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - Business Companies Property
     - Business Data Type


WebCRM Persons to BusinessCentral Contacts person
-------------------------------------------------
Every WebCRM Persons will be synchronized with a BusinessCentral Contacts person.

Once a link between a WebCRM Persons and a BusinessCentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Persons and a BusinessCentral Contacts person:

.. list-table::
   :header-rows: 1

   * - WebCRM Persons Property
     - BusinessCentral Contacts person Property
     - BusinessCentral Data Type
   * - PersonDirectPhone
     - phoneNumber
     - "string"
   * - PersonMobilePhone
     - mobilePhoneNumber
     - "string"
   * - PersonName
     - displayName
     - "string"


WebCRM Products to BusinessCentral Items
----------------------------------------
Every WebCRM Products will be synchronized with a BusinessCentral Items.

Once a link between a WebCRM Products and a BusinessCentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a BusinessCentral Items:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - BusinessCentral Items Property
     - BusinessCentral Data Type
   * - ProductCostPrice
     - unitCost
     - N/A
   * - ProductPrice
     - unitPrice
     - N/A


WebCRM Quotationline to BusinessCentral Salesorderlines
-------------------------------------------------------
Every WebCRM Quotationline will be synchronized with a BusinessCentral Salesorderlines.

Once a link between a WebCRM Quotationline and a BusinessCentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a BusinessCentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - BusinessCentral Salesorderlines Property
     - BusinessCentral Data Type

