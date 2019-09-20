import numpy as np
from IPython.display import display, Markdown

class Taster(object):
    """
    Worker for tasting the datasets in a Butler's repo (based mostly off of querying metadata).
    Instantiate with a repo.
    """
    def __init__(self, repo, vb=False, path_to_tracts=''):
        self.repo = repo
        # Instantiate a butler, or report failure:
        from lsst.daf.persistence import Butler
        try:
            self.butler = Butler(repo)
        except:
            self.butler = None
            print("Warning: failed to instantiate a butler to get data from repo '"+repo+"'")
            return None
        # Set up some internal variables:
        self.vb = vb
        self.exists = {}
        self.existence = False
        self.counts = {}
        self.tracts = []
        self.path_to_tracts = path_to_tracts
        if path_to_tracts != '':
            try:
                self.skymap_butler = Butler(repo + path_to_tracts)
            except:
                self.skymap_butler = None
                print("Warning: failed to find a skyMap for the path " + repo + path_to_tracts)
        return
    
    def what_exists(self, all=False):
        """
        Check for the existence of various useful things. 
        
        Parameters
        ==========
        all: boolean
            If true, the method will check all possible dataset types
        
        Returns
        =======
        exists: dict
            Checklist of what exists (True) and what does not (False)
        """
        # Get mappers for all tested repos
        from lsst.obs.hsc import HscMapper
        from lsst.obs.comCam import ComCamMapper
        #from lsst.obs.lsst import LsstCamMapper
        from lsst.obs.ctio0m9 import Ctio0m9Mapper
        
        #select proper mapper
        if self.repo.find('hsc') != -1: mapper = HscMapper(root=self.repo)
        elif self.repo.find('comCam') != -1: mapper = ComCamMapper(root=self.repo)
        #elif self.repo.find('DC2') != -1: mapper = LsstCamMapper(root=self.repo)
        elif self.repo.find('ctio0m9') != -1: mapper = Ctio0m9Mapper(root=self.repo)
        else: print("Unable to locate Mapper file in specified repo. Check that you selected a valid repo.")
            
        
        if all:
            #collect a list of all possible dataset types
            mapper = HscMapper(root=self.repo)
            all_dataset_types = mapper.getDatasetTypes()

            remove = ['_config', '_filename', '_md', '_sub', '_len', '_schema', '_metadata']

            interesting = []
            for dataset_type in all_dataset_types:
                keep = True
                for word in remove:
                    if word in dataset_type:
                        keep = False
                if keep:
                    interesting.append(dataset_type)
        
        else: 
            interesting = ['raw', 'calexp', 'src', 'deepCoadd_calexp', 'deepCoadd_meas']
        
        self.look_for_datasets_of_type(interesting)
        self.look_for_skymap()
        self.existence = True
        return
    
    def look_for_datasets_of_type(self, datasettypes):
        """
        Check whether dataset of given type is in the metadata.
        
        Parameters
        ==========
        datasettype: list of strings
            Types of dataset to check for, eg 'calexp', 'raw', 'wcs' etc. 
        """
        datasets_that_exist = []
        datasets_that_do_not_exist = []
        
        for datasettype in datasettypes:        
            try:
                datasetkeys = self.butler.getKeys(datasettype)
                onekey = list(datasetkeys.keys())[0]
                metadata = self.butler.queryMetadata(datasettype, [onekey])
                #if self.vb: print("{} dataset exists.".format(datasettype))
                datasets_that_exist.append(datasettype)
                self.exists[datasettype] = True
            except:
                #if self.vb: print("{} dataset doesn't exist.".format(datasettype))
                datasets_that_do_not_exist.append(datasettype)
                self.exists[datasettype] = False
        
        #Organize output
        if self.vb:
            print("Datasets that exist\n-------------------")
            print(datasets_that_exist)
            print("\nDatasets that do not exist\n--------------------------")
            print(datasets_that_do_not_exist)
            
        return
    
    def look_for_skymap(self):
        """
        Check for the existence of a skymap. 
        """
        try:
            self.skyMap = self.skymap_butler.get('deepCoadd_skyMap')
            self.exists['deepCoadd_skyMap'] = True
            if self.vb: print("\nSkymap\n-------------------\ndeepCoadd_skyMap exists.")
        except:
            self.skyMap = None
            self.exists['deepCoadd_skyMap'] = False
            if self.vb: print("\nSkymap\n-------------------\ndeepCoadd_skyMap doesn't exist.")
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
                 glob.glob(os.path.join(self.repo + self.path_to_tracts, 'deepCoadd-results', 'merged', '*'))])
        
        self.tracts = tracts
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
        Count the available number of calexp visits, sensors, fields etc.
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
    
    def plot_sky_coverage(self):
        import matplotlib.pyplot as plt
        fig = plt.figure()

        for tract in self.tracts:
            tractInfo = self.skyMap[tract]

            corners = [(x[0].asDegrees(), x[1].asDegrees()) for x in tractInfo.getVertexList()]
            x = [k[0] for k in corners] + [corners[0][0]]
            y = [k[1] for k in corners] + [corners[0][1]]

            plt.plot(x,y, color='b')

        plt.xlabel('RA (deg)')
        plt.ylabel('Dec (deg)')
        plt.title('2D Projection of Sky Coverage')

        plt.show()
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
        display(Markdown('### Main Repo: %s' % self.repo))
        if self.path_to_tracts != '':
            display(Markdown('### Specified Tract Directory: %s' %self.path_to_tracts))

        # Make a table of the collected metadata
        output_table = "|   Metadata Characteristics  |  | \n  | :---: | --- | \n "
        for key in self.counts.keys():
            output_table += "| %s |  %s | \n" %(key, self.counts[key])
        
        # Display it:
        display(Markdown(output_table))
        
        # Plot sky coverage
        self.plot_sky_coverage()

        return
