==============================
PowerOfficeGO to Wave Dataflow
==============================

Generated: 2024-09-11 11:13:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOfficeGO to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOfficeGOPowerofficegoPowerOffice GO Contactperson to Wave Customer person
------------------------------------------------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGOPowerofficegoPowerOffice GO Contactperson and a Wave Customer person must be established.

A new Wave Customer person will be created from a PowerOfficeGOPowerofficegoPowerOffice GO Contactperson if it is connected to a PowerOfficeGOPowerofficegoPowerOffice GO Powerofficego-salesorder, Powerofficego-salesorders, Powerofficego-salesorderlines, or Powerofficego-outgoinginvoices that is synchronized into Wave.

A PowerOfficeGOPowerofficegoPowerOffice GO Contactperson will merge with a Wave Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGOPowerofficegoPowerOffice GO Contactperson Property
     - Wave Customer person Property
   * - emailAddress
     - email

Once a link between a PowerOfficeGOPowerofficegoPowerOffice GO Contactperson and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGOPowerofficegoPowerOffice GO Contactperson and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGOPowerofficegoPowerOffice GO Contactperson Property
     - Wave Customer person Property
     - Wave Data Type
   * - address1
     - address.addressLine1
     - "string"
   * - address1
     - shippingDetails.address.addressLine1
     - "string"
   * - address2
     - address.addressLine2
     - "string"
   * - address2
     - shippingDetails.address.addressLine2
     - "string"
   * - city
     - address.city
     - "string"
   * - city
     - shippingDetails.address.city
     - "string"
   * - emailAddress
     - email
     - "string"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - N/A
   * - phoneNumber
     - phone
     - "string"
   * - residenceCountryCode
     - address.country.code
     - "string"
   * - residenceCountryCode
     - shippingDetails.address.country.code
     - "string"
   * - zipCode
     - address.postalCode
     - "string"
   * - zipCode
     - shippingDetails.address.postalCode
     - "string"


PowerofficegoPowerOfficeGOPowerOffice GO Contactperson to Wave Customer
-----------------------------------------------------------------------
Before any synchronization can take place, a link between a PowerofficegoPowerOfficeGOPowerOffice GO Contactperson and a Wave Customer must be established.

A new Wave Customer will be created from a PowerofficegoPowerOfficeGOPowerOffice GO Contactperson if it is connected to a PowerofficegoPowerOfficeGOPowerOffice GO Powerofficego-salesorder, Powerofficego-salesorders, Powerofficego-salesorderlines, or Powerofficego-outgoinginvoices that is synchronized into Wave.

Once a link between a PowerofficegoPowerOfficeGOPowerOffice GO Contactperson and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerofficegoPowerOfficeGOPowerOffice GO Contactperson and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - PowerofficegoPowerOfficeGOPowerOffice GO Contactperson Property
     - Wave Customer Property
     - Wave Data Type
   * - address1
     - address.addressLine1
     - "string"
   * - address1
     - shippingDetails.address.addressLine1
     - "string"
   * - address2
     - address.addressLine2
     - "string"
   * - address2
     - shippingDetails.address.addressLine2
     - "string"
   * - city
     - address.city
     - "string"
   * - city
     - shippingDetails.address.city
     - "string"
   * - emailAddress
     - email
     - "string"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - residenceCountryCode
     - address.country.code
     - "string"
   * - residenceCountryCode
     - shippingDetails.address.country.code
     - "string"
   * - zipCode
     - address.postalCode
     - "string"
   * - zipCode
     - shippingDetails.address.postalCode
     - "string"


PowerofficegoPowerOfficeGOPowerOffice GO Customers to Wave Customer person
--------------------------------------------------------------------------
Before any synchronization can take place, a link between a PowerofficegoPowerOfficeGOPowerOffice GO Customers and a Wave Customer person must be established.

A new Wave Customer person will be created from a PowerofficegoPowerOfficeGOPowerOffice GO Customers if it is connected to a PowerofficegoPowerOfficeGOPowerOffice GO Powerofficego-customer, Powerofficego-customers, Powerofficego-employees, Powerofficego-suppliers, Powerofficego-salesorder, Powerofficego-departments, Powerofficego-salesorders, Powerofficego-contactperson, Powerofficego-salesorderlines, Powerofficego-outgoinginvoices, or Powerofficego-customers-organisation that is synchronized into Wave.

Once a link between a PowerofficegoPowerOfficeGOPowerOffice GO Customers and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerofficegoPowerOfficeGOPowerOffice GO Customers and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - PowerofficegoPowerOfficeGOPowerOffice GO Customers Property
     - Wave Customer person Property
     - Wave Data Type
   * - EmailAddress
     - email
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"
   * - MailAddress.AddressLine1
     - address.addressLine1
     - "string"
   * - MailAddress.AddressLine2
     - address.addressLine2
     - "string"
   * - MailAddress.City
     - address.city
     - "string"
   * - MailAddress.CountryCode
     - address.country.code
     - "string"
   * - MailAddress.ZipCode
     - address.postalCode
     - "string"
   * - PhoneNumber
     - phone
     - "string"
   * - WebsiteUrl
     - website
     - "string"


