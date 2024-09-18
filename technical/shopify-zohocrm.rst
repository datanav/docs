===========================
Shopify to ZohoCRM Dataflow
===========================

Generated: 2024-09-18 00:00:26

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to ZohoCRM Contact
-----------------------------------
Every Shopify Customer will be synchronized with a ZohoCRM Contact.

Once a link between a Shopify Customer and a ZohoCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a ZohoCRM Contact:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - ZohoCRM Contact Property
     - ZohoCRM Data Type

