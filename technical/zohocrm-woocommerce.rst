===============================
ZohoCRM to WooCommerce Dataflow
===============================

Generated: 2024-09-22 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Deal to WooCommerce Order
---------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a WooCommerce Order.

Once a link between a ZohoCRM Deal and a WooCommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a WooCommerce Order:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - WooCommerce Order Property
     - WooCommerce Data Type
   * - Account_Name.id
     - customer_id
     - "string"
   * - Contact_Name.id
     - customer_id
     - "string"

