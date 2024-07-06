==================================
Wave Financial to ZohoCRM Dataflow
==================================

Generated: 2024-07-06 00:00:00

Introduction
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
   * - address.province.code
     - Billing_State
     - "string"
   * - address.province.code
     - Shipping_State
     - "string"
   * - fax
     - Fax
     - "string"
   * - id
     - Created_Time
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
   * - shippingDetails.address.province.code
     - Billing_State
     - "string"
   * - shippingDetails.address.province.code
     - Shipping_State
     - "string"
   * - shippingDetails.phone
     - Phone
     - "string"
   * - website
     - Website
     - "string"


Wave Customer person to ZohoCRM Contact
---------------------------------------
Every Wave Customer person will be synchronized with a ZohoCRM Contact.

Once a link between a Wave Customer person and a ZohoCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a ZohoCRM Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - ZohoCRM Contact Property
     - ZohoCRM Data Type
   * - address.city
     - Mailing_City
     - "string"
   * - address.city
     - Other_City
     - "string"
   * - address.city
     - Other_Country
     - "string"
   * - address.country.code
     - Mailing_Country
     - "string"
   * - address.country.code
     - Mailing_State
     - "string"
   * - address.country.code
     - Other_Country
     - "string"
   * - address.country.code
     - Other_State
     - "string"
   * - address.countryCode
     - Mailing_Country
     - "string"
   * - address.countryCode
     - Mailing_State
     - "string"
   * - address.countryCode
     - Other_Country
     - "string"
   * - address.countryCode
     - Other_State
     - "string"
   * - address.postalCode
     - Mailing_Country
     - "string"
   * - address.postalCode
     - Mailing_Zip
     - "string"
   * - address.postalCode
     - Other_Zip
     - "string"
   * - address.province
     - Mailing_State
     - "string"
   * - address.province
     - Other_State
     - "string"
   * - address.province.code
     - Mailing_State
     - "string"
   * - address.province.code
     - Other_State
     - "string"
   * - email
     - Email
     - "string"
   * - email
     - Secondary_Email
     - "string"
   * - firstName
     - First_Name
     - "string"
   * - firstName
     - Full_Name
     - "string"
   * - firstName
     - Last_Name
     - "string"
   * - lastName
     - First_Name
     - "string"
   * - lastName
     - Full_Name
     - "string"
   * - lastName
     - Last_Name
     - "string"
   * - mobile
     - Mobile
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
   * - phone
     - Other_Phone
     - "string"
   * - phone
     - Phone
     - "string"
   * - shippingDetails.address.city
     - Mailing_City
     - "string"
   * - shippingDetails.address.city
     - Other_City
     - "string"
   * - shippingDetails.address.city
     - Other_Country
     - "string"
   * - shippingDetails.address.country.code
     - Mailing_Country
     - "string"
   * - shippingDetails.address.country.code
     - Mailing_State
     - "string"
   * - shippingDetails.address.country.code
     - Other_Country
     - "string"
   * - shippingDetails.address.country.code
     - Other_State
     - "string"
   * - shippingDetails.address.postalCode
     - Mailing_Country
     - "string"
   * - shippingDetails.address.postalCode
     - Mailing_Zip
     - "string"
   * - shippingDetails.address.postalCode
     - Other_Zip
     - "string"
   * - shippingDetails.address.province
     - Mailing_State
     - "string"
   * - shippingDetails.address.province
     - Other_State
     - "string"
   * - shippingDetails.address.province.code
     - Mailing_State
     - "string"
   * - shippingDetails.address.province.code
     - Other_State
     - "string"
   * - shippingDetails.phone
     - Other_Phone
     - "string"
   * - shippingDetails.phone
     - Phone
     - "string"

