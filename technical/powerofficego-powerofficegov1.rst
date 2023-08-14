=========================================
Powerofficego to PowerOfficeGov1 Dataflow
=========================================

Generated: 2023-08-14 08:59:57

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to PowerOfficeGov1. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customer to PowerOfficeGov1 Department
----------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customer and a PowerOfficeGov1 Department must be established.

A new PowerOfficeGov1 Department will be created from a Powerofficego Customer if it is connected to a Powerofficego Employee that is synchronized into PowerOfficeGov1.

Once a link between a Powerofficego Customer and a PowerOfficeGov1 Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a PowerOfficeGov1 Department:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGov1 Department Property
     - PowerOfficeGov1 Data Type


Powerofficego Supplier to PowerOfficeGov1 Contact
-------------------------------------------------
Every Powerofficego Supplier will be synchronized with a PowerOfficeGov1 Contact.

Once a link between a Powerofficego Supplier and a PowerOfficeGov1 Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Supplier and a PowerOfficeGov1 Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGov1 Contact Property
     - PowerOfficeGov1 Data Type
   * - EmailAddress
     - Emails.Value
     - "string"
   * - InternationalIdNumber (Dependant on having superoffice-contactid in poweroffice-customer:InternationalIdType)
     - ContactId
     - "string"
   * - LegalName
     - Name
     - "string"
   * - PhoneNumber
     - Phones.Value
     - "string"
   * - WebsiteUrl
     - Domains
     - "list"
   * - WebsiteUrl
     - Urls.Value
     - "string"


Powerofficego Contactperson to PowerOfficeGov1 Contactperson
------------------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a PowerOfficeGov1 Contactperson.

Once a link between a Powerofficego Contactperson and a PowerOfficeGov1 Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a PowerOfficeGov1 Contactperson:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - PowerOfficeGov1 Contactperson Property
     - PowerOfficeGov1 Data Type
   * - address1
     - address1
     - "string"
   * - address2
     - address2
     - "string"
   * - city
     - city
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - "string"
   * - emailAddress
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
   * - partyId
     - partyId
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - residenceCountryCode
     - residenceCountryCode
     - "string"
   * - zipCode
     - zipCode
     - "string"


Powerofficego Customer to PowerOfficeGov1 Contactperson
-------------------------------------------------------
Every Powerofficego Customer will be synchronized with a PowerOfficeGov1 Contactperson.

Once a link between a Powerofficego Customer and a PowerOfficeGov1 Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a PowerOfficeGov1 Contactperson:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGov1 Contactperson Property
     - PowerOfficeGov1 Data Type
   * - LastName
     - lastName
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - "string"
   * - emailAddress
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"


Powerofficego Customer to PowerOfficeGov1 Customer
--------------------------------------------------
Every Powerofficego Customer will be synchronized with a PowerOfficeGov1 Customer.

