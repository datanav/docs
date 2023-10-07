=============================
Tripletex to ZohoCRM Dataflow
=============================

Generated: 2023-10-07 10:32:41

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to ZohoCRM Account
-------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a ZohoCRM Account.

Once a link between a Tripletex Customer and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - deliveryAddress.city
     - Billing_City
     - "string"
   * - deliveryAddress.city
     - Shipping_City
     - "string"
   * - deliveryAddress.country.id
     - Billing_Country
     - "string"
   * - deliveryAddress.country.id
     - Shipping_Country
     - "string"
   * - deliveryAddress.postalCode
     - Billing_Code
     - "string"
   * - deliveryAddress.postalCode
     - Shipping_Code
     - "string"
   * - name
     - Account_Name
     - "string"
   * - phoneNumber
     - Phone
     - "string"
   * - phoneNumber
     - Rating
     - "string"
   * - physicalAddress.city
     - Billing_City
     - "string"
   * - physicalAddress.city
     - Shipping_City
     - "string"
   * - physicalAddress.country.id
     - Billing_Country
     - "string"
   * - physicalAddress.country.id
     - Shipping_Country
     - "string"
   * - physicalAddress.postalCode
     - Billing_Code
     - "string"
   * - physicalAddress.postalCode
     - Shipping_Code
     - "string"
   * - postalAddress.city
     - Billing_City
     - "string"
   * - postalAddress.city
     - Shipping_City
     - "string"
   * - postalAddress.country.id
     - Billing_Country
     - "string"
   * - postalAddress.country.id
     - Shipping_Country
     - "string"
   * - postalAddress.postalCode
     - Billing_Code
     - "string"
   * - postalAddress.postalCode
     - Shipping_Code
     - "string"

