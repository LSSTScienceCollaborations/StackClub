Stack Club Course Syllabus
==========================

**Contents:**
1. [Basics](#basics)
2. [Getting Started](#gettingstarted)
3. [Visualization](#visualization)
4. [Processing Single Visits](#processing)
5. [Source Detection](#detection)
6. [Image Coaddition](#coaddition)
7. [Sky background estimation](#background)
8. [PSF estimation](#psf)
9. [Source/Object measurement](#measurement)
10. [Astrometric calibration](#astrometry)
11. [Photometric calibration](#photometry)
12. [Difference Image Analysis](#dia)
13. [Data Validation](#validation)


<a name="basics"></a>1. Basics
----------

In this Session we will provide a first glimpse at how to access LSST data on the LSST Science Platform (LSP), introducing the Butler and touring the basic image and catalog data structures.

- Topics:
  + Getting started on the LSP
  + Accessing LSST data with the Butler
  + A Guided tour of a calexp object 
  + A Guided tour of an afwtable object
  + The datasets available on the LSP
  
- Stack Club Resources:
  + [GettingStarted.md](GettingStarted/GettingStarted.md)
  + [Calexp_guided_tour.ipynb](Basics/Calexp_guided_tour.ipynb)
  + [afw_table_guided_tour.ipynb](https://github.com/LSSTScienceCollaborations/StackClub/pull/116)
  + [Exploring_A_Data_Repo.ipynb](https://github.com/LSSTScienceCollaborations/StackClub/blob/project/data_inventory/drphilmarshall/Basics/Exploring_A_Data_Repo.ipynb)
  + [DataInventory.ipynb](https://github.com/LSSTScienceCollaborations/StackClub/blob/project/data_inventory/drphilmarshall/Basics/DataInventory.ipynb)

- Other References:
  + [Getting started with the LSST Science Pipelines](https://pipelines.lsst.io/getting-started/index.html)


<a name="gettingstarted"></a>2. Getting Started
----------

In this Session we will give some introduction to the Stack Club tutorials and GitHub workflow, provide a template for your first tutorial notebook, and show you how to find documentation about the LSST science pipelines.

- Topics:
  + Getting started with the Stack Club
  + Github Basics
  + Creating your First Notebook
  + Finding documentation
   
- Stack Club Resources:
  + [GettingStarted.md](GettingStarted/GettingStarted.md)
  + [HelloWorld.ipynb](GettingStarted/HelloWorld.ipynb)
  + [template_Notebook.ipynb](GettingStarted/templates/template_Notebook.ipynb)
  + [FindingDocs.ipynb](GettingStarted/FindingDocs.ipynb)

- Other References:
  + [Getting started with the LSST Science Pipelines](https://pipelines.lsst.io/getting-started/index.html)


<a name="visualization"></a>3. Visualization 
-----------------

We will explore LSST data visualization in a bit more detail. This session will start out from where we left off in the data access tutorials, but will take a deeper dive into some more powerful resources built into the LSST Stack.

- Topics:

  + Image visualization tools
  + Image + Mask visualization
  + **Survey visualization tools**
  + **Catalog visualization tools**
  + Cutouts?

- Notes:

  + There should probably be a set of tutorials specifically devoted to visualization, even if we don’t teach a lesson on it - these may exist outside the Stack Club repo though.
- Stack Club Resources:
  + [AFW_Display_Demo.ipynb](Visualization/AFW_Display_Demo.ipynb)
  + [Bokeh_holoviews_datashader.ipynb](https://github.com/LSSTScienceCollaborations/StackClub/pull/103) **(To be merged)**
  + **Dataset Inventory (Phil)**

- Other Resources:

  + [Firefly.ipynb](https://github.com/lsst-sqre/notebook-demo/blob/master/Firefly.ipynb)
  + [dm_butler_postage_stamps.ipynb](https://github.com/LSSTDESC/DC2-analysis/blob/master/tutorials/dm_butler_postage_stamps.ipynb)

<a name="processing"></a>4. Processing Single Visits
----------------------------

- Topics:

  + Detrending, calibration, instrument signature removal
  + lsst_apps package
  + Overscan, flat-fielding, bias
  + ISR (including mask bits)

- Stack Club Resources:

  + [Re-RunHSC.ipynb](https://github.com/LSSTScienceCollaborations/StackClub/pull/86) **(To be merged)**
  + [PipelineProcessingAPI.ipynb](https://github.com/LSSTScienceCollaborations/StackClub/pull/93) **(To be merged)**
  + [BrighterFatterCorrection.ipynb](ImageProcessing/BrighterFatterCorrection.ipynb)

- Other Resources:

  + [processccd.html](https://pipelines.lsst.io/getting-started/processccd.html)
  + [data repositories](https://pipelines.lsst.io/getting-started/data-setup.html)

<a name="detection"></a>5. Source Detection
--------------------

- Topics:

  + Source detection
  + Footprint Sets (and Heavy Footprints)
  + Deblending?
  + Alerts?
  + Moving objects?
  + Ways to store and access catalogs from disk

- Stack Club Resources:

  + [LowSurfaceBrightness.ipynb](SourceDetection/LowSurfaceBrightness.ipynb)
  + [lsst_stack_deblender.ipynb](Deblending/lsst_stack_deblender.ipynb)
  + [scarlet_tutorial.ipynb](Deblending/scarlet_tutorial.ipynb)

- Other Resources:

  + [Deblender.ipynb](https://github.com/RobertLuptonTheGood/notebooks/blob/2eeee8b9fe35077387485e488c965f1ea3d39418/Demos/Deblender.ipynb)

<a name="coaddition"></a>6. Image Coaddition
--------------------

- Topics:

  + Remapping
  + PSF homogenization
  + Masking
  + Template generation for DIA

- Stack Club Resources:

  + [DIA_How_To_Generate_a_Template_Image.ipynb](https://github.com/LSSTScienceCollaborations/StackClub/blob/project/DIA/drphilmarshall/DIA/DIA_How_To_Generate_a_Template_Image.ipynb) (**in progress**)

- Other Resources

  + [coaddition.html](https://pipelines.lsst.io/getting-started/coaddition.html)

<a name="background"></a>7. Sky background estimation
-----------------------------

- Topics:

  + The sky background problem
  + How is sky background derived?
  +  Validating the sky background

- Stack Club Resources: 

  + **None**

- Other Resources:

  + https://github.com/lsst-dm-tutorial/lsst2017/blob/master/tutorial.ipynb

<a name="psf"></a>8. PSF estimation 
------------------

- Topics:

  + Where does the PSF come from?
  + How is the PSF estimated?
  + Diffraction spikes
  + How do we visualize the psf

- Stack Club Resources:

  + [Image_quality_demo.ipynb](Validation/image_quality_demo.ipynb)
  + PSF and shears?

- Other Resources:

  + [PSF.ipynb](Demos/PSF.ipynb)

<a name="measurement"></a>9. Source/Object measurement
-----------------------------

- Topics:

  + Photometry
  + Aperture magnitudes
  + PSF magnitudes
  + Model magnitudes
  + Shapes
  + Light curves

- Stack Club Resources:

  + **None**

- Other Resources:

  + [Source measurement tutorial](https://pipelines.lsst.io/getting-started/photometry.html)
  + [Kron.ipynb](https://github.com/RobertLuptonTheGood/notebooks/blob/2eeee8b9fe35077387485e488c965f1ea3d39418/Demos/Kron.ipynb)

<a name="astrometry"></a>10. Astrometric calibration
---------------------------

- Topics:

  + Internal astrometry
  + External astrometry

- Projects:

  + David Shupe? Jointcal?

- Stack Club Resources

  + **None**

- Other Resources:

  + **None**

<a name="photometry"></a>11. Photometric calibration
----------------------------

- Topics:

  + Photometric standards
  + Relative photometry
  + Absolute photometry
  + SLR and other validation techniques
  + Galactic Extinction and other bugaboos

- Stack Club Resources

  + **None**

- Other Resources:

  + [Multiband analysis tutorial](https://pipelines.lsst.io/getting-started/multiband-analysis.html)

<a name="dia"></a>12. Difference Image Analysis
------------------------------

- Topics:
 
  + Template generation (noting any differences from coadd generation)
  + Image differencing
  + DIASource detection
  + DIAObject generation
  + Real/bogus classification
 
- Projects: 
 
  + Phil - DIA DRP pipeline walk-through notebook, accompanied by supporting notebooks on (possibly): template generation; image differencing and DIAsource detection; DIAobject association; forced photometry on DIAobjects. Dataset: Twinkles?
 
- Stack Club Resources:
 
  + [DIA Notebooks](https://github.com/LSSTScienceCollaborations/StackClub/tree/project/DIA/drphilmarshall/DIA) **(to be developed)**
 
- Other Resources
 
  + Twinkles and DC2 cookbooks?
  + Ask Eric Bellm for leads?

<a name="validation"></a>13. Data Validation
--------------------
    
- Topics:
 
  + Available packages: validate_drp, pipeline_analysis
 
- Projects:
 
  + Johann: Exercise package, explain what it produces?
 
- Stack Club Resources:
 
  + [Image_quality_demo.ipynb](Validation/image_quality_demo.ipynb)
 
- Other Resources:
 
  + None
