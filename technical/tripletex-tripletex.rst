===============================
Tripletex to Tripletex Dataflow
===============================

Generated: 2023-06-20 01:08:28

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to Tripletex Employee
---------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a Tripletex Employee must be established.

A Tripletex Contact will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Tripletex Employee Property
   * - email
     - email

Once a link between a Tripletex Contact and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Tripletex Employee Property
     - Tripletex Data Type
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


Tripletex Customer to Tripletex Supplier
----------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Tripletex Supplier must be established.

A Tripletex Customer will merge with a Tripletex Supplier if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Tripletex Supplier Property
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
   * - overdueNoticeEmail
     - overdueNoticeEmail

Once a link between a Tripletex Customer and a Tripletex Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Tripletex Supplier:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Tripletex Supplier Property
     - Tripletex Data Type
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


Tripletex Department to Tripletex Employee
------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a Tripletex Employee must be established.

A Tripletex Department will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Tripletex Employee Property
   * - departmentManager.id
     - id

Once a link between a Tripletex Department and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Tripletex Employee Property
     - Tripletex Data Type


Tripletex Employee to Tripletex Contact
---------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a Tripletex Contact must be established.

A Tripletex Employee will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Tripletex Contact Property
   * - email
     - email

Once a link between a Tripletex Employee and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Tripletex Contact Property
     - Tripletex Data Type
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
     - "if","matches","+*","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
   * - phoneNumberWork
     - phoneNumberWork
     - "string"


Tripletex Product to Tripletex Productgrouprelation
---------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Product and a Tripletex Productgrouprelation must be established.

A Tripletex Product will merge with a Tripletex Productgrouprelation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Tripletex Productgrouprelation Property
   * - id
     - product.id

Once a link between a Tripletex Product and a Tripletex Productgrouprelation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Tripletex Productgrouprelation:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Tripletex Productgrouprelation Property
     - Tripletex Data Type


Tripletex Productgrouprelation to Tripletex Product
---------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Productgrouprelation and a Tripletex Product must be established.

A Tripletex Productgrouprelation will merge with a Tripletex Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgrouprelation Property
     - Tripletex Product Property
   * - product.id
     - id

Once a link between a Tripletex Productgrouprelation and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgrouprelation and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgrouprelation Property
     - Tripletex Product Property
     - Tripletex Data Type


Tripletex Supplier to Tripletex Customer
----------------------------------------
Before any synchronization can take place, a link between a Tripletex Supplier and a Tripletex Customer must be established.

A Tripletex Supplier will merge with a Tripletex Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - Tripletex Customer Property
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
   * - overdueNoticeEmail
     - overdueNoticeEmail

Once a link between a Tripletex Supplier and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - Tripletex Customer Property
     - Tripletex Data Type
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

A new Tripletex Customer will be created from a Tripletex Department if it is connected to a Tripletex Contact, or Employee that is synchronized into Tripletex.

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

