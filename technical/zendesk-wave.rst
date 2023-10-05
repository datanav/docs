========================
Zendesk to Wave Dataflow
========================

Generated: 2023-10-05 06:14:44

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organisations to Wave Customer
--------------------------------------
Every Zendesk Organisations will be synchronized with a Wave Customer.

Once a link between a Zendesk Organisations and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organisations and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Zendesk Organisations Property
     - Wave Customer Property
     - Wave Data Type
   * - name
     - name
     - "string"
   * - url
     - website
     - "string"


Zendesk Users to Wave Customer
------------------------------
Every Zendesk Users will be synchronized with a Wave Customer.

Once a link between a Zendesk Users and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Wave Customer Property
     - Wave Data Type

