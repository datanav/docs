===============================
SuperOffice to ZohoCRM Dataflow
===============================

Generated: 2024-03-26 14:20:08

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Zohocrm Account
--------------------------------------
Every SuperOffice Contact will be synchronized with a Zohocrm Account.

Once a link between a SuperOffice Contact and a Zohocrm Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Zohocrm Account:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Zohocrm Account Property
     - Zohocrm Data Type
   * - Address.Postal.City
     - Billing_City
     - "string"
   * - Address.Postal.City
     - Shipping_City
     - "string"
   * - Address.Postal.Zipcode
     - Billing_Code
     - "string"
   * - Address.Postal.Zipcode
     - Shipping_Code
     - "string"
   * - Address.Street.City
     - Billing_City
     - "string"
   * - Address.Street.City
     - Shipping_City
     - "string"
   * - Address.Street.Zipcode
     - Billing_Code
     - "string"
   * - Address.Street.Zipcode
     - Shipping_Code
     - "string"
   * - Country.CountryId
     - Billing_Country
     - "string"
   * - Country.CountryId
     - Shipping_Country
     - "string"
   * - Name
     - Account_Name
     - "string"
   * - Phones.Value
     - Phone
     - "string"
   * - Urls.Value
     - Website
     - "string"


SuperOffice Contact to Zohocrm Contact
--------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Zohocrm Contact must be established.

A new Zohocrm Contact will be created from a SuperOffice Contact if it is connected to a SuperOffice Sale that is synchronized into Zohocrm.

Once a link between a SuperOffice Contact and a Zohocrm Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Zohocrm Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Zohocrm Contact Property
     - Zohocrm Data Type


SuperOffice Person to Zohocrm Account
-------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Zohocrm Account must be established.

A new Zohocrm Account will be created from a SuperOffice Person if it is connected to a SuperOffice Sale that is synchronized into Zohocrm.

Once a link between a SuperOffice Person and a Zohocrm Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Zohocrm Account:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Zohocrm Account Property
     - Zohocrm Data Type


SuperOffice Person to Zohocrm Contact
-------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Zohocrm Contact must be established.

A new Zohocrm Contact will be created from a SuperOffice Person if it is connected to a SuperOffice Sale that is synchronized into Zohocrm.

Once a link between a SuperOffice Person and a Zohocrm Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Zohocrm Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Zohocrm Contact Property
     - Zohocrm Data Type
   * - Address.Street.City
     - Mailing_City
     - "string"
   * - Address.Street.City
     - Other_City
     - "string"
   * - Address.Street.Zipcode
     - Mailing_Zip
     - "string"
   * - Address.Street.Zipcode
     - Other_Zip
     - "string"
   * - Contact.ContactId
     - Account_Name.id
     - "string"
   * - Country.CountryId
     - Mailing_Country
     - "string"
   * - Country.CountryId
     - Other_Country
     - "string"
   * - Emails.Value
     - Email
     - "string"
   * - Emails.Value
     - Secondary_Email
     - "string"
   * - Firstname
     - First_Name
     - "string"
   * - Lastname
     - Last_Name
     - "string"
   * - MobilePhones.Value
     - Mobile
     - "string"
   * - OfficePhones.Value
     - Other_Phone
     - "string"
   * - OfficePhones.Value
     - Phone
     - "string"
   * - PrivatePhones.Value
     - Home_Phone
     - "string"


SuperOffice Sale to ZohoCRM Deal
--------------------------------
Every SuperOffice Sale will be synchronized with a ZohoCRM Deal.

Once a link between a SuperOffice Sale and a ZohoCRM Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a ZohoCRM Deal:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - ZohoCRM Deal Property
     - ZohoCRM Data Type
   * - Amount
     - Amount
     - "string"
   * - Contact.ContactId
     - Account_Name.id
     - "string"
   * - Contact.ContactId
     - Contact_Name.id
     - "string"
   * - Heading
     - Deal_Name
     - "string"
   * - Person.PersonId
     - Account_Name.id
     - "string"
   * - Person.PersonId
     - Contact_Name.id
     - "string"
   * - SaleText
     - Deal_Name
     - "string"
   * - Saledate
     - Closing_Date
     - "datetime-format","%Y-%m-%dT%H:%M:%SZ","_."]
   * - Status
     - Probability
     - "string"
   * - Status
     - Stage
     - "string"
   * - Status
     - Type
     - "string"

