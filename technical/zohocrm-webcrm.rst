====================
ZohoCRM to  Dataflow
====================

Generated: 2024-09-02 08:11:38

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to  Organisations
---------------------------------
Every ZohoCRM Account will be synchronized with a  Organisations.

Once a link between a ZohoCRM Account and a  Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a  Organisations:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     -  Organisations Property
     -  Data Type
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


ZohoCRM Deal to  Opportunities
------------------------------
Every ZohoCRM Deal will be synchronized with a  Opportunities.

Once a link between a ZohoCRM Deal and a  Opportunities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a  Opportunities:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     -  Opportunities Property
     -  Data Type
   * - Account_Name.id
     - OpportunityOrganisationId
     - "string"
   * - Contact_Name.id
     - OpportunityOrganisationId
     - "string"
   * - Owner.id
     - OpportunityPersonId
     - "string"

