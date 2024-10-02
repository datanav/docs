================================
Business Central to Wix Dataflow
================================

Generated: 2024-10-02 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Contacts (human data) to Wix Contacts
------------------------------------------------------
Every Business Central Contacts (human data) will be synchronized with a Wix Contacts.

Once a link between a Business Central Contacts (human data) and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts (human data) and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts (human data) Property
     - Wix Contacts Property
     - Wix Data Type
   * - email
     - primaryInfo.email
     - "string"
   * - phoneNumber
     - primaryInfo.phone
     - "string"


Business Central Items to Wix Products
--------------------------------------
Every Business Central Items will be synchronized with a Wix Products.

Once a link between a Business Central Items and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a Wix Products:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Wix Products Property
     - Wix Data Type
   * - displayName
     - name
     - "string"
   * - unitCost
     - costAndProfitData.itemCost
     - N/A
   * - unitPrice
     - priceData.price
     - N/A

