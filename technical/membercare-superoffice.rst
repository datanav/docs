==================================
Membercare to Superoffice Dataflow
==================================

Generated: 2024-09-03 13:28:36

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Membercare to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Membercare Companies to Superoffice Contact
-------------------------------------------
Every Membercare Companies will be synchronized with a Superoffice Contact.

Once a link between a Membercare Companies and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - companyName
     - Name
     - "string"
   * - url
     - Urls.Value
     - "string"


Membercare Invoices to Superoffice Quoteline
--------------------------------------------
Every Membercare Invoices will be synchronized with a Superoffice Quoteline.

Once a link between a Membercare Invoices and a Superoffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Invoices and a Superoffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Membercare Invoices Property
     - Superoffice Quoteline Property
     - Superoffice Data Type

