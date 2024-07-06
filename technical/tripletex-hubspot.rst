=============================
Tripletex to Hubspot Dataflow
=============================

Generated: 2024-07-06 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to Hubspot Contact
------------------------------------
Every Tripletex Contact will be synchronized with a Hubspot Contact.

If a matching Hubspot Contact already exists, the Tripletex Contact will be merged with the existing one.
If no matching Hubspot Contact is found, a new Hubspot Contact will be created.

A Tripletex Contact will merge with a Hubspot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Hubspot Contact Property
   * - email
     - properties.email

Once a link between a Tripletex Contact and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Hubspot Contact Property
     - Hubspot Data Type
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


Tripletex Customer person to Hubspot Contact
--------------------------------------------
Every Tripletex Customer person will be synchronized with a Hubspot Contact.

If a matching Hubspot Contact already exists, the Tripletex Customer person will be merged with the existing one.
If no matching Hubspot Contact is found, a new Hubspot Contact will be created.

A Tripletex Customer person will merge with a Hubspot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Hubspot Contact Property
   * - email
     - properties.email

Once a link between a Tripletex Customer person and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Hubspot Contact Property
     - Hubspot Data Type
   * - deliveryAddress.addressLine1
     - properties.address
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
   * - email
     - properties.email
     - "string"
   * - id
     - id
     - "string"
   * - phoneNumber
     - properties.phone
     - "string"
   * - phoneNumberMobile
     - properties.mobilephone
     - "string"
   * - physicalAddress.addressLine1
     - properties.address
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
   * - postalAddress.city
     - properties.city
     - "string"
   * - postalAddress.country.id
     - properties.country
     - "string"
   * - postalAddress.postalCode
     - properties.zip
     - "string"


Tripletex Employee to Hubspot Contact
-------------------------------------
Every Tripletex Employee will be synchronized with a Hubspot Contact.

If a matching Hubspot Contact already exists, the Tripletex Employee will be merged with the existing one.
If no matching Hubspot Contact is found, a new Hubspot Contact will be created.

A Tripletex Employee will merge with a Hubspot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Hubspot Contact Property
   * - email
     - properties.email

Once a link between a Tripletex Employee and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Hubspot Contact Property
     - Hubspot Data Type
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


Tripletex Customer to Hubspot Company
-------------------------------------
Every Tripletex Customer will be synchronized with a Hubspot Company.

Once a link between a Tripletex Customer and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Hubspot Company Property
     - Hubspot Data Type
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


Tripletex Department to Hubspot Company
---------------------------------------
Every Tripletex Department will be synchronized with a Hubspot Company.

Once a link between a Tripletex Department and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - departmentNumber
     - properties.description
     - "string"
   * - name
     - properties.name
     - "string"


Tripletex Orderline to Hubspot Lineitem
---------------------------------------
Every Tripletex Orderline will be synchronized with a Hubspot Lineitem.

Once a link between a Tripletex Orderline and a Hubspot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Hubspot Lineitem:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Hubspot Lineitem Property
     - Hubspot Data Type
   * - count
     - properties.quantity
     - N/A
   * - description
     - properties.description
     - "string"
   * - description
     - properties.name
     - "string"
   * - discount
     - properties.hs_discount_percentage
     - "string"
   * - product.id
     - properties.hs_product_id
     - "string"
   * - unitPriceExcludingVatCurrency
     - properties.price
     - "string"


Tripletex Product to Hubspot Product
------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Hubspot Product.

Once a link between a Tripletex Product and a Hubspot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Hubspot Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Hubspot Product Property
     - Hubspot Data Type
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