PowerOfficeGO Customers person to Wave Customer person
------------------------------------------------------
Every PowerOfficeGO Customers person will be synchronized with a Wave Customer person.

If a matching Wave Customer person already exists, the PowerOfficeGO Customers person will be merged with the existing one.
If no matching Wave Customer person is found, a new Wave Customer person will be created.

A PowerOfficeGO Customers person will merge with a Wave Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers person Property
     - Wave Customer person Property
   * - EmailAddress
     - email

Once a link between a PowerOfficeGO Customers person and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers person and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers person Property
     - Wave Customer person Property
     - Wave Data Type
   * - EmailAddress
     - email
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - N/A
   * - MailAddress.AddressLine1
     - address.addressLine1
     - "string"
   * - MailAddress.AddressLine1
     - shippingDetails.address.addressLine1
     - "string"
   * - MailAddress.AddressLine2
     - address.addressLine2
     - "string"
   * - MailAddress.AddressLine2
     - shippingDetails.address.addressLine2
     - "string"
   * - MailAddress.City
     - address.city
     - "string"
   * - MailAddress.City
     - shippingDetails.address.city
     - "string"
   * - MailAddress.CountryCode
     - address.country.code
     - "string"
   * - MailAddress.CountryCode
     - shippingDetails.address.country.code
     - "string"
   * - MailAddress.ZipCode
     - address.postalCode
     - "string"
   * - MailAddress.ZipCode
     - shippingDetails.address.postalCode
     - "string"
   * - PhoneNumber
     - phone
     - "string"


PowerOfficeGOPowerofficegoPowerOffice GO Customers to Wave Customer
-------------------------------------------------------------------
Every PowerOfficeGOPowerofficegoPowerOffice GO Customers will be synchronized with a Wave Customer.

Once a link between a PowerOfficeGOPowerofficegoPowerOffice GO Customers and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGOPowerofficegoPowerOffice GO Customers and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGOPowerofficegoPowerOffice GO Customers Property
     - Wave Customer Property
     - Wave Data Type
   * - EmailAddress
     - email
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"
   * - MailAddress.AddressLine1
     - address.addressLine1
     - "string"
   * - MailAddress.AddressLine1
     - shippingDetails.address.addressLine1
     - "string"
   * - MailAddress.AddressLine2
     - address.addressLine2
     - "string"
   * - MailAddress.AddressLine2
     - shippingDetails.address.addressLine2
     - "string"
   * - MailAddress.City
     - address.city
     - "string"
   * - MailAddress.City
     - shippingDetails.address.city
     - "string"
   * - MailAddress.CountryCode
     - address.country.code
     - "string"
   * - MailAddress.CountryCode
     - shippingDetails.address.country.code
     - "string"
   * - MailAddress.ZipCode
     - address.postalCode
     - "string"
   * - MailAddress.ZipCode
     - shippingDetails.address.postalCode
     - "string"
   * - Name
     - name
     - N/A
   * - Number
     - phone
     - "string"
   * - PhoneNumber
     - phone
     - "string"
   * - WebsiteUrl
     - website
     - "string"
   * - emailAddress
     - email
     - "string"
   * - firstName
     - firstName
     - "string"
   * - legalName
     - name
     - "string"
   * - name
     - name
     - "string"
   * - phoneNumber
     - phone
     - "string"
   * - streetAddresses.address1
     - address.addressLine1
     - "string"
   * - streetAddresses.address2
     - address.addressLine2
     - "string"
   * - streetAddresses.city
     - address.city
     - "string"
   * - streetAddresses.countryCode
     - address.country.code
     - "string"
   * - streetAddresses.zipCode
     - address.postalCode
     - "string"
   * - websiteUrl
     - website
     - "string"


PowerOfficeGOPowerofficegoPowerOffice GO Product to Wave Product
----------------------------------------------------------------
Every PowerOfficeGOPowerofficegoPowerOffice GO Product will be synchronized with a Wave Product.

Once a link between a PowerOfficeGOPowerofficegoPowerOffice GO Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGOPowerofficegoPowerOffice GO Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGOPowerofficegoPowerOffice GO Product Property
     - Wave Product Property
     - Wave Data Type
   * - Description
     - description
     - "string"
   * - Name
     - name
     - "string"
   * - SalesPrice
     - unitPrice
     - "string"
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - salesPrice
     - unitPrice
     - "string"


PowerOfficeGOPowerofficegoPowerOffice GO Salesorders to Wave Invoice
--------------------------------------------------------------------
Every PowerOfficeGOPowerofficegoPowerOffice GO Salesorders will be synchronized with a Wave Invoice.

Once a link between a PowerOfficeGOPowerofficegoPowerOffice GO Salesorders and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGOPowerofficegoPowerOffice GO Salesorders and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGOPowerofficegoPowerOffice GO Salesorders Property
     - Wave Invoice Property
     - Wave Data Type
   * - CurrencyCode
     - currency.code
     - "string"
   * - CustomerId
     - customer.id
     - "string"
   * - CustomerReferenceContactPersonId
     - customer.id
     - "string"
   * - PurchaseOrderReference
     - poNumber
     - "string"

