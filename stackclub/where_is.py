def where_is(object, in_the=None):
    """
    Print a markdown hyperlink to the source code of `object`.
    
    Parameters
    ==========
    object: python object
        The class or function you are looking for.
    inthe: string, optional
        The kind of place you want to look in: ['source','repo','technotes']
    
    Notes
    =====
    Minimal error handling. Not extensively tested.
    """
    
    # Locate the module that contains the desired object, and break its name into pieces:
    modulename = object.__module__
    pieces = str.split(modulename,'.')
    objectname = object.__name__

    # Form the URL, and a useful markdown representation of it:
    if in_the is None: in_the = 'source'
    
    if in_the == 'source':
        URL = 'https://github.com/'+pieces[0]+'/'+pieces[1]+'_'+pieces[2] \
            + '/blob/master/python/'+pieces[0]+'/'+pieces[1]+'/'+pieces[2]+'/'+pieces[3]+'.py'
        link = '['+modulename+']('+URL+')'
    
    elif in_the == 'repo':
        URL = 'https://github.com/search?l=Python&q=user%3Alsst+'+objectname+'&type=Code'
        link = '[searching for `'+objectname+'` in the `lsst` repo]('+URL+')'

    elif in_the == 'technotes':
        URL = 'https://github.com/search?l=reStructuredText&q=user%3Alsst-dm+'+objectname+'&type=Code'
        link = '[searching for `'+objectname+'` in the `lsst-dm` technotes]('+URL+')'
        
    else:
        raise ValueError("unrecognized kwarg "+in_the)
    
    from IPython.display import display, Markdown
    display(Markdown(link))

    print(link)

    return