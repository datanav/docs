===============================
Wave Financial to Wave Dataflow
===============================

Generated: 2023-05-22 22:24:57

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Business to Wave Customer
------------------------------
Every Wave Business will be synchronized with a Wave Customer.

Once a link between a Wave Business and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Business and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Wave Business Property
     - Wave Customer Property
     - Wave Data Type
   * - address.addressLine1
     - address.addressLine1
     - "string"
   * - address.addressLine2
     - address.addressLine2
     - "string"
   * - address.city
     - address.city
     - "string"
   * - address.country
     - address.country.code
     - "string"
   * - address.postalCode
     - address.postalCode
     - "string"
   * - address.province
     - address.province
     - "string"
   * - fax
     - fax
     - "string"
   * - name
     - name
     - "string"
   * - phone
     - phone
     - "string"
   * - tollFree
     - tollFree
     - "string"
   * - website
     - website
     - "string"

