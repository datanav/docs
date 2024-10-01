====================================
Business Central to ZohoCRM Dataflow
====================================

Generated: 2024-10-01 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Companies to ZohoCRM Account
---------------------------------------------
Every Business Central Companies will be synchronized with a ZohoCRM Account.

Once a link between a Business Central Companies and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Companies and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Business Central Companies Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type


Business Central Customers (organisation data) to ZohoCRM Account
-----------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a ZohoCRM Account.

Once a link between a Business Central Customers (organisation data) and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
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
   * - displayName
     - Account_Name
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
   * - website
     - Website
     - "string"


Business Central Customers (human data) to ZohoCRM Contact
----------------------------------------------------------
Every Business Central Customers (human data) will be synchronized with a ZohoCRM Contact.

Once a link between a Business Central Customers (human data) and a ZohoCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (human data) and a ZohoCRM Contact:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (human data) Property
     - ZohoCRM Contact Property
     - ZohoCRM Data Type


Business Central Customers (human data) to ZohoCRM Contact
----------------------------------------------------------
Every Business Central Customers (human data) will be synchronized with a ZohoCRM Contact.

Once a link between a Business Central Customers (human data) and a ZohoCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (human data) and a ZohoCRM Contact:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (human data) Property
     - ZohoCRM Contact Property
     - ZohoCRM Data Type
   * - city
     - Mailing_City
     - "string"
   * - city
     - Other_City
     - "string"
   * - country
     - Mailing_Country
     - "string"
   * - country
     - Other_Country
     - "string"
   * - displayName
     - Full_Name
     - "string"
   * - email
     - Email
     - "string"
   * - email
     - Secondary_Email
     - "string"
   * - phoneNumber
     - Other_Phone
     - "string"
   * - phoneNumber
     - Phone
     - "string"
   * - postalCode
     - Mailing_Zip
     - "string"
   * - postalCode
     - Other_Zip
     - "string"

