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

Get a sample NanoAOD to test on.

    mkdir -p mc/RunIISummer20UL18NanoAODv9/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/
    xrdcp root://cmsxrootd.fnal.gov//store/mc/RunIISummer20UL18NanoAODv9/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/7075899E-49EC-3B4F-BA70-877BC8E8C8CF.root mc/RunIISummer20UL18NanoAODv9/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/.

Test the package locally on the NanoAOD file just downloaded.

    sh test_package.sh package.tar.gz mc/RunIISummer20UL18NanoAODv9/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/7075899E-49EC-3B4F-BA70-877BC8E8C8CF.root

Copy the package.tar.gz to ```/nfs-7``` area

    cp package.tar.gz /nfs-7/userdata/phchang/NanoSkimmers/POGID4Lep10_v1_package.tar.gz

## Condor

First create a ```package.tar.gz```.  

Then go to ```condor/```

    cd condor

Then, setup the ```ProjectMetis```

    cd ProjectMetis
    source setup.sh
    cd ../

And run

    python runMetis.py POGID4Lep10 v1 # automatically picks up /nfs-7/userdata/phchang/NanoSkimmers/POGID4Lep10_v1_package.tar.gz as the package

NOTE: ```/nfs-7/userdata/phchang``` is hardcoded! so please change if you don't have your skimmer in philip's place. (Or ask him to put it in his place.)  

