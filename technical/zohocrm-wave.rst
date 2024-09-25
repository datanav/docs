========================
ZohoCRM to Wave Dataflow
========================

Generated: 2024-09-25 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Contact to Wave Customer
--------------------------------
Every ZohoCRM Contact will be synchronized with a Wave Customer.

Once a link between a ZohoCRM Contact and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Wave Customer Property
     - Wave Data Type
   * - Email
     - email
     - "string"
   * - First_Name
     - firstName
     - "string"
   * - Last_Name
     - lastName
     - "string"
   * - Mailing_City
     - address.city
     - "string"
   * - Mailing_City
     - shippingDetails.address.city
     - "string"
   * - Mailing_Country
     - address.country.code
     - "string"
   * - Mailing_Country
     - shippingDetails.address.country.code
     - "string"
   * - Mailing_State
     - address.province.code
     - "string"
   * - Mailing_State
     - shippingDetails.address.province.code
     - "string"
   * - Mailing_Zip
     - address.postalCode
     - "string"
   * - Mailing_Zip
     - shippingDetails.address.postalCode
     - "string"
   * - Mobile
     - mobile
     - "string"
   * - Other_City
     - address.city
     - "string"
   * - Other_City
     - shippingDetails.address.city
     - "string"
   * - Other_Country
     - address.country.code
     - "string"
   * - Other_Country
     - shippingDetails.address.country.code
     - "string"
   * - Other_State
     - address.province.code
     - "string"
   * - Other_State
     - shippingDetails.address.province.code
     - "string"
   * - Other_Zip
     - address.postalCode
     - "string"
   * - Other_Zip
     - shippingDetails.address.postalCode
     - "string"
   * - Secondary_Email
     - email
     - "string"


ZohoCRM Contact to Wave Customer (human data)
---------------------------------------------
Every ZohoCRM Contact will be synchronized with a Wave Customer (human data).

Once a link between a ZohoCRM Contact and a Wave Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Wave Customer (human data):

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Wave Customer (human data) Property
     - Wave Data Type
   * - Email
     - email
     - "string"
   * - First_Name
     - firstName
     - "string"
   * - Full_Name
     - name
     - N/A
   * - Last_Name
     - lastName
     - N/A
   * - Mailing_City
     - address.city
     - "string"
   * - Mailing_City
     - shippingDetails.address.city
     - "string"
   * - Mailing_Country
     - address.country.code
     - "string"
   * - Mailing_Country
     - shippingDetails.address.country.code
     - "string"
   * - Mailing_State
     - address.province.code
     - "string"
   * - Mailing_State
     - shippingDetails.address.province.code
     - "string"
   * - Mailing_Zip
     - address.postalCode
     - "string"
   * - Mailing_Zip
     - shippingDetails.address.postalCode
     - "string"
   * - Mobile
     - mobile
     - "string"
   * - Other_City
     - address.city
     - "string"
   * - Other_City
     - shippingDetails.address.city
     - "string"
   * - Other_Country
     - address.country.code
     - "string"
   * - Other_Country
     - shippingDetails.address.country.code
     - "string"
   * - Other_Phone
     - phone
     - "string"
   * - Other_State
     - address.province.code
     - "string"
   * - Other_State
     - shippingDetails.address.province.code
     - "string"
   * - Other_Zip
     - address.postalCode
     - "string"
   * - Other_Zip
     - shippingDetails.address.postalCode
     - "string"
   * - Phone
     - phone
     - "string"
   * - Secondary_Email
     - email
     - "string"


ZohoCRM Deal to Wave Invoice
----------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Wave Invoice.

Once a link between a ZohoCRM Deal and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - Wave Invoice Property
     - Wave Data Type
   * - Account_Name.id
     - customer.id
     - "string"
   * - Contact_Name.id
     - customer.id
     - "string"
   * - Deal_Name
     - title
     - "string"

