===========================
ZohoCRM to Shopify Dataflow
===========================

Generated: 2024-09-12 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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
     - addresses.city
     - "string"
   * - Mailing_City
     - default_address.city
     - "string"
   * - Mailing_Country
     - addresses.country
     - "string"
   * - Mailing_Country
     - default_address.country
     - "string"
   * - Mailing_State
     - addresses.province_code
     - "string"
   * - Mailing_State
     - default_address.province_code
     - "string"
   * - Mailing_Zip
     - addresses.zip
     - "string"
   * - Mailing_Zip
     - default_address.zip
     - "string"
   * - Mobile
     - phone
     - "string"
   * - Other_City
     - addresses.city
     - "string"
   * - Other_City
     - default_address.city
     - "string"
   * - Other_Country
     - addresses.country
     - "string"
   * - Other_Country
     - default_address.country
     - "string"
   * - Other_Phone
     - default_address.phone
     - "string"
   * - Other_Phone
     - phone
     - "string"
   * - Other_State
     - addresses.province_code
     - "string"
   * - Other_State
     - default_address.province_code
     - "string"
   * - Other_Zip
     - addresses.zip
     - "string"
   * - Other_Zip
     - default_address.zip
     - "string"
   * - Phone
     - default_address.phone
     - "string"
   * - Phone
     - phone
     - "string"
   * - Secondary_Email
     - email
     - "string"
   * - id
     - id
     - "string"

