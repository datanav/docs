==================================
CRMOffice to Business Nxt Dataflow
==================================

Generated: 2024-11-12 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CRMOffice to Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CRMOffice Companies to Business Nxt Product
-------------------------------------------
Every CRMOffice Companies will be synchronized with a Business Nxt Product.

Once a link between a CRMOffice Companies and a Business Nxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Companies and a Business Nxt Product:

.. list-table::
   :header-rows: 1

   * - CRMOffice Companies Property
     - Business Nxt Product Property
     - Business Nxt Data Type


CRMOffice Activities to Business Nxt Country
--------------------------------------------
Every CRMOffice Activities will be synchronized with a Business Nxt Country.

Once a link between a CRMOffice Activities and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Activities and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - CRMOffice Activities Property
     - Business Nxt Country Property
     - Business Nxt Data Type
   * - address.country
     - name
     - "string"


CRMOffice Companies to Business Nxt Address
-------------------------------------------
Every CRMOffice Companies will be synchronized with a Business Nxt Address.

Once a link between a CRMOffice Companies and a Business Nxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Companies and a Business Nxt Address:

.. list-table::
   :header-rows: 1

   * - CRMOffice Companies Property
     - Business Nxt Address Property
     - Business Nxt Data Type
   * - id
     - addressNo
     - "string"
   * - postAddress.country
     - countryNo
     - "string"
   * - postAddress.postCode
     - postCode
     - "string"
   * - postAddress.postalArea
     - postalArea
     - "string"
   * - visitAddress.country
     - countryNo
     - "string"
   * - visitAddress.postCode
     - postCode
     - "string"
   * - visitAddress.postalArea
     - postalArea
     - "string"


CRMOffice Companies to Business Nxt Company
-------------------------------------------
Every CRMOffice Companies will be synchronized with a Business Nxt Company.

Once a link between a CRMOffice Companies and a Business Nxt Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Companies and a Business Nxt Company:

.. list-table::
   :header-rows: 1

   * - CRMOffice Companies Property
     - Business Nxt Company Property
     - Business Nxt Data Type
   * - id
     - companyNo
     - "string"


CRMOffice Companies to Business Nxt Country
-------------------------------------------
Every CRMOffice Companies will be synchronized with a Business Nxt Country.

Once a link between a CRMOffice Companies and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Companies and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - CRMOffice Companies Property
     - Business Nxt Country Property
     - Business Nxt Data Type
   * - postAddress.country
     - name
     - "string"
   * - visitAddress.country
     - name
     - "string"

