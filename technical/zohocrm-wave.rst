========================
ZohoCRM to Wave Dataflow
========================

Generated: 2024-06-30 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Contact to Wave Customer person
---------------------------------------
Every ZohoCRM Contact will be synchronized with a Wave Customer person.

Once a link between a ZohoCRM Contact and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Wave Customer person Property
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

