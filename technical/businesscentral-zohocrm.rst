====================================
Business Central to ZohoCRM Dataflow
====================================

Generated: 2024-09-12 00:00:03

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


Business Central Customers company to ZohoCRM Account
-----------------------------------------------------
Every Business Central Customers company will be synchronized with a ZohoCRM Account.

Once a link between a Business Central Customers company and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - address.city
     - Billing_City
     - "string"
   * - address.city
     - Shipping_City
     - "string"
   * - address.countryLetterCode
     - Billing_Country
     - "string"
   * - address.countryLetterCode
     - Shipping_Country
     - "string"
   * - address.postalCode
     - Billing_Code
     - "string"
   * - address.postalCode
     - Shipping_Code
     - "string"
   * - address.street
     - Billing_Street
     - "string"
   * - address.street
     - Shipping_Street
     - "string"
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


Business Central Customers person to ZohoCRM Contact
----------------------------------------------------
Every Business Central Customers person will be synchronized with a ZohoCRM Contact.

Once a link between a Business Central Customers person and a ZohoCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a ZohoCRM Contact:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - ZohoCRM Contact Property
     - ZohoCRM Data Type
   * - address.city
     - Mailing_City
     - "string"
   * - address.city
     - Other_City
     - "string"
   * - address.postalCode
     - Mailing_Zip
     - "string"
   * - address.postalCode
     - Other_Zip
     - "string"
   * - address.street
     - Mailing_Street
     - "string"
   * - address.street
     - Other_Street
     - "string"
   * - addressLine1
     - Mailing_Street
     - "string"
   * - addressLine1
     - Other_Street
     - "string"
   * - addressLine2
     - Mailing_City
     - "string"
   * - addressLine2
     - Other_City
     - "string"
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
     - First_Name
     - "string"
   * - displayName
     - Full_Name
     - "string"
   * - displayName
     - Last_Name
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