Once a link between a Powerofficego Customer and a PowerOfficeGov1 Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a PowerOfficeGov1 Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGov1 Customer Property
     - PowerOfficeGov1 Data Type
   * - InternationalIdCountryCode
     - InternationalIdCountryCode
     - "string"
   * - InvoiceEmailAddressCC
     - InvoiceEmailAddressCC
     - "string"
   * - InvoiceEmailAddressCC
     - invoiceEmail
     - "string"
   * - LastName
     - LastName
     - "string"
   * - LastName
     - lastName
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - "string"
   * - emailAddress
     - email
     - "string"
   * - emailAddress
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "string"
   * - invoiceEmailAddress
     - invoiceEmailAddress
     - "string"
   * - invoiceEmailAddressCC
     - invoiceEmailAddressCC
     - "string"
   * - lastChanged
     - lastChanged
     - "string"
   * - legalName
     - legalName
     - "string"
   * - legalName
     - name
     - "string"
   * - mailAddress.address1
     - mailAddress.address1
     - "string"
   * - mailAddress.address1
     - postalAddress.addressLine1
     - "string"
   * - mailAddress.address2
     - mailAddress.address2
     - "string"
   * - mailAddress.address2
     - postalAddress.addressLine2
     - "string"
   * - mailAddress.address3
     - mailAddress.address3
     - "string"
   * - mailAddress.city
     - mailAddress.city
     - "string"
   * - mailAddress.city
     - postalAddress.city
     - "string"
   * - mailAddress.countryCode
     - mailAddress.countryCode
     - "string"
   * - mailAddress.countryCode
     - postalAddress.country.id
     - "integer"
   * - mailAddress.countryCode
     - streetAddresses.countryCode
     - "string"
   * - mailAddress.lastChanged
     - mailAddress.lastChanged
     - "string"
   * - mailAddress.zipCode
     - mailAddress.zipCode
     - "string"
   * - mailAddress.zipCode
     - postalAddress.postalCode
     - "string"
   * - ourReferenceEmployeeCode
     - accountManager.id
     - "integer"
   * - ourReferenceEmployeeCode
     - ourReferenceEmployeeCode
     - "string"
   * - phoneNumber
     - phone
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - streetAddresses.address1
     - address.addressLine1
     - "string"
   * - streetAddresses.address1
     - physicalAddress.addressLine1
     - "string"
   * - streetAddresses.address1
     - streetAddresses.address1
     - "string"
   * - streetAddresses.address2
     - address.addressLine2
     - "string"
   * - streetAddresses.address2
     - physicalAddress.addressLine2
     - "string"
   * - streetAddresses.address2
     - streetAddresses.address2
     - "string"
   * - streetAddresses.address3
     - streetAddresses.address3
     - "string"
   * - streetAddresses.city
     - address.city
     - "string"
   * - streetAddresses.city
     - physicalAddress.city
     - "string"
   * - streetAddresses.city
     - streetAddresses.city
     - "string"
   * - streetAddresses.countryCode
     - address.country.code
     - "string"
   * - streetAddresses.countryCode
     - mailAddress.countryCode
     - "string"
   * - streetAddresses.countryCode
     - physicalAddress.country.id
     - "integer"
   * - streetAddresses.countryCode
     - streetAddresses.countryCode
     - "string"
   * - streetAddresses.lastChanged
     - streetAddresses.lastChanged
     - "string"
   * - streetAddresses.zipCode
     - address.postalCode
     - "string"
   * - streetAddresses.zipCode
     - physicalAddress.postalCode
     - "string"
   * - streetAddresses.zipCode
     - streetAddresses.zipCode
     - "string"
   * - vatNumber (Dependant on having wd:Q906278 in mailAddress.countryCode)
     - mailAddress.countryCode
     - "string"
   * - vatNumber (Dependant on having NO in mailAddress.countryCode)
     - organizationNumber
     - "replace"," ","", "string"]
   * - vatNumber
     - vatNumber (Dependant on having  in mailAddress.countryCode)
     - "string"
   * - websiteUrl
     - website
     - "string"
   * - websiteUrl
     - websiteUrl
     - "string"


Powerofficego Customer to PowerOfficeGov1 Customers
---------------------------------------------------
Every Powerofficego Customer will be synchronized with a PowerOfficeGov1 Customers.

Once a link between a Powerofficego Customer and a PowerOfficeGov1 Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a PowerOfficeGov1 Customers:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGov1 Customers Property
     - PowerOfficeGov1 Data Type
   * - internationalIdNumber (Dependant on having wd:Q11994066 in poweroffice-customer:InternationalIdType)
     - OrgNumber
     - "string"
   * - vatNumber (Dependant on having wd:Q11994066 in mailAddress.countryCode)
     - OrgNumber
     - "string"
   * - websiteUrl
     - WebUrl
     - "string"


Powerofficego Employee to PowerOfficeGov1 Employee
--------------------------------------------------
Every Powerofficego Employee will be synchronized with a PowerOfficeGov1 Employee.

If a matching PowerOfficeGov1 Employee already exists, the Powerofficego Employee will be merged with the existing one.
If no matching PowerOfficeGov1 Employee is found, a new PowerOfficeGov1 Employee will be created.

A Powerofficego Employee will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employee Property
     - PowerOfficeGov1 Employee Property
   * - SocialSecurityNumber
     - SocialSecurityNumber
   * - SocialSecurityNumber
     - nationalIdentityNumber

