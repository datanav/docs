===================================
Tripletex to PowerOfficeGo Dataflow
===================================

Generated: 2023-08-04 06:26:15

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to PowerOfficeGo Customer
--------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOfficeGo Customer must be established.

A new PowerOfficeGo Customer will be created from a Tripletex Customer if it is connected to a Tripletex Contact that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Customer and a PowerOfficeGo Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGo Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGo Customer Property
     - PowerOfficeGo Data Type
   * - accountManager.id
     - ourReferenceEmployeeCode
     - "string"
   * - email
     - emailAddress
     - "string"
   * - email
     - vatNumber (Dependant on having wd:Q1273217 in mailAddress.countryCodeDependant on having wd:Q1273217 in streetAddresses.countryCode)
     - "string"
   * - id
     - id
     - "string"
   * - invoiceEmail
     - InvoiceEmailAddressCC
     - "string"
   * - invoiceEmail
     - vatNumber (Dependant on having wd:Q1273217 in mailAddress.countryCodeDependant on having wd:Q1273217 in streetAddresses.countryCode)
     - "string"
   * - name
     - legalName
     - "string"
   * - organizationNumber
     - vatNumber (Dependant on having NO in mailAddress.countryCodeDependant on having NOR in mailAddress.countryCodeDependant on having NOR in streetAddresses.countryCodeDependant on having wd:Q11994066 in mailAddress.countryCodeDependant on having wd:Q11994066 in streetAddresses.countryCode)
     - "string"
   * - overdueNoticeEmail
     - vatNumber (Dependant on having wd:Q1273217 in mailAddress.countryCodeDependant on having wd:Q1273217 in streetAddresses.countryCode)
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - phoneNumber
     - phoneNumberMobile
     - "string"
   * - physicalAddress.addressLine1
     - streetAddresses.address1
     - "string"
   * - physicalAddress.addressLine2
     - streetAddresses.address2
     - "string"
   * - physicalAddress.city
     - streetAddresses.city
     - "string"
   * - physicalAddress.country.id
     - streetAddresses.countryCode
     - "string"
   * - physicalAddress.postalCode
     - streetAddresses.zipCode
     - "string"
   * - postalAddress.addressLine1
     - mailAddress.address1
     - "string"
   * - postalAddress.addressLine2
     - mailAddress.address2
     - "string"
   * - postalAddress.city
     - mailAddress.city
     - "string"
   * - postalAddress.country.id
     - mailAddress.countryCode
     - "string"
   * - postalAddress.postalCode
     - mailAddress.zipCode
     - "string"


Tripletex Department to PowerOfficeGo Customer
----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a PowerOfficeGo Customer must be established.

A new PowerOfficeGo Customer will be created from a Tripletex Department if it is connected to a Tripletex Contact that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Department and a PowerOfficeGo Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a PowerOfficeGo Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOfficeGo Customer Property
     - PowerOfficeGo Data Type
   * - name
     - legalName
     - "string"


Tripletex Contact to PowerOfficeGo Contactperson
------------------------------------------------
Every Tripletex Contact will be synchronized with a PowerOfficeGo Contactperson.

Once a link between a Tripletex Contact and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type
   * - customer.id
     - partyCustomerCode
     - "string"
   * - customer.id
     - partyId
     - "string"
   * - customer.id
     - partySupplierCode
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


Tripletex Contact to PowerOfficeGo Customer
-------------------------------------------
Every Tripletex Contact will be synchronized with a PowerOfficeGo Customer.

Once a link between a Tripletex Contact and a PowerOfficeGo Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOfficeGo Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGo Customer Property
     - PowerOfficeGo Data Type
   * - email
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - LastName
     - "string"


Tripletex Employee to PowerOfficeGo Address
-------------------------------------------
Every Tripletex Employee will be synchronized with a PowerOfficeGo Address.

