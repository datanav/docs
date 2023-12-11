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


----------------------
Examining memory-usage
----------------------

The sesam-node has a few service api endpoints for indicating what is it using memory for.


/api/status/heap
~~~~~~~~~~~~~~~~

Returns a plain-text document with informatino about what the memory is used for. This is the most high-level memory
debug endpoint, and usually the most useful one. Example::

    Process memory information: pmem(rss=664109056, vms=3156135936, shared=71004160, text=2220032, lib=0, data=3010367488, dirty=0)

    Memory use summary:
       rocksdb.kMemTableTotal                                           :  82692096
       rocksdb.kTableReadersTotal                                       :   3266947
       rocksdb.block-cache-usage                                        :  34275312
       rocksdb.block-cache-pinned-usage                                 :    935104
       ColumnFamily memory overhead                                     :  86988000
       MemoryCachedRocksDbDataset cache size                            :  17352128
       RocksDbDataset bitsets size                                      :   1092544
       EntityBatch pool size                                            :   9244266
       Node pipes size                                                  :  14972902
       Node systems size                                                :    242230
       Node datasets size                                               :    161918
       PyMalloc cached bytes                                            :  24838224
       je_malloc fragmentation (stats.active-stats.allocated)           :  27581760
       je_malloc cached bytes and metadata (stats.resident-stats.active):  26914816
       **Total accounted for memory**                                   : 329623143
       **Unaccounted for memory (rss-total_accounted_for)               : 334485913

    Top dataset bitsets sizes:
       wikidata-organisation-organisation-enrich                      : 4672
       wikidata-organisation-collect                                  : 4672
       tripletex-account1-000002-tripletex-productunit-transform-split: 4672
       tripletex-account1-000002-tripletex-productunit-transform-emit : 4672
       tripletex-account1-000001-tripletex-productunit-transform-split: 4672
       tripletex-account1-000001-tripletex-productunit-transform-emit : 4672
       tenant000002-global-classification-enhance-merge               : 4672
       tenant000001-global-classification-enhance-merge               : 4672
       tenant-auth                                                    : 4672
       system:pump:wikidata-organisation-organisation-enrich          : 4672

    Top column family size-all-mem-tables:
       n0 (NodeState)                                                                                        : 6293504
       l760 (dataset 'system:pump:tripletex-account1-000002-tripletex-vattype-classification-enrich')        : 1050624
       l748 (dataset 'system:pump:tripletex-account1-000002-tripletex-supplier-organisation-enrich')         : 1050624
       l746 (dataset 'system:pump:tripletex-account1-000002-tripletex-supplier-location-enrich')             : 1050624
       l738 (dataset 'system:pump:tripletex-account1-000002-tripletex-supplier-collect')                     : 1050624
       l722 (dataset 'system:pump:tripletex-account1-000002-tripletex-projectcategory-classification-enrich'): 1050624
       l714 (dataset 'system:pump:tripletex-account1-000002-tripletex-project-task-enrich')                  : 1050624
       l702 (dataset 'system:pump:tripletex-account1-000002-tripletex-project-collect')                      : 1050624
       l686 (dataset 'system:pump:tripletex-account1-000002-tripletex-productunit-classification-enrich')    : 1050624
       l68 (dataset 'system:pump:wikidata-organisation-organisation-enrich')                                 : 1050624

    Top column family estimate-table-readers-mem (i.e. index and filter blocks):
       l68 (dataset 'system:pump:wikidata-organisation-organisation-enrich')                               : 29708
       l23 (dataset 'system:backup')                                                                       : 25464
       l6 (dataset 'system:pump:system:update-storage-node-pipe-entity-type')                              : 25452
       l52 (dataset 'system:pump:global-organisation')                                                     : 23342
       l67 (dataset 'wikidata-organisation-organisation-enrich')                                           : 21220
       l422 (dataset 'wikidata-organisation-collect')                                                      : 19107
       l51 (dataset 'global-organisation')                                                                 : 19098
       l335 (dataset 'system:pump:tripletex-account1-000001-tripletex-productunit-classification-enrich')  : 16984
       l325 (dataset 'system:pump:tripletex-account1-000001-tripletex-productgrouprelation-product-enrich'): 16984
       l245 (dataset 'system:pump:tripletex-account1-000001-tripletex-order-agreement-enrich')             : 16984

    Python memory summary:
                                            types |   # objects |   total size
    ============================================= | =========== | ============
                                             dict |      222350 |     57.27 MB
                                              str |      530396 |     46.13 MB
                                             list |      309512 |     27.02 MB
                                             code |       41449 |      7.37 MB
                                              set |       10204 |      5.28 MB
                                      pytrie.Node |      113661 |      5.20 MB
                                             type |        5192 |      4.88 MB
                                            tuple |       72466 |      4.40 MB
                          collections.OrderedDict |        4157 |      1.72 MB
                                          weakref |       12841 |    902.88 KB
                                collections.deque |        1114 |    680.39 KB
                                              int |       20285 |    588.96 KB
                                      abc.ABCMeta |         532 |    562.54 KB
                                datetime.datetime |       10961 |    513.80 KB
                       builtin_function_or_method |        7035 |    494.65 KB
                                        frozenset |        1854 |    490.83 KB
                              function (__init__) |        3301 |    438.41 KB
                                         property |        5573 |    391.85 KB
                                getset_descriptor |        5772 |    360.75 KB
            openpyxl.descriptors.MetaSerialisable |         334 |    347.05 KB
                                             cell |        8846 |    345.55 KB
                                       re.Pattern |         560 |    280.00 KB
                          lake.store.ext_types.NI |        4290 |    201.09 KB
                              function (__repr__) |        1248 |    165.75 KB
                                           method |        2526 |    157.88 KB
                          collections.defaultdict |         259 |    141.70 KB
                                method_descriptor |        1834 |    128.95 KB
                               wrapper_descriptor |        1804 |    126.84 KB
                              function (<lambda>) |         870 |    115.55 KB
                                            float |        4745 |    111.21 KB
                                function (__eq__) |         836 |    111.03 KB
                     _frozen_importlib.ModuleSpec |        2349 |    110.11 KB
                     cachetools.keys._HashedTuple |        1989 |    109.25 KB
               lake.store.rocksdb.SegmentedBitset |        2301 |    107.86 KB
      _frozen_importlib_external.SourceFileLoader |        2256 |    105.75 KB
                                    enum.EnumMeta |          96 |    100.55 KB
                                            bytes |        2565 |    100.25 KB
                                function (__ne__) |         726 |     96.42 KB
                                    _thread.RLock |        2039 |     95.58 KB
                  lake.store.rocksdb.ColumnFamily |        1977 |     92.67 KB
                   lake.dtl.dtl_hops.CompiledHops |        1023 |     87.91 KB
                               function (to_dict) |         611 |     81.15 KB
                                function (to_str) |         605 |     80.35 KB
                                     _thread.lock |        1882 |     73.52 KB
                            jinja2.nodes.NodeType |          68 |     70.66 KB
                                member_descriptor |        1021 |     63.81 KB
                      pgpy.types.MetaDispatchable |          61 |     63.38 KB
                        cython_function_or_method |         315 |     61.15 KB
              lake.store.rocksdb.RocksDbEntityLog |         767 |     53.93 KB
            lake.store.rocksdb.RocksDbEntityIndex |         767 |     53.93 KB



