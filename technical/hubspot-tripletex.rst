=============================
HubSpot to Tripletex Dataflow
=============================

Generated: 2023-06-05 12:53:11

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to Tripletex Customer
-------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into Tripletex.

Once a link between a HubSpot Company and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - id
     - id
     - "integer"
   * - properties.address
     - physicalAddress.addressLine1
     - "string"
   * - properties.address2
     - physicalAddress.addressLine2
     - "string"
   * - properties.city
     - physicalAddress.city
     - "string"
   * - properties.country
     - physicalAddress.country.id
     - "integer"
   * - properties.name
     - name
     - "string"
   * - properties.phone
     - phoneNumber
     - "string"
   * - properties.zip
     - physicalAddress.postalCode
     - "string"


HubSpot Contact to Tripletex Contact
------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a HubSpot Contact if it is connected to a HubSpot Deal that is synchronized into Tripletex.

Once a link between a HubSpot Contact and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - properties.email
     - email
     - "string"
   * - properties.firstname
     - firstName
     - "string"
   * - properties.lastname
     - lastName
     - "string"
   * - properties.mobilephone
     - phoneNumberMobile
     - "if","matches","+*","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
   * - properties.phone
     - phoneNumberWork
     - "string"


HubSpot Deal to Tripletex Order
-------------------------------
When a HubSpot Deal gets the has a 100% probability, it  will be synchronized with a Tripletex Order.

Once a link between a HubSpot Deal and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - properties.closedate
     - deliveryDate
     - "datetime-format","%Y-%m-%d","_."]
   * - properties.closedate
     - orderDate
     - "datetime-format","%Y-%m-%d","_."]
   * - properties.deal_currency_code
     - currency.id
     - "integer"
   * - properties.dealstage
     - isClosed
     - "string"


HubSpot Lineitem to Tripletex Orderline
---------------------------------------
Every HubSpot Lineitem will be synchronized with a Tripletex Orderline.

Once a link between a HubSpot Lineitem and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Tripletex Orderline Property
     - Tripletex Data Type
   * - properties.hs_product_id
     - unitCostCurrency
     - "string"
   * - properties.name
     - description
     - "string"
   * - properties.price
     - unitPriceExcludingVatCurrency
     - "float"
   * - properties.quantity
     - count
     - "float"


HubSpot Product to Tripletex Product
------------------------------------
Every HubSpot Product will be synchronized with a Tripletex Product.

Once a link between a HubSpot Product and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Tripletex Product Property
     - Tripletex Data Type
   * - properties.description
     - description
     - "string"
   * - properties.hs_cost_of_goods_sold
     - costExcludingVatCurrency
     - "integer"
   * - properties.hs_sku
     - number
     - "string"
   * - properties.name
     - name
     - "string"
   * - properties.price
     - priceExcludingVatCurrency
     - "float"


HubSpot User to Tripletex Employee
----------------------------------
Every HubSpot User will be synchronized with a Tripletex Employee.

Once a link between a HubSpot User and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Tripletex Employee Property
     - Tripletex Data Type

