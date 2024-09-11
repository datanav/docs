================================
ZohoCRM to Exact Online Dataflow
================================

Generated: 2024-09-11 12:17:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Exact Online Accounts
----------------------------------------
Every ZohoCRM Account will be synchronized with a Exact Online Accounts.

Once a link between a ZohoCRM Account and a Exact Online Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Exact Online Accounts:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Exact Online Accounts Property
     - Exact Online Data Type
   * - Account_Name
     - Name
     - "string"
   * - Billing_City
     - City
     - "string"
   * - Billing_Code
     - Postcode
     - "string"
   * - Billing_Country
     - Country
     - "string"
   * - Phone
     - Phone
     - "string"
   * - Shipping_City
     - City
     - "string"
   * - Shipping_Code
     - Postcode
     - "string"
   * - Shipping_Country
     - Country
     - "string"
   * - Website
     - Website
     - "string"


ZohoCRM Contact to Exact Online Contacts
----------------------------------------
Every ZohoCRM Contact will be synchronized with a Exact Online Contacts.

Once a link between a ZohoCRM Contact and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Exact Online Contacts Property
     - Exact Online Data Type
   * - Email
     - Email
     - "string"
   * - First_Name
     - FirstName
     - "string"
   * - Full_Name
     - FullName
     - "string"
   * - Last_Name
     - LastName
     - "string"
   * - Mailing_City
     - City
     - "string"
   * - Mailing_Country
     - Country
     - "string"
   * - Mobile
     - Mobile
     - "string"
   * - Other_City
     - City
     - "string"
   * - Other_Country
     - Country
     - "string"
   * - Other_Phone
     - Phone
     - "string"
   * - Phone
     - Phone
     - "string"
   * - Secondary_Email
     - Email
     - "string"


ZohoCRM Deal to Exact Online Quotations
---------------------------------------
Every ZohoCRM Deal will be synchronized with a Exact Online Quotations.

Once a link between a ZohoCRM Deal and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - Exact Online Quotations Property
     - Exact Online Data Type


ZohoCRM Contact to Exact Online Addresses
-----------------------------------------
Every ZohoCRM Contact will be synchronized with a Exact Online Addresses.

Once a link between a ZohoCRM Contact and a Exact Online Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Exact Online Addresses:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Exact Online Addresses Property
     - Exact Online Data Type
   * - Mailing_City
     - City
     - "string"
   * - Mailing_Country
     - Country
     - "string"
   * - Mailing_Country
     - CountryName
     - "string"
   * - Other_City
     - City
     - "string"
   * - Other_Country
     - Country
     - "string"
   * - Other_Country
     - CountryName
     - "string"

