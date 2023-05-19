===============================
Poweroffice to HubSpot Dataflow
===============================

Generated: 2023-05-19 11:57:00

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Poweroffice to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Poweroffice Contactperson to HubSpot Contact
--------------------------------------------
Every Poweroffice Contactperson will be synchronized with a HubSpot Contact.

Once a link between a Poweroffice Contactperson and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Contactperson and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Poweroffice Contactperson Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - DateOfBirth
     - properties.date_of_birth
     - "string"
   * - EmailAddress
     - properties.work_email
     - "string"
   * - FirstName
     - properties.firstname
     - "string"
   * - LastName
     - properties.lastname
     - "string"
   * - PhoneNumber
     - properties.phone
     - "string"
   * - dateOfBirth
     - properties.date_of_birth
     - "string"
   * - emailAddress
     - properties.work_email
     - "string"
   * - firstName
     - properties.firstname
     - "string"
   * - lastName
     - properties.lastname
     - "string"
   * - phoneNumber
     - properties.phone
     - "string"


Poweroffice Customer to HubSpot Company
---------------------------------------
Every Poweroffice Customer will be synchronized with a HubSpot Company.

Once a link between a Poweroffice Customer and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Customer and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Poweroffice Customer Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - LegalName
     - properties.name
     - "string"
   * - PhoneNumber
     - properties.phone
     - "string"
   * - WebsiteUrl
     - properties.website
     - "string"


Poweroffice Customer to HubSpot Contact
---------------------------------------
Every Poweroffice Customer will be synchronized with a HubSpot Contact.

Once a link between a Poweroffice Customer and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Customer and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Poweroffice Customer Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - DateOfBirth
     - properties.date_of_birth
     - "string"
   * - EmailAddress
     - properties.work_email
     - "string"
   * - FirstName
     - properties.firstname
     - "string"
   * - Id
     - id
     - "string"
   * - LastName
     - properties.lastname
     - "string"
   * - Name
     - properties.firstname
     - "string"
   * - dateOfBirth
     - properties.date_of_birth
     - "string"
   * - emailAddress
     - properties.work_email
     - "string"
   * - firstName
     - properties.firstname
     - "string"
   * - id
     - id
     - "string"


Poweroffice Employee to HubSpot Contact
---------------------------------------
Every Poweroffice Employee will be synchronized with a HubSpot Contact.

Once a link between a Poweroffice Employee and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Employee and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Poweroffice Employee Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - DateOfBirth
     - properties.date_of_birth
     - "string"
   * - EmailAddress
     - properties.work_email
     - "string"
   * - FirstName
     - properties.firstname
     - "string"
   * - LastName
     - properties.lastname
     - "string"


Poweroffice Supplier to HubSpot Company
---------------------------------------
Every Poweroffice Supplier will be synchronized with a HubSpot Company.

Once a link between a Poweroffice Supplier and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Supplier and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Poweroffice Supplier Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - LegalName
     - properties.name
     - "string"
   * - PhoneNumber
     - properties.phone
     - "string"
   * - WebsiteUrl
     - properties.website
     - "string"


Poweroffice Employee to HubSpot User
------------------------------------
Every Poweroffice Employee will be synchronized with a HubSpot User.

Once a link between a Poweroffice Employee and a HubSpot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Employee and a HubSpot User:

.. list-table::
   :header-rows: 1

   * - Poweroffice Employee Property
     - HubSpot User Property
     - HubSpot Data Type
   * - EmailAddress
     - email
     - "string"


Poweroffice Product to HubSpot Product
--------------------------------------
Every Poweroffice Product will be synchronized with a HubSpot Product.

Once a link between a Poweroffice Product and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Product and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - Poweroffice Product Property
     - HubSpot Product Property
     - HubSpot Data Type
   * - CostPrice
     - properties.hs_cost_of_goods_sold
     - "string"
   * - Description
     - properties.description
     - "string"
   * - Name
     - properties.name
     - "string"
   * - SalesPrice
     - properties.price
     - "string"


Poweroffice Salesorderline to HubSpot Lineitem
----------------------------------------------
Every Poweroffice Salesorderline will be synchronized with a HubSpot Lineitem.

Once a link between a Poweroffice Salesorderline and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Salesorderline and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - Poweroffice Salesorderline Property
     - HubSpot Lineitem Property
     - HubSpot Data Type
   * - Description
     - properties.name
     - "string"
   * - Discount
     - properties.hs_product_id
     - "string"
   * - ProductCode
     - properties.hs_product_id
     - "string"
   * - Quantity
     - properties.quantity
     - "string"
   * - SalesOrderLineUnitPrice
     - properties.price
     - "string"