Once a link between a Powerofficego Employee and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employee and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employee Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type
   * - DateOfBirth
     - DateOfBirth
     - "string"
   * - DateOfBirth
     - dateOfBirth
     - "datetime-format","%Y-%m-%d","_."]
   * - EmailAddress
     - EmailAddress
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - Id
     - Id
     - "string"
   * - Id
     - id
     - "integer"
   * - JobTitle
     - JobTitle
     - "string"
   * - LastChanged
     - LastChanged
     - "string"
   * - LastName
     - LastName
     - "string"
   * - LastName
     - lastName
     - "string"
   * - MailAddress.Address1
     - MailAddress.Address1
     - "string"
   * - MailAddress.Address1
     - address.addressLine1
     - "string"
   * - MailAddress.Address2
     - MailAddress.Address2
     - "string"
   * - MailAddress.Address2
     - address.addressLine2
     - "string"
   * - MailAddress.Address3
     - MailAddress.Address3
     - "string"
   * - MailAddress.City
     - MailAddress.City
     - "string"
   * - MailAddress.City
     - address.city
     - "string"
   * - MailAddress.CountryCode
     - MailAddress.CountryCode
     - "string"
   * - MailAddress.CountryCode
     - address.country.id
     - "integer"
   * - MailAddress.LastChanged
     - MailAddress.LastChanged
     - "string"
   * - MailAddress.ZipCode
     - MailAddress.ZipCode
     - "string"
   * - MailAddress.ZipCode
     - address.postalCode
     - "string"
   * - PhoneNumber
     - PhoneNumber
     - "string"
   * - id
     - id
     - "string"
   * - streetAddresses.address1
     - streetAddresses.address1
     - "string"
   * - streetAddresses.address2
     - streetAddresses.address2
     - "string"
   * - streetAddresses.address3
     - streetAddresses.address3
     - "string"
   * - streetAddresses.city
     - streetAddresses.city
     - "string"
   * - streetAddresses.countryCode
     - streetAddresses.countryCode
     - "string"
   * - streetAddresses.lastChanged
     - streetAddresses.lastChanged
     - "string"
   * - streetAddresses.zipCode
     - streetAddresses.zipCode
     - "string"


Powerofficego Outgoinginvoice to PowerOfficeGov1 Invoice
--------------------------------------------------------
Every Powerofficego Outgoinginvoice will be synchronized with a PowerOfficeGov1 Invoice.

Once a link between a Powerofficego Outgoinginvoice and a PowerOfficeGov1 Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Outgoinginvoice and a PowerOfficeGov1 Invoice:

.. list-table::
   :header-rows: 1

   * - Powerofficego Outgoinginvoice Property
     - PowerOfficeGov1 Invoice Property
     - PowerOfficeGov1 Data Type
   * - CurrencyCode
     - currency.code
     - "string"
   * - CurrencyCode
     - currency.id
     - "integer"
   * - CustomerCode
     - customer.id
     - "string"
   * - DeliveryDate
     - deliveryDate
     - "datetime-format","%Y-%m-%d","_."]
   * - NetAmount
     - amountExcludingVat
     - "integer"
   * - OrderNo
     - orders.id
     - "integer"
   * - SentDate
     - deliveryDate
     - "datetime-format","%Y-%m-%d","_."]
   * - outgoingInvoiceLines.Description
     - items.description
     - "string"
   * - outgoingInvoiceLines.ExternalImportLineReference
     - items.price
     - "float"
   * - outgoingInvoiceLines.Quantity
     - items.quantity
     - "float"
   * - outgoingInvoiceLines.UnitPrice
     - items.price
     - "float"


Powerofficego Outgoinginvoice to PowerOfficeGov1 Outgoinginvoice
----------------------------------------------------------------
Every Powerofficego Outgoinginvoice will be synchronized with a PowerOfficeGov1 Outgoinginvoice.

Once a link between a Powerofficego Outgoinginvoice and a PowerOfficeGov1 Outgoinginvoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Outgoinginvoice and a PowerOfficeGov1 Outgoinginvoice:

.. list-table::
   :header-rows: 1

   * - Powerofficego Outgoinginvoice Property
     - PowerOfficeGov1 Outgoinginvoice Property
     - PowerOfficeGov1 Data Type
   * - CreatedDate
     - CreatedDate
     - "string"
   * - CurrencyCode
     - CurrencyCode
     - "string"
   * - CustomerCode
     - CustomerCode
     - "string"
   * - CustomerEmail
     - CustomerEmail
     - "string"
   * - DeliveryAddress1
     - DeliveryAddress1
     - "string"
   * - DeliveryAddress2
     - DeliveryAddress2
     - "string"
   * - DeliveryAddressCity
     - DeliveryAddressCity
     - "string"
   * - DeliveryAddressCountryCode
     - DeliveryAddressCountryCode
     - "string"
   * - DeliveryAddressZipCode
     - DeliveryAddressZipCode
     - "string"
   * - DeliveryDate
     - DeliveryDate
     - "string"
   * - DeliveryDate
     - SentDate
     - "string"
   * - Id
     - Id
     - "string"
   * - LastChanged
     - LastChanged
     - "string"
   * - NetAmount
     - NetAmount
     - "string"
   * - OrderDate
     - OrderDate
     - "string"
   * - OrderNo
     - OrderNo
     - "string"
   * - OurReferenceEmployeeCode
     - OurReferenceEmployeeCode
     - "string"
   * - OutgoingInvoiceLines
     - OutgoingInvoiceLines
     - "string"
   * - OutgoingInvoiceLines
     - outgoingInvoiceLines.Dim3Code
     - "string"
   * - OutgoingInvoiceLines
     - outgoingInvoiceLines.Id
     - "string"
   * - OutgoingInvoiceLines
     - outgoingInvoiceLines.ProductCode
     - "string"
   * - SentDate
     - DeliveryDate
     - "string"
   * - SentDate
     - SentDate
     - "string"
   * - outgoingInvoiceLines.Description
     - outgoingInvoiceLines.Description
     - "string"
   * - outgoingInvoiceLines.Dim3Code
     - OutgoingInvoiceLines
     - "string"
   * - outgoingInvoiceLines.Dim3Code
     - outgoingInvoiceLines.Dim3Code
     - "string"
   * - outgoingInvoiceLines.Dim3Code
     - outgoingInvoiceLines.Id
     - "string"
   * - outgoingInvoiceLines.Dim3Code
     - outgoingInvoiceLines.ProductCode
     - "string"
   * - outgoingInvoiceLines.ExternalImportLineReference
     - outgoingInvoiceLines.ExternalImportLineReference
     - "string"
   * - outgoingInvoiceLines.ExternalImportLineReference
     - outgoingInvoiceLines.UnitPrice
     - "string"
   * - outgoingInvoiceLines.Id
     - OutgoingInvoiceLines
     - "string"
   * - outgoingInvoiceLines.Id
     - outgoingInvoiceLines.Dim3Code
     - "string"
   * - outgoingInvoiceLines.Id
     - outgoingInvoiceLines.Id
     - "string"
   * - outgoingInvoiceLines.Id
     - outgoingInvoiceLines.ProductCode
     - "string"
   * - outgoingInvoiceLines.IsDeleted
     - outgoingInvoiceLines.IsDeleted
     - "string"
   * - outgoingInvoiceLines.IsDeleted
     - outgoingInvoiceLines.VatCode
     - "string"
   * - outgoingInvoiceLines.ProductCode
     - OutgoingInvoiceLines
     - "string"
   * - outgoingInvoiceLines.ProductCode
     - outgoingInvoiceLines.Dim3Code
     - "string"
   * - outgoingInvoiceLines.ProductCode
     - outgoingInvoiceLines.Id
     - "string"
   * - outgoingInvoiceLines.ProductCode
     - outgoingInvoiceLines.ProductCode
     - "string"
   * - outgoingInvoiceLines.Quantity
     - outgoingInvoiceLines.Quantity
     - "string"
   * - outgoingInvoiceLines.SalesPersonEmployeeCode
     - outgoingInvoiceLines.SalesPersonEmployeeCode
     - "string"
   * - outgoingInvoiceLines.SortOrder
     - outgoingInvoiceLines.SortOrder
     - "string"
   * - outgoingInvoiceLines.UnitPrice
     - outgoingInvoiceLines.ExternalImportLineReference
     - "string"
   * - outgoingInvoiceLines.UnitPrice
     - outgoingInvoiceLines.UnitPrice
     - "string"
   * - outgoingInvoiceLines.VatCode
     - outgoingInvoiceLines.IsDeleted
     - "string"
   * - outgoingInvoiceLines.VatCode
     - outgoingInvoiceLines.VatCode
     - "string"


