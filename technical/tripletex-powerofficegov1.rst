=====================================
Tripletex to PowerOfficeGov1 Dataflow
=====================================

Generated: 2023-08-14 08:48:58

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


Tripletex Customer to PowerOfficeGov1 Customers
-----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOfficeGov1 Customers must be established.

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


Tripletex Employee to PowerOfficeGov1 Employee
----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a PowerOfficeGov1 Employee must be established.

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


Tripletex Product to PowerOfficeGov1 Product
--------------------------------------------
Before any synchronization can take place, a link between a Tripletex Product and a PowerOfficeGov1 Product must be established.

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


Tripletex Productunit to PowerOfficeGov1 Productunit
----------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Productunit and a PowerOfficeGov1 Productunit must be established.

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


Tripletex Supplier to PowerOfficeGov1 Supplier
----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Supplier and a PowerOfficeGov1 Supplier must be established.

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

