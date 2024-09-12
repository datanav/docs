===============================
Tripletex to Tripletex Dataflow
===============================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Activity to Tripletex Activity
----------------------------------------
Before any synchronization can take place, a link between a Tripletex Activity and a Tripletex Activity must be established.

A Tripletex Activity will merge with a Tripletex Activity if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Activity Property
     - Tripletex Activity Property
   * - id
     - id

Once a link between a Tripletex Activity and a Tripletex Activity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Activity and a Tripletex Activity:

.. list-table::
   :header-rows: 1

   * - Tripletex Activity Property
     - Tripletex Activity Property
     - Tripletex Data Type


Tripletex Activity to Tripletex Projectactivity
-----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Activity and a Tripletex Projectactivity must be established.

A Tripletex Activity will merge with a Tripletex Projectactivity if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Activity Property
     - Tripletex Projectactivity Property
   * - id
     - activity.id

Once a link between a Tripletex Activity and a Tripletex Projectactivity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Activity and a Tripletex Projectactivity:

.. list-table::
   :header-rows: 1

   * - Tripletex Activity Property
     - Tripletex Projectactivity Property
     - Tripletex Data Type


Tripletex Contact to Tripletex Contact
--------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a Tripletex Contact must be established.

A Tripletex Contact will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Tripletex Contact Property
   * - email
     - email

Once a link between a Tripletex Contact and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Tripletex Contact Property
     - Tripletex Data Type
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
     - N/A
   * - phoneNumberMobileCountry.id
     - phoneNumberMobileCountry.id
     - "string"
   * - phoneNumberWork
     - phoneNumberWork
     - "string"


Tripletex Contact to Tripletex Customer person
----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a Tripletex Customer person must be established.

A new Tripletex Customer person will be created from a Tripletex Contact if it is connected to a Tripletex Order, or Orderline that is synchronized into Tripletex.

A Tripletex Contact will merge with a Tripletex Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Tripletex Customer person Property
   * - email
     - email

Once a link between a Tripletex Contact and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Tripletex Customer person Property
     - Tripletex Data Type
   * - email
     - email
     - "string"
   * - phoneNumberMobile
     - phoneNumberMobile
     - "string"
   * - phoneNumberWork
     - phoneNumber
     - "string"


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
     - department.id (Dependant on having wd:Q703534 in  )
     - N/A
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
     - N/A
   * - phoneNumberMobileCountry.id
     - phoneNumberMobileCountry
     - "string"
   * - phoneNumberMobileCountry.id
     - phoneNumberMobileCountry.id
     - "integer"
   * - phoneNumberWork
     - phoneNumberWork
     - "string"


Tripletex Country to Tripletex Country
--------------------------------------
Before any synchronization can take place, a link between a Tripletex Country and a Tripletex Country must be established.

A Tripletex Country will merge with a Tripletex Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Country Property
     - Tripletex Country Property
   * - name
     - name
   * - isoAlpha2Code
     - isoAlpha2Code
   * - isoAlpha3Code
     - isoAlpha3Code

Once a link between a Tripletex Country and a Tripletex Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Country and a Tripletex Country:

.. list-table::
   :header-rows: 1

   * - Tripletex Country Property
     - Tripletex Country Property
     - Tripletex Data Type


Tripletex Currency to Tripletex Currency
----------------------------------------
Before any synchronization can take place, a link between a Tripletex Currency and a Tripletex Currency must be established.

A Tripletex Currency will merge with a Tripletex Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - Tripletex Currency Property
   * - code
     - code

Once a link between a Tripletex Currency and a Tripletex Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Currency and a Tripletex Currency:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - Tripletex Currency Property
     - Tripletex Data Type


Tripletex Customer person to Tripletex Contact
----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer person and a Tripletex Contact must be established.

A Tripletex Customer person will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Tripletex Contact Property
   * - email
     - email

Once a link between a Tripletex Customer person and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - email
     - email
     - "string"
   * - phoneNumber
     - phoneNumberWork
     - "string"
   * - phoneNumberMobile
     - phoneNumberMobile
     - N/A


Tripletex Customer person to Tripletex Customer person
------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer person and a Tripletex Customer person must be established.

A Tripletex Customer person will merge with a Tripletex Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Tripletex Customer person Property
   * - email
     - email

