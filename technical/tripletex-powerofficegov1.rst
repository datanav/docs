=====================================
Tripletex to PowerOfficeGov1 Dataflow
=====================================

Generated: 2023-08-14 09:03:59

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to PowerOfficeGov1. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to PowerOfficeGov1 Employee
---------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a PowerOfficeGov1 Employee must be established.

A Tripletex Contact will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGov1 Employee Property
   * - email
     - email

Once a link between a Tripletex Contact and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type
   * - customer.id
     - department.id
     - "if", "neq", "_.", "X"], "integer", "string"]
   * - email
     - email
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - phoneNumberMobile
     - phoneNumberMobile
     - "string"
   * - phoneNumberWork
     - phoneNumberWork
     - "string"


Tripletex Contact to PowerOfficeGov1 Person
-------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a PowerOfficeGov1 Person must be established.

A Tripletex Contact will merge with a PowerOfficeGov1 Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGov1 Person Property
   * - email
     - Emails.Value

Once a link between a Tripletex Contact and a PowerOfficeGov1 Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOfficeGov1 Person:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGov1 Person Property
     - PowerOfficeGov1 Data Type
   * - customer.id
     - Contact.ContactId
     - "integer"
   * - email
     - Emails.Value
     - "string"
   * - firstName
     - Firstname
     - "string"
   * - lastName
     - Lastname
     - "string"
   * - phoneNumberMobile
     - MobilePhones.Value
     - "string"
   * - phoneNumberWork
     - OfficePhones.Value
     - "string"


Tripletex Customer to PowerOfficeGov1 Companies
-----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOfficeGov1 Companies must be established.

A Tripletex Customer will merge with a PowerOfficeGov1 Companies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGov1 Companies Property
   * - organizationNumber
     - OrganizationNumber

Once a link between a Tripletex Customer and a PowerOfficeGov1 Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGov1 Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGov1 Companies Property
     - PowerOfficeGov1 Data Type
   * - name
     - Name
     - "string"


Tripletex Customer to PowerOfficeGov1 Contact
---------------------------------------------
Every Tripletex Customer will be synchronized with a PowerOfficeGov1 Contact.

If a matching PowerOfficeGov1 Contact already exists, the Tripletex Customer will be merged with the existing one.
If no matching PowerOfficeGov1 Contact is found, a new PowerOfficeGov1 Contact will be created.

A Tripletex Customer will merge with a PowerOfficeGov1 Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGov1 Contact Property
   * - email
     - Emails.Value
   * - invoiceEmail
     - Emails.Value
   * - overdueNoticeEmail
     - Emails.Value

Once a link between a Tripletex Customer and a PowerOfficeGov1 Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGov1 Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGov1 Contact Property
     - PowerOfficeGov1 Data Type
   * - deliveryAddress.addressLine1
     - Address.Postal.Address1
     - "string"
   * - deliveryAddress.addressLine1
     - Address.Street.Address1
     - "string"
   * - deliveryAddress.addressLine2
     - Address.Postal.Address2
     - "string"
   * - deliveryAddress.addressLine2
     - Address.Street.Address2
     - "string"
   * - deliveryAddress.city
     - Address.Postal.City
     - "string"
   * - deliveryAddress.city
     - Address.Street.City
     - "string"
   * - deliveryAddress.country.id
     - Country.CountryId
     - "integer"
   * - deliveryAddress.postalCode
     - Address.Postal.Zipcode
     - "string"
   * - deliveryAddress.postalCode
     - Address.Street.Zipcode
     - "string"
   * - email
     - Emails.Value
     - "string"
   * - id
     - ContactId
     - "integer"
   * - name
     - Name
     - "string"
   * - organizationNumber
     - OrgNr (Dependant on having NO in Country.TwoLetterISOCountry)
     - "string"
   * - phoneNumber
     - Phones.Value
     - "string"
   * - physicalAddress.addressLine1
     - Address.Postal.Address1
     - "string"
   * - physicalAddress.addressLine1
     - Address.Street.Address1
     - "string"
   * - physicalAddress.addressLine2
     - Address.Postal.Address2
     - "string"
   * - physicalAddress.addressLine2
     - Address.Street.Address2
     - "string"
   * - physicalAddress.city
     - Address.Postal.City
     - "string"
   * - physicalAddress.city
     - Address.Street.City
     - "string"
   * - physicalAddress.country.id
     - Country.CountryId
     - "integer"
   * - physicalAddress.postalCode
     - Address.Postal.Zipcode
     - "string"
   * - physicalAddress.postalCode
     - Address.Street.Zipcode
     - "string"
   * - postalAddress.addressLine1
     - Address.Postal.Address1
     - "string"
   * - postalAddress.addressLine1
     - Address.Street.Address1
     - "string"
   * - postalAddress.addressLine2
     - Address.Postal.Address2
     - "string"
   * - postalAddress.addressLine2
     - Address.Street.Address2
     - "string"
   * - postalAddress.city
     - Address.Postal.City
     - "string"
   * - postalAddress.city
     - Address.Street.City
     - "string"
   * - postalAddress.country.id
     - Country.CountryId
     - "integer"
   * - postalAddress.postalCode
     - Address.Postal.Zipcode
     - "string"
   * - postalAddress.postalCode
     - Address.Street.Zipcode
     - "string"


Tripletex Customer to PowerOfficeGov1 Supplier
----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOfficeGov1 Supplier must be established.

A Tripletex Customer will merge with a PowerOfficeGov1 Supplier if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGov1 Supplier Property
   * - email
     - email
   * - email
     - invoiceEmail
   * - invoiceEmail
     - email
   * - email
     - overdueNoticeEmail
   * - overdueNoticeEmail
     - email
   * - invoiceEmail
     - invoiceEmail
   * - invoiceEmail
     - overdueNoticeEmail
   * - overdueNoticeEmail
     - invoiceEmail
   * - organizationNumber
     - organizationNumber
   * - overdueNoticeEmail
     - overdueNoticeEmail

