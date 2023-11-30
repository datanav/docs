======================
Tripletex to  Dataflow
======================

Generated: 2023-11-30 00:00:01

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to  Contact
-----------------------------
Every Tripletex Contact will be synchronized with a  Contact.

If a matching  Contact already exists, the Tripletex Contact will be merged with the existing one.
If no matching  Contact is found, a new  Contact will be created.

A Tripletex Contact will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Contact Property
   * - email
     - properties.email

Once a link between a Tripletex Contact and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a  Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Contact Property
     -  Data Type
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


Tripletex Employee to  Contact
------------------------------
Every Tripletex Employee will be synchronized with a  Contact.

If a matching  Contact already exists, the Tripletex Employee will be merged with the existing one.
If no matching  Contact is found, a new  Contact will be created.

A Tripletex Employee will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Contact Property
   * - email
     - properties.email

Once a link between a Tripletex Employee and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a  Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Contact Property
     -  Data Type
   * - address.addressLine1
     - properties.address
     - "string"
   * - address.city
     - properties.city
     - "string"
   * - address.country.id
     - properties.country
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
   * - email
     - properties.work_email
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


Tripletex Customer to  Company
------------------------------
Every Tripletex Customer will be synchronized with a  Company.

Once a link between a Tripletex Customer and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Company:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Company Property
     -  Data Type
   * - deliveryAddress.addressLine1
     - properties.address
     - "string"
   * - deliveryAddress.addressLine2
     - properties.address2
     - "string"
   * - deliveryAddress.city
     - properties.city
     - "string"
   * - deliveryAddress.country.id
     - properties.country
     - "string"
   * - deliveryAddress.postalCode
     - properties.zip
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
   * - postalAddress.city
     - properties.city
     - "string"
   * - postalAddress.country.id
     - properties.country
     - "string"
   * - postalAddress.postalCode
     - properties.zip
     - "string"
   * - url
     - properties.website
     - "string"
   * - website
     - properties.website
     - "string"


Tripletex Department to  Company
--------------------------------
Every Tripletex Department will be synchronized with a  Company.

Once a link between a Tripletex Department and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a  Company:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     -  Company Property
     -  Data Type
   * - departmentNumber
     - properties.description
     - "string"
   * - name
     - properties.name
     - "string"


Tripletex Orderline to  Lineitem
--------------------------------
Every Tripletex Orderline will be synchronized with a  Lineitem.

Once a link between a Tripletex Orderline and a  Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a  Lineitem:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     -  Lineitem Property
     -  Data Type
   * - count
     - properties.quantity
     - "integer"
   * - description
     - properties.description
     - "string"
   * - description
     - properties.name
     - "string"
   * - product.id
     - properties.hs_product_id
     - "string"
   * - unitPriceExcludingVatCurrency
     - properties.price
     - "string"


Tripletex Orderline to  Lineitemdealassociation
-----------------------------------------------
Every Tripletex Orderline will be synchronized with a  Lineitemdealassociation.

Once a link between a Tripletex Orderline and a  Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a  Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     -  Lineitemdealassociation Property
     -  Data Type
   * - order.id
     - toObjectId (Dependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypes)
     - "string"


Tripletex Product to  Product
-----------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a  Product.

Once a link between a Tripletex Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Product Property
     -  Data Type
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

