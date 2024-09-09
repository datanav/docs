=========================
ZohoCRM to Exact Dataflow
=========================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Exact Accounts
---------------------------------
Every ZohoCRM Account will be synchronized with a Exact Accounts.

Once a link between a ZohoCRM Account and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Exact Accounts Property
     - Exact Data Type
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


ZohoCRM Contact to Exact Contacts
---------------------------------
Every ZohoCRM Contact will be synchronized with a Exact Contacts.

Once a link between a ZohoCRM Contact and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Exact Contacts Property
     - Exact Data Type
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


ZohoCRM Deal to Exact Quotations
--------------------------------
Every ZohoCRM Deal will be synchronized with a Exact Quotations.

Once a link between a ZohoCRM Deal and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - Exact Quotations Property
     - Exact Data Type


ZohoCRM Contact to Exact Addresses
----------------------------------
Every ZohoCRM Contact will be synchronized with a Exact Addresses.

Once a link between a ZohoCRM Contact and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Exact Addresses Property
     - Exact Data Type
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