Once a link between a Tripletex Employee and a PowerOfficeGo Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOfficeGo Address:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOfficeGo Address Property
     - PowerOfficeGo Data Type
   * - address.addressLine1
     - address1
     - "string"
   * - address.addressLine2
     - address2
     - "string"
   * - address.city
     - city
     - "string"
   * - address.country.id
     - countryCode
     - "string"
   * - address.postalCode
     - zipCode
     - "string"


Tripletex Employee to PowerOfficeGo Employee
--------------------------------------------
Every Tripletex Employee will be synchronized with a PowerOfficeGo Employee.

If a matching PowerOfficeGo Employee already exists, the Tripletex Employee will be merged with the existing one.
If no matching PowerOfficeGo Employee is found, a new PowerOfficeGo Employee will be created.

A Tripletex Employee will merge with a PowerOfficeGo Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOfficeGo Employee Property
   * - nationalIdentityNumber
     - SocialSecurityNumber

Once a link between a Tripletex Employee and a PowerOfficeGo Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOfficeGo Employee:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOfficeGo Employee Property
     - PowerOfficeGo Data Type
   * - dateOfBirth
     - DateOfBirth
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"


Tripletex Invoice to PowerOfficeGo Outgoinginvoice
--------------------------------------------------
Every Tripletex Invoice will be synchronized with a PowerOfficeGo Outgoinginvoice.

Once a link between a Tripletex Invoice and a PowerOfficeGo Outgoinginvoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Invoice and a PowerOfficeGo Outgoinginvoice:

.. list-table::
   :header-rows: 1

   * - Tripletex Invoice Property
     - PowerOfficeGo Outgoinginvoice Property
     - PowerOfficeGo Data Type
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


Tripletex Order to PowerOfficeGo Salesorder
-------------------------------------------
Every Tripletex Order will be synchronized with a PowerOfficeGo Salesorder.

Once a link between a Tripletex Order and a PowerOfficeGo Salesorder is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a PowerOfficeGo Salesorder:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - PowerOfficeGo Salesorder Property
     - PowerOfficeGo Data Type
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


Tripletex Orderline to PowerOfficeGo Salesorderline
---------------------------------------------------
Every Tripletex Orderline will be synchronized with a PowerOfficeGo Salesorderline.

Once a link between a Tripletex Orderline and a PowerOfficeGo Salesorderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a PowerOfficeGo Salesorderline:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - PowerOfficeGo Salesorderline Property
     - PowerOfficeGo Data Type
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


Tripletex Product to PowerOfficeGo Product
------------------------------------------
Every Tripletex Product will be synchronized with a PowerOfficeGo Product.

Once a link between a Tripletex Product and a PowerOfficeGo Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a PowerOfficeGo Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - PowerOfficeGo Product Property
     - PowerOfficeGo Data Type
   * - costExcludingVatCurrency
     - CostPrice
     - "string"
   * - description
     - Description
     - "string"
   * - ean
     - Gtin
     - "string"
   * - name
     - Name
     - "string"
   * - priceExcludingVatCurrency
     - SalesPrice
     - "string"
   * - productUnit.id
     - Unit
     - "string"
   * - stockOfGoods
     - AvailableStock
     - "string"
   * - vatType.id
     - VatCode
     - "string"


Tripletex Productgroup to PowerOfficeGo Productgroup
----------------------------------------------------
Every Tripletex Productgroup will be synchronized with a PowerOfficeGo Productgroup.

Once a link between a Tripletex Productgroup and a PowerOfficeGo Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgroup and a PowerOfficeGo Productgroup:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgroup Property
     - PowerOfficeGo Productgroup Property
     - PowerOfficeGo Data Type
   * - name
     - Name
     - "string"


Tripletex Supplier to PowerOfficeGo Supplier
--------------------------------------------
Every Tripletex Supplier will be synchronized with a PowerOfficeGo Supplier.

Once a link between a Tripletex Supplier and a PowerOfficeGo Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a PowerOfficeGo Supplier:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOfficeGo Supplier Property
     - PowerOfficeGo Data Type
   * - email
     - EmailAddress
     - "string"
   * - id
     - Id
     - "string"
   * - name
     - LegalName
     - "string"
   * - phoneNumber
     - PhoneNumber
     - "string"

