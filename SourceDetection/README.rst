Source Detection
----------------

While source detection in the LSST science pipelines is carried out (first) during the image processing step, there are subsequent detection phases - and, moreover, we are interested in how sources are detected (and how their measured properties depends on that process). See the index table below for links to tutorial notebooks exploring this.


.. list-table::
   :widths: 10 20 10 10
   :header-rows: 1

   * - Notebook
     - Short description
     - Links
     - Owner


   * - **Low Surface Brightness**
     - Run source detection, deblending, and measurement tasks; subtract bright sources from an image; convolve image and detect low-surface brightness sources.
     - `ipynb <https://github.com/LSSTScienceCollaborations/StackClub/blob/master/SourceDetection/log/LowSurfaceBrightness.ipynb>`__,
       `rendered <https://nbviewer.jupyter.org/github/LSSTScienceCollaborations/StackClub/blob/rendered/SourceDetection/LowSurfaceBrightness.nbconvert.ipynb>`__

       .. raw:: html

             <a href="https://github.com/LSSTScienceCollaborations/StackClub/blob/rendered/SourceDetection/log/LowSurfaceBrightness.log">
               <img width="72" height="16" src="https://raw.githubusercontent.com/LSSTScienceCollaborations/StackClub/rendered/SourceDetection/log/LowSurfaceBrightness.png">
               </img>
             </a>

     - `Alex Drlica-Wagner <https://github.com/LSSTScienceCollaborations/StackClub/issues/new?body=@kadrlica>`__

   * - **Footprints**
     - Investigate the concept of a footprint: the region of an image used for detecting and measuring source properties.
     - `ipynb <https://github.com/LSSTScienceCollaborations/StackClub/blob/master/SourceDetection/log/Footprints.ipynb>`__,
       `rendered <https://nbviewer.jupyter.org/github/LSSTScienceCollaborations/StackClub/blob/rendered/SourceDetection/Footprints.nbconvert.ipynb>`__

       .. raw:: html

             <a href="https://github.com/LSSTScienceCollaborations/StackClub/blob/rendered/SourceDetection/log/Footprints.log">
               <img width="72" height="16" src="https://raw.githubusercontent.com/LSSTScienceCollaborations/StackClub/rendered/SourceDetection/log/Footprints.png">
               </img>
             </a>

     - `Imran Hasan <https://github.com/LSSTScienceCollaborations/StackClub/issues/new?body=@ih64>`__
