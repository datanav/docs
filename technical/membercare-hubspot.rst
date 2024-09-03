==============================
Membercare to Hubspot Dataflow
==============================

Generated: 2024-09-03 13:28:36

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Membercare to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Membercare Companies to Hubspot Company
---------------------------------------
Every Membercare Companies will be synchronized with a Hubspot Company.

Once a link between a Membercare Companies and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - companyName
     - properties.name
     - "string"
   * - url
     - properties.website
     - "string"


Membercare Invoices to Hubspot Lineitem
---------------------------------------
Every Membercare Invoices will be synchronized with a Hubspot Lineitem.

Once a link between a Membercare Invoices and a Hubspot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Invoices and a Hubspot Lineitem:

.. list-table::
   :header-rows: 1

   * - Membercare Invoices Property
     - Hubspot Lineitem Property
     - Hubspot Data Type

