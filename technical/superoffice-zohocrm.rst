===============================
SuperOffice to ZohoCRM Dataflow
===============================

Generated: 2023-10-07 10:42:10

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to ZohoCRM Account
--------------------------------------
Every SuperOffice Contact will be synchronized with a ZohoCRM Account.

Once a link between a SuperOffice Contact and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
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

