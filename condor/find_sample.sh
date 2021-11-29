#!/bin/bash

usage()
{
    echo "Usage:"
    echo ""
    echo "   > $0 SAMPLENAME(=ZZTo4L, WWZ_4F_TuneCP5, EGamma, etc.) YEAR(=18, 17, 16, 16APV)"
    echo ""
    echo "   NOTE: For MC  : the matching is done via /SAMPLENAME*/...../"
    echo "         For Data: the matching is done via /SAMPLENAME/...../ (N.B. no wild card)"
    echo ""
    exit
}

SAMPLENAME=$1
YEAR=$2

if [ -z $1 ]; then usage; fi
if [ -z $2 ]; then usage; fi

isdata=false
if [[ "${SAMPLENAME}" == *"EGamma"* ]]; then isdata=true; fi
if [[ "${SAMPLENAME}" == *"MuonEG"* ]]; then isdata=true; fi
if [[ "${SAMPLENAME}" == *"DoubleMuon"* ]]; then isdata=true; fi
if [[ "${SAMPLENAME}" == *"SingleElectron"* ]]; then isdata=true; fi
if [[ "${SAMPLENAME}" == *"SingleMuon"* ]]; then isdata=true; fi

TAGS18="UL18NanoAODv9"
TAGS17="UL17NanoAODv9"
TAGS16="UL16NanoAODv9"
TAGS16APV="UL16NanoAODAPVv9"
EXCLUDKEYS="JMENano"

DATATAGS18="UL2018_MiniAODv2_NanoAODv9"
DATATAGS17="UL2017_MiniAODv2_NanoAODv9"
DATATAGS16="UL2016_MiniAODv2_NanoAODv9"
DATATAGS16APV="UL2016_MiniAODv2_NanoAODv9"
EXCLUDKEYS="JMENano"

TAG=""
if $isdata; then
    if [[ "${YEAR}" == *"18"* ]]; then TAG=${DATATAGS18}; fi
    if [[ "${YEAR}" == *"17"* ]]; then TAG=${DATATAGS17}; fi
    if [[ "${YEAR}" == *"16"* ]]; then TAG=${DATATAGS16}; fi
    if [[ "${YEAR}" == *"16APV"* ]]; then TAG=${DATATAGS16APV}; fi
else
    if [[ "${YEAR}" == *"18"* ]]; then TAG=${TAGS18}; fi
    if [[ "${YEAR}" == *"17"* ]]; then TAG=${TAGS17}; fi
    if [[ "${YEAR}" == *"16"* ]]; then TAG=${TAGS16}; fi
    if [[ "${YEAR}" == *"16APV"* ]]; then TAG=${TAGS16APV}; fi
fi

DATATYPE=""
if $isdata; then
    DATATYPE=NANOAOD;
else
    DATATYPE=NANOAODSIM;
fi

if $isdata; then
    ##
    ## Data then exact dataset name match
    ##
    results=$(dis_client.py /${SAMPLENAME}/*${TAG}*/${DATATYPE} | grep -v "${EXCLUDKEYS}")
else
    ##
    ## MC then wildcards are used
    ##
    results=$(dis_client.py /${SAMPLENAME}*/*${TAG}*/${DATATYPE} | grep -v "${EXCLUDKEYS}")
fi
nresults=$(echo ${results} | awk NF | tr ' ' '\n' | wc -l)

if $isdata; then

    ##
    ## Data
    ##

    for thesample in $results; do
        sampleinfo=$(dis_client.py ${thesample} | awk NF | tr '\n' ',')
        echo "DBSSample(dataset=\"${thesample}\")," \# ${sampleinfo}
    done

else

    ##
    ## MC
    ##

    # Select `thesample` if there are nresults != 1 samples matched
    thesample=""
    if [ ${nresults} -gt 1 ]; then
        # echo "found more than 1"
        sample_with_max_nevents=""
        max_nevts=0
        for res in ${results}; do
            nevts=$(dis_client.py ${res} | grep "nevents" | awk '{print $2}')
            if [ ${max_nevts} -lt ${nevts} ]; then
                max_nevts=${nevts}
                sample_with_max_nevents=${res}
            fi
        done
        thesample=${sample_with_max_nevents}
    elif [ ${nresults} -lt 1 ]; then
        echo "found zero for ${SAMPLENAME}"
        thesample=""
    else
        thesample=${results}
    fi
    
    if [ -n "${thesample}" ]; then
        sampleinfo=$(dis_client.py ${thesample} | awk NF | tr '\n' ',')
        echo "DBSSample(dataset=\"${thesample}\")," \# ${sampleinfo}
    fi

fi
