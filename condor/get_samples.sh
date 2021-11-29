#!/bin/bash

usage()
{
    echo "Usage:"
    echo ""
    echo "   > $0 YEAR(=18, 17, 16, 16APV)"
    echo ""
    echo ""
    exit
}

if [ -z $1 ]; then
    usage
fi

YEAR=$1

samples="DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8 \
DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8 \
GluGluHToZZTo4L_M125 \
GluGluToContinToZZTo2e2mu_TuneCP5 \
GluGluToContinToZZTo2e2tau_TuneCP5 \
GluGluToContinToZZTo2mu2tau_TuneCP5 \
GluGluToContinToZZTo4e_TuneCP5 \
GluGluToContinToZZTo4mu_TuneCP5 \
GluGluToContinToZZTo4tau_TuneCP5 \
TWZToLL_thad_Wlept_5f_DR_TuneCP5 \
TWZToLL_tlept_Whad_5f_DR_TuneCP5 \
TWZToLL_tlept_Wlept_5f_DR_TuneCP5 \
TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8 \
TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8 \
TTWH_TuneCP5_13TeV-madgraph-pythia8 \
TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8 \
TTWW_TuneCP5_13TeV-madgraph-pythia8 \
TTWZ_TuneCP5_13TeV-madgraph-pythia8 \
TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8 \
TTZZ_TuneCP5_13TeV-madgraph-pythia8 \
VHToNonbb_M125_TuneCP5 \
WWW_4F_TuneCP5 \
WWZ_4F_TuneCP5 \
WZG_TuneCP5_13TeV-amcatnlo-pythia8 \
WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8 \
WZZ_TuneCP5 \
ZZTo4L_TuneCP5_13TeV_powheg_pythia8 \
ZZZ_TuneCP5 \
ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8 \
GluGluZH_HToWWTo2L2Nu_M125"

if [[ "${YEAR}" == *"18"* ]]; then
    ###########
    ## 2018
    ###########
    # dis_client.py /DoubleMuon
    # dis_client.py /EGamma
    # dis_client.py /MuonEG
    samples="EGamma \
    DoubleMuon \
    MuonEG \
    $samples"
    # HZJ_HToWWTo2L2Nu_ZTo2L_M125_13TeV_powheg_jhugen714_pythia8_TuneCP5 \
    # TTZH_TuneCP5_13TeV-madgraph-pythia8 \
    # TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8 \
elif [[ "${YEAR}" == *"17"* ]]; then
    ###########
    ## 2017
    ###########
    # dis_client.py /DoubleMuon
    # dis_client.py /EGamma
    # dis_client.py /MuonEG
    samples="DoubleEG \
    DoubleMuon \
    MuonEG \
    $samples"
fi

for sample in ${samples}; do
    sh find_sample.sh ${sample} ${YEAR}
done
