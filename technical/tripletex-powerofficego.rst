===================================
Tripletex to PowerOfficeGo Dataflow
===================================

Generated: 2023-08-01 14:00:16

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Employee to PowerOfficeGo Employee
--------------------------------------------
Every Tripletex Employee will be synchronized with a PowerOfficeGo Employee.

If a matching PowerOfficeGo Employee already exists, the Tripletex Employee will be merged with the existing one.
If no matching PowerOfficeGo Employee is found, a new PowerOfficeGo Employee will be created.

A Tripletex Employee will merge with a PowerOfficeGo Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOfficeGo Employee Property
   * - nationalIdentityNumber
     - SocialSecurityNumber

Once a link between a Tripletex Employee and a PowerOfficeGo Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOfficeGo Employee:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOfficeGo Employee Property
     - PowerOfficeGo Data Type


Tripletex Invoice to PowerOfficeGo Outgoinginvoice
--------------------------------------------------
Every Tripletex Invoice will be synchronized with a PowerOfficeGo Outgoinginvoice.

Once a link between a Tripletex Invoice and a PowerOfficeGo Outgoinginvoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Invoice and a PowerOfficeGo Outgoinginvoice:

.. list-table::
   :header-rows: 1

   * - Tripletex Invoice Property
     - PowerOfficeGo Outgoinginvoice Property
     - PowerOfficeGo Data Type


Tripletex Supplier to PowerOfficeGo Supplier
--------------------------------------------
Every Tripletex Supplier will be synchronized with a PowerOfficeGo Supplier.

Once a link between a Tripletex Supplier and a PowerOfficeGo Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a PowerOfficeGo Supplier:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOfficeGo Supplier Property
     - PowerOfficeGo Data Type

