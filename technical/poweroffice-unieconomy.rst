==================================
Poweroffice to UniEconomy Dataflow
==================================

Generated: 2023-06-20 01:07:23

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Poweroffice to UniEconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Poweroffice Customer to UniEconomy Customers
--------------------------------------------
Every Poweroffice Customer will be synchronized with a UniEconomy Customers.

Once a link between a Poweroffice Customer and a UniEconomy Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Customer and a UniEconomy Customers:

.. list-table::
   :header-rows: 1

   * - Poweroffice Customer Property
     - UniEconomy Customers Property
     - UniEconomy Data Type
   * - InternationalIdNumber (Dependant on having wd:Q11994066 in poweroffice-customer:InternationalIdType)
     - OrgNumber
     - "string"
   * - WebsiteUrl
     - WebUrl
     - "string"

