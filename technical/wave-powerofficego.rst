===============================
Wave to PowerOffice GO Dataflow
===============================

Generated: 2024-09-21 00:01:13

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to PowerOffice GO Contactperson
---------------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a PowerOffice GO Contactperson must be established.

A Wave Customer will merge with a PowerOffice GO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOffice GO Contactperson Property
   * - email
     - emailAddress

Once a link between a Wave Customer and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
   * - address.addressLine1
     - address1
     - "string"
   * - address.addressLine2
     - address2
     - "string"
   * - address.city
     - city
     - "string"
   * - address.country.code
     - residenceCountryCode
     - "string"
   * - address.postalCode
     - zipCode
     - "string"
   * - email
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "integer"
   * - lastName
     - lastName
     - "string"
   * - phone
     - phoneNumber
     - "string"
   * - shippingDetails.address.addressLine1
     - address1
     - "string"
   * - shippingDetails.address.addressLine2
     - address2
     - "string"
   * - shippingDetails.address.city
     - city
     - "string"
   * - shippingDetails.address.country.code
     - residenceCountryCode
     - "string"
   * - shippingDetails.address.postalCode
     - zipCode
     - "string"
   * - shippingDetails.phone
     - phoneNumber
     - "string"


Wave Customer to PowerOffice GO Customers
-----------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a PowerOffice GO Customers must be established.

A Wave Customer will merge with a PowerOffice GO Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOffice GO Customers Property
   * - email
     - EmailAddress

Once a link between a Wave Customer and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
   * - address.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - address.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - address.city
     - MailAddress.City
     - "string"
   * - address.country.code
     - MailAddress.CountryCode
     - "string"
   * - address.postalCode
     - MailAddress.ZipCode
     - "string"
   * - email
     - EmailAddress
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - id
     - Id
     - "integer"
   * - lastName
     - LastName
     - "string"
   * - phone
     - PhoneNumber
     - "string"
   * - shippingDetails.address.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - shippingDetails.address.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - shippingDetails.address.city
     - MailAddress.City
     - "string"
   * - shippingDetails.address.country.code
     - MailAddress.CountryCode
     - "string"
   * - shippingDetails.address.postalCode
     - MailAddress.ZipCode
     - "string"
   * - shippingDetails.phone
     - PhoneNumber
     - "string"


Wave Customer to PowerOffice GO Contactperson
---------------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a PowerOffice GO Contactperson must be established.

A new PowerOffice GO Contactperson will be created from a Wave Customer if it is connected to a Wave Invoice that is synchronized into PowerOffice GO.

A Wave Customer will merge with a PowerOffice GO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOffice GO Contactperson Property
   * - email
     - emailAddress

Once a link between a Wave Customer and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
   * - email
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - partyId
     - "integer"
   * - lastName
     - lastName
     - "string"


Wave Customer to PowerOffice GO Customers
-----------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a PowerOffice GO Customers must be established.

A new PowerOffice GO Customers will be created from a Wave Customer if it is connected to a Wave Vendor, Invoice, Customer, Customer-person, or Customer-contact that is synchronized into PowerOffice GO.

A Wave Customer will merge with a PowerOffice GO Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOffice GO Customers Property
   * - email
     - EmailAddress

Once a link between a Wave Customer and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type


Wave Vendor to PowerOffice GO Contactperson
-------------------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a PowerOffice GO Contactperson must be established.

A Wave Vendor will merge with a PowerOffice GO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOffice GO Contactperson Property
   * - email
     - emailAddress

Once a link between a Wave Vendor and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
   * - address.addressLine1
     - address1
     - "string"
   * - address.addressLine2
     - address2
     - "string"
   * - address.city
     - city
     - "string"
   * - address.country.code
     - residenceCountryCode
     - "string"
   * - address.postalCode
     - zipCode
     - "string"
   * - email
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "integer"
   * - id
     - partyId
     - "integer"
   * - lastName
     - lastName
     - "string"
   * - phone
     - phoneNumber
     - "string"


Wave Vendor to PowerOffice GO Customers
---------------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a PowerOffice GO Customers must be established.