Once a link between a Tripletex Customer and a PowerOfficeGov1 Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGov1 Supplier:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGov1 Supplier Property
     - PowerOfficeGov1 Data Type
   * - deliveryAddress.addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - deliveryAddress.city
     - deliveryAddress.changes
     - "string"
   * - deliveryAddress.country.id
     - deliveryAddress.city
     - "string"
   * - deliveryAddress.postalCode
     - deliveryAddress.postalCode
     - "string"
   * - email
     - EmailAddress
     - "string"
   * - email
     - email
     - "string"
   * - id
     - Id
     - "string"
   * - id
     - id
     - "integer"
   * - invoiceEmail
     - invoiceEmail
     - "string"
   * - name
     - LegalName
     - "string"
   * - name
     - name
     - "string"
   * - overdueNoticeEmail
     - overdueNoticeEmail
     - "string"
   * - phoneNumber
     - PhoneNumber
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - phoneNumberMobile
     - phoneNumberMobile
     - "string"
   * - physicalAddress.addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - physicalAddress.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - physicalAddress.city
     - physicalAddress.city
     - "string"
   * - physicalAddress.country.id
     - physicalAddress.country.id
     - "integer"
   * - physicalAddress.postalCode
     - physicalAddress.postalCode
     - "string"
   * - postalAddress.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - postalAddress.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - postalAddress.city
     - postalAddress.city
     - "string"
   * - postalAddress.country.id
     - postalAddress.country.id
     - "integer"
   * - postalAddress.postalCode
     - postalAddress.postalCode
     - "string"


Tripletex Department to PowerOfficeGov1 Employee
------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a PowerOfficeGov1 Employee must be established.

A Tripletex Department will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOfficeGov1 Employee Property
   * - departmentManager.id
     - id

Once a link between a Tripletex Department and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type


Tripletex Employee to PowerOfficeGov1 Person
--------------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a PowerOfficeGov1 Person must be established.

A Tripletex Employee will merge with a PowerOfficeGov1 Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOfficeGov1 Person Property
   * - email
     - Emails.Value

Once a link between a Tripletex Employee and a PowerOfficeGov1 Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOfficeGov1 Person:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
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
   * - dateOfBirth
     - BirthDate
     - "datetime-format","%Y-%m-%dT%H:%M:%S","_."]
   * - department.id
     - Contact.ContactId
     - "integer"
   * - email
     - Emails.Value
     - "string"
   * - firstName
     - Firstname
     - "string"
   * - id
     - PersonId
     - "integer"
   * - lastName
     - Lastname
     - "string"
   * - phoneNumberHome
     - PrivatePhones.Value
     - "string"
   * - phoneNumberMobile
     - MobilePhones.Value
     - "string"
   * - phoneNumberWork
     - OfficePhones.Value
     - "string"


Tripletex Product to PowerOfficeGov1 Productgrouprelation
---------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Product and a PowerOfficeGov1 Productgrouprelation must be established.

A Tripletex Product will merge with a PowerOfficeGov1 Productgrouprelation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - PowerOfficeGov1 Productgrouprelation Property
   * - id
     - product.id

Once a link between a Tripletex Product and a PowerOfficeGov1 Productgrouprelation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a PowerOfficeGov1 Productgrouprelation:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - PowerOfficeGov1 Productgrouprelation Property
     - PowerOfficeGov1 Data Type


Tripletex Productgrouprelation to PowerOfficeGov1 Product
---------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Productgrouprelation and a PowerOfficeGov1 Product must be established.

A Tripletex Productgrouprelation will merge with a PowerOfficeGov1 Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgrouprelation Property
     - PowerOfficeGov1 Product Property
   * - product.id
     - id

Once a link between a Tripletex Productgrouprelation and a PowerOfficeGov1 Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgrouprelation and a PowerOfficeGov1 Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgrouprelation Property
     - PowerOfficeGov1 Product Property
     - PowerOfficeGov1 Data Type
   * - productGroup.id
     - ProductCategoryKey
     - "string"
   * - productGroup.id
     - productGroupId
     - "string"


Tripletex Productgrouprelation to PowerOfficeGov1 Productgrouprelation
----------------------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Productgrouprelation and a PowerOfficeGov1 Productgrouprelation must be established.

A Tripletex Productgrouprelation will merge with a PowerOfficeGov1 Productgrouprelation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgrouprelation Property
     - PowerOfficeGov1 Productgrouprelation Property
   * - product.id
     - product.id

Once a link between a Tripletex Productgrouprelation and a PowerOfficeGov1 Productgrouprelation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgrouprelation and a PowerOfficeGov1 Productgrouprelation:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgrouprelation Property
     - PowerOfficeGov1 Productgrouprelation Property
     - PowerOfficeGov1 Data Type
   * - productGroup.id
     - productGroup.id
     - "integer"


Tripletex Supplier to PowerOfficeGov1 Companies
-----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Supplier and a PowerOfficeGov1 Companies must be established.

A Tripletex Supplier will merge with a PowerOfficeGov1 Companies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOfficeGov1 Companies Property
   * - organizationNumber
     - OrganizationNumber

Once a link between a Tripletex Supplier and a PowerOfficeGov1 Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a PowerOfficeGov1 Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOfficeGov1 Companies Property
     - PowerOfficeGov1 Data Type
   * - name
     - Name
     - "string"


Tripletex Supplier to PowerOfficeGov1 Contact
---------------------------------------------
Every Tripletex Supplier will be synchronized with a PowerOfficeGov1 Contact.

If a matching PowerOfficeGov1 Contact already exists, the Tripletex Supplier will be merged with the existing one.
If no matching PowerOfficeGov1 Contact is found, a new PowerOfficeGov1 Contact will be created.

A Tripletex Supplier will merge with a PowerOfficeGov1 Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOfficeGov1 Contact Property
   * - email
     - Emails.Value
   * - invoiceEmail
     - Emails.Value
   * - overdueNoticeEmail
     - Emails.Value

Once a link between a Tripletex Supplier and a PowerOfficeGov1 Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a PowerOfficeGov1 Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOfficeGov1 Contact Property
     - PowerOfficeGov1 Data Type
   * - email
     - Emails.Value
     - "string"
   * - id
     - ContactId
     - "integer"
   * - name
     - Name
     - "string"
   * - phoneNumber
     - Phones.Value
     - "string"
   * - physicalAddress.addressLine1
     - Address.Street.Address1
     - "string"
   * - physicalAddress.addressLine2
     - Address.Street.Address2
     - "string"
   * - physicalAddress.city
     - Address.Street.City
     - "string"
   * - physicalAddress.postalCode
     - Address.Street.Zipcode
     - "string"
   * - postalAddress.addressLine1
     - Address.Postal.Address1
     - "string"
   * - postalAddress.addressLine2
     - Address.Postal.Address2
     - "string"
   * - postalAddress.city
     - Address.Postal.City
     - "string"
   * - postalAddress.country.id
     - Country.CountryId
     - "integer"
   * - postalAddress.postalCode
     - Address.Postal.Zipcode
     - "string"


Tripletex Supplier to PowerOfficeGov1 Customer
----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Supplier and a PowerOfficeGov1 Customer must be established.

A Tripletex Supplier will merge with a PowerOfficeGov1 Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOfficeGov1 Customer Property
   * - email
     - email
   * - email
     - invoiceEmail
   * - invoiceEmail
     - email
   * - email
     - overdueNoticeEmail
   * - overdueNoticeEmail
     - email
   * - invoiceEmail
     - invoiceEmail
   * - invoiceEmail
     - overdueNoticeEmail
   * - overdueNoticeEmail
     - invoiceEmail
   * - organizationNumber
     - organizationNumber
   * - overdueNoticeEmail
     - overdueNoticeEmail

Once a link between a Tripletex Supplier and a PowerOfficeGov1 Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a PowerOfficeGov1 Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOfficeGov1 Customer Property
     - PowerOfficeGov1 Data Type
   * - deliveryAddress.addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - deliveryAddress.changes
     - deliveryAddress.city
     - "string"
   * - deliveryAddress.city
     - deliveryAddress.country.id
     - "string"
   * - deliveryAddress.postalCode
     - deliveryAddress.postalCode
     - "string"
   * - email
     - email
     - "string"
   * - email
     - emailAddress
     - "string"
   * - id
     - id
     - "integer"
   * - invoiceEmail
     - InvoiceEmailAddressCC
     - "string"
   * - invoiceEmail
     - invoiceEmail
     - "string"
   * - name
     - legalName
     - "string"
   * - name
     - name
     - "string"
   * - overdueNoticeEmail
     - overdueNoticeEmail
     - "string"
   * - phoneNumber
     - phone
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - phoneNumberMobile
     - phoneNumberMobile
     - "string"
   * - physicalAddress.addressLine1
     - address.addressLine1
     - "string"
   * - physicalAddress.addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - physicalAddress.addressLine1
     - streetAddresses.address1
     - "string"
   * - physicalAddress.addressLine2
     - address.addressLine2
     - "string"
   * - physicalAddress.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - physicalAddress.addressLine2
     - streetAddresses.address2
     - "string"
   * - physicalAddress.city
     - address.city
     - "string"
   * - physicalAddress.city
     - physicalAddress.city
     - "string"
   * - physicalAddress.city
     - streetAddresses.city
     - "string"
   * - physicalAddress.country.id
     - address.country.code
     - "string"
   * - physicalAddress.country.id
     - physicalAddress.country.id
     - "integer"
   * - physicalAddress.country.id
     - streetAddresses.countryCode
     - "string"
   * - physicalAddress.postalCode
     - address.postalCode
     - "string"
   * - physicalAddress.postalCode
     - physicalAddress.postalCode
     - "string"
   * - physicalAddress.postalCode
     - streetAddresses.zipCode
     - "string"
   * - postalAddress.addressLine1
     - mailAddress.address1
     - "string"
   * - postalAddress.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - postalAddress.addressLine2
     - mailAddress.address2
     - "string"
   * - postalAddress.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - postalAddress.city
     - mailAddress.city
     - "string"
   * - postalAddress.city
     - postalAddress.city
     - "string"
   * - postalAddress.country.id
     - mailAddress.countryCode
     - "string"
   * - postalAddress.country.id
     - postalAddress.country.id
     - "integer"
   * - postalAddress.postalCode
     - mailAddress.zipCode
     - "string"
   * - postalAddress.postalCode
     - postalAddress.postalCode
     - "string"


Tripletex Supplier to PowerOfficeGov1 Customers
-----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Supplier and a PowerOfficeGov1 Customers must be established.

A Tripletex Supplier will merge with a PowerOfficeGov1 Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOfficeGov1 Customers Property
   * - organizationNumber
     - OrgNumber

Once a link between a Tripletex Supplier and a PowerOfficeGov1 Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a PowerOfficeGov1 Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOfficeGov1 Customers Property
     - PowerOfficeGov1 Data Type
   * - organizationNumber
     - OrgNumber
     - "string"


Tripletex Contact to PowerOfficeGov1 Contact
--------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a PowerOfficeGov1 Contact must be established.

A new PowerOfficeGov1 Contact will be created from a Tripletex Contact if it is connected to a Tripletex Order that is synchronized into PowerOfficeGov1.

Once a link between a Tripletex Contact and a PowerOfficeGov1 Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOfficeGov1 Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGov1 Contact Property
     - PowerOfficeGov1 Data Type
   * - customer.id
     - customer.id
     - "integer"
   * - email
     - email
     - "string"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - phoneNumberMobile
     - phoneNumberMobile
     - "if","matches","+*","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
   * - phoneNumberMobileCountry.id
     - phoneNumberMobileCountry.id
     - "string"
   * - phoneNumberWork
     - phoneNumberWork
     - "string"


Tripletex Customer to PowerOfficeGov1 Department
------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOfficeGov1 Department must be established.

A new PowerOfficeGov1 Department will be created from a Tripletex Customer if it is connected to a Tripletex Contact, Employee, or Department that is synchronized into PowerOfficeGov1.

Once a link between a Tripletex Customer and a PowerOfficeGov1 Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGov1 Department:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGov1 Department Property
     - PowerOfficeGov1 Data Type
   * - name
     - name
     - "string"


Tripletex Department to PowerOfficeGov1 Contact
-----------------------------------------------
Every Tripletex Department will be synchronized with a PowerOfficeGov1 Contact.

Once a link between a Tripletex Department and a PowerOfficeGov1 Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a PowerOfficeGov1 Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOfficeGov1 Contact Property
     - PowerOfficeGov1 Data Type
   * - name
     - Name
     - "string"


Tripletex Department to PowerOfficeGov1 Customer
------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a PowerOfficeGov1 Customer must be established.

A new PowerOfficeGov1 Customer will be created from a Tripletex Department if it is connected to a Tripletex Contact, Customer, Supplier, or Department that is synchronized into PowerOfficeGov1.

Once a link between a Tripletex Department and a PowerOfficeGov1 Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a PowerOfficeGov1 Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOfficeGov1 Customer Property
     - PowerOfficeGov1 Data Type
   * - departmentNumber
     - internalNotes
     - "string"
   * - name
     - legalName
     - "string"
   * - name
     - name
     - "string"


Tripletex Contact to PowerOfficeGov1 Contactperson
--------------------------------------------------
Every Tripletex Contact will be synchronized with a PowerOfficeGov1 Contactperson.

Once a link between a Tripletex Contact and a PowerOfficeGov1 Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOfficeGov1 Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGov1 Contactperson Property
     - PowerOfficeGov1 Data Type
   * - customer.id
     - partyId
     - "string"
   * - email
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - phoneNumberWork
     - phoneNumber
     - "string"


Tripletex Customer to PowerOfficeGov1 Customer
----------------------------------------------
Every Tripletex Customer will be synchronized with a PowerOfficeGov1 Customer.

If a matching PowerOfficeGov1 Customer already exists, the Tripletex Customer will be merged with the existing one.
If no matching PowerOfficeGov1 Customer is found, a new PowerOfficeGov1 Customer will be created.

A Tripletex Customer will merge with a PowerOfficeGov1 Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGov1 Customer Property
   * - email
     - email
   * - email
     - invoiceEmail
   * - invoiceEmail
     - email
   * - email
     - overdueNoticeEmail
   * - overdueNoticeEmail
     - email
   * - invoiceEmail
     - invoiceEmail
   * - invoiceEmail
     - overdueNoticeEmail
   * - overdueNoticeEmail
     - invoiceEmail
   * - organizationNumber
     - organizationNumber
   * - overdueNoticeEmail
     - overdueNoticeEmail

Once a link between a Tripletex Customer and a PowerOfficeGov1 Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGov1 Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGov1 Customer Property
     - PowerOfficeGov1 Data Type
   * - accountManager.id
     - accountManager.id
     - "integer"
   * - accountManager.id
     - ourReferenceEmployeeCode
     - "string"
   * - deliveryAddress.addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - deliveryAddress.addressLine1
     - mailAddress.address1
     - "string"
   * - deliveryAddress.addressLine1
     - streetAddresses.address1
     - "string"
   * - deliveryAddress.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - deliveryAddress.addressLine2
     - mailAddress.address2
     - "string"
   * - deliveryAddress.addressLine2
     - streetAddresses.address2
     - "string"
   * - deliveryAddress.city
     - deliveryAddress.city
     - "string"
   * - deliveryAddress.city
     - mailAddress.city
     - "string"
   * - deliveryAddress.city
     - streetAddresses.city
     - "string"
   * - deliveryAddress.country.id
     - deliveryAddress.country.id
     - "string"
   * - deliveryAddress.country.id
     - mailAddress.countryCode
     - "string"
   * - deliveryAddress.country.id
     - streetAddresses.countryCode
     - "string"
   * - deliveryAddress.postalCode
     - deliveryAddress.postalCode
     - "string"
   * - deliveryAddress.postalCode
     - mailAddress.zipCode
     - "string"
   * - deliveryAddress.postalCode
     - streetAddresses.zipCode
     - "string"
   * - email
     - email
     - "string"
   * - email
     - emailAddress
     - "string"
   * - id
     - id
     - "integer"
   * - invoiceEmail
     - InvoiceEmailAddressCC
     - "string"
   * - invoiceEmail
     - invoiceEmail
     - "string"
   * - name
     - legalName
     - "string"
   * - name
     - name
     - "string"
   * - organizationNumber
     - organizationNumber
     - "replace"," ","", "string"]
   * - organizationNumber
     - vatNumber (Dependant on having NO in mailAddress.countryCode)
     - "string"
   * - overdueNoticeEmail
     - overdueNoticeEmail
     - "string"
   * - phoneNumber
     - phone
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - phoneNumberMobile
     - phoneNumberMobile
     - "string"
   * - physicalAddress.addressLine1
     - address.addressLine1
     - "string"
   * - physicalAddress.addressLine1
     - mailAddress.address1
     - "string"
   * - physicalAddress.addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - physicalAddress.addressLine1
     - streetAddresses.address1
     - "string"
   * - physicalAddress.addressLine2
     - address.addressLine2
     - "string"
   * - physicalAddress.addressLine2
     - mailAddress.address2
     - "string"
   * - physicalAddress.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - physicalAddress.addressLine2
     - streetAddresses.address2
     - "string"
   * - physicalAddress.city
     - address.city
     - "string"
   * - physicalAddress.city
     - mailAddress.city
     - "string"
   * - physicalAddress.city
     - physicalAddress.city
     - "string"
   * - physicalAddress.city
     - streetAddresses.city
     - "string"
   * - physicalAddress.country.id
     - address.country.code
     - "string"
   * - physicalAddress.country.id
     - mailAddress.countryCode
     - "string"
   * - physicalAddress.country.id
     - physicalAddress.country.id
     - "integer"
   * - physicalAddress.country.id
     - streetAddresses.countryCode
     - "string"
   * - physicalAddress.postalCode
     - address.postalCode
     - "string"
   * - physicalAddress.postalCode
     - mailAddress.zipCode
     - "string"
   * - physicalAddress.postalCode
     - physicalAddress.postalCode
     - "string"
   * - physicalAddress.postalCode
     - streetAddresses.zipCode
     - "string"
   * - postalAddress.addressLine1
     - mailAddress.address1
     - "string"
   * - postalAddress.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - postalAddress.addressLine1
     - streetAddresses.address1
     - "string"
   * - postalAddress.addressLine2
     - mailAddress.address2
     - "string"
   * - postalAddress.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - postalAddress.addressLine2
     - streetAddresses.address2
     - "string"
   * - postalAddress.city
     - mailAddress.city
     - "string"
   * - postalAddress.city
     - postalAddress.city
     - "string"
   * - postalAddress.city
     - streetAddresses.city
     - "string"
   * - postalAddress.country.id
     - mailAddress.countryCode
     - "string"
   * - postalAddress.country.id
     - postalAddress.country.id
     - "integer"
   * - postalAddress.country.id
     - streetAddresses.countryCode
     - "string"
   * - postalAddress.postalCode
     - mailAddress.zipCode
     - "string"
   * - postalAddress.postalCode
     - postalAddress.postalCode
     - "string"
   * - postalAddress.postalCode
     - streetAddresses.zipCode
     - "string"


Tripletex Customer to PowerOfficeGov1 Customers
-----------------------------------------------
Every Tripletex Customer will be synchronized with a PowerOfficeGov1 Customers.

If a matching PowerOfficeGov1 Customers already exists, the Tripletex Customer will be merged with the existing one.
If no matching PowerOfficeGov1 Customers is found, a new PowerOfficeGov1 Customers will be created.

A Tripletex Customer will merge with a PowerOfficeGov1 Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGov1 Customers Property
   * - organizationNumber
     - OrgNumber

Once a link between a Tripletex Customer and a PowerOfficeGov1 Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGov1 Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGov1 Customers Property
     - PowerOfficeGov1 Data Type
   * - organizationNumber
     - OrgNumber
     - "string"


Tripletex Customercategory to PowerOfficeGov1 Customercategory
--------------------------------------------------------------
Every Tripletex Customercategory will be synchronized with a PowerOfficeGov1 Customercategory.

Once a link between a Tripletex Customercategory and a PowerOfficeGov1 Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customercategory and a PowerOfficeGov1 Customercategory:

.. list-table::
   :header-rows: 1

   * - Tripletex Customercategory Property
     - PowerOfficeGov1 Customercategory Property
     - PowerOfficeGov1 Data Type
   * - name
     - name
     - "string"
   * - number
     - number
     - "string"


Tripletex Department to PowerOfficeGov1 Department
--------------------------------------------------
Every Tripletex Department will be synchronized with a PowerOfficeGov1 Department.

Once a link between a Tripletex Department and a PowerOfficeGov1 Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a PowerOfficeGov1 Department:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOfficeGov1 Department Property
     - PowerOfficeGov1 Data Type
   * - departmentNumber
     - departmentNumber
     - "string"
   * - name
     - name
     - "string"


Tripletex Department to PowerOfficeGov1 Departments
---------------------------------------------------
Every Tripletex Department will be synchronized with a PowerOfficeGov1 Departments.

Once a link between a Tripletex Department and a PowerOfficeGov1 Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a PowerOfficeGov1 Departments:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOfficeGov1 Departments Property
     - PowerOfficeGov1 Data Type
   * - departmentNumber
     - DepartmentNumber
     - "string"
   * - name
     - Name
     - "string"


Tripletex Employee to PowerOfficeGov1 Employee
----------------------------------------------
Every Tripletex Employee will be synchronized with a PowerOfficeGov1 Employee.

If a matching PowerOfficeGov1 Employee already exists, the Tripletex Employee will be merged with the existing one.
If no matching PowerOfficeGov1 Employee is found, a new PowerOfficeGov1 Employee will be created.

A Tripletex Employee will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOfficeGov1 Employee Property
   * - id
     - id
   * - email
     - email
   * - employeeNumber
     - employeeNumber
   * - nationalIdentityNumber
     - SocialSecurityNumber
   * - nationalIdentityNumber
     - nationalIdentityNumber

