HMpTy
=====

*Tools for working with Hierarchical Triangular Meshes (HTMs). Generate
HTMIDs, crossmatch sky-coordinates via angular separation and more*.

Usage
=====

    hmpty table <tableName> <primaryIdCol> <raCol> <decCol> -s <pathToSettingsFile>
    hmpty table --host=<host> --user=<user> --passwd=<passwd> --dbName=<dbName> <tableName> <primaryIdCol> <raCol> <decCol> [-s <pathToSettingsFile>]

    COMMANDS
    ========
    table                 add HTMids to database table

    ARGUMENTS
    =========
    tableName             name of the table to add the HTMids to
    primaryIdCol          the name of the unique primary ID column of the database table
    raCol                 name of the talbe column containing the right ascension
    decCol                name of the talbe column containing the declination
    host                  database host address
    user                  database username
    passwd                database password
    dbName                database name

    FLAGS
    =====
    -h, --help            show this help message
    -s, --settings        the settings file

Documentation
=============

Documentation for HMpTy is hosted by [Read the
Docs](http://HMpTy.readthedocs.org/en/stable/) (last [stable
version](http://HMpTy.readthedocs.org/en/stable/) and [latest
version](http://HMpTy.readthedocs.org/en/latest/)).

Installation
============

The easiest way to install HMpTy us to use `pip`:

    pip install HMpTy

Or you can clone the [github
repo](https://github.com/thespacedoctor/HMpTy) and install from a local
version of the code:

    git clone git@github.com:thespacedoctor/HMpTy.git
    cd HMpTy
    python setup.py install

To upgrade to the latest version of HMpTy use the command:

    pip install HMpTy --upgrade

Development
-----------

If you want to tinker with the code, then install in development mode.
This means you can modify the code from your cloned repo:

    git clone git@github.com:thespacedoctor/HMpTy.git
    cd HMpTy
    python setup.py develop

[Pull requests](https://github.com/thespacedoctor/HMpTy/pulls) are
welcomed!

Issues
------

Please report any issues
[here](https://github.com/thespacedoctor/HMpTy/issues).

License
=======

Copyright (c) 2016 David Young

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
