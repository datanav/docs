============================
Businesscentral to  Dataflow
============================

Generated: 2024-03-26 00:00:01

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Contacts person to  Contacts
--------------------------------------------
Every Businesscentral Contacts person will be synchronized with a  Contacts.

Once a link between a Businesscentral Contacts person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     -  Contacts Property
     -  Data Type
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


Businesscentral Items to  Products
----------------------------------
Every Businesscentral Items will be synchronized with a  Products.

Once a link between a Businesscentral Items and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Products:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Products Property
     -  Data Type
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
     - "decimal"
   * - unitCost
     - costRange.maxValue
     - "string"
   * - unitPrice
     - priceData.price
     - "decimal"