Once a link between a Tripletex Employee and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - MailAddress.Address1
     - "string"
   * - address.addressLine1
     - address.addressLine1
     - "string"
   * - address.addressLine2
     - MailAddress.Address2
     - "string"
   * - address.addressLine2
     - address.addressLine2
     - "string"
   * - address.city
     - MailAddress.City
     - "string"
   * - address.city
     - address.city
     - "string"
   * - address.country.id
     - MailAddress.CountryCode
     - "string"
   * - address.country.id
     - address.country.id
     - "integer"
   * - address.postalCode
     - MailAddress.ZipCode
     - "string"
   * - address.postalCode
     - address.postalCode
     - "string"
   * - dateOfBirth
     - DateOfBirth
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - "datetime-format","%Y-%m-%d","_."]
   * - department.id
     - department.id
     - "if", "neq", "_.", "X"], "integer", "string"]
   * - email
     - email
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - Id
     - "string"
   * - id
     - id
     - "integer"
   * - lastName
     - LastName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - phoneNumberHome
     - phoneNumberHome
     - "string"
   * - phoneNumberMobile
     - phoneNumberMobile
     - "string"
   * - phoneNumberWork
     - phoneNumberWork
     - "string"
   * - userType
     - userType
     - "string"


Tripletex Invoice to PowerOfficeGov1 Invoice
--------------------------------------------
Every Tripletex Invoice will be synchronized with a PowerOfficeGov1 Invoice.

Once a link between a Tripletex Invoice and a PowerOfficeGov1 Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Invoice and a PowerOfficeGov1 Invoice:

.. list-table::
   :header-rows: 1

   * - Tripletex Invoice Property
     - PowerOfficeGov1 Invoice Property
     - PowerOfficeGov1 Data Type
   * - amountExcludingVat
     - amountExcludingVat
     - "integer"
   * - currency.id
     - currency.code
     - "string"
   * - currency.id
     - currency.id
     - "integer"
   * - customer.id
     - customer.id
     - "string"
   * - deliveryDate
     - deliveryDate
     - "datetime-format","%Y-%m-%d","_."]
   * - invoiceDate
     - invoiceDate
     - "datetime-format","%Y-%m-%d","_."]
   * - invoiceDueDate
     - dueDate
     - "datetime-format","%Y-%m-%d","_."]
   * - invoiceDueDate
     - invoiceDueDate
     - "datetime-format","%Y-%m-%d","_."]
   * - orders.id
     - orders.id
     - "integer"


Tripletex Invoice to PowerOfficeGov1 Outgoinginvoice
----------------------------------------------------
Every Tripletex Invoice will be synchronized with a PowerOfficeGov1 Outgoinginvoice.

Once a link between a Tripletex Invoice and a PowerOfficeGov1 Outgoinginvoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Invoice and a PowerOfficeGov1 Outgoinginvoice:

.. list-table::
   :header-rows: 1

   * - Tripletex Invoice Property
     - PowerOfficeGov1 Outgoinginvoice Property
     - PowerOfficeGov1 Data Type
   * - amountExcludingVat
     - NetAmount
     - "string"
   * - changes.timestamp
     - CreatedDate
     - "string"
   * - currency.id
     - CurrencyCode
     - "string"
   * - customer.id
     - CustomerCode
     - "string"
   * - deliveryDate
     - DeliveryDate
     - "string"
   * - deliveryDate
     - SentDate
     - "string"
   * - orders.id
     - OrderNo
     - "string"


Tripletex Order to PowerOfficeGov1 Invoice
------------------------------------------
Every Tripletex Order will be synchronized with a PowerOfficeGov1 Invoice.

Once a link between a Tripletex Order and a PowerOfficeGov1 Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a PowerOfficeGov1 Invoice:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - PowerOfficeGov1 Invoice Property
     - PowerOfficeGov1 Data Type
   * - currency.id
     - currency.code
     - "string"
   * - currency.id
     - currency.id
     - "integer"
   * - customer.id
     - customer.id
     - "string"
   * - deliveryDate
     - deliveryDate
     - "datetime-format","%Y-%m-%d","_."]
   * - invoiceComment
     - title
     - "string"
   * - reference
     - poNumber
     - "string"


Tripletex Order to PowerOfficeGov1 Order
----------------------------------------
Every Tripletex Order will be synchronized with a PowerOfficeGov1 Order.

Once a link between a Tripletex Order and a PowerOfficeGov1 Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a PowerOfficeGov1 Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - PowerOfficeGov1 Order Property
     - PowerOfficeGov1 Data Type
   * - contact.id
     - contact.id
     - "integer"
   * - currency.id
     - currency.id
     - "integer"
   * - customer.id
     - customer.id
     - "integer"
   * - deliveryDate
     - deliveryDate
     - "datetime-format","%Y-%m-%d","_."]
   * - invoiceComment
     - invoiceComment
     - "string"
   * - orderDate
     - orderDate
     - "datetime-format","%Y-%m-%d","_."]
   * - ourContactEmployee.id
     - ourContactEmployee.id
     - "integer"
   * - overdueNoticeEmail
     - overdueNoticeEmail
     - "string"
   * - reference
     - reference
     - "string"


Tripletex Order to PowerOfficeGov1 Salesorder
---------------------------------------------
Every Tripletex Order will be synchronized with a PowerOfficeGov1 Salesorder.

Once a link between a Tripletex Order and a PowerOfficeGov1 Salesorder is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a PowerOfficeGov1 Salesorder:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - PowerOfficeGov1 Salesorder Property
     - PowerOfficeGov1 Data Type
   * - currency.id
     - Currency
     - "string"
   * - customer.id
     - DepartmentCode
     - "string"
   * - deliveryDate
     - DeliveryDate
     - "string"
   * - orderDate
     - OrderDate
     - "string"


Tripletex Orderline to PowerOfficeGov1 Orderline
------------------------------------------------
Every Tripletex Orderline will be synchronized with a PowerOfficeGov1 Orderline.

