=============================
Tripletex to HubSpot Dataflow
=============================

Generated: 2023-06-08 11:49:37

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to HubSpot Contact
------------------------------------
Every Tripletex Contact will be synchronized with a HubSpot Contact.

Once a link between a Tripletex Contact and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - email
     - properties.email
     - "string"
   * - firstName
     - properties.firstname
     - "string"
   * - lastName
     - properties.lastname
     - "string"
   * - phoneNumberMobile
     - properties.mobilephone
     - "string"
   * - phoneNumberWork
     - properties.phone
     - "string"


Tripletex Customer to HubSpot Company
-------------------------------------
Every Tripletex Customer will be synchronized with a HubSpot Company.

Once a link between a Tripletex Customer and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - deliveryAddress.addressLine1
     - properties.address
     - "string"
   * - deliveryAddress.addressLine2
     - properties.address2
     - "string"
   * - id
     - id
     - "string"
   * - name
     - properties.name
     - "string"
   * - phoneNumber
     - properties.phone
     - "string"
   * - physicalAddress.addressLine1
     - properties.address
     - "string"
   * - physicalAddress.addressLine2
     - properties.address2
     - "string"
   * - physicalAddress.city
     - properties.city
     - "string"
   * - physicalAddress.country.id
     - properties.country
     - "string"
   * - physicalAddress.postalCode
     - properties.zip
     - "string"
   * - postalAddress.addressLine1
     - properties.address
     - "string"
   * - postalAddress.addressLine2
     - properties.address2
     - "string"


Tripletex Department to HubSpot Company
---------------------------------------
Every Tripletex Department will be synchronized with a HubSpot Company.

Once a link between a Tripletex Department and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - departmentNumber
     - properties.description
     - "string"
   * - name
     - properties.name
     - "string"


Tripletex Employee to HubSpot Contact
-------------------------------------
Every Tripletex Employee will be synchronized with a HubSpot Contact.

Once a link between a Tripletex Employee and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - address.addressLine1
     - properties.address
     - "string"
   * - address.changes
     - properties.city
     - "string"
   * - address.city
     - properties.city
     - "string"
   * - address.city
     - properties.country
     - "string"
   * - address.country.id
     - properties.country
     - "string"
   * - address.id
     - properties.zip
     - "string"
   * - address.postalCode
     - properties.zip
     - "string"
   * - dateOfBirth
     - properties.date_of_birth
     - "string"
   * - email
     - properties.email
     - "string"
   * - firstName
     - properties.firstname
     - "string"
   * - id
     - id
     - "string"
   * - lastName
     - properties.lastname
     - "string"
   * - phoneNumberMobile
     - properties.mobilephone
     - "string"
   * - phoneNumberWork
     - properties.phone
     - "string"
   * - userType
     - properties.country
     - "string"


Tripletex Supplier to HubSpot Company
-------------------------------------
Every Tripletex Supplier will be synchronized with a HubSpot Company.

Once a link between a Tripletex Supplier and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - deliveryAddress.addressLine1
     - properties.address
     - "string"
   * - deliveryAddress.addressLine2
     - properties.address2
     - "string"
   * - id
     - id
     - "string"
   * - name
     - properties.name
     - "string"
   * - phoneNumber
     - properties.phone
     - "string"
   * - physicalAddress.addressLine1
     - properties.address
     - "string"
   * - physicalAddress.addressLine2
     - properties.address2
     - "string"
   * - physicalAddress.city
     - properties.city
     - "string"
   * - physicalAddress.country.id
     - properties.country
     - "string"
   * - physicalAddress.postalCode
     - properties.zip
     - "string"
   * - postalAddress.addressLine1
     - properties.address
     - "string"
   * - postalAddress.addressLine2
     - properties.address2
     - "string"


Tripletex Employee to HubSpot User
----------------------------------
Every Tripletex Employee will be synchronized with a HubSpot User.

Once a link between a Tripletex Employee and a HubSpot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a HubSpot User:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - HubSpot User Property
     - HubSpot Data Type


Tripletex Orderline to HubSpot Lineitemdealassociation
------------------------------------------------------
Every Tripletex Orderline will be synchronized with a HubSpot Lineitemdealassociation.

Once a link between a Tripletex Orderline and a HubSpot Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a HubSpot Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - HubSpot Lineitemdealassociation Property
     - HubSpot Data Type
   * - order.id
     - toObjectId (Dependant on having wd:Q566889 in sesam_simpleAssociationTypes)
     - "string"


Tripletex Product to HubSpot Product
------------------------------------
Every Tripletex Product will be synchronized with a HubSpot Product.

Once a link between a Tripletex Product and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - HubSpot Product Property
     - HubSpot Data Type
   * - changes.timestamp
     - properties.createdate
     - "string"
   * - costExcludingVatCurrency
     - properties.hs_cost_of_goods_sold
     - "string"
   * - description
     - properties.description
     - "string"
   * - name
     - properties.name
     - "string"
   * - number
     - properties.hs_sku
     - "string"
   * - priceExcludingVatCurrency
     - properties.price
     - "string"

