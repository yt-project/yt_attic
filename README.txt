This is the yt attic, a repository of yt analysis modules that have
fallen by the wayside and could use a new home.  If you find anything
interesting in here, please feel free to take it over.

These modules can be installed as a python package by doing:

python setup.py develop

Once installed, they can be imported as yt.extensions.attic.  For
example,

from yt.extensions.attic.star_analysis.api import StarFormationRate

These modules come with all documentation that was written for them.
To see these docs, do the following:

cd doc
make html

Enjoy!
