===============================
Businesscentral to Wix Dataflow
===============================

Generated: 2024-07-04 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Contacts person to Wix Contacts
-----------------------------------------------
Every Businesscentral Contacts person will be synchronized with a Wix Contacts.

Once a link between a Businesscentral Contacts person and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     - Wix Contacts Property
     - Wix Data Type
   * - displayName
     - info.name.first
     - "string"
   * - displayName
     - info.name.last
     - "string"
   * - email
     - primaryInfo.email
     - "string"
   * - mobilePhoneNumber
     - primaryInfo.phone
     - "string"
   * - phoneNumber
     - primaryInfo.phone
     - "string"


Businesscentral Items to Wix Products
-------------------------------------
Every Businesscentral Items will be synchronized with a Wix Products.

Once a link between a Businesscentral Items and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a Wix Products:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     - Wix Products Property
     - Wix Data Type
   * - displayName
     - name
     - "string"
   * - displayName.string
     - name
     - "string"
   * - displayName2
     - name
     - "string"
   * - unitCost
     - costAndProfitData.itemCost
     - N/A
   * - unitCost
     - costRange.maxValue
     - "string"
   * - unitPrice
     - priceData.price
     - N/A