Once a link between a Tripletex Customer person and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Tripletex Customer person Property
     - Tripletex Data Type
   * - deliveryAddress.addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - deliveryAddress.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - deliveryAddress.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - deliveryAddress.city
     - physicalAddress.city
     - "string"
   * - deliveryAddress.city
     - postalAddress.city
     - "string"
   * - deliveryAddress.country.id
     - physicalAddress.country.id
     - "integer"
   * - deliveryAddress.country.id
     - postalAddress.country.id
     - "integer"
   * - deliveryAddress.postalCode
     - physicalAddress.postalCode
     - "string"
   * - deliveryAddress.postalCode
     - postalAddress.postalCode
     - "string"
   * - id
     - id
     - "integer"
   * - physicalAddress.addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - physicalAddress.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - physicalAddress.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - physicalAddress.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - physicalAddress.city
     - deliveryAddress.city
     - "string"
   * - physicalAddress.city
     - postalAddress.city
     - "string"
   * - physicalAddress.country.id
     - deliveryAddress.country.id
     - "string"
   * - physicalAddress.country.id
     - postalAddress.country.id
     - "integer"
   * - physicalAddress.postalCode
     - deliveryAddress.postalCode
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
   * - postalAddress.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - postalAddress.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - postalAddress.city
     - deliveryAddress.city
     - "string"
   * - postalAddress.city
     - physicalAddress.city
     - "string"
   * - postalAddress.country.id
     - deliveryAddress.country.id
     - "string"
   * - postalAddress.country.id
     - physicalAddress.country.id
     - "integer"
   * - postalAddress.postalCode
     - deliveryAddress.postalCode
     - "string"
   * - postalAddress.postalCode
     - physicalAddress.postalCode
     - "string"


Tripletex Customer person to Tripletex Employee
-----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer person and a Tripletex Employee must be established.

A Tripletex Customer person will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Tripletex Employee Property
   * - email
     - email

Once a link between a Tripletex Customer person and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - deliveryAddress.addressLine1
     - address.addressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - address.addressLine2
     - "string"
   * - deliveryAddress.city
     - address.city
     - "string"
   * - deliveryAddress.country.id
     - address.country.id
     - "integer"
   * - deliveryAddress.postalCode
     - address.postalCode
     - "string"
   * - id
     - id
     - "integer"
   * - invoiceSendMethod
     - department.id (Dependant on having wd:Q7590 in  )
     - N/A
   * - phoneNumber
     - phoneNumberWork
     - "string"
   * - phoneNumberMobile
     - phoneNumberMobile
     - N/A
   * - physicalAddress.addressLine1
     - address.addressLine1
     - "string"
   * - physicalAddress.addressLine2
     - address.addressLine2
     - "string"
   * - physicalAddress.city
     - address.city
     - "string"
   * - physicalAddress.country.id
     - address.country.id
     - "integer"
   * - physicalAddress.postalCode
     - address.postalCode
     - "string"
   * - postalAddress.addressLine1
     - address.addressLine1
     - "string"
   * - postalAddress.addressLine2
     - address.addressLine2
     - "string"
   * - postalAddress.city
     - address.city
     - "string"
   * - postalAddress.country.id
     - address.country.id
     - "integer"
   * - postalAddress.postalCode
     - address.postalCode
     - "string"


Tripletex Customer to Tripletex Customer
----------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Tripletex Customer must be established.

A Tripletex Customer will merge with a Tripletex Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Tripletex Customer Property
   * - email
     - email
   * - customerNumber
     - customerNumber
   * - organizationNumber
     - organizationNumber

Once a link between a Tripletex Customer and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Tripletex Customer Property
     - Tripletex Data Type
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
     - N/A
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
   * - organizationNumber
     - organizationNumber

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
     - deliveryAddress.changes
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
     - deliveryAddress.city
     - "string"
   * - deliveryAddress.country.id
     - deliveryAddress.country.id
     - "integer"
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
     - deliveryAddress.changes
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
     - deliveryAddress.city
     - "string"
   * - physicalAddress.country.id
     - deliveryAddress.country.id
     - "integer"
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
     - deliveryAddress.changes
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
     - deliveryAddress.city
     - "string"
   * - postalAddress.country.id
     - deliveryAddress.country.id
     - "integer"
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


Tripletex Department to Tripletex Department
--------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a Tripletex Department must be established.

A Tripletex Department will merge with a Tripletex Department if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Tripletex Department Property
   * - departmentNumber
     - departmentNumber

Once a link between a Tripletex Department and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Tripletex Department Property
     - Tripletex Data Type


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


Tripletex Department to Tripletex Employment
--------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a Tripletex Employment must be established.

A Tripletex Department will merge with a Tripletex Employment if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Tripletex Employment Property
   * - departmentManager.id
     - employee.id