A new PowerOffice GO Customers will be created from a Wave Vendor if it is connected to a Wave Vendor, Customer, Customer-person, or Customer-contact that is synchronized into PowerOffice GO.

A Wave Vendor will merge with a PowerOffice GO Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOffice GO Customers Property
   * - email
     - EmailAddress

Once a link between a Wave Vendor and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
   * - address.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - address.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - address.city
     - MailAddress.City
     - "string"
   * - address.country.code
     - MailAddress.CountryCode
     - "string"
   * - address.postalCode
     - MailAddress.ZipCode
     - "string"
   * - id
     - Id
     - "integer"


Wave Customer (organisation data) to PowerOffice GO Customers
-------------------------------------------------------------
Every Wave Customer (organisation data) will be synchronized with a PowerOffice GO Customers.

Once a link between a Wave Customer (organisation data) and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer (organisation data) and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Wave Customer (organisation data) Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type


Wave Customer (human data) to PowerOffice GO Customers (human data)
-------------------------------------------------------------------
Every Wave Customer (human data) will be synchronized with a PowerOffice GO Customers (human data).

Once a link between a Wave Customer (human data) and a PowerOffice GO Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer (human data) and a PowerOffice GO Customers (human data):

.. list-table::
   :header-rows: 1

   * - Wave Customer (human data) Property
     - PowerOffice GO Customers (human data) Property
     - PowerOffice GO Data Type


Wave Customer to PowerOffice GO Contactperson
---------------------------------------------
Every Wave Customer will be synchronized with a PowerOffice GO Contactperson.

Once a link between a Wave Customer and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type


Wave Customer to PowerOffice GO Customers
-----------------------------------------
Every Wave Customer will be synchronized with a PowerOffice GO Customers.

Once a link between a Wave Customer and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
   * - address.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - address.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - address.city
     - MailAddress.City
     - "string"
   * - address.country.code
     - MailAddress.CountryCode
     - "string"
   * - address.postalCode
     - MailAddress.ZipCode
     - "string"
   * - id
     - Id
     - "integer"
   * - name
     - Name
     - "string"
   * - phone
     - PhoneNumber
     - "string"
   * - shippingDetails.address.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - shippingDetails.address.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - shippingDetails.address.city
     - MailAddress.City
     - "string"
   * - shippingDetails.address.country.code
     - MailAddress.CountryCode
     - "string"
   * - shippingDetails.address.postalCode
     - MailAddress.ZipCode
     - "string"
   * - shippingDetails.phone
     - PhoneNumber
     - "string"
   * - website
     - WebsiteUrl
     - "string"


Wave Customer to PowerOffice GO Customers (human data)
------------------------------------------------------
Every Wave Customer will be synchronized with a PowerOffice GO Customers (human data).

Once a link between a Wave Customer and a PowerOffice GO Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOffice GO Customers (human data):

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOffice GO Customers (human data) Property
     - PowerOffice GO Data Type


Wave Invoice to PowerOffice GO Salesorderlines
----------------------------------------------
Every Wave Invoice will be synchronized with a PowerOffice GO Salesorderlines.

Once a link between a Wave Invoice and a PowerOffice GO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a PowerOffice GO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - PowerOffice GO Salesorderlines Property
     - PowerOffice GO Data Type


Wave Invoice to PowerOffice GO Salesorders
------------------------------------------
Every Wave Invoice will be synchronized with a PowerOffice GO Salesorders.

Once a link between a Wave Invoice and a PowerOffice GO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a PowerOffice GO Salesorders:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - PowerOffice GO Salesorders Property
     - PowerOffice GO Data Type


Wave Product to PowerOffice GO Product
--------------------------------------
Every Wave Product will be synchronized with a PowerOffice GO Product.

Once a link between a Wave Product and a PowerOffice GO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a PowerOffice GO Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - PowerOffice GO Product Property
     - PowerOffice GO Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - unitPrice
     - salesPrice
     - N/A


Wave Vendor to PowerOffice GO Contactperson
-------------------------------------------
Every Wave Vendor will be synchronized with a PowerOffice GO Contactperson.

Once a link between a Wave Vendor and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type

