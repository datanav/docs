
.. _example-library:

===============
Example library
===============


.. contents:: Table of Contents
   :depth: 2
   :local:


Introduction
------------

In this chapter all examples with belonging config for you to use, is gathered.
Each example has context with belong cpde for you to copy into your node and test. The expected result is also included for you to see task is completed correctly.

Generating a new pipe
=====================

Below is an example of sending master data from from crm system to antoher system that needs this data. You can do this using the *"New pipe"* *template*.

In order to do this you need to generate a new pipe with information on *where does the data in question come from*, *does it need any changes*; i.e. does it need to be transformed to fit with target system and lastly you need to specify *where are we sending it to*.

Using the template we add *the source* chosing which system and which specific dataset we are using (called **"Provider"**).

Next blokc of the pipe is **"transforms"** where we add functions to transform or change the data as appropriate.

 "transform": {
    "type": "dtl",
    "rules": {
      "default": [
        ["copy", "_id"],
        ["add", "Fullname",
          ["concat", "_S.FirstName", " ", "_S.LastName"]]]
    }
  }
}
 Type: "dtl"

Rules contains the various functions or rules for transforms. They are listed in the **square brackets** of **"Default"**

The first transform is decideing which data do we need from the source.  In this case it is only *name* we need to send, so we nedo not need to copy whole dataset. 

The**id** is always useful so we copy the "_id" by adding following code: ``["copy", "_id"]`` in the **deafult** part of pipe.

In this example in the **crm system** the name is split into **"First name"** and **"Last name"** and in erp system the value is "Full name". To fix this we have to add a transform to add "Full name" and tell Sesam where to pick up data and how to "assemble" or "concatinate" the new peoperty. We can do this by adding following code after the ["copy", "_id] *seperated by comma*.


  ["add", "Fullname", 
                  ["concat","_S.FirstName"," ","_S.LastName"]]

Pipe will look like this:
  
    .. image:: images/new-pipe-transform.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept


Expected output you can see below. As seen Property "Full name" is added to the dataset. **Testpipe** is the **namespace** and is added automatically to output.
The **"_id"** is a **"system attribute"** it will not automatically show in the output. In order to see these attributes, so you need to click tick box at bottom of screen to.

.. image:: images/new-pipe-no-sys-output.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

As you can see on bottom of screen, the box with **"Show system attributes"** is ticked. The **"_id"** is now part of output together with a handfull of other system attributes.

 .. image:: images/new-pipe-output.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept



DTL config
^^^^^^^^^^

::

    {
    "_id": "testpipe",
    "type": "pipe",
    "source": {
      "type": "sql",
      "system": "crm",
      "table": "customer"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "_id"],
          ["add", "Fullname",
            ["concat", "_S.FirstName", " ", "_S.LastName"]]]
      }
    }
  }


Expected output
^^^^^^^^^^^^^^^

Expected output using code above

::

  {
    "testpipe:Fullname": "Sivert Asp"
  }

If we choose to copy all ["copy", "*"], it will loook like below

::

  {
    "testpipe:Address": "Eventyrvegen 44",
    "testpipe:Customerid": "77",
    "testpipe:EmailAddress": "SivertAsp@dayrep.com",
    "testpipe:FirstName": "Sivert",
    "testpipe:Fullname": "Sivert Asp",
    "testpipe:Gender": "male",
    "testpipe:LastName": "Asp",
    "testpipe:MiddleInitial": "N",
    "testpipe:PostalCode": "2815",
    "testpipe:SSN": "01065237389",
    "testpipe:Username": "Altond"
  }

The final step is to add the **target system**. Not all pipes have this, so a seperate example will be shown.

When add the *Target* you choose values for **"system"** and **"sink"**.

In this example we are sending to *erp* so we pick that as **system value**. For sink we chose **json prototype**.

When adding **sink** to the config, the output interface changes a little. Please see below.

 .. image:: images/new-pipe-sink-output.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

DTL config with sink
^^^^^^^^^^^^^^^^^^^^

{
  "_id": "testpipe",
  "type": "pipe",
  "source": {
    "type": "sql",
    "system": "crm",
    "table": "person"
  },
  "sink": {
    "type": "json",
    "system": "erp",
    "url": ""
  },
  "transform": {
    "type": "dtl",
    "rules": {
      "default": [
        ["copy", "_id"],
        ["add", "Fullname",
          ["concat", "_S.FirstName", " ", "_S.LastName"]]]
    }
  }
}


Expected output
^^^^^^^^^^^^^^^

Expected output when adding **sink** to the *config*, the output should look like this:

::

  {
    "Fullname": "Sivert Asp",
    "_id": "77"
  }


    