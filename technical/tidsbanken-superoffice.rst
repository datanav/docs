==================================
Tidsbanken to SuperOffice Dataflow
==================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to SuperOffice Person
---------------------------------------
Every Tidsbanken Ansatt will be synchronized with a SuperOffice Person.

If a matching SuperOffice Person already exists, the Tidsbanken Ansatt will be merged with the existing one.
If no matching SuperOffice Person is found, a new SuperOffice Person will be created.

A Tidsbanken Ansatt will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - SuperOffice Person Property
   * - Epost
     - Emails.Value

Once a link between a Tidsbanken Ansatt and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - Adresse
     - Address.Street.Address1
     - "string"
   * - Etternavn
     - Lastname
     - "string"
   * - Fodt
     - BirthDate
     - N/A
   * - Fornavn
     - Firstname
     - "string"
   * - Id
     - PersonId
     - "integer"
   * - Mobil
     - MobilePhones.Value
     - "string"
   * - Postnummer
     - Address.Street.Zipcode
     - "string"
   * - Poststed
     - Address.Street.City
     - "string"
   * - TlfPrivat
     - PrivatePhones.Value
     - "string"


Tidsbanken Ansatt to SuperOffice User
-------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a SuperOffice User must be established.

A Tidsbanken Ansatt will merge with a SuperOffice User if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - SuperOffice User Property
   * - Epost
     - personEmail

Once a link between a Tidsbanken Ansatt and a SuperOffice User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a SuperOffice User:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - SuperOffice User Property
     - SuperOffice Data Type


Tidsbanken Kunde to SuperOffice Contact
---------------------------------------
Every Tidsbanken Kunde will be synchronized with a SuperOffice Contact.

If a matching SuperOffice Contact already exists, the Tidsbanken Kunde will be merged with the existing one.
If no matching SuperOffice Contact is found, a new SuperOffice Contact will be created.

A Tidsbanken Kunde will merge with a SuperOffice Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - SuperOffice Contact Property
   * - Epost
     - Emails.Value

Once a link between a Tidsbanken Kunde and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - Epost
     - Emails.Value
     - "string"
   * - Gateadresse
     - Address.Postal.Address1
     - "string"
   * - Gateadresse
     - Address.Street.Address1
     - "string"
   * - Id
     - ContactId
     - "integer"
   * - LevPostNr
     - Address.Postal.Zipcode
     - "string"
   * - LevPostNr
     - Address.Street.Zipcode
     - "string"
   * - LevPoststed
     - Address.Postal.City
     - "string"
   * - LevPoststed
     - Address.Street.City
     - "string"
   * - Leveringsadresse
     - Address.Postal.Address1
     - "string"
   * - Leveringsadresse
     - Address.Street.Address1
     - "string"
   * - Leveringsadresse2
     - Address.Postal.Address2
     - "string"
   * - Leveringsadresse2
     - Address.Street.Address2
     - "string"
   * - Navn
     - Name
     - "string"
   * - Organisasjonsnummer
     - OrgNr (Dependant on having NO in Country.TwoLetterISOCountryDependant on having wd:Q11994066 in Country.TwoLetterISOCountry)
     - "string"
   * - Postadresse
     - Address.Postal.Address2
     - "string"
   * - Postadresse
     - Address.Street.Address2
     - "string"
   * - Postnr
     - Address.Postal.Zipcode
     - "string"
   * - Postnr
     - Address.Street.Zipcode
     - "string"
   * - Poststed
     - Address.Postal.City
     - "string"
   * - Poststed
     - Address.Street.City
     - "string"
   * - Telefon
     - Phones.Value
     - "string"
   * - Url
     - Urls.Value
     - "string"
   * - sesam_kundeId
     - OrgNr (Dependant on having wd:Q852835 in Country.TwoLetterISOCountry)
     - "string"


Tidsbanken Avdeling to SuperOffice Contact
------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a SuperOffice Contact.

Once a link between a Tidsbanken Avdeling and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - Adresse
     - Address.Postal.Address1
     - "string"
   * - Adresse
     - Address.Street.Address1
     - "string"
   * - Id
     - ContactId
     - "integer"
   * - Navn
     - Name
     - "string"
   * - Organisasjonsnr
     - OrgNr (Dependant on having wd:Q11994066 in Country.TwoLetterISOCountry)
     - "string"
   * - Postnr
     - Address.Postal.Zipcode
     - "string"
   * - Postnr
     - Address.Street.Zipcode
     - "string"
   * - Poststed
     - Address.Postal.City
     - "string"
   * - Poststed
     - Address.Street.City
     - "string"
   * - sesam_avdelingId
     - OrgNr (Dependant on having wd:Q2366457 in Country.TwoLetterISOCountry)
     - "string"

