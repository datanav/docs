.. _projects-and-infrastructure-beginner-4-1:

Projects & Infrastructure Beginner
----------------------------------

.. _sesam-node-gui-4-1:

Sesam Node GUI
~~~~~~~~~~~~~~

The graphical user interface (GUI) in a Sesam node provides you with a multitude of options. In this section we are going to go through some of these options and explain how they are used when working on a project.

On the below picture the Sesam GUI can be seen.  

.. _figure-sesamGUI-4-1:
.. figure:: ./media/Sesam_GUI.png
   :align: center

   Sesam Node GUI

It is crucial that you learn and feel confident about navigating the vertical menu on the left hand side of the above picture. The tabs "Pipes" and "Systems" will become your bread and butter tabs when working on projects. The tab "Pipes" will display all pipes from inbound to outbound and the "Systems" tab will show both source and target systems. As such, these tabs will hold all the information you need to get an overview as to how data moves through Sesam. In addition, the "Datahub" and "Subscription" tab also plays an important part in projects, especially so when setting up your Sesam node for use or throughout a project as users change, configuration configs need to be updated or groups of users need to be defined.


Tabs
^^^^

The "Pipes" tab will display to you an overview of all the pipes in Sesam. This overview can be sorted and/or filtered depending on your preference or particular use case. When looking at the overview of all the pipes, you can click on a particular pipe `_id` and then you'll jump to the output of that pipe. The output of a pipe is the result of how that pipe transforms the data flowing through that pipe.

.. _figure-pipejump4-1:
.. figure:: ./media/pipejump.png
   :align: center

   Pipe View

In addition to the output view of a pipe, you will have multiple other views when looking at a particular pipe. These different views can be found horizontally aligned with the "Output" Tab, as can be seen in the above picture as well. The most frequently used are the "Config", "Input", "Output", "Execution Log" and "Graph" Tabs. The "Config" tab entails the rules that transform data flowing through the pipe, the "Input" tab shows the data as is when it enters the pipe, the "Execution log" tab shows diagnostics messages based on pipe runs. To extend on this, when a pipe runs successfully you will find the message *pump completed* at the top of the execution log and when a pipe fails its run you will find "pump failed" at the top of the execution log. Additionally, you will be able to expand these entries in the execution log to gain additional information with regards to individual runs. Finally, the "Graph" tab shows a graphical representation of how data is modelled to and from the pipe you are currently looking at. This makes it extremely easy to get an overview of the modelling landscape as well as how data is connected. By clicking on a specific pipe via the graphical representation you can navigate to other pipes as well, which is really handy for navigating a dataflow. 

Moving onto the "Systems" tab. This tab will hold your start- and endpoints with regards to dataflows in Sesam. This is because Sesam works with systems. Emphasizing the importance of systems here as they both provide Sesam with data and consumes data from Sesam as it is shaped, transformed and/or enriched via dataflows. Typically systems either are databases or microservices. Important here to remember, that inside Sesam anything that produces or consumes data is a system, albeit outside of Sesam these producers or consumers of data can be a wide variety of things. As with pipes, the "Systems" tab will display to you an overview of all the systems currently in Sesam. In addition, you can also click on a particular system `_id` and you'll jump to the config of that system. What you'll see here is what you will typically define as connection parameters. Connection parameters are typically variables like username, password, server, port, database name and/or access token. Obviously these will vary depending on the specific microservice or database in question, albeit it is sure to state that you will always need to apply some of these to connect successfully to a database or microservice inside of Sesam. On the below picture you can see an example system config.

.. _figure-systemconfig4-1:
.. figure:: ./media/systemconfig.png
   :align: center

   System View

As can be seen from the config, all these connection variables are defined in a JSON dictionary. Albeit two of these variables look a little different. This is the `database` and `password` variables. These variables are what we in Sesam call environment variables. The database variable is prefixed with the `$ENV()` and the `password` is prefixed with the `$SECRET()`. To extend on the mechanics of environment variables, you will provide a value that goes inside of the parenthesis, i.e. `$ENV(<my_awesome_example_value>)`. These values are stored in the "Datahub" tab and can be used globally in a Sesam node, i.e. one `$ENV(<global_value_for_multiple_systems>)` can be used in multiple systems. In comparison to `$ENV()` values, the `$SECRET()` values are stored confidentially in Sesam, whilst the `$ENV()` values can be viewed by anyone. As such, `$SECRET()` values can be used globally, albeit viewing their value, is not possible. To clarify, `$SECRET()` values are confidential, whilst `$ENV()` values are not and they are both stored in the "Datahub" tab, which we will talk about now.  

The "Datahub" tab is your view of what is globally in effect on your Sesam node. When navigating to this tab you will be presented with the "Variables" view. This view will show you all the variables defined in your Sesam node and an example of this can be seen in the below picture.

.. _figure-datahubview4-1:
.. figure:: ./media/datahubview.png
   :align: center

   Datahub View

On the left hand side of the above picture you see what, in a system config, is defined as an `$ENV()` value, i.e. `prod_database_name` holds a value of `sesam_training` and that value can be effectively used in a system. On the right hand side of the above picture, you can see your `$SECRET()` values. Again, these are stored in a confidential way, so you cannot actually retrieve their individual values. You can however, point to them in a system config as explained previously, by using the prefix `$SECRET()`. As an example use case, you could retrieve the value of `sesam_jwt` by doing the following in a system config `$SECRET(sesam_jwt)`. This secret will now hold the value of `sesam_jwt`. Finishing of the "Datahub" tab the "Metadata" view is also quite crucial when working on projects in a Sesam node. In the "Metadata" view you can see all the global settings that will affect how your individual Sesam node will work by default with respect to reading and handling metadata. This means in practice that what is defined in the "Metadata" tab shapes metadata flowing through Sesam passively. As such, you could state that this is the polar opposite of how we use pipes in a project to actively shape, transform and enrich data.

