===============================
HubSpot to PowerOffice Dataflow
===============================

Generated: 2023-06-08 10:19:37

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to PowerOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to PowerOffice Address
--------------------------------------
Every HubSpot Contact will be synchronized with a PowerOffice Address.

Once a link between a HubSpot Contact and a PowerOffice Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a PowerOffice Address:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOffice Address Property
     - PowerOffice Data Type
   * - properties.address
     - Address1
     - "string"
   * - properties.address
     - address1
     - "string"
   * - properties.city
     - City
     - "string"
   * - properties.city
     - city
     - "string"
   * - properties.country
     - CountryCode
     - "string"
   * - properties.country
     - countryCode
     - "string"
   * - properties.zip
     - ZipCode
     - "string"
   * - properties.zip
     - zipCode
     - "string"


HubSpot Deal to PowerOffice Salesorder
--------------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a PowerOffice Salesorder.

Once a link between a HubSpot Deal and a PowerOffice Salesorder is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a PowerOffice Salesorder:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - PowerOffice Salesorder Property
     - PowerOffice Data Type
   * - properties.closedate
     - DeliveryDate
     - "string"
   * - properties.closedate
     - OrderDate
     - "string"
   * - properties.deal_currency_code
     - Currency
     - "string"


HubSpot Lineitemdealassociation to PowerOffice Salesorderline
-------------------------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a PowerOffice Salesorderline.

Once a link between a HubSpot Lineitemdealassociation and a PowerOffice Salesorderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a PowerOffice Salesorderline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - PowerOffice Salesorderline Property
     - PowerOffice Data Type


HubSpot Product to PowerOffice Product
--------------------------------------
Every HubSpot Product will be synchronized with a PowerOffice Product.

Once a link between a HubSpot Product and a PowerOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a PowerOffice Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - PowerOffice Product Property
     - PowerOffice Data Type
   * - properties.description
     - Description
     - "string"
   * - properties.hs_cost_of_goods_sold
     - CostPrice
     - "string"
   * - properties.name
     - Name
     - "string"
   * - properties.price
     - SalesPrice
     - "string"


HubSpot User to PowerOffice Employee
------------------------------------
Every HubSpot User will be synchronized with a PowerOffice Employee.

Once a link between a HubSpot User and a PowerOffice Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a PowerOffice Employee:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - PowerOffice Employee Property
     - PowerOffice Data Type
   * - email
     - EmailAddress
     - "string"

