======================
Webcrm to Wix Dataflow
======================

Generated: 2024-09-06 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Persons to Wix Contacts
------------------------------
Every Webcrm Persons will be synchronized with a Wix Contacts.

Once a link between a Webcrm Persons and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Persons and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Webcrm Persons Property
     - Wix Contacts Property
     - Wix Data Type
   * - PersonDirectPhone
     - primaryInfo.phone
     - "string"
   * - PersonFirstName
     - info.name.first
     - "string"
   * - PersonLastName
     - info.name.last
     - "string"


Webcrm Products to Wix Products
-------------------------------
Every Webcrm Products will be synchronized with a Wix Products.

Once a link between a Webcrm Products and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Products and a Wix Products:

.. list-table::
   :header-rows: 1

   * - Webcrm Products Property
     - Wix Products Property
     - Wix Data Type
   * - ProductCostPrice
     - costAndProfitData.itemCost
     - N/A
   * - ProductPrice
     - priceData.price
     - N/A

