=================================
Powerofficego to HubSpot Dataflow
=================================

Generated: 2023-08-02 12:48:33

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to HubSpot Contact
----------------------------------------------
Every Powerofficego Contactperson will be synchronized with a HubSpot Contact.

Once a link between a Powerofficego Contactperson and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - HubSpot Contact Property
     - HubSpot Data Type
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


Powerofficego Customer to HubSpot Company
-----------------------------------------
Every Powerofficego Customer will be synchronized with a HubSpot Company.

Once a link between a Powerofficego Customer and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
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
   * - legalName
     - properties.name
     - "string"
   * - phoneNumberMobile
     - properties.phone
     - "string"
   * - websiteUrl
     - properties.website
     - "string"


Powerofficego Customer to HubSpot Contact
-----------------------------------------
Every Powerofficego Customer will be synchronized with a HubSpot Contact.

Once a link between a Powerofficego Customer and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - HubSpot Contact Property
     - HubSpot Data Type


Powerofficego Employee to HubSpot Contact
-----------------------------------------
Every Powerofficego Employee will be synchronized with a HubSpot Contact.

Once a link between a Powerofficego Employee and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employee and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employee Property
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


Powerofficego Supplier to HubSpot Company
-----------------------------------------
Every Powerofficego Supplier will be synchronized with a HubSpot Company.

Once a link between a Powerofficego Supplier and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Supplier and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
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


Powerofficego Product to HubSpot Product
----------------------------------------
Every Powerofficego Product will be synchronized with a HubSpot Product.

Once a link between a Powerofficego Product and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
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


Powerofficego Salesorderline to HubSpot Lineitemdealassociation
---------------------------------------------------------------
Every Powerofficego Salesorderline will be synchronized with a HubSpot Lineitemdealassociation.

Once a link between a Powerofficego Salesorderline and a HubSpot Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderline and a HubSpot Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderline Property
     - HubSpot Lineitemdealassociation Property
     - HubSpot Data Type

