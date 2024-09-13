===============================
ZohoCRM to SuperOffice Dataflow
===============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to SuperOffice Contact
--------------------------------------
Every ZohoCRM Account will be synchronized with a SuperOffice Contact.

Once a link between a ZohoCRM Account and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - Account_Name
     - Name
     - "string"
   * - Billing_City
     - Address.Postal.City
     - "string"
   * - Billing_City
     - Address.Street.City
     - "string"
   * - Billing_Code
     - Address.Postal.Zipcode
     - "string"
   * - Billing_Code
     - Address.Street.Zipcode
     - "string"
   * - Billing_Country
     - Country.CountryId
     - "integer"
   * - Phone
     - Phones.Value
     - "string"
   * - Shipping_City
     - Address.Postal.City
     - "string"
   * - Shipping_City
     - Address.Street.City
     - "string"
   * - Shipping_Code
     - Address.Postal.Zipcode
     - "string"
   * - Shipping_Code
     - Address.Street.Zipcode
     - "string"
   * - Shipping_Country
     - Country.CountryId
     - "integer"
   * - Website
     - Urls.Value
     - "string"
   * - id
     - ContactId
     - "integer"


ZohoCRM Account to SuperOffice Person
-------------------------------------
Before any synchronization can take place, a link between a ZohoCRM Account and a SuperOffice Person must be established.

A new SuperOffice Person will be created from a ZohoCRM Account if it is connected to a ZohoCRM Deal that is synchronized into SuperOffice.

Once a link between a ZohoCRM Account and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - SuperOffice Person Property
     - SuperOffice Data Type


ZohoCRM Contact to SuperOffice Contact
--------------------------------------
Before any synchronization can take place, a link between a ZohoCRM Contact and a SuperOffice Contact must be established.

A new SuperOffice Contact will be created from a ZohoCRM Contact if it is connected to a ZohoCRM Deal that is synchronized into SuperOffice.

Once a link between a ZohoCRM Contact and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - SuperOffice Contact Property
     - SuperOffice Data Type


ZohoCRM Contact to SuperOffice Person
-------------------------------------
Every ZohoCRM Contact will be synchronized with a SuperOffice Person.

Once a link between a ZohoCRM Contact and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - Email
     - Emails.Value
     - "string"
   * - First_Name
     - Firstname
     - "string"
   * - Home_Phone
     - PrivatePhones.Value
     - "string"
   * - Last_Name
     - Lastname
     - "string"
   * - Mailing_City
     - Address.Street.City
     - "string"
   * - Mailing_Country
     - Country.CountryId
     - "integer"
   * - Mailing_Zip
     - Address.Street.Zipcode
     - "string"
   * - Mobile
     - MobilePhones.Value
     - "string"
   * - Other_City
     - Address.Street.City
     - "string"
   * - Other_Country
     - Country.CountryId
     - "integer"
   * - Other_Phone
     - OfficePhones.Value
     - "string"
   * - Other_Zip
     - Address.Street.Zipcode
     - "string"
   * - Phone
     - OfficePhones.Value
     - "string"
   * - Secondary_Email
     - Emails.Value
     - "string"
   * - id
     - PersonId
     - "integer"


ZohoCRM Deal to SuperOffice Sale
--------------------------------
Every ZohoCRM Deal will be synchronized with a SuperOffice Sale.

Once a link between a ZohoCRM Deal and a SuperOffice Sale is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a SuperOffice Sale:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - SuperOffice Sale Property
     - SuperOffice Data Type
   * - Account_Name.id
     - Contact.ContactId
     - "integer"
   * - Account_Name.id
     - Person.PersonId
     - "integer"
   * - Amount
     - Amount
     - "float"
   * - Closing_Date
     - Saledate
     - N/A
   * - Contact_Name.id
     - Contact.ContactId
     - "integer"
   * - Contact_Name.id
     - Person.PersonId
     - "integer"
   * - Deal_Name
     - Heading
     - "string"

