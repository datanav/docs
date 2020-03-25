
.. _example-library:

===============
Example library
===============


.. contents:: Table of Contents
   :depth: 2
   :local:


Introduction
------------

Generating a new pipe
-----------------------
Say we want to send name from crm system to erp system. Crm system is masterdata for customer names and we want to use Sesam to send customer name from crm to erp system.
To do this, we need to generate a new pipe.

The first transsform is to copy wthe data we need from source. In this case it si only name we need to send, so we copy the "_id" only. In this example say in **crm system** the name is split into **"First name"** and **"Last name"** and in erp system the vlaue is "Full name". We then have to add a transform to add "Full name" and tell Sesam where to pick up data and how to "assemble" og "concatinate" the new peoperty. we can do this by adding following code:


  ["add", "Fullname", 
                  ["concat","_S.FirstName"," ","_S.LastName"]]

  Pipe will look like this:
  
    .. image:: images/new-pipe-transform.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept


Expected output you can see below. As seen Property "Full name" is added to the dataset. Testpipe is the namespace and addedd automatically to output.

 .. image:: images/new-pipe-output.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

     Pipe looks like this:

 	.. image:: images/new-pipe-4.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept


    DTL:

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


Expected output:

If we choose to copy all ["copy", "*"], it will loook like below

::

  {
    "_deleted": false,
    "_hash": "24a142c9c6be2fe119b0cc2dff3452d5",
    "_id": "testpipe:77",
    "_previous": 275,
    "_ts": 1585123420716638,
    "_updated": 375,
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

However in this example all we needed is the name, so we choose to copy the id only ["copy", "_id"] and to add "Full name". Now we get the data we need only, see output below:

::

  {
    "_deleted": false,
    "_hash": "4b3c775f6821422299269b6608ca421e",
    "_id": "testpipe:77",
    "_previous": 375,
    "_ts": 1585123695287529,
    "_updated": 475,
    "testpipe:Fullname": "Sivert Asp"
  }



    