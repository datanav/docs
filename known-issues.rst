============
Known Issues
============

.. contents:: Table of Contents
   :depth: 2
   :local:

The following issues are known issues with the beta release:

  - Open Sesam is automatically upgraded every night, and the user might experience short disruptions of
    service during the upgrade.

  - Users on the same Open sesam segment (``A``, ``B``, etc.) share namespace for systems and pipes.

  - Chrome on Windows will occasionally display dropdowns at the wrong location
    when opening them. This only happens on an external screen, and is a
    `known Chrome bug<https://bugs.chromium.org/p/chromium/issues/detail?id=489997>`_.
    A simple workaround is to close and reopen the dropdown again.
