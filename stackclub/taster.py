class Taster(object):
    """
    Worker for tasting all the datasets in a Butler's repo.
    Instantiate with a Butler object.
    """
    def __init__(self, butler):
        self.butler = butler
        
        return
    
    def look_for_dataset_of_type(self, datasettype):
        """
        Check for the existence of the dataset of given type.
        
        Parameters
        ==========
        datasettype: string
            Type of dataset to check for, eg 'calexp', 'raw', 'wcs' etc. 
        """        
        try:
            datasetkeys = self.butler.getKeys(datasettype)
            onekey = list(datasetkeys.keys())[0]
            metadata = self.butler.queryMetadata(datasettype, [onekey])
            print("{} dataset exists.".format(datasettype))
            return True
        except:
            print("{} dataset doesn't exist.".format(datasettype))
            return False
