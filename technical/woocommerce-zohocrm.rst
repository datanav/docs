===============================
WooCommerce to ZohoCRM Dataflow
===============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Customer to ZohoCRM Contact
---------------------------------------
Every WooCommerce Customer will be synchronized with a ZohoCRM Contact.

Once a link between a WooCommerce Customer and a ZohoCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a ZohoCRM Contact:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - ZohoCRM Contact Property
     - ZohoCRM Data Type
   * - billing.city
     - Mailing_City
     - "string"
   * - billing.city
     - Other_City
     - "string"
   * - billing.country
     - Mailing_Country
     - "string"
   * - billing.country
     - Other_Country
     - "string"
   * - billing.postcode
     - Mailing_Zip
     - "string"
   * - billing.postcode
     - Other_Zip
     - "string"
   * - billing.state
     - Mailing_State
     - "string"
   * - billing.state
     - Other_State
     - "string"
   * - email
     - Email
     - "string"
   * - email
     - Secondary_Email
     - "string"
   * - last_name
     - Last_Name
     - "string"
   * - shipping.city
     - Mailing_City
     - "string"
   * - shipping.city
     - Other_City
     - "string"
   * - shipping.country
     - Mailing_Country
     - "string"
   * - shipping.country
     - Other_Country
     - "string"
   * - shipping.postcode
     - Mailing_Zip
     - "string"
   * - shipping.postcode
     - Other_Zip
     - "string"
   * - shipping.state
     - Mailing_State
     - "string"
   * - shipping.state
     - Other_State
     - "string"

