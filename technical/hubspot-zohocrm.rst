===========================
HubSpot to ZohoCRM Dataflow
===========================

Generated: 2024-06-30 00:00:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to ZohoCRM Account
----------------------------------
Every HubSpot Company will be synchronized with a ZohoCRM Account.

Once a link between a HubSpot Company and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - properties.city
     - Billing_City
     - "string"
   * - properties.city
     - Shipping_City
     - "string"
   * - properties.country
     - Billing_Country
     - "string"
   * - properties.country
     - Industry
     - "string"
   * - properties.country
     - Mailing_Country
     - "string"
   * - properties.country
     - Other_Country
     - "string"
   * - properties.country
     - Shipping_Country
     - "string"
   * - properties.description
     - Created_Time
     - "string"
   * - properties.industry
     - Billing_Country
     - "string"
   * - properties.industry
     - Industry
     - "string"
   * - properties.industry
     - Mailing_Country
     - "string"
   * - properties.industry
     - Other_Country
     - "string"
   * - properties.industry
     - Shipping_Country
     - "string"
   * - properties.name
     - Account_Name
     - "string"
   * - properties.phone
     - Phone
     - "string"
   * - properties.state
     - Billing_Country
     - "string"
   * - properties.state
     - Billing_State
     - "string"
   * - properties.state
     - Industry
     - "string"
   * - properties.state
     - Shipping_Country
     - "string"
   * - properties.state
     - Shipping_State
     - "string"
   * - properties.type
     - Billing_Country
     - "string"
   * - properties.type
     - Industry
     - "string"
   * - properties.type
     - Mailing_Country
     - "string"
   * - properties.type
     - Other_Country
     - "string"
   * - properties.type
     - Shipping_Country
     - "string"
   * - properties.website
     - Website
     - "string"
   * - properties.zip
     - Billing_Code
     - "string"
   * - properties.zip
     - Shipping_Code
     - "string"


HubSpot Company to ZohoCRM Contact
----------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a ZohoCRM Contact must be established.

A new ZohoCRM Contact will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into ZohoCRM.

Once a link between a HubSpot Company and a ZohoCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a ZohoCRM Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - ZohoCRM Contact Property
     - ZohoCRM Data Type
   * - properties.country
     - Mailing_Country
     - "string"
   * - properties.country
     - Other_Country
     - "string"
   * - properties.industry
     - Mailing_Country
     - "string"
   * - properties.industry
     - Other_Country
     - "string"
   * - properties.state
     - Mailing_Country
     - "string"
   * - properties.state
     - Other_Country
     - "string"
   * - properties.type
     - Mailing_Country
     - "string"
   * - properties.type
     - Other_Country
     - "string"


HubSpot Contact to ZohoCRM Account
----------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a ZohoCRM Account must be established.

A new ZohoCRM Account will be created from a HubSpot Contact if it is connected to a HubSpot Deal that is synchronized into ZohoCRM.

Once a link between a HubSpot Contact and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type


HubSpot Contact to ZohoCRM Contact
----------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a ZohoCRM Contact must be established.

A new ZohoCRM Contact will be created from a HubSpot Contact if it is connected to a HubSpot Deal that is synchronized into ZohoCRM.

Once a link between a HubSpot Contact and a ZohoCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a ZohoCRM Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - ZohoCRM Contact Property
     - ZohoCRM Data Type
   * - properties.city
     - Mailing_City
     - "string"
   * - properties.city
     - Other_City
     - "string"
   * - properties.country
     - Mailing_Country
     - "string"
   * - properties.country
     - Other_Country
     - "string"
   * - properties.email
     - Email
     - "string"
   * - properties.email
     - Secondary_Email
     - "string"
   * - properties.firstname
     - First_Name
     - "string"
   * - properties.lastname
     - Last_Name
     - "string"
   * - properties.mobilephone
     - Mobile
     - "string"
   * - properties.phone
     - Other_Phone
     - "string"
   * - properties.phone
     - Phone
     - "string"
   * - properties.state
     - Mailing_State
     - "string"
   * - properties.state
     - Other_State
     - "string"
   * - properties.zip
     - Mailing_Zip
     - "string"
   * - properties.zip
     - Other_Zip
     - "string"


HubSpot Owner to ZohoCRM Contact
--------------------------------
Before any synchronization can take place, a link between a HubSpot Owner and a ZohoCRM Contact must be established.

A new ZohoCRM Contact will be created from a HubSpot Owner if it is connected to a HubSpot Deal that is synchronized into ZohoCRM.

Once a link between a HubSpot Owner and a ZohoCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Owner and a ZohoCRM Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Owner Property
     - ZohoCRM Contact Property
     - ZohoCRM Data Type
   * - firstName
     - First_Name
     - "string"
   * - lastName
     - Last_Name
     - "string"


HubSpot Deal to ZohoCRM Deal
----------------------------
Every HubSpot Deal will be synchronized with a ZohoCRM Deal.

Once a link between a HubSpot Deal and a ZohoCRM Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a ZohoCRM Deal:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - ZohoCRM Deal Property
     - ZohoCRM Data Type
   * - properties.amount
     - Amount
     - "string"
   * - properties.closedate
     - Closing_Date
     - N/A
   * - properties.dealname
     - Deal_Name
     - "string"
   * - properties.dealstage
     - Probability
     - "string"
   * - properties.dealstage
     - Type
     - "string"
   * - properties.description
     - Deal_Name
     - "string"
   * - properties.hubspot_owner_id
     - Owner.id
     - "string"
   * - properties.pipeline
     - Stage
     - "string"