/api/status
~~~~~~~~~~~

Returns a json document that among other things include memoryrelated output from the https://pypi.org/project/psutil package. Example::

    {
      "node_id": "singlenode",
      "node_version": "1.0.230521.651",
      "node_start_time": "2023-05-23T08:41:53Z",
      "node_uptime": "1 hours, 59 minutes, 19 seconds",
      "psutil.virtual_memory": {
        "total": 50481627136,
        "available": 30703407104,
        "percent": 39.2,
        "used": 18712219648,
        "free": 1521696768,
        "active": 9185828864,
        "inactive": 36309233664,
        "buffers": 2002059264,
        "cached": 28245651456,
        "shared": 542887936,
        "slab": 2964918272
      },
      ...

/api/status/debugmallocstats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns the results of running the sys._debugmallocstats() function. Example::

    Small block threshold = 512, in 32 size classes.

    class   size   num pools   blocks in use  avail blocks
    -----   ----   ---------   -------------  ------------
        0     16         133           32277          1372
        1     32        2711          310874         30712
    ...
       30    496         139            1084            28
       31    512         265            1839            16

    # arenas allocated total           =                1,784
    # arenas reclaimed                 =                  851
    # arenas highwater mark            =                1,054
    # arenas allocated current         =                  933
    933 arenas * 262144 bytes/arena    =          244,580,352

    # bytes in allocated blocks        =          215,139,648
    # bytes in available blocks        =           14,324,112
    2670 unused pools * 4096 bytes     =           10,936,320
    # bytes lost to pool headers       =            2,738,016
    # bytes lost to quantization       =            1,442,256
    # bytes lost to arena alignment    =                    0
    Total                              =          244,580,352

               13 free PyDictObjects * 48 bytes each =                  624
              31 free PyFloatObjects * 24 bytes each =                  744
              ...

