
.. _microservices-beginner-5-1:

Microservices: Beginner
-----------------------


.. _what-is-a-microservice-5-1:

What is a microservice?
~~~~~~~~~~~~~~~~~~~~~~~



Nevn bruksområder

språk

Docker

.. seealso::

  TODO

.. _why-use-microservices-in-sesam-5-1:

Why use Microservices in Sesam?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System som gjør ting andre systemer ikke kan

.. seealso::

  TODO

.. _how-are-microservices-used-in-sesam-5-1:

How are Microservices used in Sesam?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ekte Use caser

.. seealso::

  TODO

.. _microservice-hosting-5-1:

Microservice hosting
~~~~~~~~~~~~~~~~~~~~

Sesamcommunity Git & Docker

Intro til Hosting

.. seealso::

  TODO

.. _running-a-microservice-in-sesam-5-1:

Running a microservice in Sesam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Intro til Running I sesam

Forklare GUI

Pull & Restart

   Status

   Refresh

Forklare Config

Pipe source/sink/http

.. seealso::

  TODO

.. _categories-of-microservices-5-1:

Categories of Microservices
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extending on the topic of running microservices in Sesam, the following categories of microservices will be elaborated on in this section:
  
  - Internal microservices
  - External microservices

Both internal microservices and external microservices will figurate in a Sesam node as systems. However, microservices that connect to a Sesam node via the `Service API <https://docs.sesam.io/api.html>`_ can also be seen on the `Sesam Community on GitHub <https://github.com/sesam-community>`_. These kinds of microservices will not be elaborated on in this section, albeit you should be aware that these microservices exist and that they are also a viable option when extending upon default functionality.


Internal microservices
######################

These kinds of microservices are the ones used with regards to Sesam dataflows. Therefore, these are also the most commonly used. Internal microservices can be used at specific points in time with regards to a dataflow. As such, internal microservices can be used in the beginning, in the middle or at the end of a dataflow, which will respectively, in a Sesam node, turn out as a source system, http-transform system or sink system. Many of these internal microservices can be found on the `Sesam Community on GitHub <https://github.com/sesam-community>`_.


External microservices
######################

Even though external microservices figurate in Sesam as systems, they do not read or write data into or out of Sesam with regards to a defined dataflow. Rather, they implement their functionality in such a way that does not affect dataflows.

An example of such a microservice is the `Github Autodeployer <https://github.com/sesam-community/github-autodeployer>`_. This microservice connects to the GitHub API and uploads the latest version of files present on the GitHub repository in question to a Sesam node. This allows for continous integration/continous deployment (CICD) workflows and allows for easy peer reviews as changes are made to specific pipe configs.

Additional examples of external examples are listed below:  

    - `Statuspage <https://github.com/sesam-community/statuspage>`_
    - `Statuspage Monitoring Pipes <https://github.com/sesam-community/statuspage-monitoring-pipes>`_


.. seealso::
  
  Developer Guide > Service Configuration > Systems: :ref:`microservice_system`

  Systems: Beginner: :ref:`pipe-interaction-with-systems-2-1`

  `Sesam Community at GitHub <https://github.com/sesam-community>`_

  `Sesam Community Guidelines <https://github.com/sesam-community/guidelines>`_

.. _naming-convention-5-1:

Naming Convention this should probs be under architecture namegiving conventions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

\_id standard system naming convention (source/sink system name)

Repo/microservice naming convention recommendation:
sesam-<system>[-<special-functionality>]

.. seealso::

  TODO

.. _tasks-for-microservices-beginner-tasks-5-1:

Tasks for Microservices: Beginner – Tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run a microservice in Sesam [could be sink, http, source]
