===========================
Wave Financial to  Dataflow
===========================

Generated: 2024-08-26 15:42:44

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to  Company
-------------------------
Every Wave Customer will be synchronized with a  Company.

Once a link between a Wave Customer and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Company:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Company Property
     -  Data Type


Wave Country to  Country
------------------------
Every Wave Country will be synchronized with a  Country.

Once a link between a Wave Country and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Country and a  Country:

.. list-table::
   :header-rows: 1

   * - Wave Country Property
     -  Country Property
     -  Data Type
   * - currency.code
     - currencyNo
     - "string"
   * - name
     - name
     - "string"

