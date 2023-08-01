===================================
Tripletex to PowerOfficeGo Dataflow
===================================

Generated: 2023-08-01 14:00:43

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Tripletex Customer to PowerOfficeGo Customer
--------------------------------------------
Every Tripletex Customer will be synchronized with a PowerOfficeGo Customer.

Once a link between a Tripletex Customer and a PowerOfficeGo Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGo Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGo Customer Property
     - PowerOfficeGo Data Type


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