Once a link between a Tripletex Orderline and a PowerOfficeGov1 Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a PowerOfficeGov1 Orderline:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - PowerOfficeGov1 Orderline Property
     - PowerOfficeGov1 Data Type
   * - count
     - count
     - "float"
   * - description
     - description
     - "string"
   * - discount
     - discount
     - "float"
   * - order.id
     - order.id
     - "integer"
   * - product.id
     - product.id
     - "integer"
   * - unitCostCurrency
     - unitCostCurrency
     - "float"
   * - unitPriceExcludingVatCurrency
     - unitPriceExcludingVatCurrency
     - "float"
   * - vatType.id
     - vatType.id
     - "integer"


Tripletex Orderline to PowerOfficeGov1 Quoteline
------------------------------------------------
Every Tripletex Orderline will be synchronized with a PowerOfficeGov1 Quoteline.

Once a link between a Tripletex Orderline and a PowerOfficeGov1 Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a PowerOfficeGov1 Quoteline:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - PowerOfficeGov1 Quoteline Property
     - PowerOfficeGov1 Data Type
   * - count
     - Quantity
     - "integer"
   * - description
     - Name
     - "string"
   * - discount
     - DiscountPercent
     - "integer"
   * - order.id
     - QuoteAlternativeId
     - "integer"
   * - product.id
     - ERPProductKey
     - "string"
   * - unitPriceExcludingVatCurrency
     - UnitListPrice
     - "string"
   * - vatType.id
     - VAT
     - "integer"


Tripletex Orderline to PowerOfficeGov1 Salesorderline
-----------------------------------------------------
Every Tripletex Orderline will be synchronized with a PowerOfficeGov1 Salesorderline.

Once a link between a Tripletex Orderline and a PowerOfficeGov1 Salesorderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a PowerOfficeGov1 Salesorderline:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - PowerOfficeGov1 Salesorderline Property
     - PowerOfficeGov1 Data Type
   * - count
     - Quantity
     - "string"
   * - description
     - Description
     - "string"
   * - discount
     - Discount
     - "string"
   * - unitPriceExcludingVatCurrency
     - SalesOrderLineUnitPrice
     - "string"
   * - vatType.id
     - VatReturnSpecification
     - "string"


Tripletex Product to PowerOfficeGov1 Product
--------------------------------------------
Every Tripletex Product will be synchronized with a PowerOfficeGov1 Product.

If a matching PowerOfficeGov1 Product already exists, the Tripletex Product will be merged with the existing one.
If no matching PowerOfficeGov1 Product is found, a new PowerOfficeGov1 Product will be created.

A Tripletex Product will merge with a PowerOfficeGov1 Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - PowerOfficeGov1 Product Property
   * - id
     - id
   * - number
     - number
   * - number
     - ERPProductKey

Once a link between a Tripletex Product and a PowerOfficeGov1 Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a PowerOfficeGov1 Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - PowerOfficeGov1 Product Property
     - PowerOfficeGov1 Data Type
   * - costExcludingVatCurrency
     - UnitCost
     - "string"
   * - costExcludingVatCurrency
     - costExcludingVatCurrency
     - "integer"
   * - costExcludingVatCurrency
     - costPrice
     - "string"
   * - currency.id
     - ERPPriceListKey
     - "string"
   * - currency.id
     - currency.id
     - "integer"
   * - description
     - Description
     - "string"
   * - description
     - description
     - "string"
   * - ean
     - ean
     - "string"
   * - ean
     - gtin
     - "string"
   * - name
     - Name
     - "string"
   * - name
     - name
     - "string"
   * - number
     - number
     - "string"
   * - priceExcludingVatCurrency
     - UnitListPrice
     - "decimal"
   * - priceExcludingVatCurrency
     - priceExcludingVatCurrency
     - "float"
   * - priceExcludingVatCurrency
     - salesPrice
     - "string"
   * - priceExcludingVatCurrency
     - unitPrice
     - "string"
   * - productUnit.id
     - QuantityUnit
     - "string"
   * - productUnit.id
     - productUnit.id
     - "integer"
   * - productUnit.id
     - unitOfMeasureCode
     - "string"
   * - stockOfGoods
     - availableStock
     - "string"
   * - stockOfGoods
     - stockOfGoods
     - "integer"
   * - supplier.id
     - Supplier
     - "string"
   * - supplier.id
     - supplier.id
     - "integer"
   * - vatType.id
     - VAT
     - "integer"
   * - vatType.id
     - vatCode
     - "string"
   * - vatType.id
     - vatType.id
     - "integer"


Tripletex Productgroup to PowerOfficeGov1 Listproductcategoryitems
------------------------------------------------------------------
Every Tripletex Productgroup will be synchronized with a PowerOfficeGov1 Listproductcategoryitems.

Once a link between a Tripletex Productgroup and a PowerOfficeGov1 Listproductcategoryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgroup and a PowerOfficeGov1 Listproductcategoryitems:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgroup Property
     - PowerOfficeGov1 Listproductcategoryitems Property
     - PowerOfficeGov1 Data Type
   * - name
     - Name
     - "string"


Tripletex Productgroup to PowerOfficeGov1 Productgroup
------------------------------------------------------
Every Tripletex Productgroup will be synchronized with a PowerOfficeGov1 Productgroup.

Once a link between a Tripletex Productgroup and a PowerOfficeGov1 Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgroup and a PowerOfficeGov1 Productgroup:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgroup Property
     - PowerOfficeGov1 Productgroup Property
     - PowerOfficeGov1 Data Type
   * - name
     - Name
     - "string"
   * - name
     - name
     - "string"
   * - parentGroup.id
     - parentGroup.id
     - "integer"
   * - url
     - url
     - "string"


Tripletex Productunit to PowerOfficeGov1 Productunit
----------------------------------------------------
Every Tripletex Productunit will be synchronized with a PowerOfficeGov1 Productunit.

If a matching PowerOfficeGov1 Productunit already exists, the Tripletex Productunit will be merged with the existing one.
If no matching PowerOfficeGov1 Productunit is found, a new PowerOfficeGov1 Productunit will be created.

