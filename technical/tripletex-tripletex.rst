======================
Tripletex to  Dataflow
======================

Generated: 2023-11-29 23:37:14

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to  Contact
-----------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a  Contact must be established.

A Tripletex Contact will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Contact Property
   * - email
     - email

Once a link between a Tripletex Contact and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a  Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Contact Property
     -  Data Type
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


Tripletex Contact to  Employee
------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a  Employee must be established.

A Tripletex Contact will merge with a  Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Employee Property
   * - email
     - email

Once a link between a Tripletex Contact and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a  Employee:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Employee Property
     -  Data Type
   * - customer.id
     - department.id
     - "if", "neq", "_.", "X"], "integer", "string"]
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
     - "string"
   * - phoneNumberWork
     - phoneNumberWork
     - "string"


Tripletex Customer to  Customer
-------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a  Customer must be established.

A Tripletex Customer will merge with a  Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Customer Property
   * - email
     - email
   * - organizationNumber
     - organizationNumber

Once a link between a Tripletex Customer and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Customer Property
     -  Data Type
   * - accountManager.id
     - accountManager.id
     - "integer"
   * - deliveryAddress.addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - deliveryAddress.addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - deliveryAddress.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - deliveryAddress.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - deliveryAddress.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - deliveryAddress.city
     - deliveryAddress.city
     - "string"
   * - deliveryAddress.city
     - physicalAddress.city
     - "string"
   * - deliveryAddress.city
     - postalAddress.city
     - "string"
   * - deliveryAddress.country.id
     - deliveryAddress.country.id
     - "string"
   * - deliveryAddress.country.id
     - physicalAddress.country.id
     - "integer"
   * - deliveryAddress.country.id
     - postalAddress.country.id
     - "integer"
   * - deliveryAddress.postalCode
     - deliveryAddress.postalCode
     - "string"
   * - deliveryAddress.postalCode
     - physicalAddress.postalCode
     - "string"
   * - deliveryAddress.postalCode
     - postalAddress.postalCode
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "integer"
   * - invoiceEmail
     - invoiceEmail
     - "string"
   * - name
     - name
     - "string"
   * - organizationNumber
     - organizationNumber
     - "replace"," ","", "string"]
   * - overdueNoticeEmail
     - overdueNoticeEmail
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - phoneNumberMobile
     - phoneNumberMobile
     - "string"
   * - physicalAddress.addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - physicalAddress.addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - physicalAddress.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - physicalAddress.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - physicalAddress.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - physicalAddress.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - physicalAddress.city
     - deliveryAddress.city
     - "string"
   * - physicalAddress.city
     - physicalAddress.city
     - "string"
   * - physicalAddress.city
     - postalAddress.city
     - "string"
   * - physicalAddress.country.id
     - deliveryAddress.country.id
     - "string"
   * - physicalAddress.country.id
     - physicalAddress.country.id
     - "integer"
   * - physicalAddress.country.id
     - postalAddress.country.id
     - "integer"
   * - physicalAddress.postalCode
     - deliveryAddress.postalCode
     - "string"
   * - physicalAddress.postalCode
     - physicalAddress.postalCode
     - "string"
   * - physicalAddress.postalCode
     - postalAddress.postalCode
     - "string"
   * - postalAddress.addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - postalAddress.addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - postalAddress.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - postalAddress.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - postalAddress.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - postalAddress.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - postalAddress.city
     - deliveryAddress.city
     - "string"
   * - postalAddress.city
     - physicalAddress.city
     - "string"
   * - postalAddress.city
     - postalAddress.city
     - "string"
   * - postalAddress.country.id
     - deliveryAddress.country.id
     - "string"
   * - postalAddress.country.id
     - physicalAddress.country.id
     - "integer"
   * - postalAddress.country.id
     - postalAddress.country.id
     - "integer"
   * - postalAddress.postalCode
     - deliveryAddress.postalCode
     - "string"
   * - postalAddress.postalCode
     - physicalAddress.postalCode
     - "string"
   * - postalAddress.postalCode
     - postalAddress.postalCode
     - "string"


