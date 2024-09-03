===============================
Woocommerce to ZohoCRM Dataflow
===============================

Generated: 2024-09-03 08:16:35

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Woocommerce to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Woocommerce Customer to ZohoCRM Contact
---------------------------------------
Every Woocommerce Customer will be synchronized with a ZohoCRM Contact.

Once a link between a Woocommerce Customer and a ZohoCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Customer and a ZohoCRM Contact:

.. list-table::
   :header-rows: 1

   * - Woocommerce Customer Property
     - ZohoCRM Contact Property
     - ZohoCRM Data Type

