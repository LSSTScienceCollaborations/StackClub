import os, sys
import urllib.request
import importlib

def wimport(url, vb=False):
    """
    Download a module and import it.
    
    Parameters
    ==========
    url: string
        Web address of the target module
    vb: boolean
        Verbose in operation [def=False]
    
    Returns
    =======
    globals()[modulename]: module
        The module, as imported.
    
    Notes
    =====
    `wimport` maintains a secret local cache of downloaded modules, 
    hidden from the user so that they are not tempted to edit the 
    module locally. (If they need to do that, they should clone
    the relevant repo.)
    
    Example use:
    
        where_is_url = "https://github.com/LSSTScienceCollaborations/StackClub/raw/issue/79/library/stackclub/where_is.py"
        so = wimport(where_is_url, vb=True)
        so.where_is(Butler.get, in_the='source')
    """

    # First set up wimport's .downloads directory and prepare to 
    # download the module into it:
    a = urllib.parse.urlparse(url)
    modulefile = os.path.basename(a.path)
    modulefolder = ".downloads"
    if not os.path.exists(modulefolder):
        os.makedirs(modulefolder)
    sys.path.append(modulefolder)
    modulepath = modulefolder+'/'+modulefile
    
    # Get the file, over-writing anything that is already there:
    urllib.request.urlretrieve(url, modulepath)

    # Now import the module, and add it to the global namespace:
    modulename = os.path.splitext(modulefile)[0]
    try:
        globals()[modulename] = importlib.import_module(modulename)
    except:
        print("WARNING: module was downloaded to {} but cound not be imported.")
        print("Returning path to module: {}".format(modulepath))
        return modulepath
    
    # Report to the user:
    if vb: 
        print("Imported external module '{}' (downloaded from {} and stored in {})".format(modulename, url, modulepath))
        # print("Module file contains the following lines: ")
        # with open(modulepath, 'r') as fin:
        #     print(fin.read(), end="")

    # Pass back the module, so it can be named and then used by the user.
    return globals()[modulename]