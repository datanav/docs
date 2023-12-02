============================
Businesscentral to  Dataflow
============================

Generated: 2023-12-02 00:00:00

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Items to  Product
---------------------------------
Every Businesscentral Items will be synchronized with a  Product.

Once a link between a Businesscentral Items and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Product:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Product Property
     -  Data Type
   * - displayName
     - name
     - "string"
   * - displayName.string
     - name
     - "string"
   * - unitPrice
     - unitPrice
     - "string"


Businesscentral Salesorders to  Invoice
---------------------------------------
Every Businesscentral Salesorders will be synchronized with a  Invoice.

Once a link between a Businesscentral Salesorders and a  Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a  Invoice:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     -  Invoice Property
     -  Data Type
   * - currencyId
     - currency.code
     - "string"
   * - customerId
     - customer.id
     - "string"

