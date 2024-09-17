========================
ZohoCRM to Wave Dataflow
========================

Generated: 2024-09-17 07:28:49

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Wave Customer person
---------------------------------------
Before any synchronization can take place, a link between a ZohoCRM Account and a Wave Customer person must be established.

A new Wave Customer person will be created from a ZohoCRM Account if it is connected to a ZohoCRM Deal that is synchronized into Wave.

Once a link between a ZohoCRM Account and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Wave Customer person Property
     - Wave Data Type
   * - Billing_City
     - address.city
     - "string"
   * - Billing_City
     - shippingDetails.address.city
     - "string"
   * - Billing_Code
     - address.postalCode
     - "string"
   * - Billing_Code
     - shippingDetails.address.postalCode
     - "string"
   * - Billing_Country
     - address.country.code
     - "string"
   * - Billing_Country
     - shippingDetails.address.country.code
     - "string"
   * - Billing_State
     - address.province.code
     - "string"
   * - Billing_State
     - shippingDetails.address.province.code
     - "string"
   * - Shipping_City
     - address.city
     - "string"
   * - Shipping_City
     - shippingDetails.address.city
     - "string"
   * - Shipping_Code
     - address.postalCode
     - "string"
   * - Shipping_Code
     - shippingDetails.address.postalCode
     - "string"
   * - Shipping_Country
     - address.country.code
     - "string"
   * - Shipping_Country
     - shippingDetails.address.country.code
     - "string"
   * - Shipping_State
     - address.province.code
     - "string"
   * - Shipping_State
     - shippingDetails.address.province.code
     - "string"


ZohoCRM Account to Wave Customer
--------------------------------
Before any synchronization can take place, a link between a ZohoCRM Account and a Wave Customer must be established.

A new Wave Customer will be created from a ZohoCRM Account if it is connected to a ZohoCRM Deal that is synchronized into Wave.

Once a link between a ZohoCRM Account and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Wave Customer Property
     - Wave Data Type
   * - Account_Name
     - name
     - N/A
   * - Billing_City
     - address.city
     - "string"
   * - Billing_City
     - shippingDetails.address.city
     - "string"
   * - Billing_Code
     - address.postalCode
     - "string"
   * - Billing_Code
     - shippingDetails.address.postalCode
     - "string"
   * - Billing_Country
     - address.country.code
     - "string"
   * - Billing_Country
     - shippingDetails.address.country.code
     - "string"
   * - Billing_State
     - address.province.code
     - "string"
   * - Billing_State
     - shippingDetails.address.province.code
     - "string"
   * - Created_Time
     - internalNotes
     - "string"
   * - Fax
     - fax
     - "string"
   * - Phone
     - phone
     - "string"
   * - Shipping_City
     - address.city
     - "string"
   * - Shipping_City
     - shippingDetails.address.city
     - "string"
   * - Shipping_Code
     - address.postalCode
     - "string"
   * - Shipping_Code
     - shippingDetails.address.postalCode
     - "string"
   * - Shipping_Country
     - address.country.code
     - "string"
   * - Shipping_Country
     - shippingDetails.address.country.code
     - "string"
   * - Shipping_State
     - address.province.code
     - "string"
   * - Shipping_State
     - shippingDetails.address.province.code
     - "string"
   * - Website
     - website
     - "string"


ZohoCRM Contact to Wave Customer person
---------------------------------------
Before any synchronization can take place, a link between a ZohoCRM Contact and a Wave Customer person must be established.

A new Wave Customer person will be created from a ZohoCRM Contact if it is connected to a ZohoCRM Deal that is synchronized into Wave.

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


ZohoCRM Contact to Wave Customer
--------------------------------
Before any synchronization can take place, a link between a ZohoCRM Contact and a Wave Customer must be established.

A new Wave Customer will be created from a ZohoCRM Contact if it is connected to a ZohoCRM Deal that is synchronized into Wave.

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

