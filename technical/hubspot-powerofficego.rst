=================================
HubSpot to PowerOfficeGo Dataflow
=================================

Generated: 2023-08-14 14:58:57

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Deal to PowerOfficeGo Outgoinginvoices
----------------------------------------------
Every HubSpot Deal will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a HubSpot Deal and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - properties.amount
     - NetAmount
     - "string"
   * - properties.closedate
     - DeliveryDate
     - "string"
   * - properties.closedate
     - OrderDate
     - "string"
   * - properties.closedate
     - sentDateTimeOffset
     - "string"
   * - properties.createdate
     - createdDateTimeOffset
     - "string"
   * - properties.deal_currency_code
     - CurrencyCode
     - "string"


HubSpot Dealcompanyassociation to PowerOfficeGo Outgoinginvoices
----------------------------------------------------------------
Every HubSpot Dealcompanyassociation will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a HubSpot Dealcompanyassociation and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customerId
     - "string"


HubSpot Dealcontactassociation to PowerOfficeGo Outgoinginvoices
----------------------------------------------------------------
Every HubSpot Dealcontactassociation will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a HubSpot Dealcontactassociation and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customerId
     - "string"


HubSpot Lineitem to PowerOfficeGo Outgoinginvoices
--------------------------------------------------
Every HubSpot Lineitem will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a HubSpot Lineitem and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - properties.createdate
     - createdDateTimeOffset
     - "string"

