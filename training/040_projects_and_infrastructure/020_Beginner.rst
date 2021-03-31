.. _projects-and-infrastructure-beginner-4-1:

Projects & Infrastructure Beginner
----------------------------------

.. _portal-gui-4-1:

Portal GUI
~~~~~~~~~~

Bli kjent med gui

Datasets

previous version etc.

Task på å sette opp ting som gjøres når man er i prosjekt

Laste opp/ned node i tools

Legge til brukere

Legge til env-vars/secrets (system secrets vs secrets)

Lage JWT

se på Execution logs/system dataset

system:config-dataset

Lage grupp/tilganger

.. _sesam-cli-4-1:

sesam-CLI
~~~~~~~~~
There is an Sesam Commad Line Toole on Sesam Community on github. It is often refered to as Sesam-CLI or sesam-py.
This is **NOT** a full command line replacement for the sesam portal web user interface. It is a tool related to development and testing. 
It should only be used with a development sesam node and **not with a PRODUCTION sesam node**. But it is very usful for development.

sesam-py supports a workflow where you work with your sesam config files localy on your computer in you prefered text editor and usually with a 
version controll system. sesam-py works in conjunction with your sesam development node to do tests and to send configs and data back and fort with your 
local computer. The sesam development node do not run on your computer but on a remote machine (in the sky or dedicated server).

You can work both in the web portal and the user interface there and with sesam-py, but you should allways think of what you have in the node as something that 
can get lost. Only think of configuratios that are saved in the version controll system as saved. With this mindset you will not lose a lot of work if you 
inadvertently wipe the node or overwrite it with new configs.

https://github.com/sesam-community/sesam-py

https://github.com/sesam-community/sesam-py/blob/master/README.md

https://github.com/sesam-community/sesam-py/releases/

NB!! IKKE BRUK SYNCCONFIG TIL Å LASTE OPP/NED TIL AKTIVE NODER (PROD)

pre-requisite lære seg hvordan man installerer det.

lag en sesam-init <- feature request

setup

expected folder

test.conf.json

whitelist/blacklist

test.json

entiteter

env-var-folder

set up vars for different environments

test-env

.syncconfig

jwt, node

kommandoer

sesam upload/download

test

update

-print-scheduler-log

-vv

-use-internal-scheduler

wipe

restart

verify

run

-version

Hvordan funker expected output

.. _testing-and-testdata-4-1:

Testing & Testdata
~~~~~~~~~~~~~~~~~~

testing

Manuell testing med sesam-cli før opplasting til versjonskontroll

Manuell testing med config-group på live node

Automatisk testing med ci-node

Testdata

Bør lage data som reflekterer virkelige koblinger mellom data i systemer

Bør være nok for å beskrive de caser man kan møte i virkeligheten

Bør ikke være all data i prod

Bør være anonymisert

Bør reflektere \*innkommende\* data

Bør utvidet behov legges til data, ikke endre eksisterende

Bør gis navn utfra det case du vil teste, f.eks gi entiteten navn utfra
casen

Dokumenter testdata

\\\oppdater prosjekt i docs utfra hva vi skriver\\\

Hvordan funker expected output

.. _documentation-4-1:

Documentation
~~~~~~~~~~~~~

Hvordan bruke docs.sesam.io

developer guide!!

ctrl + f "hva du tror funksjon heter"

Hvordan dokumentere

Schema definition

hva mener vi er dokumentasjon

Generell dokumentasjon

DTL dokumentasjon(comments)

clean code

.. _jwt-authentication-4-1:

JWT/Authentisering
~~~~~~~~~~~~~~~~~~

Hvordan fungerer JWT’er?

NB: Skal snake mer om API I sesam-in-the-wild

.. _groups-and-permissions-4-1:

Groups & Permissions
~~~~~~~~~~~~~~~~~~~~

Hvordan virker det

Får man satt opp tilgangsstyring i Sesam?

.. _tasks-for-projects-infrastructure-beginner-4-1:

Tasks for Projects & Infrastructure: Beginner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
