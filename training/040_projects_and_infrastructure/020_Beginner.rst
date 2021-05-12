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

Finne API-URL

se på Execution logs/system dataset

system:config-dataset

Lage grupp/tilganger

.. _sesam-cli-4-1:

sesam-CLI
~~~~~~~~~
There is an Sesam Commad Line Toole on Sesam Community on github. It is often refered to as Sesam-CLI or sesam-py.
This is **NOT** a full command line replacement for the sesam portal web user interface. It is a tool related to development and testing. 
It should only be used with a development sesam node and **not with a PRODUCTION sesam node**. But it is very usful for development and testing.

sesam-py supports a workflow where you work with your sesam config files localy on your computer. You can use your prefered text editor and version controll system. sesam-py works in conjunction with your sesam development node to do tests and to send configs and data back and fort with your 
local computer. The sesam development node do not run on your computer but on a remote machine (in the sky or dedicated server).

Visual studio code will be a good choice of editor for moste people, but others prefer Atom, Sublime Text, Vim etc. the importaint thing is that it support utf-8 character encoding and is nice for editing json.

git on github works well with sesam-py as version controll system, but most version controll sytems will work as long as long as it does not "mess up" filenames and folder structures.
sesam-py is a command line tool and basically what you *see* when you navigate in the terminal is what sesam-py *see* and use. 

You can use your favorit terminal. However a version of bash for your operating system is a good choice, and make it easier to relate to documentaion and examples. 

You can work both in the web portal with the user interface in web portal and with sesam-py, but you should allways think of what you have in the node as **something that 
can get lost**. Only think of configurations that are saved in the version controll system as saved. With this mindset you will not lose a lot of work if you 
inadvertently wipe the developer node or overwrite it with new configs.

You find sesam-py on github:

https://github.com/sesam-community/sesam-py

Make sure to read README for install instructions and recommendations:

https://github.com/sesam-community/sesam-py/blob/master/README.md

You find different releases on this page

https://github.com/sesam-community/sesam-py/releases/

Remember to check for importaint updates of sesam-py on these pages from time to time.

In :ref:`portal-gui-4-1` you learned how to find API-URL (node service url) and make a JWT for a sesam Node. To use sesam-py with your **developer-node** you need the API-URL for your **developer-node** and a JWT with admin rights for this Node.
Make **sure** you are in **developer-node** and not in a **production** node when you get API-URL and JWT.

Make a folder for you project if you don't have one and initiate it with version control system. Make a file called .syncconfig and put your **developer-node API-URL and JWT** in it as this:
::

    NODE="your-dev-node-at.sesam.cloud"
    JWT="your-JWT-for-your-dev-node"

Use UTF-8 character encoding and line feed as line endings for best compatability.

The optimal directory structure of a Sesam Node project in Git should look like this:
    ::
    
        my-project-directory
          ├ node
          | ├ expected/
          | ├ pipes/
          | ├ systems/
          | ├ variables/
          | ├ testdata/
          | ├ node-metadata.conf.json
          | ├ test-env.json
          | └ .syncconfig
          ├ README.md
          ├ LICENSE
          ├ .gitignore
          └ ++

You can fork and clone ... as a start project. Except for the .gitignore file this structure will be the same for other version controll systems.
To avoid to leak secret eg. JWT for your developer node, make sure files with secrets are listed in the .gitignore file or a eqvivelent file.

sesam-py will expect several of the files and folders shown in the node folder to exist to work propperly.
    
If you have unsaved work in your developer node (not recommend workflow) or are not sure if you have unsaved work, you can easily download this to an empty folder with the *download* command. 
For this to work you need to put a valid .syncconfig in the empty folder configured with NODE and JWT values to connect to your dev-container. Depending on how *compleat*
yor dev-node is configured, this will produce a filestructure eqvivelant to node folder above. You will need to run the command *update* also to get an *expected* folder.

If you use the *download* command in a non empty folder it is a risk that it will overwrite existing files, so be carefull if you chose to do this.

If you work on many different projects with different configurations for sesam nodes, you will have many different project folders. However you will probably use your own dveloper node to develop and test on.
This means that everything in the developer node will be replaced when you switch from working on one project to an other. To make sure that you start work on a *clean slate* you will use the *wipe* command. 
This command can also be followe by the *restart* command to make sure the dev-node is as *fresh* as it can be.

Usual work flow
go to project folder, check out version of config you want to develop on and test
wipe dev-node
restart dev-node
run sesam *test* command. This will do an upload (of checked out config in project folder), a *run* and a *verify*.
look at output from *verify*. If you expect the new config to produce all the same output/endpoint data as previous configs, *verify* should return that all tests passed.
If output is not the same you need to look for bugs in your config. If you expected output to change, you need to check if new output is as you expected. If you use command *update*, you will download
the current output values from your dev-node to your expected folder. You can than use diff functionallity in you version controll system to check differenses from previous expect values. If this is as you intended
you can make this the new expected values by staging/commiting changes to expected to your project. If not you can revert to old expected files.

Example with bash, git and sesam-py:
::
    cd your-sesam-project
    git status
    git checkout my-feature
    cd node/
    sesam wipe -vv
    sesam restart -vv
    sesam test -vv -scheduler-max-run-time 3000 -print-scheduler-log
    sesam -vv update
    git add -A .
    git commit -m "Expected updated for new feature"



?? Full github based init and example. Use internal ref for docs URL?
https://docs.sesam.io/project-workflow.html
https://docs.sesam.io/project-workflow.html#using-git-in-a-sesam-project

?? docs not up to date with current sesam client. No intit command anymore, and not in PIP (??)
https://docs.sesam.io/sesam-client.html#concepts-sesam-client

NB!! IKKE BRUK SYNCCONFIG TIL Å LASTE OPP/NED TIL AKTIVE NODER (PROD)
?? (feature request: tags to set node type [PROD,DEVELOP,CI,TEST,etc] sesam-py should not accept PROD and TEST, or at least only non-destructive (read) operations)

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
