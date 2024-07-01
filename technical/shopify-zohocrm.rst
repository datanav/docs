===========================
Shopify to ZohoCRM Dataflow
===========================

Generated: 2024-07-01 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to ZohoCRM Contact
-----------------------------------
Every Shopify Customer will be synchronized with a ZohoCRM Contact.

Once a link between a Shopify Customer and a ZohoCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a ZohoCRM Contact:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - ZohoCRM Contact Property
     - ZohoCRM Data Type
   * - addresses.city
     - Mailing_City
     - "string"
   * - addresses.city
     - Other_City
     - "string"
   * - addresses.country
     - Mailing_Country
     - "string"
   * - addresses.country
     - Other_Country
     - "string"
   * - addresses.province_code
     - Mailing_State
     - "string"
   * - addresses.province_code
     - Other_State
     - "string"
   * - addresses.zip
     - Mailing_Zip
     - "string"
   * - addresses.zip
     - Other_Zip
     - "string"
   * - email
     - Email
     - "string"
   * - email
     - Secondary_Email
     - "string"
   * - phone
     - Other_Phone
     - "string"
   * - phone
     - Phone
     - "string"

