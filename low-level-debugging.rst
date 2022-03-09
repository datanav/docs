===================
Low-level debugging
===================

This page contains tips and tricks for doing various low-level debugging tasks. This information is only relevant
for system administrators who are hosting a sesam instance, since most of the techiques require access to the
filesystem of the box that the sesam instance is running on.

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

Adding the special "SESAM-API-PROFILER" header to the Sesam APi request will make the Sesam instance return a file
containing the profile-information for the api-call. The "real" response from the api-call is discarded.

A header-value of "pstats" will return a file that can be loaded with pythons `pstats module
<https://docs.python.org/3/library/profile.html#the-stats-class>`_.

A header-value of "calltree" will return a file that can be opened in `KCachegrind
<https://kcachegrind.github.io/html/Home.html>`_.

    Examples using curl::

      curl -v -O -J -H "SESAM-API-PROFILER:calltree" http://localhost:9042/api/pipes

      curl -v -O -J -H "SESAM-API-PROFILER:pstats" http://localhost:9042/api/pipes


Profiling a pump run
~~~~~~~~~~~~~~~~~~~~

Adding a special "profiler" request parameter to the Sesam API request will make the Sesam instance write files
containing the profile-information for the pump run. The profile files are written to the logs folder of the instance
with a "*.pstat" and "*.calltree" extension. The filename also contains the id of the pipe and the start
timestamp.

    Examples using curl::

      curl -s --data "profiler=true" --data "operation=start" http://localhost:9042/api/pipes/foo/pump


---------------------------------------------------
Getting a stacktrace of all the threads in the node
---------------------------------------------------

If the sesam node seems to be frozen or otherwise is behaving oddly, it can be useful to look at the stacktraces of
all the currently running threads in the node. There are two ways of retrieving this information:


Using the "/api/status/stacktrace" api endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is an "unofficial" endpoint that returns a html file. If the node has authentication enabled (this is the usual
case) the endpoint requires that the JWT grants the "group:Admin" role.

   Example::

     curl -o stacktrace.html http://localhost:9042/api/status/stacktrace


Sending the SIGUSR1 signal to the sesam node process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This will create a new "stacktrace.html"-file in the "logs"-folder on the server. This requires you to have
login-access to the server running the node, both for sending the signal and for looking at the resulting file.
The advantage of this method compared to the api endpoint is that this will work even if the api itself
is broken. If the signal is sent more than once, any existing "stacktrace.html"-file will be renamed to
"stacktrace.html.1" (and any existing "stacktrace.html.1" will be renamed to "stacktrace.html.2", etc. This is similar
to the way the "node.log" file is rotated).

   Example::

      knut.johannessen@myserver:/sesam/logs/sesam-node$ ls -l
      total 33104
      -rwxrwxrwx 1 777 sesam  1548906 Mar 21 12:43 node_access.log
      -rwxrwxrwx 1 777 sesam   113395 Mar 21 12:41 node_config.log
      -rwxrwxrwx 1 777 sesam    35058 Mar 21 12:43 node_health.log
      -rwxrwxrwx 1 777 sesam  1401190 Mar 21 12:43 node.log
      -rwxrwxrwx 1 777 sesam        0 Mar 17 17:49 node_memory_profile.log
      -rwxrwxrwx 1 777 sesam   136744 Mar 21 12:43 node_metrics.log
      -rwxrwxrwx 1 777 sesam 30627178 Mar 21 12:43 node_pipe_execution.log

      # First, find the process identifier of the node you are interested in.
      knut.johannessen@myserver:/sesam/logs/sesam-node$ docker inspect testsesamportal_storage-sesam-node_1 | grep '"Pid"'
            "Pid": 6280,

      # Send the SIGUSR1 signal to the node-process
      knut.johannessen@myserver:/sesam/logs/sesam-node$ sudo kill -SIGUSR1 6280

      # A new "stacktrace.html" file is created in the logs folder:
      knut.johannessen@myserver:/sesam/logs/sesam-node$ ls -l
      total 33476
      -rwxrwxrwx 1   777 sesam  1548906 Mar 21 12:43 node_access.log
      -rwxrwxrwx 1   777 sesam   113395 Mar 21 12:41 node_config.log
      -rwxrwxrwx 1   777 sesam    35058 Mar 21 12:43 node_health.log
      -rwxrwxrwx 1   777 sesam  1406116 Mar 21 12:44 node.log
      -rwxrwxrwx 1   777 sesam        0 Mar 17 17:49 node_memory_profile.log
      -rwxrwxrwx 1   777 sesam   136744 Mar 21 12:43 node_metrics.log
      -rwxrwxrwx 1   777 sesam 30723086 Mar 21 12:44 node_pipe_execution.log
      -rw-r--r-- 1 sesam sesam   279164 Mar 21 12:43 stacktrace.html

      # Sending a second signal will create a new "stacktrace.html" file and rotate the existing file:
      knut.johannessen@myserver:/sesam/logs/sesam-node$ sudo kill -SIGUSR1 6280
      knut.johannessen@myserver:/sesam/logs/sesam-node$ ls -l
      total 34148
      -rwxrwxrwx 1   777 sesam  1549330 Mar 21 12:47 node_access.log
      -rwxrwxrwx 1   777 sesam   113395 Mar 21 12:41 node_config.log
      -rwxrwxrwx 1   777 sesam    35702 Mar 21 12:47 node_health.log
      -rwxrwxrwx 1   777 sesam  1424737 Mar 21 12:47 node.log
      -rwxrwxrwx 1   777 sesam        0 Mar 17 17:49 node_memory_profile.log
      -rwxrwxrwx 1   777 sesam   139364 Mar 21 12:47 node_metrics.log
      -rwxrwxrwx 1   777 sesam 31109009 Mar 21 12:47 node_pipe_execution.log
      -rw-r--r-- 1 sesam sesam   279164 Mar 21 12:47 stacktrace.html
      -rw-r--r-- 1 sesam sesam   279164 Mar 21 12:43 stacktrace.html.1
      knut.johannessen@myserver:/sesam/logs/sesam-node$ 


