=====================================
Tripletex to PowerOfficeGov1 Dataflow
=====================================

Generated: 2023-08-14 08:49:52

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


Tripletex Customer to PowerOfficeGov1 Contact
---------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOfficeGov1 Contact must be established.

A new PowerOfficeGov1 Contact will be created from a Tripletex Customer if it is connected to a Tripletex Contact, or Employee that is synchronized into PowerOfficeGov1.

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


Tripletex Customer to PowerOfficeGov1 Customer
----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOfficeGov1 Customer must be established.

A new PowerOfficeGov1 Customer will be created from a Tripletex Customer if it is connected to a Tripletex Customer, or Supplier that is synchronized into PowerOfficeGov1.

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


Tripletex Supplier to PowerOfficeGov1 Contact
---------------------------------------------
Before any synchronization can take place, a link between a Tripletex Supplier and a PowerOfficeGov1 Contact must be established.

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


Tripletex Department to PowerOfficeGov1 Contact
-----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a PowerOfficeGov1 Contact must be established.

A new PowerOfficeGov1 Contact will be created from a Tripletex Department if it is connected to a Tripletex Contact, or Employee that is synchronized into PowerOfficeGov1.

Once a link between a Tripletex Department and a PowerOfficeGov1 Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a PowerOfficeGov1 Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOfficeGov1 Contact Property
     - PowerOfficeGov1 Data Type


Tripletex Department to PowerOfficeGov1 Customer
------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a PowerOfficeGov1 Customer must be established.

A new PowerOfficeGov1 Customer will be created from a Tripletex Department if it is connected to a Tripletex Customer, or Supplier that is synchronized into PowerOfficeGov1.

Once a link between a Tripletex Department and a PowerOfficeGov1 Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a PowerOfficeGov1 Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOfficeGov1 Customer Property
     - PowerOfficeGov1 Data Type


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

