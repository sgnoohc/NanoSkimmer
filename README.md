# Overview

This creates a NanoSkimmer based on ```nanoAOD-tools```.  

First, update the NanoTools to have some higher max values following the below section.  

## VBSHWWNanoSkimmer

Then, we need to create a ```package.tar.gz``` for the condor jobs.  
The selections are defined in ```extra/vbsHwwSkimModule.py```.  
Also ```extra/keep_and_drop.txt``` contains the list of branches to keep or drop.  
Modify the files to your liking.  

Then, to create a ```package.tar.gz``` for the condor jobs

    sh create_package.sh # This creates a package.tar.gz

To test the package locally on some NanoAOD file

    sh test_package.sh package.tar.gz /hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWH_C2V_4p5_RunIIAutumn18NanoAOD_VBSWWH_C2V_4p5_v3_ext1/merged/output.root

Copy the package.tar.gz to ```/nfs-7``` area

    cp package.tar.gz /nfs-7/userdata/phchang/VBSHWWNanoSkimmer_v41_CMSSW_10_2_13_slc7_amd64_gcc700.package.tar.gz

## Condor

First create a ```package.tar.gz```.  

Then go to ```condor/```

    cd condor

Then, setup the ```ProjectMetis```

    cd ProjectMetis
    source setup.sh
    cd ../

And run

    python runMetis.py v41 # automatically picks up /nfs-7/userdata/phchang/VBSHWWNanoSkimmer_v41_CMSSW_10_2_13_slc7_amd64_gcc700.package.tar.gz as the package

NOTE: ```/nfs-7/userdata/phchang``` is hardcoded! so please change if you don't have your skimmer in philip's place. (Or ask him to put it in his place.)  
Or, if needed, in ```runMetis.py```, point to the desired ```package.tar.gz``` by modifying ```tarfile``` variable, and give a new ```tag```.