Checking if the health-checker thread in the node has created a stacktrace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The node will periodically call its own "/api/health" endpoint and log the results to the "node_health.log" file.
If the call to the "/api/health" endpoint fails, the health-checker thread will create a new "stacktrace.html"-file,
just as if a SIGUSR1 signal had been sent to the node. If the node is misbehaving it is therefore worth having a
look in the "logs" folder to check if there are any recent "stacktrace.html" files.


-------------------------------------------
Preventing pipes from automatically running
-------------------------------------------

Most pipes will be configured to run automatically at certain intervals. In some cases we want to prevent
all such pipes from being started automatically.

Examples of cases where this functionality can be useful:

1. We suspect that one or more pipes are using a lot of memory, but it is hard to isolate the
   problem because lots of pipes are being started by the taskmanager.

2. The sesam node crashes on or soon after startup because of a problem with a pipe.


Using the "Instance configuration" gui
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the easiest way of disabling the pump scheduler.

   1. Log in to https://portal.sesam.io
   2. Navigate to the subscription in question.
   3. Go to the "Settings" => "Instance configuration" page.
   4. Use the "Insert configuration" dropdown to add a "TaskManager settings" item and set the "disable_pump_scheduler"
      property to "true". The resulting configuration should look something like this::

         {
           "_id": "node",
           "type": "metadata",
           "task_manager": {
             "disable_pump_scheduler": true
           }
         }

Upload a full node-config with a node metadata entity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to upload a full sesam node configuration and prevent any of the pipes in the config from starting
automatically, you can add this entity in the configuration you are uploading::

      {
        "_id": "node",
        "type": "metadata",
        "task_manager": {
          "disable_pump_scheduler": true
        }
      }

Writing a "/sesam/node/data/startup_options.json" file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If GUI is not accessable for some reason (for example if the node crashes on start-up), it is also possible to
disable the pump scheduler by creating a file in the sesam node's "data" folder.

The file must be called "startup_options.json". It must be a valid json-file and look like this::

   {
        "task_manager": {
          "disable_pump_scheduler": true
        }
   }

The sesam node must be restarted in order for the file to take effect (use docker restart <node-container-name>).
