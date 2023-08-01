=================================
HubSpot to PowerOfficeGo Dataflow
=================================

Generated: 2023-08-01 14:01:16

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to PowerOfficeGo Address
----------------------------------------
Every HubSpot Contact will be synchronized with a PowerOfficeGo Address.

Once a link between a HubSpot Contact and a PowerOfficeGo Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a PowerOfficeGo Address:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOfficeGo Address Property
     - PowerOfficeGo Data Type
   * - properties.address
     - address1
     - "string"
   * - properties.city
     - city
     - "string"
   * - properties.country
     - countryCode
     - "string"
   * - properties.zip
     - zipCode
     - "string"


HubSpot Deal to PowerOfficeGo Salesorder
----------------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a PowerOfficeGo Salesorder.

Once a link between a HubSpot Deal and a PowerOfficeGo Salesorder is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a PowerOfficeGo Salesorder:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - PowerOfficeGo Salesorder Property
     - PowerOfficeGo Data Type


HubSpot Lineitemdealassociation to PowerOfficeGo Salesorderline
---------------------------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a PowerOfficeGo Salesorderline.

Once a link between a HubSpot Lineitemdealassociation and a PowerOfficeGo Salesorderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a PowerOfficeGo Salesorderline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - PowerOfficeGo Salesorderline Property
     - PowerOfficeGo Data Type


HubSpot Product to PowerOfficeGo Product
----------------------------------------
Every HubSpot Product will be synchronized with a PowerOfficeGo Product.

Once a link between a HubSpot Product and a PowerOfficeGo Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a PowerOfficeGo Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - PowerOfficeGo Product Property
     - PowerOfficeGo Data Type

