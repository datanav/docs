==========================================
Wave Financial to PowerOfficeGov1 Dataflow
==========================================

Generated: 2023-08-14 09:09:56

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to PowerOfficeGov1. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to PowerOfficeGov1 Employee
-----------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a PowerOfficeGov1 Employee must be established.

A Wave Customer will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGov1 Employee Property
   * - email
     - email

Once a link between a Wave Customer and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - MailAddress.Address1
     - "string"
   * - address.addressLine1
     - address.addressLine1
     - "string"
   * - address.addressLine1
     - streetAddresses.address1
     - "string"
   * - address.addressLine2
     - MailAddress.Address2
     - "string"
   * - address.addressLine2
     - address.addressLine2
     - "string"
   * - address.addressLine2
     - streetAddresses.address2
     - "string"
   * - address.city
     - MailAddress.City
     - "string"
   * - address.city
     - address.city
     - "string"
   * - address.city
     - streetAddresses.city
     - "string"
   * - address.country.code
     - MailAddress.CountryCode
     - "string"
   * - address.country.code
     - address.country.id
     - "integer"
   * - address.country.code
     - streetAddresses.countryCode
     - "string"
   * - address.postalCode
     - MailAddress.ZipCode
     - "string"
   * - address.postalCode
     - address.postalCode
     - "string"
   * - address.postalCode
     - streetAddresses.zipCode
     - "string"
   * - id
     - Id
     - "string"
   * - id
     - id
     - "integer"
   * - mobile
     - phoneNumberMobile
     - "string"


Wave Customer to PowerOfficeGov1 Person
---------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a PowerOfficeGov1 Person must be established.

A Wave Customer will merge with a PowerOfficeGov1 Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGov1 Person Property
   * - email
     - Emails.Value

Once a link between a Wave Customer and a PowerOfficeGov1 Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGov1 Person:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGov1 Person Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - Address.Street.Address1
     - "string"
   * - address.addressLine2
     - Address.Street.Address2
     - "string"
   * - address.city
     - Address.Street.City
     - "string"
   * - address.postalCode
     - Address.Street.Zipcode
     - "string"
   * - email
     - Emails.Value
     - "string"
   * - firstName
     - Firstname
     - "string"
   * - id
     - Contact.ContactId
     - "integer"
   * - id
     - PersonId
     - "integer"
   * - lastName
     - Lastname
     - "string"
   * - mobile
     - MobilePhones.Value
     - "string"


Wave Vendor to PowerOfficeGov1 Employee
---------------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a PowerOfficeGov1 Employee must be established.

A Wave Vendor will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGov1 Employee Property
   * - email
     - email

Once a link between a Wave Vendor and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - MailAddress.Address1
     - "string"
   * - address.addressLine1
     - address.addressLine1
     - "string"
   * - address.addressLine1
     - streetAddresses.address1
     - "string"
   * - address.addressLine2
     - MailAddress.Address2
     - "string"
   * - address.addressLine2
     - address.addressLine2
     - "string"
   * - address.addressLine2
     - streetAddresses.address2
     - "string"
   * - address.city
     - MailAddress.City
     - "string"
   * - address.city
     - address.city
     - "string"
   * - address.city
     - streetAddresses.city
     - "string"
   * - address.country.code
     - MailAddress.CountryCode
     - "string"
   * - address.country.code
     - address.country.id
     - "integer"
   * - address.country.code
     - streetAddresses.countryCode
     - "string"
   * - address.postalCode
     - MailAddress.ZipCode
     - "string"
   * - address.postalCode
     - address.postalCode
     - "string"
   * - address.postalCode
     - streetAddresses.zipCode
     - "string"
   * - id
     - Id
     - "string"
   * - id
     - id
     - "integer"
   * - mobile
     - phoneNumberMobile
     - "string"
   * - phone
     - phoneNumberWork
     - "string"


Wave Vendor to PowerOfficeGov1 Person
-------------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a PowerOfficeGov1 Person must be established.

A Wave Vendor will merge with a PowerOfficeGov1 Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGov1 Person Property
   * - email
     - Emails.Value

Once a link between a Wave Vendor and a PowerOfficeGov1 Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGov1 Person:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGov1 Person Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - Address.Street.Address1
     - "string"
   * - address.addressLine2
     - Address.Street.Address2
     - "string"
   * - address.city
     - Address.Street.City
     - "string"
   * - address.postalCode
     - Address.Street.Zipcode
     - "string"
   * - email
     - Emails.Value
     - "string"
   * - firstName
     - Firstname
     - "string"
   * - id
     - Contact.ContactId
     - "integer"
   * - id
     - PersonId
     - "integer"
   * - lastName
     - Lastname
     - "string"
   * - mobile
     - MobilePhones.Value
     - "string"
   * - phone
     - OfficePhones.Value
     - "string"


Wave Customer to PowerOfficeGov1 Customer
-----------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a PowerOfficeGov1 Customer must be established.

A new PowerOfficeGov1 Customer will be created from a Wave Customer if it is connected to a Wave Invoice that is synchronized into PowerOfficeGov1.

Once a link between a Wave Customer and a PowerOfficeGov1 Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGov1 Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGov1 Customer Property
     - PowerOfficeGov1 Data Type


Wave Customer to PowerOfficeGov1 Contact
----------------------------------------
Every Wave Customer will be synchronized with a PowerOfficeGov1 Contact.

Once a link between a Wave Customer and a PowerOfficeGov1 Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGov1 Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGov1 Contact Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - Address.Street.Address1
     - "string"
   * - address.addressLine2
     - Address.Street.Address2
     - "string"
   * - address.city
     - Address.Street.City
     - "string"
   * - address.postalCode
     - Address.Street.Zipcode
     - "string"
   * - id
     - ContactId
     - "integer"
   * - mobile
     - phoneNumberMobile
     - "if","matches","+*","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
   * - name
     - Name
     - "string"
   * - phone
     - Phones.Value
     - "string"
   * - shippingDetails.phone
     - Phones.Value
     - "string"
   * - website
     - Domains
     - "list"
   * - website
     - Urls.Value
     - "string"


Wave Vendor to PowerOfficeGov1 Contact
--------------------------------------
Every Wave Vendor will be synchronized with a PowerOfficeGov1 Contact.

Once a link between a Wave Vendor and a PowerOfficeGov1 Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGov1 Contact:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGov1 Contact Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - Address.Street.Address1
     - "string"
   * - address.addressLine2
     - Address.Street.Address2
     - "string"
   * - address.city
     - Address.Street.City
     - "string"
   * - address.postalCode
     - Address.Street.Zipcode
     - "string"
   * - id
     - ContactId
     - "integer"
   * - mobile
     - phoneNumberMobile
     - "if","matches","+*","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
   * - name
     - Name
     - "string"
   * - phone
     - phoneNumberWork
     - "string"
   * - website
     - Domains
     - "list"
   * - website
     - Urls.Value
     - "string"