Powerofficego Product to PowerOfficeGov1 Product
------------------------------------------------
Every Powerofficego Product will be synchronized with a PowerOfficeGov1 Product.

If a matching PowerOfficeGov1 Product already exists, the Powerofficego Product will be merged with the existing one.
If no matching PowerOfficeGov1 Product is found, a new PowerOfficeGov1 Product will be created.

A Powerofficego Product will merge with a PowerOfficeGov1 Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - PowerOfficeGov1 Product Property
   * - id
     - id

Once a link between a Powerofficego Product and a PowerOfficeGov1 Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a PowerOfficeGov1 Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - PowerOfficeGov1 Product Property
     - PowerOfficeGov1 Data Type
   * - availableStock
     - availableStock
     - "string"
   * - availableStock
     - stockOfGoods
     - "integer"
   * - costPrice
     - UnitCost
     - "string"
   * - costPrice
     - costExcludingVatCurrency
     - "integer"
   * - costPrice
     - costPrice
     - "string"
   * - description
     - Description
     - "string"
   * - description
     - description
     - "string"
   * - gtin
     - ean
     - "string"
   * - gtin
     - gtin
     - "string"
   * - id
     - id
     - "string"
   * - lastChanged
     - lastChanged
     - "string"
   * - name
     - Name
     - "string"
   * - name
     - name
     - "string"
   * - productGroupId
     - ProductCategoryKey
     - "string"
   * - productGroupId
     - productGroupId
     - "string"
   * - salesPrice
     - UnitListPrice
     - "decimal"
   * - salesPrice
     - priceExcludingVatCurrency
     - "float"
   * - salesPrice
     - salesPrice
     - "string"
   * - salesPrice
     - unitPrice
     - "string"
   * - type
     - ProductTypeKey
     - "string"
   * - type
     - type
     - "string"
   * - unitOfMeasureCode
     - QuantityUnit
     - "string"
   * - unitOfMeasureCode
     - productUnit.id
     - "integer"
   * - unitOfMeasureCode
     - unitOfMeasureCode
     - "string"
   * - vatCode
     - VAT
     - "integer"
   * - vatCode
     - vatCode
     - "string"
   * - vatCode
     - vatType.id
     - "integer"


Powerofficego Product to PowerOfficeGov1 Productunit
----------------------------------------------------
Every Powerofficego Product will be synchronized with a PowerOfficeGov1 Productunit.

If a matching PowerOfficeGov1 Productunit already exists, the Powerofficego Product will be merged with the existing one.
If no matching PowerOfficeGov1 Productunit is found, a new PowerOfficeGov1 Productunit will be created.

A Powerofficego Product will merge with a PowerOfficeGov1 Productunit if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - PowerOfficeGov1 Productunit Property
   * - unitOfMeasureCode
     - name

Once a link between a Powerofficego Product and a PowerOfficeGov1 Productunit is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a PowerOfficeGov1 Productunit:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - PowerOfficeGov1 Productunit Property
     - PowerOfficeGov1 Data Type
   * - unitOfMeasureCode
     - commonCode
     - "string"


Powerofficego Productgroup to PowerOfficeGov1 Listproductcategoryitems
----------------------------------------------------------------------
Every Powerofficego Productgroup will be synchronized with a PowerOfficeGov1 Listproductcategoryitems.

Once a link between a Powerofficego Productgroup and a PowerOfficeGov1 Listproductcategoryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Productgroup and a PowerOfficeGov1 Listproductcategoryitems:

.. list-table::
   :header-rows: 1

   * - Powerofficego Productgroup Property
     - PowerOfficeGov1 Listproductcategoryitems Property
     - PowerOfficeGov1 Data Type
   * - Name
     - Name
     - "string"


Powerofficego Productgroup to PowerOfficeGov1 Productgroup
----------------------------------------------------------
Every Powerofficego Productgroup will be synchronized with a PowerOfficeGov1 Productgroup.

Once a link between a Powerofficego Productgroup and a PowerOfficeGov1 Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Productgroup and a PowerOfficeGov1 Productgroup:

.. list-table::
   :header-rows: 1

   * - Powerofficego Productgroup Property
     - PowerOfficeGov1 Productgroup Property
     - PowerOfficeGov1 Data Type
   * - Code
     - Code
     - "string"
   * - Name
     - Name
     - "string"
   * - Name
     - name
     - "string"
   * - Type
     - Type
     - "string"


Powerofficego Salesorder to PowerOfficeGov1 Invoice
---------------------------------------------------
Every Powerofficego Salesorder will be synchronized with a PowerOfficeGov1 Invoice.

Once a link between a Powerofficego Salesorder and a PowerOfficeGov1 Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorder and a PowerOfficeGov1 Invoice:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorder Property
     - PowerOfficeGov1 Invoice Property
     - PowerOfficeGov1 Data Type
   * - Currency
     - currency.code
     - "string"
   * - Currency
     - currency.id
     - "integer"
   * - DeliveryDate
     - deliveryDate
     - "datetime-format","%Y-%m-%d","_."]
   * - DepartmentCode
     - customer.id
     - "string"


Powerofficego Salesorder to PowerOfficeGov1 Order
-------------------------------------------------
Every Powerofficego Salesorder will be synchronized with a PowerOfficeGov1 Order.

Once a link between a Powerofficego Salesorder and a PowerOfficeGov1 Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorder and a PowerOfficeGov1 Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorder Property
     - PowerOfficeGov1 Order Property
     - PowerOfficeGov1 Data Type
   * - Currency
     - currency.id
     - "integer"
   * - DeliveryDate
     - deliveryDate
     - "datetime-format","%Y-%m-%d","_."]
   * - DepartmentCode
     - customer.id
     - "integer"
   * - OrderDate
     - orderDate
     - "datetime-format","%Y-%m-%d","_."]


Powerofficego Salesorder to PowerOfficeGov1 Salesorder
------------------------------------------------------
Every Powerofficego Salesorder will be synchronized with a PowerOfficeGov1 Salesorder.

Once a link between a Powerofficego Salesorder and a PowerOfficeGov1 Salesorder is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorder and a PowerOfficeGov1 Salesorder:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorder Property
     - PowerOfficeGov1 Salesorder Property
     - PowerOfficeGov1 Data Type
   * - ContactPersonId
     - ContactPersonId
     - "string"
   * - Currency
     - Currency
     - "string"
   * - DeliveryDate
     - DeliveryDate
     - "string"
   * - DepartmentCode
     - DepartmentCode
     - "string"
   * - OrderDate
     - OrderDate
     - "string"
   * - SalesOrderLines
     - SalesOrderLines
     - "string"
   * - SalesPersonEmployeeNo
     - SalesPersonEmployeeNo
     - "string"


Powerofficego Salesorderline to PowerOfficeGov1 Orderline
---------------------------------------------------------
Every Powerofficego Salesorderline will be synchronized with a PowerOfficeGov1 Orderline.

Once a link between a Powerofficego Salesorderline and a PowerOfficeGov1 Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderline and a PowerOfficeGov1 Orderline:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderline Property
     - PowerOfficeGov1 Orderline Property
     - PowerOfficeGov1 Data Type
   * - Description
     - description
     - "string"
   * - Discount
     - discount
     - "float"
   * - Quantity
     - count
     - "float"
   * - SalesOrderLineUnitPrice
     - unitPriceExcludingVatCurrency
     - "float"
   * - VatReturnSpecification
     - vatType.id
     - "integer"


