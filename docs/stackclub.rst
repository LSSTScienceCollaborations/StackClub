The ``stackclub`` Package
=========================
The Stack Club tutorial Jupyter notebooks make use of a number of homegrown functions and classes, which are kept in the ``stackclub`` package for easy import. You can browse these modules below.


Finding Documentation
---------------------
There are a number of good places to find information about the classes and functions in the LSST software Stack: the built-in Jupyter notebook ``help()`` function already gets us a long way, but if you want to locate and read the source code, the ``stackclub.where_is`` function can help.

.. automodule:: where_is
    :members:
    :undoc-members:


Importing Notebooks as Modules
------------------------------
Once this module has been imported, further ``import`` statements will treat Jupyter notebooks as importable modules. It's unlikely that you will need to call any of the functions or classes in :mod:`nbimport` yourself - this section is just for reference.

.. automodule:: nbimport
    :members:
    :undoc-members:


Importing Modules from the Web
------------------------------
This is pretty experimental!

.. automodule:: wimport
    :members:
    :undoc-members:
