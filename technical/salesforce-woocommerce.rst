==================================
Salesforce to Woocommerce Dataflow
==================================

Generated: 2024-09-10 00:00:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Woocommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Order to Woocommerce Order
-------------------------------------
Every Salesforce Order will be synchronized with a Woocommerce Order.

Once a link between a Salesforce Order and a Woocommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Woocommerce Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Woocommerce Order Property
     - Woocommerce Data Type
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


Salesforce Product2 to Woocommerce Product
------------------------------------------
Every Salesforce Product2 will be synchronized with a Woocommerce Product.

Once a link between a Salesforce Product2 and a Woocommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Woocommerce Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Woocommerce Product Property
     - Woocommerce Data Type
   * - Name
     - name
     - "string"
   * - Name	
     - name
     - "string"

