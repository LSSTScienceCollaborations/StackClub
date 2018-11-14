import numpy as np
from IPython.display import display, Markdown

class Taster(object):
    """
    Worker for tasting all the datasets in a Butler's repo.
    Instantiate with a repo.
    """
    def __init__(self, repo, vb=False):
        self.repo = repo
        from lsst.daf.persistence import Butler
        self.butler = Butler(repo)
        self.vb = vb
        self.exists = {}
        self.existence = False
        self.counts = {}
        return
    
    def what_exists(self):
        """
        Check for the existence of various useful things. 
        
        Returns
        =======
        exists: dict
            Checklist of what exists (True) and what does not (False)
        """
        interesting = ['raw', 'calexp', 'src', 'deepCoadd_calexp', 'deepCoadd_mergeDet']
        self.look_for_datasets_of_type(interesting)
        self.look_for_skymap()
        self.existence = True
        return self.exists
    
    def look_for_datasets_of_type(self, datasettypes):
        """
        Check for the existence of the dataset of given type.
        
        Parameters
        ==========
        datasettype: list of strings
            Types of dataset to check for, eg 'calexp', 'raw', 'wcs' etc. 
        """
        for datasettype in datasettypes:        
            try:
                datasetkeys = self.butler.getKeys(datasettype)
                onekey = list(datasetkeys.keys())[0]
                metadata = self.butler.queryMetadata(datasettype, [onekey])
                if self.vb: print("{} dataset exists.".format(datasettype))
                self.exists[datasettype] = True
            except:
                if self.vb: print("{} dataset doesn't exist.".format(datasettype))
                self.exists[datasettype] = False
        return
    
    def look_for_skymap(self):
        """
        Check for the existence of a skymap. 
        """
        try:
            self.skyMap = self.butler.get('deepCoadd_skyMap')
            self.exists['deepCoadd_skyMap'] = True
            if self.vb: print("deepCoadd_skyMap exists.")
        except:
            self.skyMap = None
            self.exists['deepCoadd_skyMap'] = False
            if self.vb: print("deepCoadd_skyMap doesn't exist.")
        return
    
    def estimate_sky_area(self):
        """
        Use available skymap to estimate sky area covered by tracts and patches.
        
        Returns
        =======
        area: float
            Sky area in square degrees
        """
        if self.skyMap is None: return None
        
        area_label = 'Total Sky Area (deg$^2$)'
        if area_label in self.counts.keys():
            return self.counts[area_label]
        
        # Collect tracts from files
        import os, glob
        tracts = sorted([int(os.path.basename(x)) for x in
                 glob.glob(os.path.join(self.repo, 'deepCoadd-results', 'merged', '*'))])
        self.counts['Number of Tracts'] = len(tracts)
        # Note: We'd like to do this with the butler, but it appears 'tracts' have to be
        #       specified in the dataId to be queried, so the queryMetadata method fails

        # Calculate area from all tracts
        total_area = 0.0  #deg^2
        plotting_vertices = []
        for test_tract in tracts:
            # Get inner vertices for tract
            tractInfo = self.skyMap[test_tract]
            vertices = tractInfo._vertexCoordList
            plotting_vertices.append(vertices)

            # Calculate area of box
            av_dec = 0.5 * (vertices[2][1] + vertices[0][1])
            av_dec = av_dec.asRadians()
            delta_ra_raw = vertices[0][0] - vertices[1][0] 
            delta_ra = delta_ra_raw.asDegrees() * np.cos(av_dec)
            delta_dec= vertices[2][1] - vertices[0][1]
            area = delta_ra * delta_dec.asDegrees()

            # Combine areas
            total_area += area

        if self.vb: print(area_label, ": ", total_area)

        # Round of the total area for table purposes
        self.counts[area_label] = round(total_area, 2)
        return self.counts[area_label]

    def count_things(self):
        """
        Count the available number of visits, sensors, fields etc.
        """
        # Collect numbers of images of various kinds:
        if self.exists['calexp']:
            self.counts['Number of Visits'] = \
                len(self.butler.queryMetadata('calexp', ['visit']))
            self.counts['Number of Pointings'] = \
                len(self.butler.queryMetadata('calexp', ['pointing']))
            self.counts['Number of Sensor Visits'] = \
                len(self.butler.queryMetadata('calexp', ['ccd']))
            self.counts['Number of Fields'] = \
                len(self.butler.queryMetadata('calexp', ['field']))
            self.counts['Number of Filters'] = \
                len(self.butler.queryMetadata('calexp', ['filter']))
        # Collect number of objects from Source Catalog
        if self.exists['src']:
            self.counts['Number of Sources'] = \
                len(self.butler.queryMetadata('src', ['id']))
        return
    
    def report(self):
        """
        Print a nice report of the data available in this repo.
        """
        # First check what's there:
        if not self.existence: self.what_exists()
        
        # Then, get the numbers:
        self.count_things()
        self.estimate_sky_area()
        
        # A nice bold section heading:
        display(Markdown('### %s' % self.repo))

        # Make a table of the collected metadata
        output_table = "|   Metadata Characteristics  |  | \n  | :---: | --- | \n "
        for key in self.counts.keys():
            output_table += "| %s |  %s | \n" %(key, self.counts[key])
        
        # Display it:
        display(Markdown(output_table))

        return