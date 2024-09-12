==================================
Salesforce to WooCommerce Dataflow
==================================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Order to WooCommerce Order
-------------------------------------
Every Salesforce Order will be synchronized with a WooCommerce Order.

Once a link between a Salesforce Order and a WooCommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a WooCommerce Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - WooCommerce Order Property
     - WooCommerce Data Type
   * - BillingCity
     - billing.city
     - "string"
   * - BillingCity
     - shipping.city
     - "string"
   * - BillingCountry
     - billing.country
     - "string"
   * - BillingCountry
     - shipping.country
     - "string"
   * - BillingPostalCode
     - billing.postcode
     - "string"
   * - BillingPostalCode
     - shipping.postcode
     - "string"
   * - BillingStreet
     - billing.address_1
     - "string"
   * - BillingStreet
     - shipping.address_1
     - "string"
   * - CurrencyIsoCode
     - currency
     - "string"
   * - ID
     - id
     - "string"
   * - ShippingCity
     - billing.city
     - "string"
   * - ShippingCity
     - shipping.city
     - "string"
   * - ShippingCountry
     - billing.country
     - "string"
   * - ShippingCountry
     - shipping.country
     - "string"
   * - ShippingStateCode
     - billing.postcode
     - "string"
   * - ShippingStateCode
     - shipping.postcode
     - "string"


Salesforce Product2 to WooCommerce Product
------------------------------------------
Every Salesforce Product2 will be synchronized with a WooCommerce Product.

Once a link between a Salesforce Product2 and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - WooCommerce Product Property
     - WooCommerce Data Type
   * - Name
     - name
     - "string"
   * - Name	
     - name
     - "string"
   * - ProductCode
     - status
     - "string"

