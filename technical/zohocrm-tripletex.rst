=============================
ZohoCRM to Tripletex Dataflow
=============================

Generated: 2024-09-17 07:28:49

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Tripletex Contact
------------------------------------
Before any synchronization can take place, a link between a ZohoCRM Account and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a ZohoCRM Account if it is connected to a ZohoCRM Deal that is synchronized into Tripletex.

Once a link between a ZohoCRM Account and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Tripletex Contact Property
     - Tripletex Data Type


ZohoCRM Account to Tripletex Customer person
--------------------------------------------
Before any synchronization can take place, a link between a ZohoCRM Account and a Tripletex Customer person must be established.

A new Tripletex Customer person will be created from a ZohoCRM Account if it is connected to a ZohoCRM Deal that is synchronized into Tripletex.

Once a link between a ZohoCRM Account and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Tripletex Customer person Property
     - Tripletex Data Type
   * - Billing_City
     - deliveryAddress.city
     - "string"
   * - Billing_City
     - physicalAddress.city
     - "string"
   * - Billing_City
     - postalAddress.city
     - "string"
   * - Billing_Code
     - deliveryAddress.postalCode
     - "string"
   * - Billing_Code
     - physicalAddress.postalCode
     - "string"
   * - Billing_Code
     - postalAddress.postalCode
     - "string"
   * - Billing_Country
     - deliveryAddress.country.id
     - "string"
   * - Billing_Country
     - physicalAddress.country.id
     - "integer"
   * - Billing_Country
     - postalAddress.country.id
     - "integer"
   * - Shipping_City
     - deliveryAddress.city
     - "string"
   * - Shipping_City
     - physicalAddress.city
     - "string"
   * - Shipping_City
     - postalAddress.city
     - "string"
   * - Shipping_Code
     - deliveryAddress.postalCode
     - "string"
   * - Shipping_Code
     - physicalAddress.postalCode
     - "string"
   * - Shipping_Code
     - postalAddress.postalCode
     - "string"
   * - Shipping_Country
     - deliveryAddress.country.id
     - "string"
   * - Shipping_Country
     - physicalAddress.country.id
     - "integer"
   * - Shipping_Country
     - postalAddress.country.id
     - "integer"
   * - id
     - id
     - "integer"


ZohoCRM Account to Tripletex Customer
-------------------------------------
Before any synchronization can take place, a link between a ZohoCRM Account and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a ZohoCRM Account if it is connected to a ZohoCRM Deal that is synchronized into Tripletex.

Once a link between a ZohoCRM Account and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - Account_Name
     - name
     - "string"
   * - Billing_City
     - deliveryAddress.city
     - "string"
   * - Billing_City
     - physicalAddress.city
     - "string"
   * - Billing_City
     - postalAddress.city
     - "string"
   * - Billing_Code
     - deliveryAddress.postalCode
     - "string"
   * - Billing_Code
     - physicalAddress.postalCode
     - "string"
   * - Billing_Code
     - postalAddress.postalCode
     - "string"
   * - Billing_Country
     - deliveryAddress.country.id
     - "string"
   * - Billing_Country
     - physicalAddress.country.id
     - "integer"
   * - Billing_Country
     - postalAddress.country.id
     - "integer"
   * - Phone
     - phoneNumber
     - "string"
   * - Shipping_City
     - deliveryAddress.city
     - "string"
   * - Shipping_City
     - physicalAddress.city
     - "string"
   * - Shipping_City
     - postalAddress.city
     - "string"
   * - Shipping_Code
     - deliveryAddress.postalCode
     - "string"
   * - Shipping_Code
     - physicalAddress.postalCode
     - "string"
   * - Shipping_Code
     - postalAddress.postalCode
     - "string"
   * - Shipping_Country
     - deliveryAddress.country.id
     - "string"
   * - Shipping_Country
     - physicalAddress.country.id
     - "integer"
   * - Shipping_Country
     - postalAddress.country.id
     - "integer"
   * - Website
     - website
     - "string"
   * - id
     - id
     - "integer"


ZohoCRM Contact to Tripletex Contact
------------------------------------
Before any synchronization can take place, a link between a ZohoCRM Contact and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a ZohoCRM Contact if it is connected to a ZohoCRM Deal that is synchronized into Tripletex.

Once a link between a ZohoCRM Contact and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - Email
     - email
     - "string"
   * - First_Name
     - firstName
     - "string"
   * - Last_Name
     - lastName
     - "string"
   * - Mobile
     - phoneNumberMobile
     - N/A
   * - Other_Phone
     - phoneNumberWork
     - "string"
   * - Phone
     - phoneNumberWork
     - "string"
   * - Secondary_Email
     - email
     - "string"


