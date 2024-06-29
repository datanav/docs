===============================
ZohoCRM to Superoffice Dataflow
===============================

Generated: 2024-06-29 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Superoffice Contact
--------------------------------------
Every ZohoCRM Account will be synchronized with a Superoffice Contact.

Once a link between a ZohoCRM Account and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Superoffice Contact Property
     - Superoffice Data Type
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


ZohoCRM Account to Superoffice Person
-------------------------------------
Before any synchronization can take place, a link between a ZohoCRM Account and a Superoffice Person must be established.

A new Superoffice Person will be created from a ZohoCRM Account if it is connected to a ZohoCRM Deal that is synchronized into Superoffice.

Once a link between a ZohoCRM Account and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Superoffice Person Property
     - Superoffice Data Type


ZohoCRM Contact to Superoffice Contact
--------------------------------------
Before any synchronization can take place, a link between a ZohoCRM Contact and a Superoffice Contact must be established.

A new Superoffice Contact will be created from a ZohoCRM Contact if it is connected to a ZohoCRM Deal that is synchronized into Superoffice.

Once a link between a ZohoCRM Contact and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Superoffice Contact Property
     - Superoffice Data Type


ZohoCRM Contact to Superoffice Person
-------------------------------------
Every ZohoCRM Contact will be synchronized with a Superoffice Person.

Once a link between a ZohoCRM Contact and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Superoffice Person Property
     - Superoffice Data Type
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


ZohoCRM Deal to Superoffice Sale
--------------------------------
Every ZohoCRM Deal will be synchronized with a Superoffice Sale.

Once a link between a ZohoCRM Deal and a Superoffice Sale is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a Superoffice Sale:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - Superoffice Sale Property
     - Superoffice Data Type
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

