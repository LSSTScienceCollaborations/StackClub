: 'HSC Re-Run: Making Forced Photometry Light Curves from Scratch
Owner: **Justin Myles** (@jtmyles)
Last Verified to Run: **2018-09-05**
Verified Stack Release: **16.0**

This project addresses issue #63: HSC Re-run

This shell script runs the command-line tasks from the tutorial at pipelines.lsst.io for analysis
from raw images through source detection and forced photometry measurements. It is intended as an 
intermediate step toward the end-goal of making a forced photometry lightcurve in the notebook at
StackClub/ImageProcessing/Re-RunHSC.ipynb

Recommended to run with 
$ bash Re-RunHSC.sh > output.txt
'


# Setup the LSST Stack
source /opt/lsst/software/stack/loadLSST.bash
eups list lsst_distrib
setup lsst_distrib


# I. Setting up the Butler data repository
date
echo "Re-RunHSC INFO: set up the Butler"

setup -j -r /project/shared/data/ci_hsc
DATADIR="/home/$USER/DATA"
mkdir -p "$DATADIR"

# A Butler needs a *mapper* file "to find and organize data in a format specific to each camera." 
# We write this file to the data repository so that any instantiated Butler object knows which mapper to use.
echo lsst.obs.hsc.HscMapper > $DATADIR/_mapper

# The ingest script creates links in the instantiated butler repository to the original data files
date
echo "Re-RunHSC INFO: ingest images with ingestImages.py"

ingestImages.py $DATADIR $CI_HSC_DIR/raw/*.fits --mode=link

# Grab calibration files
date
echo "Re-RunHSC INFO: obtain calibration files with installTransmissionCurves.py"

installTransmissionCurves.py $DATADIR
ln -s $CI_HSC_DIR/CALIB/ $DATADIR/CALIB
mkdir -p $DATADIR/ref_cats
ln -s $CI_HSC_DIR/ps1_pv3_3pi_20170110 $DATADIR/ref_cats/ps1_pv3_3pi_20170110


# II. Calibrate a single frame with processCcd.py
date
echo "Re-RunHSC INFO: process raw exposures with processCcd.py"

# Use calibration files to do CCD processing
processCcd.py $DATADIR --rerun processCcdOutputs --id


# III. (omitted) Visualize images.


# IV. Make coadds

# IV. A. Make skymap
# A sky map is a tiling of the celestial sphere. It is composed of one or more tracts.
# A tract is composed of one or more overlapping patches. Each tract has a WCS.
# We define a skymap so that we can warp all of the exposure to fit on a single coordinate system
# This is a necessary step for making coadds
date
echo "Re-RunHSC INFO: make skymap with makeDiscreteSkyMap.py"

makeDiscreteSkyMap.py $DATADIR --id --rerun processCcdOutputs:coadd --config skyMap.projection="TAN"

# IV. B. Warp images onto skymap
date
echo "Re-RunHSC INFO: warp images with makeCoaddTempExp.py"

makeCoaddTempExp.py $DATADIR --rerun coadd \
        --selectId filter=HSC-R \
        --id filter=HSC-R tract=0 patch=0,0^0,1^0,2^1,0^1,1^1,2^2,0^2,1^2,2 \
        --config doApplyUberCal=False doApplySkyCorr=False

makeCoaddTempExp.py $DATADIR --rerun coadd \
        --selectId filter=HSC-I \
        --id filter=HSC-I tract=0 patch=0,0^0,1^0,2^1,0^1,1^1,2^2,0^2,1^2,2 \
        --config doApplyUberCal=False doApplySkyCorr=False

# IV. C. Coadd warped images
# Now that we have warped images, we can perform coaddition to get deeper images
# The motivation for this is to have the deepest image possible for source detection
date
echo "Re-RunHSC INFO: coadd warped images with assembleCoadd.py"

assembleCoadd.py $DATADIR --rerun coadd \
        --selectId filter=HSC-R \
        --id filter=HSC-R tract=0 patch=0,0^0,1^0,2^1,0^1,1^1,2^2,0^2,1^2,2

assembleCoadd.py $DATADIR --rerun coadd \
        --selectId filter=HSC-I \
        --id filter=HSC-I tract=0 patch=0,0^0,1^0,2^1,0^1,1^1,2^2,0^2,1^2,2


# V. Measuring Sources

# V. A. Source detection
# As noted above, we do source detection on the deepest image possible.
date
echo "Re-RunHSC INFO: detect objects in the coadd images with detectCoaddSources.py"

detectCoaddSources.py $DATADIR --rerun coadd:coaddPhot \
        --id filter=HSC-R tract=0 patch=0,0^0,1^0,2^1,0^1,1^1,2^2,0^2,1^2,2

detectCoaddSources.py $DATADIR --rerun coaddPhot \
        --id filter=HSC-I tract=0 patch=0,0^0,1^0,2^1,0^1,1^1,2^2,0^2,1^2,2

# V. B. Merge multi-band detection catalogs
# Ultimately, for photometry, we will need to deblend objects. 
# In order to do this, we first merge the detected source catalogs.
date
echo "Re-RunHSC INFO: merge detection catalogs with mergeCoaddDetections.py"

mergeCoaddDetections.py $DATADIR --rerun coaddPhot --id filter=HSC-R^HSC-I

# V. C. Measure objects in coadds
# Given a full coaddSource catalog, we can do regular photometry with implicit deblending.
date
echo "Re-RunHSC INFO: measure objects in coadds with measureCoaddSources.py"

measureCoaddSources.py $DATADIR --rerun coaddPhot --id filter=HSC-R
measureCoaddSources.py $DATADIR --rerun coaddPhot --id filter=HSC-I

# V. D. Merge multi-band catalogs from coadds
date
echo "Re-RunHSC INFO: merge measurements from coadds with mergeCoaddMeasurements.py"

mergeCoaddMeasurements.py $DATADIR --rerun coaddPhot --id filter=HSC-R^HSC-I

# V. E. Run forced photometry on coadds
# Given a full source catalog, we can do forced photometry with implicit deblending.
date
echo "Re-RunHSC INFO: perform forced photometry on coadds with forcedPhotCoadd.py"

forcedPhotCoadd.py $DATADIR --rerun coaddPhot:coaddForcedPhot --id filter=HSC-R
forcedPhotCoadd.py $DATADIR --rerun coaddForcedPhot --id filter=HSC-I


# VI. Multi-band catalog analysis
# For analysis of the catalog, see part VI of StackClub/ImageProcessing/Re-RunHSC.ipynb