Powerofficego Salesorderline to PowerOfficeGov1 Quoteline
---------------------------------------------------------
Every Powerofficego Salesorderline will be synchronized with a PowerOfficeGov1 Quoteline.

Once a link between a Powerofficego Salesorderline and a PowerOfficeGov1 Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderline and a PowerOfficeGov1 Quoteline:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderline Property
     - PowerOfficeGov1 Quoteline Property
     - PowerOfficeGov1 Data Type
   * - Description
     - Name
     - "string"
   * - Discount
     - DiscountPercent
     - "integer"
   * - Quantity
     - Quantity
     - "integer"
   * - SalesOrderLineUnitPrice
     - UnitListPrice
     - "string"
   * - VatReturnSpecification
     - VAT
     - "integer"


Powerofficego Salesorderline to PowerOfficeGov1 Salesorderline
--------------------------------------------------------------
Every Powerofficego Salesorderline will be synchronized with a PowerOfficeGov1 Salesorderline.

Once a link between a Powerofficego Salesorderline and a PowerOfficeGov1 Salesorderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderline and a PowerOfficeGov1 Salesorderline:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderline Property
     - PowerOfficeGov1 Salesorderline Property
     - PowerOfficeGov1 Data Type
   * - Description
     - Description
     - "string"
   * - Discount
     - Discount
     - "string"
   * - ProductCode
     - ProductCode
     - "string"
   * - Quantity
     - Quantity
     - "string"
   * - SalesOrderLineUnitPrice
     - SalesOrderLineUnitPrice
     - "string"
   * - SortOrder
     - SortOrder
     - "string"
   * - VatReturnSpecification
     - VatReturnSpecification
     - "string"


Powerofficego Supplier to PowerOfficeGov1 Supplier
--------------------------------------------------
Every Powerofficego Supplier will be synchronized with a PowerOfficeGov1 Supplier.

Once a link between a Powerofficego Supplier and a PowerOfficeGov1 Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Supplier and a PowerOfficeGov1 Supplier:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGov1 Supplier Property
     - PowerOfficeGov1 Data Type
   * - EmailAddress
     - EmailAddress
     - "string"
   * - EmailAddress
     - email
     - "string"
   * - Id
     - Id
     - "string"
   * - Id
     - id
     - "integer"
   * - InternationalIdCountryCode
     - InternationalIdCountryCode
     - "string"
   * - LastChanged
     - LastChanged
     - "string"
   * - LegalName
     - LegalName
     - "string"
   * - LegalName
     - name
     - "string"
   * - PhoneNumber
     - PhoneNumber
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"
   * - WebsiteUrl
     - WebsiteUrl
     - "string"


Powerofficego Supplier to PowerOfficeGov1 Vendor
------------------------------------------------
Every Powerofficego Supplier will be synchronized with a PowerOfficeGov1 Vendor.

Once a link between a Powerofficego Supplier and a PowerOfficeGov1 Vendor is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Supplier and a PowerOfficeGov1 Vendor:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGov1 Vendor Property
     - PowerOfficeGov1 Data Type
   * - LegalName
     - name
     - "string"
   * - WebsiteUrl
     - website
     - "string"


Powerofficego Vatcode to PowerOfficeGov1 Vatcode
------------------------------------------------
Every Powerofficego Vatcode will be synchronized with a PowerOfficeGov1 Vatcode.

If a matching PowerOfficeGov1 Vatcode already exists, the Powerofficego Vatcode will be merged with the existing one.
If no matching PowerOfficeGov1 Vatcode is found, a new PowerOfficeGov1 Vatcode will be created.

A Powerofficego Vatcode will merge with a PowerOfficeGov1 Vatcode if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Vatcode Property
     - PowerOfficeGov1 Vatcode Property
   * - id
     - id

Once a link between a Powerofficego Vatcode and a PowerOfficeGov1 Vatcode is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Vatcode and a PowerOfficeGov1 Vatcode:

.. list-table::
   :header-rows: 1

   * - Powerofficego Vatcode Property
     - PowerOfficeGov1 Vatcode Property
     - PowerOfficeGov1 Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - rate
     - rate
     - "string"

