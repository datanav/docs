==================================
Wave Financial to ZohoCRM Dataflow
==================================

Generated: 2023-10-07 10:23:22

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to ZohoCRM Account
--------------------------------
Every Wave Customer will be synchronized with a ZohoCRM Account.

Once a link between a Wave Customer and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - fax
     - Fax
     - "string"
   * - name
     - Account_Name
     - "string"
   * - phone
     - Rating
     - "string"
   * - shippingDetails.phone
     - Rating
     - "string"
   * - tollFree
     - Phone
     - "string"
   * - website
     - Website
     - "string"

