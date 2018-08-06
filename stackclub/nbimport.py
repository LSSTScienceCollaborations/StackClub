"""
Adapted from the Jupyter notebook documentation at https://github.com/jupyter/notebook/blob/master/docs/source/examples/Notebook/Importing%20Notebooks.ipynb for use in the stackclub package Phil Marshall (August 2018).

Copyright (c) Jupyter Development Team, Phil Marshall. 
Distributed under the terms of the Modified BSD License, 
https://github.com/jupyter/notebook/blob/master/COPYING.md
"""
import io, os, sys, types
from IPython import get_ipython
from nbformat import read
from IPython.core.interactiveshell import InteractiveShell
from io import StringIO
import contextlib

def find_notebook(fullname, path=None):
    """find a notebook, given its fully qualified name and an optional path
    
    This turns "foo.bar" into "foo/bar.ipynb"
    and tries turning "Foo_Bar" into "Foo Bar" if Foo_Bar
    does not exist.
    """
    name = fullname.rsplit('.', 1)[-1]
    if not path:
        path = ['']
    for d in path:
        nb_path = os.path.join(d, name + ".ipynb")
        if os.path.isfile(nb_path):
            return nb_path
        # let import Notebook_Name find "Notebook Name.ipynb"
        nb_path = nb_path.replace("_", " ")
        if os.path.isfile(nb_path):
            return nb_path


@contextlib.contextmanager
def stdoutIO(stdout=None):
    """
    Catching the stdout of the imported notebook cells. 
    From https://stackoverflow.com/questions/3906232/python-get-the-print-output-in-an-exec-statement/3906390#3906390
    This does not capture any rich output, though.
    """
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old
    return

class NotebookLoader(object):
    """Module Loader for Jupyter Notebooks"""
    def __init__(self, path=None):
        self.shell = InteractiveShell.instance()
        self.path = path
    
    def load_module(self, fullname):
        """Import a notebook as a module"""
        path = find_notebook(fullname, self.path)
        
        print ("Importing code from Jupyter notebook %s" % path)
                                       
        # load the notebook object
        with io.open(path, 'r', encoding='utf-8') as f:
            nb = read(f, 4)
        
        # create the module and add it to sys.modules
        # if name in sys.modules:
        #    return sys.modules[name]
        mod = types.ModuleType(fullname)
        mod.__file__ = path
        mod.__loader__ = self
        mod.__dict__['get_ipython'] = get_ipython
        sys.modules[fullname] = mod
        
        # extra work to ensure that magics that would affect the user_ns
        # actually affect the notebook module's ns
        save_user_ns = self.shell.user_ns
        self.shell.user_ns = mod.__dict__
        
        try:
          for cell in nb.cells:
            if cell.cell_type == 'code':
                # transform the input to executable Python
                code = self.shell.input_transformer_manager.transform_cell(cell.source)
                # run the code in the module, catching the stdout:
                with stdoutIO() as s:
                    try:
                        exec(code, mod.__dict__)
                    except:
                        print("Something wrong with one of the imported notebook cells:")
                        print(s.getvalue())        
        finally:
            self.shell.user_ns = save_user_ns
        return mod

class NotebookFinder(object):
    """Module finder that locates Jupyter Notebooks"""
    def __init__(self):
        self.loaders = {}
    
    def find_module(self, fullname, path=None):
        nb_path = find_notebook(fullname, path)
        if not nb_path:
            return
        
        key = path
        if path:
            # lists aren't hashable
            key = os.path.sep.join(path)
        
        if key not in self.loaders:
            self.loaders[key] = NotebookLoader(path)
        return self.loaders[key]

# Register the NotebookFinder:
sys.meta_path.append(NotebookFinder())

