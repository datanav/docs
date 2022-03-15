.. _getting-started-setting-up-our-sesam-node:

Setting up our Sesam instance
-----------------------------
You must sign up using the `Sesam Portal <https://portal.sesam.io/auth/login?redirect=dashboard>`__ to purchase new or access existing Sesam instances. The default instance type is cloud based, but it's also possible to install Sesam on-premise or in a local cloud environment. If you consider this option, please be free to contact us on info@sesam.io for further information). This document assumes a cloud based installation. You can also access an existing Sesam instance by registering in the `Sesam Portal <https://portal.sesam.io/auth/login?redirect=dashboard>`__ and obtaining an invitation from someone with management permissions for the existing installation.

The following guide requires the use of Python 3.5.x/3.4.x and a Git client.

.. _getting-started-sign-up:

Sign up
=======

Go to the `Sesam Portal <https://portal.sesam.io/auth/login?redirect=dashboard>`__ and sign up.

Once you've signed up you'll see this page. Click on Request private trial.

.. image:: images/getting-started/dashboard-view.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Once you get access to your requested private trial from the Sesam team you'll get a card for your requested node in the Dashboard. If wanted, you can change the name of the node in the 'Basics' section under 'Subscription'-settings.

.. _getting-started-upload-config:

Upload config
=============

Please note that uploading a config as described below **will overwrite** any config already on the node. You should have a node dedicated for the purpose if you are going set it up for this guide and its labs.

Download the :download:`getting-started-config.json<files/getting-started-config.json>` and save it locally on your computer.

Go to your 'Requested private trial node' on the Sesam portal. Click on **Datahub** in the left menu and select the **Tools tab**.

.. image:: images/getting-started/importdata.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Upload the getting-started-config.json file through the drag & drop interface. Then go to the **Variables** tab and paste the below code as environment variables.

::

  {
    "node-env": "test",
    "pump-mode": "manual",
    "udir-baseurl": "https://data-nxr-fellestjeneste.udir.no/api/%s"
  }

You should now have several pipes available in the **pipes** tab. Select all pipes and click the **Enable** and **Start** buttons. This will first populate the input pipes' datasets with test data and then subsecuently the rest of the pipes will run to make the data flow downstream and populate the node. You can click on a pipe in the list to see details on how it's configured.

Config contents
^^^^^^^^^^^^^^^

The config, and now our node, contains eight input pipes. Six of them have embedded person data, one has postal codes and the last one has embedded orders from a webshop. In addition there is a a merge pipe for person data, two global pipes, and example pipes for modelling and exporting person address data. Have a look at how the pipes are connected by navigating between them through their Graph-tabs. The "merged-person" pipe is a good place to start.
