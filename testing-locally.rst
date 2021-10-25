.. _setup-local-tests:

-------------------------------------
Testing a Sesam configuration locally
-------------------------------------

In a normal workflow you should test your local changes before committing them to a repository. For setting up local testing of a Sesam configuration we recommend using the Sesam client, which is a command line tool for interacting with a Sesam service instance. To install and configure the Sesam client, read this :ref:`document <concepts-sesam-client>`.

Testing a Sesam configuration should be done by running all the pipes in your local node until no pipes has any entities left in their queues, except the output pipes (which should either be disabled or unable to send data to their respective systems). Doing this manually could hence be a tedious job, especially if your configuration consists of numerous pipes, having to repeatedly start all or several pipes. The output of the endpoint pipes should then be verified against the expected output of the pipes. The Sesam client includes a nifty feature for this, both for running the pipes to their conclusion and verifying the end result.

Configuring tests
-----------------

However, for this to work, you have to configure your Sesam configuration with a test-file for each endpoint pipe. In the same directory as you have your 'pipes' and 'systems' folders, you need to add a new folder named 'expected', this will be the folder that contains the test files and the expected result for each pipe.

For each endpoint pipe in your Sesam configuration, you need to add two files (replace <name_of_pipe> with the name of the pipe):

	* <name_of_pipe>.json
	* <name_of_pipe>.test.json

The file with the .json extension is the file that shall contain the expected result. The file with the .test.json extension should contain the test configuration for that pipe, the available settings for this file are listed below:

.. list-table::
   :header-rows: 1
   :widths: 10, 25, 10, 10, 30

   * - Property
     - Description
     - Type
     - Required
     - Default

   * - ``_id``
     - | Name of the test.
     - | ``string``
     - |  No
     - |  Name of the ``.test.json file``

   * - ``type``
     - | Config type so that this later can just be part of the rest of the config.
     - | ``string``
     - |  No
     - |  Test

   * - ``description``
     - | A description of the test.
     - | ``string``
     - |  No
     - |

   * - ``ignore``
     - | If the output should be ignored during tests.
     - | ``boolean``
     - |   No
     - | ``false``

   * - ``endpoint``
     - | If the output should be fetched from a published endpoint instead.
     - | ``string``
     - |   No
     - | By default the json is grabbed from ``/pipes/<my-pipe>/entities``

   * - ``stage``
     - | In which pipe stage to get the entities (source/before-transform/after-transform/sink).
     - | ``string``
     - |   No
     - | By default the stage is ``sink``

   * - ``file``
     - | File that contains the expected results.
     - | ``string``
     - |   No
     - | Name of the .test.json file without .test (e.g. foo.test.json looks for foo.json).

   * - ``pipe``
     - | Pipe that contains the output to test.
     - | ``string``
     - |   No
     - | Name of the .test.json file without .test (e.g. foo.test.json looks for foo.json).

   * - ``blacklist``
     - | Properties to ignore in the output.
     - | ``Array of strings``
     - |   No
     - | ``[]``

   * - ``parameters``
     - | Which parameters to pass as bound parameters. Note that parameters only works for published endpoints.
     - | ``Object``
     - |   No
     - | ``{}``

Example:

::

    {
    	$ cat foo.test.json
        {
	      "_id": "foo",
	      "type": "test",
	      "file": "foo.json"
	      "blacklist": ["my-last-updated-ts"],
	      "ignore": false
        }
    }

DTL parameters
==============

If you need to pass various variations of bound parameters to the DTL, you just create multiple .test.json files for each combination of parameters.

Example:

::

    {
    	$ cat foo-A.test.json
	    {
	      "pipe": "foo",
	      "file": "foo-A.xml",
	      "endpoint": "xml",
	      "parameters": {
	      	"my-param": "A"
	      }
	    }

    	$ cat foo-B.test.json
	    {
	      "pipe": "foo",
	      "file": "foo-B.xml",
	      "endpoint": "xml",
	      "parameters": {
	      	"my-param": "B"
	      }
	    }
	}

This will compare the output of ``/publishers/foo/xml?my-param=A`` with the contents of ``foo-A.xml`` and ``/publishers/foo/xml?my-param=B`` with the contents of ``foo-B.xml``.

Internal properties
===================

All internal properties except ``_id`` and ``_deleted`` are removed from the output. Entities that has ``_deleted`` set to ``false`` will also be removed.

Endpoints
=========

By default the entities are fetched from ``/pipes/<my-pipe>/entities``, but if endpoint is set it will be fetched from
``/publishers/<my-pipe>/<endpoint-type>`` based on the endpoint type specified. Note that the pipe needs to be configured to publish to this endpoint.

Example:

::

    {
      "_id": "foo",
      "type": "test",
      "endpoint": "xml",
      "file": "foo.xml"
    }

This will compare the output of ``/publishers/foo/xml`` with the contents of ``foo.xml``.

Example:

::

    {
      "_id": "foo",
      "type": "test",
      "endpoint": "json",
      "stage": "source"
    }

This will compare the output of ``/pipes/foo/entities?stage=source`` with the contents of ``foo.json``, useful when the pipe's sink strips away the "_id" property for example.

Running tests locally
=====================

To test your Sesam configuration locally, run the following commmand:
::

    sesam -vv test

If you haven't configured up the tests correctly or there are endpoint pipes that doesn't have any corresponding test file, you will be notified. If so, fix the missing tests and then run the commmand again. If the tests runs ok, you will get a message that all the tests has passed. If any test failed, you will be notified which test / pipe that failed and get a comparision of the expected result and the received result.