Tripletex Department to  Employee
---------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a  Employee must be established.

A Tripletex Department will merge with a  Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     -  Employee Property
   * - departmentManager.id
     - id

Once a link between a Tripletex Department and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a  Employee:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     -  Employee Property
     -  Data Type


Tripletex Employee to  Contact
------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a  Contact must be established.

A Tripletex Employee will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Contact Property
   * - email
     - email

Once a link between a Tripletex Employee and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a  Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Contact Property
     -  Data Type
   * - department.id
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
     - "if","matches","+* *","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
   * - phoneNumberWork
     - phoneNumberWork
     - "string"


Tripletex Employee to  Employee
-------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a  Employee must be established.

A Tripletex Employee will merge with a  Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Employee Property
   * - id
     - id
   * - email
     - email
   * - employeeNumber
     - employeeNumber
   * - nationalIdentityNumber
     - nationalIdentityNumber

Once a link between a Tripletex Employee and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a  Employee:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Employee Property
     -  Data Type
   * - dateOfBirth
     - dateOfBirth
     - "datetime-format","%Y-%m-%d","_."]
   * - department.id
     - department.id
     - "if", "neq", "_.", "X"], "integer", "string"]
   * - email
     - email
     - "string"


Tripletex Product to  Product
-----------------------------
Before any synchronization can take place, a link between a Tripletex Product and a  Product must be established.

A Tripletex Product will merge with a  Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Product Property
   * - id
     - id

Once a link between a Tripletex Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Product Property
     -  Data Type


Tripletex Product to  Productgrouprelation
------------------------------------------
Before any synchronization can take place, a link between a Tripletex Product and a  Productgrouprelation must be established.

A Tripletex Product will merge with a  Productgrouprelation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Productgrouprelation Property
   * - id
     - product.id

Once a link between a Tripletex Product and a  Productgrouprelation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a  Productgrouprelation:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Productgrouprelation Property
     -  Data Type


Tripletex Productgrouprelation to  Product
------------------------------------------
Before any synchronization can take place, a link between a Tripletex Productgrouprelation and a  Product must be established.

A Tripletex Productgrouprelation will merge with a  Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgrouprelation Property
     -  Product Property
   * - product.id
     - id

Once a link between a Tripletex Productgrouprelation and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgrouprelation and a  Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgrouprelation Property
     -  Product Property
     -  Data Type


Tripletex Productgrouprelation to  Productgrouprelation
-------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Productgrouprelation and a  Productgrouprelation must be established.

A Tripletex Productgrouprelation will merge with a  Productgrouprelation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgrouprelation Property
     -  Productgrouprelation Property
   * - product.id
     - product.id

Once a link between a Tripletex Productgrouprelation and a  Productgrouprelation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgrouprelation and a  Productgrouprelation:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgrouprelation Property
     -  Productgrouprelation Property
     -  Data Type


Tripletex Productunit to  Productunit
-------------------------------------
Before any synchronization can take place, a link between a Tripletex Productunit and a  Productunit must be established.

A Tripletex Productunit will merge with a  Productunit if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Productunit Property
     -  Productunit Property
   * - name
     - name

Once a link between a Tripletex Productunit and a  Productunit is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productunit and a  Productunit:

.. list-table::
   :header-rows: 1

   * - Tripletex Productunit Property
     -  Productunit Property
     -  Data Type


Tripletex Supplier to  Customer
-------------------------------
Before any synchronization can take place, a link between a Tripletex Supplier and a  Customer must be established.

A Tripletex Supplier will merge with a  Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     -  Customer Property
   * - email
     - email
   * - organizationNumber
     - organizationNumber

