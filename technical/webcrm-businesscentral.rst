==================================
Webcrm to Businesscentral Dataflow
==================================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Webcrm Persons to Businesscentral Contacts person
-------------------------------------------------
Every Webcrm Persons will be synchronized with a Businesscentral Contacts person.

Once a link between a Webcrm Persons and a Businesscentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Persons and a Businesscentral Contacts person:

.. list-table::
   :header-rows: 1

   * - Webcrm Persons Property
     - Businesscentral Contacts person Property
     - Businesscentral Data Type
   * - PersonDirectPhone
     - phoneNumber
     - "string"
   * - PersonMobilePhone
     - mobilePhoneNumber
     - "string"
   * - PersonName
     - displayName
     - "string"


Webcrm Products to Businesscentral Items
----------------------------------------
Every Webcrm Products will be synchronized with a Businesscentral Items.

Once a link between a Webcrm Products and a Businesscentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Products and a Businesscentral Items:

.. list-table::
   :header-rows: 1

   * - Webcrm Products Property
     - Businesscentral Items Property
     - Businesscentral Data Type
   * - ProductCostPrice
     - unitCost
     - N/A
   * - ProductPrice
     - unitPrice
     - N/A


Webcrm Quotationline to Businesscentral Salesorderlines
-------------------------------------------------------
Every Webcrm Quotationline will be synchronized with a Businesscentral Salesorderlines.

Once a link between a Webcrm Quotationline and a Businesscentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Quotationline and a Businesscentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Webcrm Quotationline Property
     - Businesscentral Salesorderlines Property
     - Businesscentral Data Type

