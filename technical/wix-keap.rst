========================
Wix.com to Keap Dataflow
========================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Keap Contacts
---------------------------------
Every Wix.com Contacts will be synchronized with a Keap Contacts.

Once a link between a Wix.com Contacts and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Keap Contacts Property
     - Keap Data Type


Wix.com Products to Keap Product
--------------------------------
Every Wix.com Products will be synchronized with a Keap Product.

Once a link between a Wix.com Products and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Keap Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Keap Product Property
     - Keap Data Type
   * - name
     - product_name
     - "string"
   * - priceData.price
     - product_price
     - "string"

