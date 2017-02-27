=========
Profiling
=========

.. contents:: Table of Contents
   :depth: 2
   :local:




-------------------
Profiling API calls
-------------------

If a call to one of the
:ref:`Sesam API  <api-top>` endpoints are too slow it is sometimes useful to do some profiling to figure out what
the cause of the problem is.

There are two different options for doing this:

Profiling all Sesam API calls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Starting the sesam service with the '--enable-api-profiler' commanline option set. This will make the sesam service
log *all* api calls to files in the "<LOGFILE_FOLDER>/api_profiler" folder.

This is mainly useful for development and debugging, since it requires you to restart the sesam service with
the commanline option set and to have access to files in the <LOGFILE_FOLDER>. This is not possible to do with
a Sesam service that is running in the Sesam cloud.

Also, this option generates a lot of log-files (which are not automatically cleaned up), so on a production box it
would eventually fill up the disk.

Profiling one specific Sesam API call
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adding the special "SESAM_API_PROFILER" header to the Sesam APi request will make the Sesam instance return a file
containing the profile-information for the api-call. The "real" response from the api-call is discarded.

A header-value of "pstats" will return a file that can be loaded with pythons `pstats module
<https://docs.python.org/3/library/profile.html#the-stats-class>`_.

A header-value of "calltree" will return a file that can be opened in `KCachegrind
<https://kcachegrind.github.io/html/Home.html>`_.

[adfsaf|http://www.repoze.org/LICENSE.txt]

    Examples using curl:

      curl -v -O -J -H "SESAM_API_PROFILER:pstats" http://localhost:9042/api/pipes

      curl -v -O -J -H "SESAM_API_PROFILER:calltree" http://localhost:9042/api/pipes
