.. yt_attic documentation master file, created by
   sphinx-quickstart on Wed Apr 19 15:51:58 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

This is the yt attic.
=====================

This is a repository of yt analysis modules that have fallen by the
wayside.  Some have not been updated to stay current with yt
development and some may not be working correctly.  If you would like
to revive anything in here and/or incorporate into your own software
packages, please do!  Also, consider listing your code on the
`yt Extensions page <http://yt-project.org/extensions.html>`__.

Checking out the yt Attic
-------------------------

The yt Attic repository can be found `here
<https://github.com/yt-project/yt_attic>`__.  In order to work
with attic packages, `yt <http://yt-project.org/>`__ must be installed.
To download and install the attic, do the following:

.. code-block:: bash

   $ git clone https://github.com/yt-project/yt_attic
   $ cd yt_attic
   $ python setup.py develop

Importing Modules
-----------------

Packages in the attic can be imported as
``yt.extensions.attic.<package_name>``.  For example,

.. code-block:: python

   from yt.extensions.attic.star_analysis.api import StarFormationRate

If you find something you like in here, give it a new home!

.. _attic-modules:

In the Attic
------------
Below is the existing documentation for all modules in the attic.

.. toctree::
   :maxdepth: 1

   halo_mass_function.rst
   star_analysis.rst
   sunrise_export.rst
   two_point_functions.rst
