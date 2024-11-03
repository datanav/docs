===========================
SuperOffice to Wix Dataflow
===========================

Generated: 2024-11-03 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to Wix Contacts
----------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Wix Contacts must be established.

A new Wix Contacts will be created from a SuperOffice Person if it is connected to a SuperOffice Quoteline, or Quotealternative that is synchronized into Wix.

A SuperOffice Person will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Wix Contacts Property
   * - Emails.Value
     - primaryInfo.email

Once a link between a SuperOffice Person and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Wix Contacts Property
     - Wix Data Type
   * - Emails.Value
     - primaryInfo.email
     - "string"
   * - Firstname
     - info.name.first
     - "string"
   * - Lastname
     - info.name.last
     - "string"
   * - OfficePhones.Value
     - primaryInfo.phone
     - "string"


SuperOffice User to Wix Contacts
--------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a Wix Contacts must be established.

A SuperOffice User will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Wix Contacts Property
   * - personEmail
     - primaryInfo.email

Once a link between a SuperOffice User and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Wix Contacts Property
     - Wix Data Type
   * - firstName
     - info.name.first
     - "string"
   * - lastName
     - info.name.last
     - "string"
   * - personEmail
     - primaryInfo.email
     - "string"


SuperOffice Product to Wix Products
-----------------------------------
Every SuperOffice Product will be synchronized with a Wix Products.

Once a link between a SuperOffice Product and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Wix Products:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Wix Products Property
     - Wix Data Type
   * - ERPPriceListKey
     - priceData.currency
     - "string"
   * - Name
     - name
     - "string"
   * - UnitCost
     - costAndProfitData.itemCost
     - N/A
   * - UnitListPrice
     - priceData.price
     - N/A

