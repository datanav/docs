==================================
Wave Financial to ZohoCRM Dataflow
==================================

Generated: 2023-10-07 10:32:41

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
   * - address.city
     - Billing_City
     - "string"
   * - address.city
     - Shipping_City
     - "string"
   * - address.country.code
     - Billing_Country
     - "string"
   * - address.country.code
     - Shipping_Country
     - "string"
   * - address.countryCode
     - Billing_Country
     - "string"
   * - address.countryCode
     - Shipping_Country
     - "string"
   * - address.postalCode
     - Billing_Code
     - "string"
   * - address.postalCode
     - Shipping_Code
     - "string"
   * - fax
     - Fax
     - "string"
   * - internalNotes
     - Created_Time
     - "string"
   * - name
     - Account_Name
     - "string"
   * - phone
     - Phone
     - "string"
   * - phone
     - Rating
     - "string"
   * - shippingDetails.address.city
     - Billing_City
     - "string"
   * - shippingDetails.address.city
     - Shipping_City
     - "string"
   * - shippingDetails.address.country.code
     - Billing_Country
     - "string"
   * - shippingDetails.address.country.code
     - Shipping_Country
     - "string"
   * - shippingDetails.address.postalCode
     - Billing_Code
     - "string"
   * - shippingDetails.address.postalCode
     - Shipping_Code
     - "string"
   * - shippingDetails.phone
     - Phone
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