Once a link between a Tripletex Supplier and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a  Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     -  Customer Property
     -  Data Type
   * - deliveryAddress.addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - deliveryAddress.addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - deliveryAddress.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - deliveryAddress.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - deliveryAddress.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - deliveryAddress.changes
     - deliveryAddress.city
     - "string"
   * - deliveryAddress.changes
     - physicalAddress.city
     - "string"
   * - deliveryAddress.changes
     - postalAddress.city
     - "string"
   * - deliveryAddress.city
     - deliveryAddress.city
     - "string"
   * - deliveryAddress.city
     - deliveryAddress.country.id
     - "string"
   * - deliveryAddress.city
     - physicalAddress.city
     - "string"
   * - deliveryAddress.city
     - physicalAddress.country.id
     - "integer"
   * - deliveryAddress.city
     - postalAddress.city
     - "string"
   * - deliveryAddress.city
     - postalAddress.country.id
     - "integer"
   * - deliveryAddress.country.id
     - deliveryAddress.country.id
     - "string"
   * - deliveryAddress.country.id
     - physicalAddress.country.id
     - "integer"
   * - deliveryAddress.country.id
     - postalAddress.country.id
     - "integer"
   * - deliveryAddress.postalCode
     - deliveryAddress.postalCode
     - "string"
   * - deliveryAddress.postalCode
     - physicalAddress.postalCode
     - "string"
   * - deliveryAddress.postalCode
     - postalAddress.postalCode
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "integer"
   * - invoiceEmail
     - invoiceEmail
     - "string"
   * - name
     - name
     - "string"
   * - overdueNoticeEmail
     - overdueNoticeEmail
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - phoneNumberMobile
     - phoneNumberMobile
     - "string"
   * - physicalAddress.addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - physicalAddress.addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - physicalAddress.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - physicalAddress.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - physicalAddress.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - physicalAddress.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - physicalAddress.city
     - deliveryAddress.city
     - "string"
   * - physicalAddress.city
     - physicalAddress.city
     - "string"
   * - physicalAddress.city
     - postalAddress.city
     - "string"
   * - physicalAddress.country.id
     - deliveryAddress.country.id
     - "string"
   * - physicalAddress.country.id
     - physicalAddress.country.id
     - "integer"
   * - physicalAddress.country.id
     - postalAddress.country.id
     - "integer"
   * - physicalAddress.postalCode
     - deliveryAddress.postalCode
     - "string"
   * - physicalAddress.postalCode
     - physicalAddress.postalCode
     - "string"
   * - physicalAddress.postalCode
     - postalAddress.postalCode
     - "string"
   * - postalAddress.addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - postalAddress.addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - postalAddress.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - postalAddress.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - postalAddress.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - postalAddress.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - postalAddress.city
     - deliveryAddress.city
     - "string"
   * - postalAddress.city
     - physicalAddress.city
     - "string"
   * - postalAddress.city
     - postalAddress.city
     - "string"
   * - postalAddress.country.id
     - deliveryAddress.country.id
     - "string"
   * - postalAddress.country.id
     - physicalAddress.country.id
     - "integer"
   * - postalAddress.country.id
     - postalAddress.country.id
     - "integer"
   * - postalAddress.postalCode
     - deliveryAddress.postalCode
     - "string"
   * - postalAddress.postalCode
     - physicalAddress.postalCode
     - "string"
   * - postalAddress.postalCode
     - postalAddress.postalCode
     - "string"


Tripletex Contact to Tripletex Customer
---------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a Tripletex Contact if it is connected to a Tripletex Order, or Orderline that is synchronized into Tripletex.

Once a link between a Tripletex Contact and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Tripletex Customer Property
     - Tripletex Data Type


Tripletex Customer to Tripletex Contact
---------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a Tripletex Customer if it is connected to a Tripletex Order, or Orderline that is synchronized into Tripletex.

Once a link between a Tripletex Customer and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Tripletex Contact Property
     - Tripletex Data Type


Tripletex Customer to Tripletex Department
------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Tripletex Department must be established.

A new Tripletex Department will be created from a Tripletex Customer if it is connected to a Tripletex Contact, Employee, or Department that is synchronized into Tripletex.

Once a link between a Tripletex Customer and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - name
     - name
     - "string"


Tripletex Department to Tripletex Customer
------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a Tripletex Department if it is connected to a Tripletex Contact, Customer, or Employee that is synchronized into Tripletex.

Once a link between a Tripletex Department and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - name
     - name
     - "string"