Finally, the "Subscription" tab. This tab is your, you could say, "manage my Sesam node" view. It lets you add users to your node, it lets you look at the amount of data currently in your node and lets you define user groups. You can do way more in the "Subscription" tab but in terms of working on a project, this is usually not where you will spend the majority of your time, so in terms of maximizing your learning gain, we will stick to this for now.  


.. seealso::

  Learn Sesam > Architecture & Concepts: :ref:`systems-1-1`
  
  Learn Sesam > Architecture & Concepts: :ref:`pipes-1-1`

  Getting started: :ref:`getting-started-microservices`

  Developer Guide > Service Configuration > Systems: :ref:`microservice_system`

.. _sesam-cli-4-1:

sesam-CLI
~~~~~~~~~

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

.. seealso::

  TODO

.. _testing-and-testdata-4-1:

Testing & Testdata
~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  Testing and testdata is used for...

  - validating transformation of data meets desired shape
  - validate dataflows run as expected
  - ensure changes made are robust enough to be pushed to production 

Extending on the testing aspect of running your CI/CD workflows via the Sesam CLI - testdata comes into play. In practice, testing via the Sesam CLI uses testdata defined in your Sesam development node. As such, testdata is used in a Sesam project to allow for testing of a given change with respect to an intented or desired outcome, i.e. applying filters to only get a subset of data flowing through a dataflow. This is useful because it allows for verification in a self-contained space without relying on real life data or an active system that receives and/or retrieves data. As such, testing is useful in creating a self contained space in which you can fine-tune and verify that your shape of data aligns with how you want it to look like when it hits production and leaves your personal Sesam development node.

To use testdata in Sesam, you will first need to create it. In order for you to do so, Sesam has developed a nifty transformation rule called the ``conditional`` transform statement. An example of a pipe config using this transform statement can be seen below:

.. code-block:: json

  {
    "_id": "crm-persondata",
    "type": "pipe",
    "source": {
      "type": "conditional",
      "alternatives": {
        "prod": {
          "type": "sql",
          "system": "crm",
          "primary_key": "PersonID",
          "schema": "person",
          "table": "PersonDepartment"
        },
        "test": {
          "type": "embedded",
          "entities": [{
            "_id": "164",
            "PersonID": 164,
            "Department": "MIT Product",
            "Departmentref": 804,
            "RegionID": 7
          }, {
            "_id": "165",
            "PersonID": 165,
            "Department": "MIT Sales",
            "Departmentref": 805,
            "RegionID": 7
          }, {
            "_id": "1",
            "PersonID": 1,
            "Department": "MIT Tech",
            "Departmentref": 803,
            "RegionID": 12
          }, {
            "_id": "3",
            "PersonID": 3,
            "Department": "MIT Product",
            "Departmentref": 804,
            "RegionID": 12
          }, {
            "_id": "231",
            "PersonID": 231,
            "Department": "MIT Tech",
            "Departmentref": 803,
            "RegionID": 6
          }, {
            "_id": "229",
            "PersonID": 229,
            "Department": "MIT Sales",
            "Departmentref": 805,
            "RegionID": 6
          }]
        }
      },
      "condition": "$ENV(node-env)"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*"],
          ["add", "rdf:type",
            ["ni", "crm:personData"]
          ]
        ]
      }
    }
  }

When the above pipe completes a run, given that the property ``"condition": "$ENV(node-env)"`` equals ``"condition": "test"`` and **not** ``"condition": "prod"``, it will only see the data that is defined within the dictionary key named ``test``. As such, by changing the value of ``$ENV(node-env)`` one can alter whether a pipe executes the DTL defined within the ``test`` or ``prod`` dictionary, as defined in the above config. Moving on to the actual testdata itself, you should take into account how well your testdata represents expected "real life" data. This is important to consider as a close resemblance between testing and reality minimizes room for error. Room for error is in this aspect related to how data is intended to be modelled through a given Sesam dataflow. **Note**: In case you work with personally identifiable indicators, you should anonymize these to make sure you are not breeching any rules or regulations with regards to the General Data Protection Regulation (GDPR).     

.. seealso::

  :ref:`dtl-beginner-3-1`

  Tools > Sesam Client :ref:`concepts-sesam-client`

  Best Practices > Working on a Sesam Project :ref:`setting-up-a-new-sesam-project`

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

.. seealso::

  TODO

.. _jwt-authentication-4-1:

JWT/Authentisering
~~~~~~~~~~~~~~~~~~

Hvordan fungerer JWT’er?

NB: Skal snake mer om API I sesam-in-the-wild

.. seealso::

  TODO

.. _groups-and-permissions-4-1:

Groups & Permissions
~~~~~~~~~~~~~~~~~~~~

Hvordan virker det

Får man satt opp tilgangsstyring i Sesam?

.. seealso::

  TODO

.. _tasks-for-projects-infrastructure-beginner-4-1:

Tasks for Projects & Infrastructure: Beginner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
