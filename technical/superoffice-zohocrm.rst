========================
SuperOffice to  Dataflow
========================

Generated: 2023-11-29 23:45:21

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to  Account
-------------------------------
Every SuperOffice Contact will be synchronized with a  Account.

Once a link between a SuperOffice Contact and a  Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Account:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Account Property
     -  Data Type
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


SuperOffice Contact to  Contact
-------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a  Contact must be established.

A new  Contact will be created from a SuperOffice Contact if it is connected to a SuperOffice Sale that is synchronized into .

Once a link between a SuperOffice Contact and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Contact Property
     -  Data Type


SuperOffice Person to  Account
------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a  Account must be established.

A new  Account will be created from a SuperOffice Person if it is connected to a SuperOffice Sale that is synchronized into .

Once a link between a SuperOffice Person and a  Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a  Account:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Account Property
     -  Data Type


SuperOffice Person to  Contact
------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a  Contact must be established.

A new  Contact will be created from a SuperOffice Person if it is connected to a SuperOffice Sale that is synchronized into .

Once a link between a SuperOffice Person and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a  Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Contact Property
     -  Data Type
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


SuperOffice Sale to  Deal
-------------------------
Every SuperOffice Sale will be synchronized with a  Deal.

Once a link between a SuperOffice Sale and a  Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a  Deal:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     -  Deal Property
     -  Data Type
   * - Amount
     - Amount
     - "string"
   * - Contact.ContactId
     - Account_Name.id
     - "string"
   * - Contact.ContactId
     - Contact_Name.id
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

