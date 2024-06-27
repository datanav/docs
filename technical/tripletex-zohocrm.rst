=============================
Tripletex to ZohoCRM Dataflow
=============================

Generated: 2024-06-27 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to ZohoCRM Account
-------------------------------------
Every Tripletex Customer will be synchronized with a ZohoCRM Account.

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
   * - url
     - Website
     - "string"
   * - website
     - Website
     - "string"


Tripletex Department to ZohoCRM Account
---------------------------------------
Every Tripletex Department will be synchronized with a ZohoCRM Account.

Once a link between a Tripletex Department and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - name
     - Account_Name
     - "string"


Tripletex Customer person to ZohoCRM Contact
--------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a ZohoCRM Contact.

Once a link between a Tripletex Customer person and a ZohoCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a ZohoCRM Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - ZohoCRM Contact Property
     - ZohoCRM Data Type
   * - deliveryAddress.city
     - Mailing_City
     - "string"
   * - deliveryAddress.city
     - Other_City
     - "string"
   * - deliveryAddress.country.id
     - Mailing_Country
     - "string"
   * - deliveryAddress.country.id
     - Other_Country
     - "string"
   * - deliveryAddress.postalCode
     - Mailing_Zip
     - "string"
   * - deliveryAddress.postalCode
     - Other_Zip
     - "string"
   * - email
     - Email
     - "string"
   * - email
     - Secondary_Email
     - "string"
   * - name
     - First_Name
     - "string"
   * - name
     - Full_Name
     - "string"
   * - name
     - Last_Name
     - "string"
   * - phoneNumber
     - Other_Phone
     - "string"
   * - phoneNumber
     - Phone
     - "string"
   * - phoneNumberMobile
     - Mobile
     - "string"
   * - physicalAddress.city
     - Mailing_City
     - "string"
   * - physicalAddress.city
     - Other_City
     - "string"
   * - physicalAddress.country.id
     - Mailing_Country
     - "string"
   * - physicalAddress.country.id
     - Other_Country
     - "string"
   * - physicalAddress.postalCode
     - Mailing_Zip
     - "string"
   * - physicalAddress.postalCode
     - Other_Zip
     - "string"
   * - postalAddress.city
     - Mailing_City
     - "string"
   * - postalAddress.city
     - Other_City
     - "string"
   * - postalAddress.country.id
     - Mailing_Country
     - "string"
   * - postalAddress.country.id
     - Other_Country
     - "string"
   * - postalAddress.postalCode
     - Mailing_Zip
     - "string"
   * - postalAddress.postalCode
     - Other_Zip
     - "string"