A Tripletex Productunit will merge with a PowerOfficeGov1 Productunit if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Productunit Property
     - PowerOfficeGov1 Productunit Property
   * - name
     - name

Once a link between a Tripletex Productunit and a PowerOfficeGov1 Productunit is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productunit and a PowerOfficeGov1 Productunit:

.. list-table::
   :header-rows: 1

   * - Tripletex Productunit Property
     - PowerOfficeGov1 Productunit Property
     - PowerOfficeGov1 Data Type
   * - commonCode
     - commonCode
     - "string"
   * - name
     - name
     - "string"
   * - url
     - url
     - "string"


Tripletex Project to PowerOfficeGov1 Projects
---------------------------------------------
Every Tripletex Project will be synchronized with a PowerOfficeGov1 Projects.

Once a link between a Tripletex Project and a PowerOfficeGov1 Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a PowerOfficeGov1 Projects:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     - PowerOfficeGov1 Projects Property
     - PowerOfficeGov1 Data Type
   * - endDate
     - due_on
     - "string"
   * - name
     - name
     - "string"
   * - projectManager.id
     - owner.gid
     - "string"
   * - startDate
     - start_on
     - "string"


Tripletex Projectcategory to PowerOfficeGov1 Projectcategory
------------------------------------------------------------
Every Tripletex Projectcategory will be synchronized with a PowerOfficeGov1 Projectcategory.

Once a link between a Tripletex Projectcategory and a PowerOfficeGov1 Projectcategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Projectcategory and a PowerOfficeGov1 Projectcategory:

.. list-table::
   :header-rows: 1

   * - Tripletex Projectcategory Property
     - PowerOfficeGov1 Projectcategory Property
     - PowerOfficeGov1 Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - number
     - number
     - "string"
   * - url
     - url
     - "string"


Tripletex Supplier to PowerOfficeGov1 Supplier
----------------------------------------------
Every Tripletex Supplier will be synchronized with a PowerOfficeGov1 Supplier.

If a matching PowerOfficeGov1 Supplier already exists, the Tripletex Supplier will be merged with the existing one.
If no matching PowerOfficeGov1 Supplier is found, a new PowerOfficeGov1 Supplier will be created.

A Tripletex Supplier will merge with a PowerOfficeGov1 Supplier if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOfficeGov1 Supplier Property
   * - email
     - email
   * - email
     - invoiceEmail
   * - invoiceEmail
     - email
   * - email
     - overdueNoticeEmail
   * - overdueNoticeEmail
     - email
   * - invoiceEmail
     - invoiceEmail
   * - invoiceEmail
     - overdueNoticeEmail
   * - overdueNoticeEmail
     - invoiceEmail
   * - organizationNumber
     - organizationNumber
   * - overdueNoticeEmail
     - overdueNoticeEmail

Once a link between a Tripletex Supplier and a PowerOfficeGov1 Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a PowerOfficeGov1 Supplier:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOfficeGov1 Supplier Property
     - PowerOfficeGov1 Data Type
   * - deliveryAddress.addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - deliveryAddress.changes
     - deliveryAddress.changes
     - "string"
   * - deliveryAddress.city
     - deliveryAddress.city
     - "string"
   * - deliveryAddress.postalCode
     - deliveryAddress.postalCode
     - "string"
   * - email
     - EmailAddress
     - "string"
   * - email
     - email
     - "string"
   * - id
     - Id
     - "string"
   * - id
     - id
     - "integer"
   * - invoiceEmail
     - invoiceEmail
     - "string"
   * - name
     - LegalName
     - "string"
   * - name
     - name
     - "string"
   * - overdueNoticeEmail
     - overdueNoticeEmail
     - "string"
   * - phoneNumber
     - PhoneNumber
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - phoneNumberMobile
     - phoneNumberMobile
     - "string"
   * - physicalAddress.addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - physicalAddress.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - physicalAddress.city
     - physicalAddress.city
     - "string"
   * - physicalAddress.country.id
     - physicalAddress.country.id
     - "integer"
   * - physicalAddress.postalCode
     - physicalAddress.postalCode
     - "string"
   * - postalAddress.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - postalAddress.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - postalAddress.city
     - postalAddress.city
     - "string"
   * - postalAddress.country.id
     - postalAddress.country.id
     - "integer"
   * - postalAddress.postalCode
     - postalAddress.postalCode
     - "string"


Tripletex Supplier to PowerOfficeGov1 Vendor
--------------------------------------------
Every Tripletex Supplier will be synchronized with a PowerOfficeGov1 Vendor.

Once a link between a Tripletex Supplier and a PowerOfficeGov1 Vendor is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a PowerOfficeGov1 Vendor:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOfficeGov1 Vendor Property
     - PowerOfficeGov1 Data Type
   * - name
     - name
     - "string"
   * - physicalAddress.addressLine1
     - address.addressLine1
     - "string"
   * - physicalAddress.addressLine2
     - address.addressLine2
     - "string"
   * - physicalAddress.city
     - address.city
     - "string"
   * - physicalAddress.country.id
     - address.country.code
     - "string"
   * - physicalAddress.postalCode
     - address.postalCode
     - "string"


Tripletex Vattype to PowerOfficeGov1 Vatcode
--------------------------------------------
Every Tripletex Vattype will be synchronized with a PowerOfficeGov1 Vatcode.

Once a link between a Tripletex Vattype and a PowerOfficeGov1 Vatcode is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Vattype and a PowerOfficeGov1 Vatcode:

.. list-table::
   :header-rows: 1

   * - Tripletex Vattype Property
     - PowerOfficeGov1 Vatcode Property
     - PowerOfficeGov1 Data Type
   * - name
     - name
     - "string"
   * - percentage
     - rate
     - "string"

