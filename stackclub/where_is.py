def where_is(object, in_the='source', assuming_its_a=None):
    """
    Print a markdown hyperlink to the source code of `object`.
    
    Parameters
    ----------
    object: python object or string
        The class or function you are looking for, or the name of a python object or file.
    in_the: string, optional
        The kind of place you want to look in: `['source', 'repo', 'technotes']`
    assuming_its_a: string, optional
        The kind of object you think you have: `['cmdlinetask'], default=None
        
    Examples
    --------

    >>> from stackclub import where_is
    >>> from lsst.daf.persistence import Butler
    >>> where_is(Butler.get, in_the='source')
    >>> where_is(Butler, in_the='repo')
    >>> where_is(Butler, in_the='technotes')
    >>> where_is("makeDiscreteSkyMap.py", in_the="source", assuming_its_a="cmdlinetask")
    
    Notes
    -----
    See also the `FindingDocs tutorial notebook <https://github.com/LSSTScienceCollaborations/StackClub/blob/master/GettingStarted/FindingDocs.ipynb>`_ for a working demo.
    
    """
    # Deal with string object names - useful for locating command line tasks:
    if isinstance(object, str):
        objectname = object
        if in_the == 'source' and assuming_its_a == None:
            raise ValueError('Cannot locate task/object `'+object+'` in the source by name. Either pass in an object, or use the "assuming_its_a" kwarg to guess what kind of object it is.')
        if assuming_its_a == "cmdlinetask":
            modulename = 'lsst.pipe.tasks.'+objectname
            
    elif hasattr(object, '__module__') and hasattr(object, '__name__'):
        # Locate the module that contains the desired object, and break its name into pieces:
        modulename = object.__module__
        objectname = object.__name__
    
    else:
        raise TypeError('Expecting "string" or "object"')

    # Form the URL, and a useful markdown representation of it:    
    if in_the == 'source':
        pieces = str.split(modulename,'.')
        URL = 'https://github.com/'+pieces[0]+'/'+pieces[1]+'_'+pieces[2] \
            + '/blob/master/python/'+pieces[0]+'/'+pieces[1]+'/'+pieces[2]+'/'+pieces[3]+'.py'
        link = '[`'+modulename+'`]('+URL+')'
    
    elif in_the == 'repo':
        URL = 'https://github.com/search?l=Python&q=org%3Alsst+'+objectname+'&type=Code'
        link = '[searching for `'+objectname+'` in the `lsst` repo]('+URL+')'

    elif in_the == 'technotes':
        URL = 'https://github.com/search?l=reStructuredText&q=org%3Alsst-dm+'+objectname+'&type=Code'
        link = '[searching for `'+objectname+'` in the `lsst-dm` technotes]('+URL+')'
        
    else:
        raise ValueError("unrecognized kwarg "+in_the)
    
    from IPython.display import display, Markdown
    display(Markdown(link))

    print(link)

    return
