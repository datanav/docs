==================================
ZohoCRM to PowerOffice GO Dataflow
==================================

Generated: 2024-09-17 07:28:49

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to PowerOffice GO Contactperson
-----------------------------------------------
Before any synchronization can take place, a link between a ZohoCRM Account and a PowerOffice GO Contactperson must be established.

A new PowerOffice GO Contactperson will be created from a ZohoCRM Account if it is connected to a ZohoCRM Deal that is synchronized into PowerOffice GO.

Once a link between a ZohoCRM Account and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type


ZohoCRM Account to PowerOffice GO Customers person
--------------------------------------------------
Before any synchronization can take place, a link between a ZohoCRM Account and a PowerOffice GO Customers person must be established.

A new PowerOffice GO Customers person will be created from a ZohoCRM Account if it is connected to a ZohoCRM Deal that is synchronized into PowerOffice GO.

Once a link between a ZohoCRM Account and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - PowerOffice GO Customers person Property
     - PowerOffice GO Data Type


ZohoCRM Account to PowerOffice GO Customers
-------------------------------------------
Before any synchronization can take place, a link between a ZohoCRM Account and a PowerOffice GO Customers must be established.

A new PowerOffice GO Customers will be created from a ZohoCRM Account if it is connected to a ZohoCRM Deal that is synchronized into PowerOffice GO.

Once a link between a ZohoCRM Account and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
   * - Account_Name
     - Name
     - "string"
   * - Billing_City
     - MailAddress.City
     - "string"
   * - Billing_Code
     - MailAddress.ZipCode
     - "string"
   * - Billing_Country
     - MailAddress.CountryCode
     - "string"
   * - Phone
     - PhoneNumber
     - "string"
   * - Shipping_City
     - MailAddress.City
     - "string"
   * - Shipping_Code
     - MailAddress.ZipCode
     - "string"
   * - Shipping_Country
     - MailAddress.CountryCode
     - "string"
   * - Website
     - WebsiteUrl
     - "string"
   * - id
     - Id
     - "integer"


ZohoCRM Contact to PowerOffice GO Contactperson
-----------------------------------------------
Before any synchronization can take place, a link between a ZohoCRM Contact and a PowerOffice GO Contactperson must be established.

A new PowerOffice GO Contactperson will be created from a ZohoCRM Contact if it is connected to a ZohoCRM Deal that is synchronized into PowerOffice GO.

Once a link between a ZohoCRM Contact and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
   * - Email
     - emailAddress
     - "string"
   * - First_Name
     - firstName
     - "string"
   * - Last_Name
     - lastName
     - "string"
   * - Mailing_City
     - city
     - "string"
   * - Mailing_Country
     - residenceCountryCode
     - "string"
   * - Mailing_Zip
     - zipCode
     - "string"
   * - Other_City
     - city
     - "string"
   * - Other_Country
     - residenceCountryCode
     - "string"
   * - Other_Phone
     - phoneNumber
     - "string"
   * - Other_Zip
     - zipCode
     - "string"
   * - Phone
     - phoneNumber
     - "string"
   * - Secondary_Email
     - emailAddress
     - "string"
   * - id
     - id
     - "integer"


ZohoCRM Contact to PowerOffice GO Customers person
--------------------------------------------------
Before any synchronization can take place, a link between a ZohoCRM Contact and a PowerOffice GO Customers person must be established.

A new PowerOffice GO Customers person will be created from a ZohoCRM Contact if it is connected to a ZohoCRM Deal that is synchronized into PowerOffice GO.

Once a link between a ZohoCRM Contact and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - PowerOffice GO Customers person Property
     - PowerOffice GO Data Type
   * - Email
     - EmailAddress
     - "string"
   * - First_Name
     - FirstName
     - "string"
   * - Last_Name
     - LastName
     - "string"
   * - Mailing_City
     - MailAddress.City
     - "string"
   * - Mailing_Country
     - MailAddress.CountryCode
     - "string"
   * - Mailing_Zip
     - MailAddress.ZipCode
     - "string"
   * - Other_City
     - MailAddress.City
     - "string"
   * - Other_Country
     - MailAddress.CountryCode
     - "string"
   * - Other_Phone
     - PhoneNumber
     - "string"
   * - Other_Zip
     - MailAddress.ZipCode
     - "string"
   * - Phone
     - PhoneNumber
     - "string"
   * - Secondary_Email
     - EmailAddress
     - "string"
   * - id
     - Id
     - "integer"


ZohoCRM Contact to PowerOffice GO Customers
-------------------------------------------
Before any synchronization can take place, a link between a ZohoCRM Contact and a PowerOffice GO Customers must be established.

A new PowerOffice GO Customers will be created from a ZohoCRM Contact if it is connected to a ZohoCRM Deal that is synchronized into PowerOffice GO.

Once a link between a ZohoCRM Contact and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type


ZohoCRM Contact to PowerOffice GO Customers
-------------------------------------------
Every ZohoCRM Contact will be synchronized with a PowerOffice GO Customers.

Once a link between a ZohoCRM Contact and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type


ZohoCRM Contact to PowerOffice GO Customers person
--------------------------------------------------
Every ZohoCRM Contact will be synchronized with a PowerOffice GO Customers person.

Once a link between a ZohoCRM Contact and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - PowerOffice GO Customers person Property
     - PowerOffice GO Data Type


ZohoCRM Deal to PowerOffice GO Salesorders
------------------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a PowerOffice GO Salesorders.

Once a link between a ZohoCRM Deal and a PowerOffice GO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a PowerOffice GO Salesorders:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - PowerOffice GO Salesorders Property
     - PowerOffice GO Data Type
   * - Account_Name.id
     - CustomerId
     - "integer"
   * - Account_Name.id
     - CustomerReferenceContactPersonId
     - "integer"
   * - Closing_Date
     - SalesOrderDate
     - "string"
   * - Contact_Name.id
     - CustomerId
     - "integer"
   * - Contact_Name.id
     - CustomerReferenceContactPersonId
     - "integer"

