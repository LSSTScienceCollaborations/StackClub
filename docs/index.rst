The Stack Club Library
======================
The LSST science collaborations' `Stack Club <https://github.com/LSSTScienceCollaborations/StackClub/>`_ is learning the LSST software "stack" by writing tutorial Jupyter notebooks about it. These notebooks make use of a number of homegrown functions and classes, which are kept in the ``stackclub`` package for easy import. You can browse these modules below. 

Contents:

.. toctree::
    :maxdepth: 2
    
    index


Finding Documentation
---------------------

.. automodule:: where_is
    :members:
    :undoc-members:

Importing Modules from the Web
------------------------------

.. automodule:: wimport
    :members:
    :undoc-members:

Importing Notebooks as Modules
------------------------------

Once this module has been imported, further ``import`` statements will treat Jupyter notebooks as importable modules. It's unlikely that you will need to call any of the functions or classes in :mod:`nbimport` yourself - this section is just for reference. 

.. automodule:: nbimport
    :members:
    :undoc-members:
