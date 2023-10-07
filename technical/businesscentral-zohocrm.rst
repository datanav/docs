===================================
Businesscentral to ZohoCRM Dataflow
===================================

Generated: 2023-10-07 10:40:10

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Company to ZohoCRM Account
------------------------------------------
Every Businesscentral Company will be synchronized with a ZohoCRM Account.

Once a link between a Businesscentral Company and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Company and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Businesscentral Company Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type


Businesscentral Contact company to ZohoCRM Account
--------------------------------------------------
Every Businesscentral Contact company will be synchronized with a ZohoCRM Account.

Once a link between a Businesscentral Contact company and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contact company and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contact company Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - city
     - Billing_City
     - "string"
   * - city
     - Shipping_City
     - "string"
   * - country
     - Billing_Country
     - "string"
   * - country
     - Shipping_Country
     - "string"
   * - phoneNumber
     - Phone
     - "string"
   * - postalCode
     - Billing_Code
     - "string"
   * - postalCode
     - Shipping_Code
     - "string"

