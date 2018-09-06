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
echo "setup Butler"
setup -j -r /project/shared/data/ci_hsc
DATADIR="/home/$USER/DATA"
mkdir -p "$DATADIR"

# A Butler needs a *mapper* file "to find and organize data in a format specific to each camera." 
# We write this file to the data repository so that any instantiated Butler object knows which mapper to use.
echo lsst.obs.hsc.HscMapper > $DATADIR/_mapper

# The injest script creates links in the instantiated butler repository to the original data files
ingestImages.py $DATADIR $CI_HSC_DIR/raw/*.fits --mode=link

# Grab calibration files
installTransmissionCurves.py $DATADIR
ln -s $CI_HSC_DIR/CALIB/ $DATADIR/CALIB
mkdir -p $DATADIR/ref_cats
ln -s $CI_HSC_DIR/ps1_pv3_3pi_20170110 $DATADIR/ref_cats/ps1_pv3_3pi_20170110

date
echo "processCcd"
# II. Calibrate a single frame with processCcd.py
# Use calibration files to do CCD processing
processCcd.py $DATADIR --rerun processCcdOutputs --id

# III. (omitted) Visualize images.

# IV. Make coadds
date
echo "make coadds"
# IV. A. Make skymap
# A sky map is a tiling of the celestial sphere. It is composed of one or more tracts.
# A tract is composed of one or more overlapping patches. Each tract has a WCS.
# We define a skymap so that we can warp all of the exposure to fit on a single coordinate system
# This is a necessary step for making coadds

date
echo "make skymap"
makeDiscreteSkyMap.py $DATADIR --id --rerun processCcdOutputs:coadd --config skyMap.projection="TAN"
# IV. B. Warp images onto skymap
date
echo "warp images"
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
echo "coadd warped images"
assembleCoadd.py $DATADIR --rerun coadd \
        --selectId filter=HSC-R \
        --id filter=HSC-R tract=0 patch=0,0^0,1^0,2^1,0^1,1^1,2^2,0^2,1^2,2

assembleCoadd.py $DATADIR --rerun coadd \
        --selectId filter=HSC-I \
        --id filter=HSC-I tract=0 patch=0,0^0,1^0,2^1,0^1,1^1,2^2,0^2,1^2,2

# V. Measuring sources
date
echo "measure sources"
# V. A. Source detection
# As noted above, we do source detection on the deepest image possible.
echo "detect sources"
detectCoaddSources.py $DATADIR --rerun coadd:coaddPhot \
        --id filter=HSC-R tract=0 patch=0,0^0,1^0,2^1,0^1,1^1,2^2,0^2,1^2,2

detectCoaddSources.py $DATADIR --rerun coaddPhot \
        --id filter=HSC-I tract=0 patch=0,0^0,1^0,2^1,0^1,1^1,2^2,0^2,1^2,2

# V. B. Merge multi-band detection catalogs
# Ultimately, for photometry, we will need to deblend objects. 
# In order to do this, we first merge the detected source catalogs.
date
echo "merge detection cats"
mergeCoaddDetections.py $DATADIR --rerun coaddPhot --id filter=HSC-R^HSC-I

# V. C. Measure source catalogs on coadds
# Given a full source catalog, we can do regular photometry with implicit deblending.
date
echo "measure source cats on coadds"
measureCoaddSources.py $DATADIR --rerun coaddPhot --id filter=HSC-R
measureCoaddSources.py $DATADIR --rerun coaddPhot --id filter=HSC-I

# V. D. Merge multi-band source catalogs from coadds
date
echo "merge source cats from coadds"
mergeCoaddMeasurements.py $DATADIR --rerun coaddPhot --id filter=HSC-R^HSC-I

# V. E. Run forced photometry on coadds
# Given a full source catalog, we can do forced photometry with implicit deblending.
date
echo "run forcedphot on coadds"
forcedPhotCoadd.py $DATADIR --rerun coaddPhot:coaddForcedPhot --id filter=HSC-R
forcedPhotCoadd.py $DATADIR --rerun coaddForcedPhot --id filter=HSC-I

# VI. Multi-band catalog analysis
# For analysis of the catalog, see part VI of StackClub/ImageProcessing/Re-RunHSC.ipynb