Once a link between a Tripletex Department and a Tripletex Employment is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Tripletex Employment:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Tripletex Employment Property
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
   * - department.id (Dependant on having wd:Q703534 in  )
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
     - N/A
   * - phoneNumberMobileCountry
     - phoneNumberMobileCountry.id
     - "string"
   * - phoneNumberMobileCountry.id
     - phoneNumberMobileCountry.id
     - "string"
   * - phoneNumberWork
     - phoneNumberWork
     - "string"


Tripletex Employee to Tripletex Customer person
-----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a Tripletex Customer person must be established.

A Tripletex Employee will merge with a Tripletex Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Tripletex Customer person Property
   * - email
     - email

Once a link between a Tripletex Employee and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Tripletex Customer person Property
     - Tripletex Data Type
   * - address.addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - address.addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - address.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - address.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - address.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - address.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - address.city
     - deliveryAddress.city
     - "string"
   * - address.city
     - physicalAddress.city
     - "string"
   * - address.city
     - postalAddress.city
     - "string"
   * - address.country.id
     - deliveryAddress.country.id
     - "string"
   * - address.country.id
     - physicalAddress.country.id
     - "integer"
   * - address.country.id
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
   * - department.id (Dependant on having wd:Q7590 in  )
     - invoiceSendMethod
     - "string"
   * - id
     - id
     - "integer"
   * - phoneNumberMobile
     - phoneNumberMobile
     - "string"
   * - phoneNumberWork
     - phoneNumber
     - "string"


Tripletex Employee to Tripletex Employee
----------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a Tripletex Employee must be established.

A Tripletex Employee will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Tripletex Employee Property
   * - id
     - id
   * - email
     - email
   * - employeeNumber
     - employeeNumber
   * - nationalIdentityNumber
     - nationalIdentityNumber

Once a link between a Tripletex Employee and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - dateOfBirth
     - dateOfBirth
     - N/A
   * - department.id
     - department.id
     - N/A
   * - department.id (Dependant on having wd:Q29415466 in  Dependant on having wd:Q29415492 in  )
     - sesam_employment_status
     - "boolean"
   * - email
     - email
     - "string"
   * - firstName
     - lastName
     - "string"
   * - lastName
     - firstName
     - "string"
   * - sesam_employment_status
     - department.id (Dependant on having wd:Q29415466 in  Dependant on having wd:Q29415492 in  )
     - N/A


Tripletex Employee to Tripletex Employment
------------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a Tripletex Employment must be established.

A Tripletex Employee will merge with a Tripletex Employment if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Tripletex Employment Property
   * - id
     - employee.id

Once a link between a Tripletex Employee and a Tripletex Employment is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Tripletex Employment:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Tripletex Employment Property
     - Tripletex Data Type


Tripletex Employment to Tripletex Employee
------------------------------------------
Before any synchronization can take place, a link between a Tripletex Employment and a Tripletex Employee must be established.

A Tripletex Employment will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employment Property
     - Tripletex Employee Property
   * - employee.id
     - id

Once a link between a Tripletex Employment and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employment and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Tripletex Employment Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - sesam_employment_status
     - department.id (Dependant on having wd:Q29415466 in  Dependant on having wd:Q29415492 in  )
     - N/A
   * - sesam_employment_status
     - sesam_employment_status
     - "boolean"


Tripletex Employment to Tripletex Employment
--------------------------------------------
Before any synchronization can take place, a link between a Tripletex Employment and a Tripletex Employment must be established.

A Tripletex Employment will merge with a Tripletex Employment if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employment Property
     - Tripletex Employment Property
   * - employee.id
     - employee.id

Once a link between a Tripletex Employment and a Tripletex Employment is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employment and a Tripletex Employment:

.. list-table::
   :header-rows: 1

   * - Tripletex Employment Property
     - Tripletex Employment Property
     - Tripletex Data Type


Tripletex Product to Tripletex Product
--------------------------------------
Before any synchronization can take place, a link between a Tripletex Product and a Tripletex Product must be established.

A Tripletex Product will merge with a Tripletex Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Tripletex Product Property
   * - id
     - id
   * - ean
     - ean

Once a link between a Tripletex Product and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Tripletex Product Property
     - Tripletex Data Type


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


Tripletex Productgrouprelation to Tripletex Productgrouprelation
----------------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Productgrouprelation and a Tripletex Productgrouprelation must be established.

A Tripletex Productgrouprelation will merge with a Tripletex Productgrouprelation if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgrouprelation Property
     - Tripletex Productgrouprelation Property
   * - product.id
     - product.id

