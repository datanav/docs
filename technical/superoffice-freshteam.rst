========================
SuperOffice to  Dataflow
========================

Generated: 2023-11-30 00:00:01

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Ownercontactlink to  Department
-------------------------------------------
Every SuperOffice Ownercontactlink will be synchronized with a  Department.

Once a link between a SuperOffice Ownercontactlink and a  Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ownercontactlink and a  Department:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     -  Department Property
     -  Data Type
   * - name
     - name
     - "string"


SuperOffice User to  Employee
-----------------------------
Every SuperOffice User will be synchronized with a  Employee.

Once a link between a SuperOffice User and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a  Employee:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     -  Employee Property
     -  Data Type
   * - contactCategory
     - Billing_Country
     - "string"
   * - contactCategory
     - Shipping_Country
     - "string"
   * - contactCategory
     - address.country
     - "string"
   * - contactCategory
     - communication_address.communication_country
     - "string"
   * - contactId
     - designation
     - "string"
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"
   * - personEmail
     - personal_email
     - "string"

