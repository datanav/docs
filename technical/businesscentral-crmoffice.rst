============================
Businesscentral to  Dataflow
============================

Generated: 2024-08-23 10:56:14

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Items to  Companies
-----------------------------------
Every Businesscentral Items will be synchronized with a  Companies.

Once a link between a Businesscentral Items and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Companies:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Companies Property
     -  Data Type


Businesscentral Customers company to  Companies
-----------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Companies.

Once a link between a Businesscentral Customers company and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Companies:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Companies Property
     -  Data Type
   * - city
     - postAddress.postalArea
     - "string"
   * - country
     - postAddress.country
     - "string"
   * - country
     - visitAddress.country
     - "string"
   * - postalCode
     - postAddress.postCode
     - "string"

