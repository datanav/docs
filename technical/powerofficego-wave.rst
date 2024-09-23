===============================
PowerOffice GO to Wave Dataflow
===============================

Generated: 2024-09-23 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Contactperson to Wave Customer
---------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Contactperson and a Wave Customer must be established.

A new Wave Customer will be created from a PowerOffice GO Contactperson if it is connected to a PowerOffice GO Powerofficego-salesorder, Powerofficego-salesorders, Powerofficego-salesorderlines, or Powerofficego-outgoinginvoices that is synchronized into Wave.

A PowerOffice GO Contactperson will merge with a Wave Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Wave Customer Property
   * - emailAddress
     - email

Once a link between a PowerOffice GO Contactperson and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
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


PowerOffice GO Customers to Wave Customer
-----------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers and a Wave Customer must be established.

A PowerOffice GO Customers will merge with a Wave Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Wave Customer Property
   * - EmailAddress
     - email

Once a link between a PowerOffice GO Customers and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
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


PowerOffice GO Customers (organisation data) to Wave Customer
-------------------------------------------------------------
Every PowerOffice GO Customers (organisation data) will be synchronized with a Wave Customer.

Once a link between a PowerOffice GO Customers (organisation data) and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers (organisation data) and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers (organisation data) Property
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


PowerOffice GO Customers (human data) to Wave Customer (human data)
-------------------------------------------------------------------
Every PowerOffice GO Customers (human data) will be synchronized with a Wave Customer (human data).

Once a link between a PowerOffice GO Customers (human data) and a Wave Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers (human data) and a Wave Customer (human data):

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers (human data) Property
     - Wave Customer (human data) Property
     - Wave Data Type


PowerOffice GO Customers to Wave Customer
-----------------------------------------
Every PowerOffice GO Customers will be synchronized with a Wave Customer.

Once a link between a PowerOffice GO Customers and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Wave Customer Property
     - Wave Data Type


PowerOffice GO Customers to Wave Customer (human data)
------------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Wave Customer (human data).

Once a link between a PowerOffice GO Customers and a Wave Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Wave Customer (human data):

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Wave Customer (human data) Property
     - Wave Data Type


PowerOffice GO Product to Wave Product
--------------------------------------
Every PowerOffice GO Product will be synchronized with a Wave Product.

Once a link between a PowerOffice GO Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
     - Wave Product Property
     - Wave Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - salesPrice
     - unitPrice
     - "string"


PowerOffice GO Salesorders to Wave Invoice
------------------------------------------
Every PowerOffice GO Salesorders will be synchronized with a Wave Invoice.

Once a link between a PowerOffice GO Salesorders and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorders and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorders Property
     - Wave Invoice Property
     - Wave Data Type