ZohoCRM Contact to Tripletex Customer person
--------------------------------------------
Before any synchronization can take place, a link between a ZohoCRM Contact and a Tripletex Customer person must be established.

A new Tripletex Customer person will be created from a ZohoCRM Contact if it is connected to a ZohoCRM Deal that is synchronized into Tripletex.

Once a link between a ZohoCRM Contact and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Tripletex Customer person Property
     - Tripletex Data Type
   * - Email
     - email
     - "string"
   * - Full_Name
     - name
     - "string"
   * - Mailing_City
     - deliveryAddress.city
     - "string"
   * - Mailing_City
     - physicalAddress.city
     - "string"
   * - Mailing_City
     - postalAddress.city
     - "string"
   * - Mailing_Country
     - deliveryAddress.country.id
     - "string"
   * - Mailing_Country
     - physicalAddress.country.id
     - "integer"
   * - Mailing_Country
     - postalAddress.country.id
     - "integer"
   * - Mailing_Zip
     - deliveryAddress.postalCode
     - "string"
   * - Mailing_Zip
     - physicalAddress.postalCode
     - "string"
   * - Mailing_Zip
     - postalAddress.postalCode
     - "string"
   * - Mobile
     - phoneNumberMobile
     - "string"
   * - Other_City
     - deliveryAddress.city
     - "string"
   * - Other_City
     - physicalAddress.city
     - "string"
   * - Other_City
     - postalAddress.city
     - "string"
   * - Other_Country
     - deliveryAddress.country.id
     - "string"
   * - Other_Country
     - physicalAddress.country.id
     - "integer"
   * - Other_Country
     - postalAddress.country.id
     - "integer"
   * - Other_Phone
     - phoneNumber
     - "string"
   * - Other_Zip
     - deliveryAddress.postalCode
     - "string"
   * - Other_Zip
     - physicalAddress.postalCode
     - "string"
   * - Other_Zip
     - postalAddress.postalCode
     - "string"
   * - Phone
     - phoneNumber
     - "string"
   * - Secondary_Email
     - email
     - "string"
   * - id
     - id
     - "integer"


ZohoCRM Contact to Tripletex Customer
-------------------------------------
Before any synchronization can take place, a link between a ZohoCRM Contact and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a ZohoCRM Contact if it is connected to a ZohoCRM Deal that is synchronized into Tripletex.

Once a link between a ZohoCRM Contact and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - Mailing_City
     - deliveryAddress.city
     - "string"
   * - Mailing_City
     - physicalAddress.city
     - "string"
   * - Mailing_City
     - postalAddress.city
     - "string"
   * - Mailing_Country
     - deliveryAddress.country.id
     - "string"
   * - Mailing_Country
     - physicalAddress.country.id
     - "integer"
   * - Mailing_Country
     - postalAddress.country.id
     - "integer"
   * - Mailing_Zip
     - deliveryAddress.postalCode
     - "string"
   * - Mailing_Zip
     - physicalAddress.postalCode
     - "string"
   * - Mailing_Zip
     - postalAddress.postalCode
     - "string"
   * - Other_City
     - deliveryAddress.city
     - "string"
   * - Other_City
     - physicalAddress.city
     - "string"
   * - Other_City
     - postalAddress.city
     - "string"
   * - Other_Country
     - deliveryAddress.country.id
     - "string"
   * - Other_Country
     - physicalAddress.country.id
     - "integer"
   * - Other_Country
     - postalAddress.country.id
     - "integer"
   * - Other_Zip
     - deliveryAddress.postalCode
     - "string"
   * - Other_Zip
     - physicalAddress.postalCode
     - "string"
   * - Other_Zip
     - postalAddress.postalCode
     - "string"
   * - id
     - id
     - "integer"


ZohoCRM Contact to Tripletex Customer
-------------------------------------
Every ZohoCRM Contact will be synchronized with a Tripletex Customer.

Once a link between a ZohoCRM Contact and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Tripletex Customer Property
     - Tripletex Data Type


ZohoCRM Contact to Tripletex Customer person
--------------------------------------------
Every ZohoCRM Contact will be synchronized with a Tripletex Customer person.

Once a link between a ZohoCRM Contact and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Tripletex Customer person Property
     - Tripletex Data Type


ZohoCRM Deal to Tripletex Order
-------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Tripletex Order.

Once a link between a ZohoCRM Deal and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - Account_Name.id
     - contact.id
     - "integer"
   * - Account_Name.id
     - customer.id
     - "integer"
   * - Closing_Date
     - orderDate
     - N/A
   * - Contact_Name.id
     - contact.id
     - "integer"
   * - Contact_Name.id
     - customer.id
     - "integer"

