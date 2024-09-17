===========================
ZohoCRM to Shopify Dataflow
===========================

Generated: 2024-09-17 07:28:49

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Shopify Customer
-----------------------------------
Before any synchronization can take place, a link between a ZohoCRM Account and a Shopify Customer must be established.

A new Shopify Customer will be created from a ZohoCRM Account if it is connected to a ZohoCRM Deal that is synchronized into Shopify.

Once a link between a ZohoCRM Account and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Shopify Customer Property
     - Shopify Data Type
   * - Billing_City
     - default_address.city
     - "string"
   * - Billing_Code
     - default_address.zip
     - "string"
   * - Billing_Country
     - default_address.country
     - "string"
   * - Billing_State
     - default_address.province_code
     - "string"
   * - Shipping_City
     - default_address.city
     - "string"
   * - Shipping_Code
     - default_address.zip
     - "string"
   * - Shipping_Country
     - default_address.country
     - "string"
   * - Shipping_State
     - default_address.province_code
     - "string"


ZohoCRM Contact to Shopify Customer
-----------------------------------
Before any synchronization can take place, a link between a ZohoCRM Contact and a Shopify Customer must be established.

A new Shopify Customer will be created from a ZohoCRM Contact if it is connected to a ZohoCRM Deal that is synchronized into Shopify.

Once a link between a ZohoCRM Contact and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Shopify Customer Property
     - Shopify Data Type
   * - Email
     - email
     - "string"
   * - First_Name
     - first_name
     - "string"
   * - Last_Name
     - last_name
     - "string"
   * - Mailing_City
     - default_address.city
     - "string"
   * - Mailing_Country
     - default_address.country
     - "string"
   * - Mailing_State
     - default_address.province_code
     - "string"
   * - Mailing_Zip
     - default_address.zip
     - "string"
   * - Mobile
     - phone
     - "string"
   * - Other_City
     - default_address.city
     - "string"
   * - Other_Country
     - default_address.country
     - "string"
   * - Other_Phone
     - default_address.phone
     - "string"
   * - Other_State
     - default_address.province_code
     - "string"
   * - Other_Zip
     - default_address.zip
     - "string"
   * - Phone
     - default_address.phone
     - "string"
   * - Secondary_Email
     - email
     - "string"


ZohoCRM Contact to Shopify Customer
-----------------------------------
Every ZohoCRM Contact will be synchronized with a Shopify Customer.

Once a link between a ZohoCRM Contact and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Shopify Customer Property
     - Shopify Data Type


ZohoCRM Deal to Shopify Order
-----------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Shopify Order.

Once a link between a ZohoCRM Deal and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - Shopify Order Property
     - Shopify Data Type
   * - Account_Name.id
     - customer.id
     - "string"
   * - Amount
     - current_total_price
     - "string"
   * - Amount
     - total_price
     - "string"
   * - Contact_Name.id
     - customer.id
     - "string"
   * - Deal_Name
     - name
     - "string"

