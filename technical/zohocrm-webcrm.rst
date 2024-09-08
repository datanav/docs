==========================
ZohoCRM to Webcrm Dataflow
==========================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Webcrm Organisations
---------------------------------------
Every ZohoCRM Account will be synchronized with a Webcrm Organisations.

Once a link between a ZohoCRM Account and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - Account_Name
     - OrganisationName
     - "string"
   * - Billing_City
     - OrganisationCity
     - "string"
   * - Billing_City
     - OrganisationDeliveryCity
     - "string"
   * - Billing_Code
     - OrganisationDeliveryPostCode
     - "string"
   * - Billing_Code
     - OrganisationPostCode
     - "string"
   * - Billing_State
     - OrganisationDeliveryState
     - "string"
   * - Created_Time
     - OrganisationCompanyDescription
     - "string"
   * - Phone
     - OrganisationTelephone
     - "string"
   * - Shipping_City
     - OrganisationCity
     - "string"
   * - Shipping_City
     - OrganisationDeliveryCity
     - "string"
   * - Shipping_Code
     - OrganisationDeliveryPostCode
     - "string"
   * - Shipping_Code
     - OrganisationPostCode
     - "string"
   * - Shipping_State
     - OrganisationDeliveryState
     - "string"
   * - id
     - OrganisationId
     - "string"


ZohoCRM Deal to Webcrm Opportunities
------------------------------------
Every ZohoCRM Deal will be synchronized with a Webcrm Opportunities.

Once a link between a ZohoCRM Deal and a Webcrm Opportunities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a Webcrm Opportunities:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - Webcrm Opportunities Property
     - Webcrm Data Type
   * - Account_Name.id
     - OpportunityOrganisationId
     - "string"
   * - Contact_Name.id
     - OpportunityOrganisationId
     - "string"
   * - Owner.id
     - OpportunityPersonId
     - "string"

