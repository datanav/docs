============================
Businesscentral to  Dataflow
============================

Generated: 2023-12-28 00:00:00

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Customers to  Contact
-------------------------------------
Before any synchronization can take place, a link between a Businesscentral Customers and a  Contact must be established.

A new  Contact will be created from a Businesscentral Customers if it is connected to a Businesscentral Salesorders that is synchronized into .

Once a link between a Businesscentral Customers and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a  Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     -  Contact Property
     -  Data Type


Businesscentral Customers to  Customer
--------------------------------------
Before any synchronization can take place, a link between a Businesscentral Customers and a  Customer must be established.

A new  Customer will be created from a Businesscentral Customers if it is connected to a Businesscentral Customers, Salesorders, Contact-person, or Contacts-person that is synchronized into .

Once a link between a Businesscentral Customers and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a  Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     -  Customer Property
     -  Data Type


Businesscentral Customers to  Department
----------------------------------------
Before any synchronization can take place, a link between a Businesscentral Customers and a  Department must be established.

A new  Department will be created from a Businesscentral Customers if it is connected to a Businesscentral Employee that is synchronized into .

Once a link between a Businesscentral Customers and a  Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a  Department:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     -  Department Property
     -  Data Type


Businesscentral Contacts person to  Contact
-------------------------------------------
Every Businesscentral Contacts person will be synchronized with a  Contact.

Once a link between a Businesscentral Contacts person and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a  Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     -  Contact Property
     -  Data Type
   * - email
     - email
     - "string"
   * - mobilePhoneNumber
     - phoneNumberMobile
     - "if","matches","+* *","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
   * - phoneNumber
     - phoneNumberWork
     - "string"


Businesscentral Customers company to  Customer
----------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Customer.

Once a link between a Businesscentral Customers company and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Customer Property
     -  Data Type
   * - address.city
     - deliveryAddress.city
     - "string"
   * - address.city
     - physicalAddress.city
     - "string"
   * - address.city
     - postalAddress.city
     - "string"
   * - address.countryLetterCode
     - deliveryAddress.country.id
     - "string"
   * - address.countryLetterCode
     - physicalAddress.country.id
     - "integer"
   * - address.countryLetterCode
     - postalAddress.country.id
     - "integer"
   * - address.postalCode
     - deliveryAddress.postalCode
     - "string"
   * - address.postalCode
     - physicalAddress.postalCode
     - "string"
   * - address.postalCode
     - postalAddress.postalCode
     - "string"
   * - displayName
     - name
     - "string"
   * - id
     - id
     - "integer"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - website
     - website
     - "string"


Businesscentral Employee to  Employee
-------------------------------------
Every Businesscentral Employee will be synchronized with a  Employee.

Once a link between a Businesscentral Employee and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employee and a  Employee:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employee Property
     -  Employee Property
     -  Data Type
   * - birthDate
     - dateOfBirth
     - "datetime-format","%Y-%m-%d","_."]
   * - city
     - address.city
     - "string"
   * - country
     - address.country.id
     - "integer"
   * - postalCode
     - address.postalCode
     - "string"


Businesscentral Items to  Product
---------------------------------
Every Businesscentral Items will be synchronized with a  Product.

If a matching  Product already exists, the Businesscentral Items will be merged with the existing one.
If no matching  Product is found, a new  Product will be created.

A Businesscentral Items will merge with a  Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Product Property
   * - gtin
     - ean

Once a link between a Businesscentral Items and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Product:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Product Property
     -  Data Type
   * - displayName
     - name
     - "string"
   * - displayName.string
     - name
     - "string"
   * - gtin
     - ean
     - "string"
   * - inventory
     - stockOfGoods
     - "integer"
   * - taxGroupCode
     - vatType.id
     - "integer"
   * - unitCost
     - costExcludingVatCurrency
     - "float"
   * - unitPrice
     - priceExcludingVatCurrency
     - "float"


Businesscentral Salesorderlines to  Orderline
---------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a  Orderline.

Once a link between a Businesscentral Salesorderlines and a  Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a  Orderline:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     -  Orderline Property
     -  Data Type
   * - amountExcludingTax
     - unitPriceExcludingVatCurrency
     - "float"
   * - description
     - description
     - "string"
   * - discountPercent
     - discount
     - "float"
   * - documentId
     - order.id
     - "integer"
   * - invoiceQuantity
     - count
     - "float"
   * - itemId
     - product.id
     - "integer"
   * - quantity
     - count
     - "float"
   * - taxPercent
     - vatType.id
     - "integer"
   * - unitPrice
     - unitPriceExcludingVatCurrency
     - "float"


Businesscentral Salesorders to  Order
-------------------------------------
Every Businesscentral Salesorders will be synchronized with a  Order.

Once a link between a Businesscentral Salesorders and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a  Order:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     -  Order Property
     -  Data Type
   * - currencyId
     - currency.id
     - "integer"
   * - customerId
     - contact.id
     - "integer"
   * - customerId
     - customer.id
     - "integer"
   * - orderDate
     - orderDate
     - "datetime-format","%Y-%m-%d","_."]
   * - requestedDeliveryDate
     - deliveryDate
     - "datetime-format","%Y-%m-%d","_."]
   * - salesperson
     - ourContactEmployee.id
     - "integer"