Once a link between a Tripletex Productgrouprelation and a Tripletex Productgrouprelation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgrouprelation and a Tripletex Productgrouprelation:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgrouprelation Property
     - Tripletex Productgrouprelation Property
     - Tripletex Data Type


Tripletex Productunit to Tripletex Productunit
----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Productunit and a Tripletex Productunit must be established.

A Tripletex Productunit will merge with a Tripletex Productunit if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Productunit Property
     - Tripletex Productunit Property
   * - name
     - name

Once a link between a Tripletex Productunit and a Tripletex Productunit is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productunit and a Tripletex Productunit:

.. list-table::
   :header-rows: 1

   * - Tripletex Productunit Property
     - Tripletex Productunit Property
     - Tripletex Data Type


Tripletex Projectactivity to Tripletex Activity
-----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Projectactivity and a Tripletex Activity must be established.

A Tripletex Projectactivity will merge with a Tripletex Activity if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Projectactivity Property
     - Tripletex Activity Property
   * - activity.id
     - id

Once a link between a Tripletex Projectactivity and a Tripletex Activity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Projectactivity and a Tripletex Activity:

.. list-table::
   :header-rows: 1

   * - Tripletex Projectactivity Property
     - Tripletex Activity Property
     - Tripletex Data Type


Tripletex Projectactivity to Tripletex Projectactivity
------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Projectactivity and a Tripletex Projectactivity must be established.

A Tripletex Projectactivity will merge with a Tripletex Projectactivity if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Projectactivity Property
     - Tripletex Projectactivity Property
   * - activity.id
     - activity.id

Once a link between a Tripletex Projectactivity and a Tripletex Projectactivity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Projectactivity and a Tripletex Projectactivity:

.. list-table::
   :header-rows: 1

   * - Tripletex Projectactivity Property
     - Tripletex Projectactivity Property
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
   * - organizationNumber
     - organizationNumber

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
   * - organizationNumber
     - organizationNumber
     - N/A
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
   * - url
     - website
     - "string"


Tripletex Supplier to Tripletex Supplier
----------------------------------------
Before any synchronization can take place, a link between a Tripletex Supplier and a Tripletex Supplier must be established.

A Tripletex Supplier will merge with a Tripletex Supplier if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - Tripletex Supplier Property
   * - email
     - email
   * - organizationNumber
     - organizationNumber

Once a link between a Tripletex Supplier and a Tripletex Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a Tripletex Supplier:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - Tripletex Supplier Property
     - Tripletex Data Type
   * - deliveryAddress.addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - deliveryAddress.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - deliveryAddress.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - deliveryAddress.city
     - physicalAddress.city
     - "string"
   * - deliveryAddress.city
     - postalAddress.city
     - "string"
   * - deliveryAddress.country.id
     - physicalAddress.country.id
     - "integer"
   * - deliveryAddress.country.id
     - postalAddress.country.id
     - "integer"
   * - deliveryAddress.postalCode
     - physicalAddress.postalCode
     - "string"
   * - deliveryAddress.postalCode
     - postalAddress.postalCode
     - "string"
   * - id
     - id
     - "integer"
   * - physicalAddress.addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - physicalAddress.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - physicalAddress.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - physicalAddress.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - physicalAddress.city
     - deliveryAddress.city
     - "string"
   * - physicalAddress.city
     - postalAddress.city
     - "string"
   * - physicalAddress.country.id
     - deliveryAddress.country.id
     - "integer"
   * - physicalAddress.country.id
     - postalAddress.country.id
     - "integer"
   * - physicalAddress.postalCode
     - deliveryAddress.postalCode
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
   * - postalAddress.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - postalAddress.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - postalAddress.city
     - deliveryAddress.city
     - "string"
   * - postalAddress.city
     - physicalAddress.city
     - "string"
   * - postalAddress.country.id
     - deliveryAddress.country.id
     - "integer"
   * - postalAddress.country.id
     - physicalAddress.country.id
     - "integer"
   * - postalAddress.postalCode
     - deliveryAddress.postalCode
     - "string"
   * - postalAddress.postalCode
     - physicalAddress.postalCode
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


Tripletex Customer to Tripletex Customer person
-----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Tripletex Customer person must be established.

A new Tripletex Customer person will be created from a Tripletex Customer if it is connected to a Tripletex Order, Contact, Project, Customer, Employee, Orderline, or Customer-person that is synchronized into Tripletex.

Once a link between a Tripletex Customer and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Tripletex Customer person Property
     - Tripletex Data Type
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
   * - id
     - id
     - "integer"
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

