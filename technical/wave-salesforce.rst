===========================
Wave to Salesforce Dataflow
===========================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Salesforce Division
------------------------------------
Every Wave Customer will be synchronized with a Salesforce Division.

Once a link between a Wave Customer and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"


Wave Invoice to Salesforce Invoice
----------------------------------
Every Wave Invoice will be synchronized with a Salesforce Invoice.

Once a link between a Wave Invoice and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - currency.code
     - CurrencyIsoCode
     - "string"
   * - dueDate
     - DueDate
     - "string"
   * - invoiceDate
     - InvoiceDate
     - "string"
   * - invoiceDate
     - PostedDate
     - "string"
   * - invoiceNumber
     - InvoiceNumber
     - "string"
   * - memo
     - Description
     - "string"
   * - total.value
     - TotalAmount
     - "string"


Wave Currency to Salesforce Currencytype
----------------------------------------
Every Wave Currency will be synchronized with a Salesforce Currencytype.

Once a link between a Wave Currency and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Currency and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Wave Customer person to Salesforce Customer
-------------------------------------------
Every Wave Customer person will be synchronized with a Salesforce Customer.

Once a link between a Wave Customer person and a Salesforce Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Salesforce Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Salesforce Customer Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"


Wave Customer to Salesforce Contact
-----------------------------------
Every Wave Customer will be synchronized with a Salesforce Contact.

Once a link between a Wave Customer and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - address.city
     - MailingCity
     - "string"
   * - address.country.code
     - MailingCountry
     - "string"
   * - address.postalCode
     - MailingPostalCode
     - "string"
   * - address.province.code
     - MailingState
     - "string"
   * - email
     - Email
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - id
     - ID
     - "string"
   * - id
     - Id
     - "string"
   * - lastName
     - LastName
     - "string"
   * - mobile
     - MobilePhone
     - "string"
   * - shippingDetails.address.city
     - MailingCity
     - "string"
   * - shippingDetails.address.country.code
     - MailingCountry
     - "string"
   * - shippingDetails.address.postalCode
     - MailingPostalCode
     - "string"
   * - shippingDetails.address.province.code
     - MailingState
     - "string"


Wave Invoice to Salesforce Invoiceline
--------------------------------------
Every Wave Invoice will be synchronized with a Salesforce Invoiceline.

Once a link between a Wave Invoice and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type
   * - currency.code
     - CurrencyIsoCode
     - "string"
   * - items.description
     - Description
     - "string"
   * - items.price
     - UnitPrice
     - "string"
   * - items.quantity
     - Quantity
     - "string"
   * - memo
     - Description
     - "string"


Wave Invoice to Salesforce Order
--------------------------------
Every Wave Invoice will be synchronized with a Salesforce Order.

Once a link between a Wave Invoice and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Salesforce Order Property
     - Salesforce Data Type
   * - currency.code
     - CurrencyIsoCode
     - "string"
   * - memo
     - Description
     - "string"
   * - title
     - Name
     - "string"
   * - total.value
     - TotalAmount
     - "string"


Wave Invoice to Salesforce Orderitem
------------------------------------
Every Wave Invoice will be synchronized with a Salesforce Orderitem.

Once a link between a Wave Invoice and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Salesforce Orderitem Property
     - Salesforce Data Type
   * - currency.code
     - CurrencyIsoCode
     - "string"
   * - id
     - OrderId
     - "string"
   * - items.price
     - TotalPrice
     - "string"
   * - items.quantity
     - Quantity
     - "string"


Wave Invoice to Salesforce Quotelineitem
----------------------------------------
Every Wave Invoice will be synchronized with a Salesforce Quotelineitem.

Once a link between a Wave Invoice and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Salesforce Quotelineitem Property
     - Salesforce Data Type
   * - currency.code
     - CurrencyIsoCode
     - "string"
   * - items.description
     - Description
     - "string"
   * - items.price
     - TotalPriceWithTax
     - "string"
   * - items.quantity
     - Quantity
     - "string"


Wave Product to Salesforce Product2
-----------------------------------
Every Wave Product will be synchronized with a Salesforce Product2.

Once a link between a Wave Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - description
     - Description
     - "string"
   * - description
     - Description	
     - "string"
   * - name
     - Name
     - "string"
   * - name
     - Name	
     - "string"


Wave Vendor to Salesforce Contact
---------------------------------
Every Wave Vendor will be synchronized with a Salesforce Contact.

Once a link between a Wave Vendor and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - address.city
     - MailingCity
     - "string"
   * - address.postalCode
     - MailingPostalCode
     - "string"
   * - address.province.code
     - MailingState
     - "string"
   * - email
     - Email
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - id
     - Id
     - "string"
   * - lastName
     - LastName
     - "string"
   * - mobile
     - MobilePhone
     - "string"
   * - phone
     - HomePhone
     - "string"
   * - phone
     - Phone
     - "string"

