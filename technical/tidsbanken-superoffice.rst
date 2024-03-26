==================================
Tidsbanken to Superoffice Dataflow
==================================

Generated: 2024-03-26 14:24:14

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Superoffice Person
---------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a Superoffice Person must be established.

A Tidsbanken Ansatt will merge with a Superoffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Superoffice Person Property
   * - Epost
     - Emails.Value

Once a link between a Tidsbanken Ansatt and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - Adresse
     - Address.Street.Address1
     - "string"
   * - Etternavn
     - Lastname
     - "string"
   * - Fodt
     - BirthDate
     - "datetime-format","%Y-%m-%dT%H:%M:%SZ","_."]
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


Tidsbanken Kunde to Superoffice Contact
---------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Kunde and a Superoffice Contact must be established.

A Tidsbanken Kunde will merge with a Superoffice Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Superoffice Contact Property
   * - Epost
     - Emails.Value

Once a link between a Tidsbanken Kunde and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Superoffice Contact Property
     - Superoffice Data Type
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

