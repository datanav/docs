========================
SuperOffice to  Dataflow
========================

Generated: 2024-08-29 11:02:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to  Accounts
--------------------------------
Every SuperOffice Contact will be synchronized with a  Accounts.

Once a link between a SuperOffice Contact and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Accounts:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Accounts Property
     -  Data Type
   * - Address.Postal.Address1
     - AddressLine1
     - "string"
   * - Address.Postal.Address2
     - AddressLine2
     - "string"
   * - Address.Postal.Address3
     - AddressLine3
     - "string"
   * - Address.Postal.City
     - City
     - "string"
   * - Address.Street.Address1
     - AddressLine1
     - "string"
   * - Address.Street.Address2
     - AddressLine2
     - "string"
   * - Address.Street.Address3
     - AddressLine3
     - "string"
   * - Address.Street.City
     - City
     - "string"
   * - Country.CountryId
     - Country
     - "string"
   * - Name
     - Name
     - "string"


SuperOffice Person to  Contacts
-------------------------------
Every SuperOffice Person will be synchronized with a  Contacts.

Once a link between a SuperOffice Person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Contacts Property
     -  Data Type
   * - Address.Street.City
     - City
     - "string"
   * - BirthDate
     - BirthDate
     - "string"
   * - Country.CountryId
     - Country
     - "string"
   * - Emails.Value
     - Email
     - "string"
   * - Firstname
     - FirstName
     - "string"
   * - Lastname
     - LastName
     - "string"
   * - MobilePhones.Value
     - Mobile
     - "string"
   * - OfficePhones.Value
     - Phone
     - "string"


SuperOffice Person to  Addresses
--------------------------------
Every SuperOffice Person will be synchronized with a  Addresses.

Once a link between a SuperOffice Person and a  Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a  Addresses:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Addresses Property
     -  Data Type
   * - Address.Street.Address1
     - AddressLine1
     - "string"
   * - Address.Street.Address2
     - AddressLine2
     - "string"
   * - Address.Street.Address3
     - AddressLine3
     - "string"
   * - Address.Street.City
     - City
     - "string"
   * - Country.CountryId
     - Country
     - "string"

