Stack Club Course Syllabus
==========================

0. Basics

   - Overview: In this Session we will go through how to access the LSST Science Pipelines, ….
   - Topics:

     + Getting started with the Stack Club
     + Accessing the LSP
     + Github Basics
     + Finding documentation
     + Creating your First Notebook

   - Getting data and common data structures
     + Butler actions and data access
     + Guided tour of a calexp 
     + Guided tour of an afwtable
     + Available catalogs: DPDD-ification will put them into queriable database, but until then tasks produce catalogs that the butler can get. 
     
   - Suggested Projects:

     + Greg: data structures and the tasks that make them

   - Stack Club Resources:

     + GettingStarted.md
     + HelloWorld.ipynb
     + FindingDocs.ipynb
     + template_Notebook.ipynb 
     + Calexp_guided_tour.ipynb
     + afw_table_guided_tour.ipynb
     + Dataset Inventory (Phil)

   - Other References:

     + Getting started with the LSST Science Pipelines

1. Visualization (1st) 

   We will explore LSST data visualization in a bit more detail. This session will start out from where we left off in the data access tutorials, but will take a deeper dive into some more powerful resources built into the LSST Stack.

   - Topics:

     + Image visualization tools
     + Image + Mask visualization
     + Survey visualization tools
     + Catalog visualization tools
     + Cutouts?

   - Notes:

     + There should probably be a set of tutorials specifically devoted to visualization, even if we don’t teach a lesson on it - these may exist outside the Stack Club repo though.
   - Stack Club Resources:
     + AFW_Display_Demo.ipynb
     + Bokeh_holoviews_datashader.ipynb (To be merged)
     + Guided Calexp 
     + Dataset Inventory (Phil)
   - Other Resources:

     + Firefly.ipynb
     + WMWV Cutout notebook

2. Processing of Single Visit Images

   - Topics:

     + Detrending, calibration, instrument signature removal
     + lsst_apps package
     + Overscan, flat-fielding, bias
     + ISR (including mask bits)

   - Stack Club Resources:

     + Re-RunHSC.ipynb (To be merged)
     + PipelineProcessingAPI.ipynb (To be merged)
     + BrighterFatterCorrection.ipynb

   - Other Resources:

     + processccd.html
     + data repositories

3. Source Detection

   - Topics:

     + Source detection
     + Footprint Sets (and Heavy Footprints)
     + Deblending?
     + Alerts
     + Moving objects
     + Topics
     + The butler
     + DAF framework
     + Ways to store and access catalogs from disk

   - Notes

     + Seeds for Phase 1 development:  Probably need to go through the step of image co-addition - it is in Image coaddition v15 HTML tutorial, but deblender is in Also v15 HTML tutorial could be a nice match, includes sample extraction of the HST data

   - Stack Club Resources:

     + LowSurfaceBrightness.ipynb
     + lsst_stack_deblender.ipynb
     + scarlet_tutorial.ipynb

   - Other Resources:

     + Deblender.ipynb

4. Image Coaddition

   - Topics:

     + Remapping
     + PSF homogenization
     + Masking
     + Template generation for DIA

   - Stack Club Resources:

     + None

   - Other Resources

     + Small bit in the HSC re-run script

5. Sky background estimation

   - Topics:

     + The sky background problem
     + How is sky background derived?
     +  Validating the sky background

   - Stack Club Resources: 

     + None

   - Other Resources:

     + https://github.com/lsst-dm-tutorial/lsst2017/blob/master/tutorial.ipynb

6. PSF estimation 

   - Topics:

     + Where does the PSF come from?
     + How is the PSF estimated?
     + Diffraction spikes
     + How do we visualize the psf

   - Stack Club Resources:

     + Image_quality_demo.ipynb
     + PSF and shears?

   - Other Resources:

     + PSF.ipynb 

7. Source/Object measurement

   - Topics:

     + Photometry
     + Aperture magnitudes
     + PSF magnitudes
     + Model magnitudes
     + Shapes
     + Light curves

   - Stack Club Resources:

     + None

   - Other Resources:

     + Source measurement
     + Kron.ipynb

8. Astrometric calibration

   - Topics:

     + Internal astrometry
     + External astrometry

   - Projects:

     + David Shupe? Jointcal?

   - Stack Club Resources

     + None

   - Other Resources:

     + None

9. Photometric calibration

   - Topics:

     + Photometric standards
     + Relative photometry
     + Absolute photometry
     + SLR and other validation techniques
     + Galactic Extinction and other bugaboos

   - Stack Club Resources

     + None

   - Other Resources:

     + https://pipelines.lsst.io/getting-started/multiband-analysis.html 

10. Difference Image Analysis (DIA)

    - Topics:
     
      + Template generation (noting any differences from coadd generation)
      + Image differencing
      + DIASource detection
      + DIAObject generation
      + Real/bogus classification
     
    - Projects: 
     
      + Phil - DIA DRP pipeline walk-through notebook, accompanied by supporting notebooks on (possibly): template generation; image differencing and DIAsource detection; DIAobject association; forced photometry on DIAobjects. Dataset: Twinkles?
     
    - Stack Club Resources:
     
      + DIA Notebooks (to be developed)
     
    - Other Resources
     
      + Twinkles and DC2 cookbooks?
      + Ask Eric Bellm for leads?

11. Data Validation
    
    - Topics:
     
      + Available packages: validate_drp, pipeline_analysis
     
    - Projects:
     
      + Johann: Exercise package, explain what it produces?
     
    - Stack Club Resources:
     
      + Image_quality_demo.ipynb
     
    - Other Resources:
     
      + None
