==============================
Shopify to Custom HRM Dataflow
==============================

Generated: 2024-09-11 11:39:33

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Custom HRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to CustomHRM Employee
--------------------------------------
Every Shopify Customer will be synchronized with a CustomHRM Employee.

Once a link between a Shopify Customer and a CustomHRM Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a CustomHRM Employee:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - CustomHRM Employee Property
     - CustomHRM Data Type

