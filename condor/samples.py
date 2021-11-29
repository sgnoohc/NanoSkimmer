#!/bin/env python

from metis.Sample import DBSSample, DirectorySample

samples_UL = [

        # 2018 Data
        DBSSample(dataset="/DoubleMuon/Run2018A-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2018B-UL2018_MiniAODv1_NanoAODv2-v2/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2018C-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2018A-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2018B-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2018C-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/EGamma/Run2018A-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/EGamma/Run2018B-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/EGamma/Run2018C-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/EGamma/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2018A-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2018B-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2018C-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        # DBSSample(dataset="/SingleMuon/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2018D-UL2018_MiniAODv1_NanoAODv2-v2/NANOAOD"), #

        # Data 2017 (NanoAODv7)
        DBSSample(dataset="/DoubleEG/Run2017B-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")       , #     filesizeGB: 54.04  , nfiles: 43  , nevents: 58088760  , nlumis: 26447
        DBSSample(dataset="/DoubleEG/Run2017C-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")       , #     filesizeGB: 61.81  , nfiles: 56  , nevents: 65181125  , nlumis: 59165
        DBSSample(dataset="/DoubleEG/Run2017D-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")       , #     filesizeGB: 24.69  , nfiles: 28  , nevents: 25911432  , nlumis: 27927
        DBSSample(dataset="/DoubleEG/Run2017E-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")       , #     filesizeGB: 57.43  , nfiles: 53  , nevents: 56241190  , nlumis: 45495
        DBSSample(dataset="/DoubleEG/Run2017F-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")       , #     filesizeGB: 77.78  , nfiles: 66  , nevents: 74344288  , nlumis: 60474
        DBSSample(dataset="/DoubleMuon/Run2017B-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")     , #     filesizeGB: 12.83  , nfiles: 15  , nevents: 14501767  , nlumis: 26734
        DBSSample(dataset="/DoubleMuon/Run2017C-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")     , #     filesizeGB: 46.53  , nfiles: 36  , nevents: 49636525  , nlumis: 57320
        DBSSample(dataset="/DoubleMuon/Run2017D-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")     , #     filesizeGB: 21.75  , nfiles: 23  , nevents: 23075733  , nlumis: 28105
        DBSSample(dataset="/DoubleMuon/Run2017E-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")     , #     filesizeGB: 52.02  , nfiles: 41  , nevents: 51589661  , nlumis: 44980
        DBSSample(dataset="/DoubleMuon/Run2017F-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")     , #     filesizeGB: 79.59  , nfiles: 55  , nevents: 79756560  , nlumis: 60685
        DBSSample(dataset="/MuonEG/Run2017B-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")         , #     filesizeGB: 4.81   , nfiles: 8   , nevents: 4453465   , nlumis: 26734
        DBSSample(dataset="/MuonEG/Run2017C-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")         , #     filesizeGB: 17.69  , nfiles: 21  , nevents: 15595214  , nlumis: 57320
        DBSSample(dataset="/MuonEG/Run2017D-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")         , #     filesizeGB: 10.34  , nfiles: 13  , nevents: 9164365   , nlumis: 28105
        DBSSample(dataset="/MuonEG/Run2017E-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")         , #     filesizeGB: 22.55  , nfiles: 20  , nevents: 19043421  , nlumis: 44980
        DBSSample(dataset="/MuonEG/Run2017F-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")         , #     filesizeGB: 31.04  , nfiles: 33  , nevents: 25776363  , nlumis: 60631
        DBSSample(dataset="/SingleElectron/Run2017B-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD") , #     filesizeGB: 49.17  , nfiles: 53  , nevents: 60537490  , nlumis: 26448
        DBSSample(dataset="/SingleElectron/Run2017C-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD") , #     filesizeGB: 119.06 , nfiles: 96  , nevents: 136637888 , nlumis: 59164
        DBSSample(dataset="/SingleElectron/Run2017D-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD") , #     filesizeGB: 44.23  , nfiles: 38  , nevents: 51526710  , nlumis: 27927
        DBSSample(dataset="/SingleElectron/Run2017E-UL2017_MiniAODv1_NanoAODv2-v2/NANOAOD") , #     filesizeGB: 94.05  , nfiles: 85  , nevents: 102117532 , nlumis: 45490
        DBSSample(dataset="/SingleElectron/Run2017F-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD") , #     filesizeGB: 120.92 , nfiles: 117 , nevents: 126793514 , nlumis: 59668
        DBSSample(dataset="/SingleMuon/Run2017B-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")     , #     filesizeGB: 102.64 , nfiles: 110 , nevents: 136300266 , nlumis: 26734
        DBSSample(dataset="/SingleMuon/Run2017C-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")     , #     filesizeGB: 130.59 , nfiles: 139 , nevents: 165652756 , nlumis: 57320
        DBSSample(dataset="/SingleMuon/Run2017D-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")     , #     filesizeGB: 55.42  , nfiles: 58  , nevents: 70361660  , nlumis: 28105
        DBSSample(dataset="/SingleMuon/Run2017E-UL2017_MiniAODv1_NanoAODv2-v2/NANOAOD")     , #     filesizeGB: 131.35 , nfiles: 135 , nevents: 154626280 , nlumis: 44971
        DBSSample(dataset="/SingleMuon/Run2017F-UL2017_MiniAODv1_NanoAODv2-v2/NANOAOD")     , #     filesizeGB: 211.48 , nfiles: 174 , nevents: 242140980 , nlumis: 60685

        # Data 2016 (NanoAODv7)
        DBSSample(dataset="/DoubleEG/Run2016B-02Apr2020_ver1-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016B-02Apr2020_ver2-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016G-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016H-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016B-02Apr2020_ver1-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016B-02Apr2020_ver2-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016G-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016H-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016B-02Apr2020_ver1-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016B-02Apr2020_ver2-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016E-02Apr2020-v2/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016E-02Apr2020_17Jul2018-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016G-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016H-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016B-02Apr2020_ver1-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016B-02Apr2020_ver2-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016G-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016H-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016B-02Apr2020_ver1-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016B-02Apr2020_ver2-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016G-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016H-02Apr2020-v1/NANOAOD"), #

        # 2018 MC
        # Top backgrounds
        # # ttbar
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                                  , # filesizeGB :  1055.12 , nfiles :  465 , nevents :  486770000 , nlumis :  486770
        DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                                         , # filesizeGB :  313.34  , nfiles :  181 , nevents :  148470000 , nlumis :  148470
        # single top                                                                                                                                                                                                                                       
        DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")            , # filesizeGB :  23.47   , nfiles :  10  , nevents :  11695231  , nlumis :  11328
        DBSSample(dataset="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                , # filesizeGB :  23.11   , nfiles :  10  , nevents :  11518444  , nlumis :  111656
        DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                    , # filesizeGB :  32.34   , nfiles :  69  , nevents :  19957999  , nlumis :  19958
        DBSSample(dataset="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")   , # filesizeGB :  40.01   , nfiles :  30  , nevents :  23421300  , nlumis :  234213
        DBSSample(dataset="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")       , # filesizeGB :  81.19   , nfiles :  37  , nevents :  47707100  , nlumis :  477071
        # ttW                                                                                                                                                                                                                                              
        DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                        , # filesizeGB :  28.45   , nfiles :  12  , nevents :  10522657  , nlumis :  9995
        # ttZ                                                                                                                                                                                                                                              
        DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                                , # filesizeGB :  51.28   , nfiles :  18  , nevents :  19992000  , nlumis :  19992
        # Boson backgrounds                                                                                                                                                                                                                                
        # DY                                                                                                                                                                                                                                               
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                          , # filesizeGB :  84.93   , nfiles :  46  , nevents :  99449093  , nlumis :  99427
        DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                              , # filesizeGB :  120.19  , nfiles :  53  , nevents :  98433266  , nlumis :  93924
        # W                                                                                                                                                                                                                                                
        DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                                   , # filesizeGB :  85.55   , nfiles :  45  , nevents :  83009353  , nlumis :  75385
        # ssWW                                                                                                                                                                                                                                             
        DBSSample(dataset="/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                                            , # filesizeGB :  2.09    , nfiles :  19  , nevents :  998000    , nlumis :  998
        # WW                                                                                                                                                                                                                                               
        DBSSample(dataset="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                                                       , # filesizeGB :  19.17   , nfiles :  21  , nevents :  15670000  , nlumis :  15670
        # WZ                                                                                                                                                                                                                                               
        DBSSample(dataset="/WZTo3LNu_mllmin01_NNPDF31_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                         , # filesizeGB :  128.13  , nfiles :  54  , nevents :  89670000  , nlumis :  89670
        # ZZ                                                                                                                                                                                                                                               
        DBSSample(dataset="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                                            , # filesizeGB :  138.39  , nfiles :  65  , nevents :  99218000  , nlumis :  99218
        # Higgs samples                                                                                                                                                                                                                                    
        DBSSample(dataset="/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                  , # filesizeGB :  29.33   , nfiles :  16  , nevents :  10002677  , nlumis :  9257
        DBSSample(dataset="/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                     , # filesizeGB :  29.23   , nfiles :  11  , nevents :  9909517   , nlumis :  9391
        # Rare multi-X backgrounds                                                                                                                                                                                                                         
        DBSSample(dataset="/TWZToLL_thad_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                        , # filesizeGB :  8       , nfiles :  21  , nevents :  2984000   , nlumis :  2984
        DBSSample(dataset="/TWZToLL_tlept_Whad_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                        , # filesizeGB :  7.2     , nfiles :  21  , nevents :  2690000   , nlumis :  2690
        DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                                            , # filesizeGB :  3.04    , nfiles :  19  , nevents :  1000000   , nlumis :  1000
        DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                                            , # filesizeGB :  1.47    , nfiles :  4   , nevents :  500000    , nlumis :  500

        # Not used yet
        # DBSSample(dataset="/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 200000
        # DBSSample(dataset="/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 200000
        # DBSSample(dataset="/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 200000
        # DBSSample(dataset="/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext2-v1/NANOAODSIM"), # 9592768

        # 2017 MC
        # Top backgrounds
        # # ttbar
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                                , # filesizeGB : 790.81 , nfiles : 305 , nevents : 355826000 , nlumis : 355826
        DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                                       , # filesizeGB : 231.16 , nfiles : 85  , nevents : 106978000 , nlumis : 106978
        # single top
        DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")          , # filesizeGB : 16.96  , nfiles : 16  , nevents : 8238224   , nlumis : 7982
        DBSSample(dataset="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")              , # filesizeGB : 17.47  , nfiles : 9   , nevents : 8498506   , nlumis : 8233
        DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                  , # filesizeGB : 23.52  , nfiles : 51  , nevents : 14162000  , nlumis : 14162
        DBSSample(dataset="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM") , # filesizeGB : 42.45  , nfiles : 20  , nevents : 24265600  , nlumis : 242656
        DBSSample(dataset="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")     , # filesizeGB : 79.87  , nfiles : 62  , nevents : 45754100  , nlumis : 457541
        # ttW
        DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                      , # filesizeGB : 20.58  , nfiles : 9   , nevents : 7464889   , nlumis : 7089
        # ttZ
        DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                              , # filesizeGB : 37.16  , nfiles : 14  , nevents : 14196000  , nlumis : 14196
        # Boson backgrounds
        # DY
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                        , # filesizeGB : 59.79  , nfiles : 31  , nevents : 68072143  , nlumis : 68472
        DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                            , # filesizeGB : 128.43 , nfiles : 72  , nevents : 102486448 , nlumis : 976795
        # W
        DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                                 , # filesizeGB : 86.02  , nfiles : 42  , nevents : 81254459  , nlumis : 73794
        # ssWW
        DBSSample(dataset="/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                                          , # filesizeGB : 2.09   , nfiles : 1   , nevents : 1000000   , nlumis : 10000
        # WW
        DBSSample(dataset="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                                                     , # filesizeGB : 20.08  , nfiles : 30  , nevents : 15883000  , nlumis : 15883
        # WZ
        DBSSample(dataset="/WZTo3LNu_mllmin01_NNPDF31_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                       , # filesizeGB : 92.27  , nfiles : 50  , nevents : 62930000  , nlumis : 62930
        # ZZ
        DBSSample(dataset="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                                                     , # filesizeGB : 3.44   , nfiles : 3   , nevents : 2708000   , nlumis : 2708
        # Higgs samples
        DBSSample(dataset="/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                , # filesizeGB : 29.3   , nfiles : 31  , nevents : 9804430   , nlumis : 9074
        DBSSample(dataset="/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                   , # filesizeGB : 29.68  , nfiles : 13  , nevents : 9897140   , nlumis : 9379
        # Rare multi-X backgrounds
        DBSSample(dataset="/TWZToLL_thad_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                      , # filesizeGB : 5.69   , nfiles : 6   , nevents : 2090000   , nlumis : 2090
        DBSSample(dataset="/TWZToLL_tlept_Whad_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                      , # filesizeGB : 5.69   , nfiles : 32  , nevents : 2066000   , nlumis : 2066
        DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                                          , # filesizeGB : 2.15   , nfiles : 10  , nevents : 701000    , nlumis : 701
        DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                                          , # filesizeGB : 1.08   , nfiles : 5   , nevents : 358000    , nlumis : 358

        # # 2016 NanoAODv7
        # DBSSample(dataset="/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1/NANOAODSIM"),
        # DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        # DBSSample(dataset="/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1/NANOAODSIM"),
        # DBSSample(dataset="/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"), # 67860400
        # DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"), # 107604800
        # DBSSample(dataset="/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/WpWpJJ_EWK-QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/ZZTo4L_13TeV_powheg_pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/ST_tWll_5f_LO_13TeV-MadGraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        # DBSSample(dataset="/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        # DBSSample(dataset="/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        # DBSSample(dataset="/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        # DBSSample(dataset="/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        # DBSSample(dataset="/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/WWToLNuQQ_13TeV-powheg/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        # DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v2/NANOAODSIM"),
        # DBSSample(dataset="/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        # DBSSample(dataset="/WWTo2L2Nu_13TeV-powheg/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),

        # for i in $(grep 16NanoAODv2 samples.py | grep -v "hadoop" | tr '"' ' ' | col 2); do echo $i $(dis_client.py "$i" | tr '\n' ' ');  done
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),                                  # /TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM                                filesizeGB: 335.21 nfiles: 266 nevents: 158594000 nlumis: 158594
        DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),                                         # /TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM                                       filesizeGB: 99.09 nfiles: 102 nevents: 48232000 nlumis: 48232
        DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),            # /ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM          filesizeGB: 7.48 nfiles: 23 nevents: 3800996 nlumis: 3682
        DBSSample(dataset="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),                # /ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM              filesizeGB: 6.57 nfiles: 4 nevents: 3361253 nlumis: 3257
        DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),                    # /ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM                  filesizeGB: 9.78 nfiles: 26 nevents: 6275000 nlumis: 6275
        DBSSample(dataset="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),   # /ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM filesizeGB: 50.27 nfiles: 31 nevents: 30463000 nlumis: 30463
        DBSSample(dataset="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),       # /ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM     filesizeGB: 103.45 nfiles: 81 nevents: 62824000 nlumis: 62824
        DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),                        # /TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM                      filesizeGB: 8.9 nfiles: 11 nevents: 3368017 nlumis: 3200
        DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),                                # /TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM                              filesizeGB: 15.62 nfiles: 40 nevents: 6211000 nlumis: 6211
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),                          # /DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM                        filesizeGB: 20.76 nfiles: 34 nevents: 26927726 nlumis: 26361
        DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),                              # /DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM                            filesizeGB: 119.63 nfiles: 69 nevents: 104072004 nlumis: 98480
        DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),                                   # /WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM                                 filesizeGB: 84.66 nfiles: 62 nevents: 88463979 nlumis: 79576
        DBSSample(dataset="/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),                                            # /SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM                                          filesizeGB: 1.99 nfiles: 27 nevents: 960000 nlumis: 960
        DBSSample(dataset="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),                                                       # /WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM                                                     filesizeGB: 18.6 nfiles: 36 nevents: 15907000 nlumis: 15907
        DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),                                    # /WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM                                  filesizeGB: 15.02 nfiles: 6 nevents: 10532228 nlumis: 101595
        DBSSample(dataset="/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),                                   # /ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM                                 filesizeGB: 19.72 nfiles: 18 nevents: 18128956 nlumis: 23729
        DBSSample(dataset="/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),                  # /ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM                filesizeGB: 15.19 nfiles: 11 nevents: 5307830 nlumis: 4913
        DBSSample(dataset="/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),                     # /ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM                   filesizeGB: 15.06 nfiles: 8 nevents: 5237891 nlumis: 4963
        DBSSample(dataset="/TWZToLL_thad_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),                        # /TWZToLL_thad_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM                      filesizeGB: 2.61 nfiles: 12 nevents: 993000 nlumis: 993
        DBSSample(dataset="/TWZToLL_tlept_Whad_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),                        # /TWZToLL_tlept_Whad_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM                      filesizeGB: 2.6 nfiles: 10 nevents: 994000 nlumis: 994
        DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),                                            # /TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM                                          filesizeGB: 0.97 nfiles: 14 nevents: 320000 nlumis: 320
        DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"),                                            # /TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM                                          filesizeGB: 0.46 nfiles: 4 nevents: 159000 nlumis: 159

        # for i in $(grep 16NanoAODv2 samples.py | grep -v "hadoop" | tr '"' ' ' | col 2); do echo $i $(dis_client.py "$i" | tr '\n' ' ');  done
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"),                                                                             # /TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM                                filesizeGB: 291.21 nfiles: 236 nevents: 138169000 nlumis: 138169
        DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"),                                                                                    # /TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM                                       filesizeGB: 84.76 nfiles: 102 nevents: 41364000 nlumis: 41364
        DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"),                                                       # /ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM          filesizeGB: 6.66 nfiles: 11 nevents: 3411747 nlumis: 3306
        DBSSample(dataset="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v2/NANOAODSIM"),                                                           # /ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v2/NANOAODSIM              filesizeGB: 6.48 nfiles: 25 nevents: 3294673 nlumis: 3192
        DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"),                                                               # /ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM                  filesizeGB: 8.81 nfiles: 27 nevents: 5665000 nlumis: 5665
        DBSSample(dataset="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer19UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"), # This one is not 20UL16NanoAODAPVv2!        # /ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer19UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM filesizeGB: 38.13 nfiles: 72 nevents: 23036400 nlumis: 230364
        DBSSample(dataset="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"),                                                  # /ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM     filesizeGB: 91.77 nfiles: 43 nevents: 55961000 nlumis: 55961
        DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"),                                                                   # /TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM                      filesizeGB: 7.56 nfiles: 6 nevents: 2873397 nlumis: 2731
        DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"),                                                                           # /TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM                              filesizeGB: 14.47 nfiles: 33 nevents: 5776000 nlumis: 5776
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"),                                                                     # /DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM                        filesizeGB: 24.75 nfiles: 16 nevents: 32305345 nlumis: 32046
        DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"),                                                                         # /DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM                            filesizeGB: 111.18 nfiles: 51 nevents: 96862861 nlumis: 92434
        DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"),                                                                             # /WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM                                filesizeGB: 29.89 nfiles: 43 nevents: 28785032 nlumis: 29328
        DBSSample(dataset="/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"),                                                                                       # /SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM                                          filesizeGB: 1.99 nfiles: 3 nevents: 1000000 nlumis: 1000
        DBSSample(dataset="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"),                                                                                                  # /WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM                                                     filesizeGB: 18.5 nfiles: 18 nevents: 15919000 nlumis: 15919
        DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"),                                                                               # /WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM                                  filesizeGB: 13.73 nfiles: 9 nevents: 9650030 nlumis: 9280
        DBSSample(dataset="/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"),                                                                              # /ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM                                 filesizeGB: 21.44 nfiles: 70 nevents: 19640450 nlumis: 42238
        DBSSample(dataset="/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"),                                                             # /ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM                filesizeGB: 13.76 nfiles: 7 nevents: 4824845 nlumis: 4463
        DBSSample(dataset="/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"),                                                                # /ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM                   filesizeGB: 14.63 nfiles: 21 nevents: 5087191 nlumis: 4823
        DBSSample(dataset="/TWZToLL_thad_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"),                                                                   # /TWZToLL_thad_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM                      filesizeGB: 2.32 nfiles: 12 nevents: 885000 nlumis: 885
        DBSSample(dataset="/TWZToLL_tlept_Whad_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"),                                                                   # /TWZToLL_tlept_Whad_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM                      filesizeGB: 2.31 nfiles: 19 nevents: 873000 nlumis: 873
        DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"),                                                                                       # /TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM                                          filesizeGB: 0.88 nfiles: 16 nevents: 288000 nlumis: 288
        DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"),                                                                                       # /TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM                                          filesizeGB: 0.4 nfiles: 2 nevents: 140000 nlumis: 140

        ]

samples_UL = [
        #2018
        DBSSample(dataset="/EGamma/Run2018A-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 341.3,nfiles: 226,nevents: 339013231,nlumis: 60824,
        DBSSample(dataset="/EGamma/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 155.3,nfiles: 74,nevents: 153792795,nlumis: 29576,
        DBSSample(dataset="/EGamma/Run2018D-UL2018_MiniAODv2_NanoAODv9-v3/NANOAOD"), # filesizeGB: 775.55,nfiles: 355,nevents: 752524583,nlumis: 134305,
        DBSSample(dataset="/EGamma/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 154.83,nfiles: 83,nevents: 147827904,nlumis: 27563,
        DBSSample(dataset="/DoubleMuon/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 35.45,nfiles: 25,nevents: 34565869,nlumis: 27721,
        DBSSample(dataset="/DoubleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 35.36,nfiles: 20,nevents: 35057758,nlumis: 29913,
        DBSSample(dataset="/DoubleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 77.89,nfiles: 54,nevents: 75491789,nlumis: 61127,
        DBSSample(dataset="/DoubleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD"), # filesizeGB: 166.62,nfiles: 107,nevents: 168600679,nlumis: 136952,
        DBSSample(dataset="/MuonEG/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 19.62,nfiles: 20,nevents: 16211567,nlumis: 29912,
        DBSSample(dataset="/MuonEG/Run2018A-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 39.96,nfiles: 33,nevents: 32958503,nlumis: 61133,
        DBSSample(dataset="/MuonEG/Run2018D-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 87.49,nfiles: 63,nevents: 71952025,nlumis: 136955,
        DBSSample(dataset="/MuonEG/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 19.45,nfiles: 22,nevents: 15652198,nlumis: 27721,
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"), # filesizeGB: 81.59,nfiles: 84,nevents: 94452816,nlumis: 94431,
        DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v1/NANOAODSIM"), # filesizeGB: 124.78,nfiles: 118,nevents: 101415750,nlumis: 96790,
        DBSSample(dataset="/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"), # filesizeGB: 1.69,nfiles: 24,nevents: 940000,nlumis: 940,
        DBSSample(dataset="/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"), # filesizeGB: 0.98,nfiles: 17,nevents: 500000,nlumis: 500,
        DBSSample(dataset="/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"), # filesizeGB: 0.91,nfiles: 6,nevents: 500000,nlumis: 500,
        DBSSample(dataset="/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"), # filesizeGB: 0.84,nfiles: 16,nevents: 496000,nlumis: 496,
        DBSSample(dataset="/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"), # filesizeGB: 2.01,nfiles: 28,nevents: 974000,nlumis: 974,
        DBSSample(dataset="/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"), # filesizeGB: 1.43,nfiles: 34,nevents: 845232,nlumis: 1274,
        DBSSample(dataset="/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"), # filesizeGB: 0.78,nfiles: 10,nevents: 493998,nlumis: 494,
        DBSSample(dataset="/TWZToLL_thad_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"), # filesizeGB: 8.12,nfiles: 32,nevents: 2976000,nlumis: 2976,
        DBSSample(dataset="/TWZToLL_tlept_Whad_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"), # filesizeGB: 7.28,nfiles: 16,nevents: 2690000,nlumis: 2690,
        DBSSample(dataset="/TWZToLL_tlept_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"), # filesizeGB: 2.65,nfiles: 10,nevents: 1000000,nlumis: 1000,
        DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"), # filesizeGB: 309.02,nfiles: 155,nevents: 145020000,nlumis: 145020,
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"), # filesizeGB: 1030.79,nfiles: 391,nevents: 476408000,nlumis: 476408,
        DBSSample(dataset="/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"), # filesizeGB: 1.54,nfiles: 4,nevents: 497000,nlumis: 497,
        DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"), # filesizeGB: 28.34,nfiles: 13,nevents: 10450000,nlumis: 9926,
        DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"), # filesizeGB: 2.81,nfiles: 3,nevents: 944000,nlumis: 944,
        DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"), # filesizeGB: 1.46,nfiles: 2,nevents: 498000,nlumis: 498,
        DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"), # filesizeGB: 50.37,nfiles: 21,nevents: 19608000,nlumis: 19608,
        DBSSample(dataset="/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"), # filesizeGB: 1.5,nfiles: 8,nevents: 498000,nlumis: 498,
        DBSSample(dataset="/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"), # filesizeGB: 2.17,nfiles: 13,nevents: 1208288,nlumis: 1094,
        DBSSample(dataset="/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM"), # filesizeGB: 19.1,nfiles: 35,nevents: 9894000,nlumis: 9894,
        DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM"), # filesizeGB: 20.4,nfiles: 37,nevents: 9961999,nlumis: 9962,
        DBSSample(dataset="/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"), # filesizeGB: 3.76,nfiles: 5,nevents: 2000000,nlumis: 2000,
        DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"), # filesizeGB: 14.94,nfiles: 18,nevents: 9821283,nlumis: 9445,
        DBSSample(dataset="/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM"), # filesizeGB: 20.59,nfiles: 20,nevents: 9994000,nlumis: 9994,
        DBSSample(dataset="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"), # filesizeGB: 140.16,nfiles: 144,nevents: 98488000,nlumis: 98488,
        DBSSample(dataset="/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM"), # filesizeGB: 18.55,nfiles: 60,nevents: 9889000,nlumis: 9889,
        DBSSample(dataset="/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"), # filesizeGB: 20.99,nfiles: 48,nevents: 7328993,nlumis: 7329,
        DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_M125_13TeV_powheg_pythia8_TuneCP5_PSweights/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"), # filesizeGB: 3.95,nfiles: 5,nevents: 1955168,nlumis: 4537,

        # 2017
        DBSSample(dataset="/DoubleEG/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 63.79,nfiles: 44,nevents: 65181125,nlumis: 59165,
        DBSSample(dataset="/DoubleEG/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 54.43,nfiles: 29,nevents: 58088760,nlumis: 26447,
        DBSSample(dataset="/DoubleEG/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 25.52,nfiles: 14,nevents: 25911432,nlumis: 27927,
        DBSSample(dataset="/DoubleEG/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 59.18,nfiles: 32,nevents: 56241190,nlumis: 45495,
        DBSSample(dataset="/DoubleEG/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 80.81,nfiles: 54,nevents: 74265012,nlumis: 60418,
        DBSSample(dataset="/DoubleMuon/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 12.67,nfiles: 8,nevents: 14501767,nlumis: 26734,
        DBSSample(dataset="/DoubleMuon/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 22.21,nfiles: 16,nevents: 23075733,nlumis: 28105,
        DBSSample(dataset="/DoubleMuon/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 47.48,nfiles: 29,nevents: 49636525,nlumis: 57320,
        DBSSample(dataset="/DoubleMuon/Run2017H-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 6.73,nfiles: 7,nevents: 16142576,nlumis: 12675,
        DBSSample(dataset="/DoubleMuon/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 82.39,nfiles: 60,nevents: 79756560,nlumis: 60685,
        DBSSample(dataset="/DoubleMuon/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 53.21,nfiles: 34,nevents: 51531477,nlumis: 44913,
        DBSSample(dataset="/DoubleMuon/Run2017G-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 215.4,nfiles: 157,nevents: 892686175,nlumis: 27477,
        DBSSample(dataset="/MuonEG/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 23.42,nfiles: 15,nevents: 19043421,nlumis: 44980,
        DBSSample(dataset="/MuonEG/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 18.35,nfiles: 17,nevents: 15595214,nlumis: 57320,
        DBSSample(dataset="/MuonEG/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 4.87,nfiles: 6,nevents: 4453465,nlumis: 26734,
        DBSSample(dataset="/MuonEG/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 32.47,nfiles: 23,nevents: 25776363,nlumis: 60631,
        DBSSample(dataset="/MuonEG/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"), # filesizeGB: 10.76,nfiles: 13,nevents: 9164365,nlumis: 28105,
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"), # filesizeGB: 60.46,nfiles: 77,nevents: 68480179,nlumis: 68883,
        DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"), # filesizeGB: 129.12,nfiles: 75,nevents: 102863931,nlumis: 980390,
        DBSSample(dataset="/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"), # filesizeGB: 1.79,nfiles: 14,nevents: 998000,nlumis: 998,
        DBSSample(dataset="/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"), # filesizeGB: 1.02,nfiles: 22,nevents: 500000,nlumis: 500,
        DBSSample(dataset="/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"), # filesizeGB: 0.97,nfiles: 20,nevents: 498000,nlumis: 498,
        DBSSample(dataset="/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"), # filesizeGB: 0.87,nfiles: 20,nevents: 500000,nlumis: 500,
        DBSSample(dataset="/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"), # filesizeGB: 2.1,nfiles: 26,nevents: 997000,nlumis: 997,
        DBSSample(dataset="/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"), # filesizeGB: 1.65,nfiles: 31,nevents: 975090,nlumis: 1336,
        DBSSample(dataset="/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"), # filesizeGB: 0.83,nfiles: 19,nevents: 499000,nlumis: 499,
        DBSSample(dataset="/TWZToLL_thad_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"), # filesizeGB: 5.76,nfiles: 6,nevents: 2092000,nlumis: 2092,
        DBSSample(dataset="/TWZToLL_tlept_Whad_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"), # filesizeGB: 5.66,nfiles: 3,nevents: 2066000,nlumis: 2066,
        DBSSample(dataset="/TWZToLL_tlept_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"), # filesizeGB: 1.9,nfiles: 5,nevents: 708000,nlumis: 708,
        DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"), # filesizeGB: 232.43,nfiles: 99,nevents: 106724000,nlumis: 106724,
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"), # filesizeGB: 766.34,nfiles: 297,nevents: 346052000,nlumis: 346052,
        DBSSample(dataset="/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"), # filesizeGB: 1.15,nfiles: 11,nevents: 360000,nlumis: 360,
        DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"), # filesizeGB: 19.71,nfiles: 9,nevents: 7140411,nlumis: 6781,
        DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"), # filesizeGB: 2.13,nfiles: 9,nevents: 698000,nlumis: 698,
        DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"), # filesizeGB: 1.04,nfiles: 2,nevents: 350000,nlumis: 350,
        DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"), # filesizeGB: 36.75,nfiles: 19,nevents: 14036000,nlumis: 14036,
        DBSSample(dataset="/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"), # filesizeGB: 1.01,nfiles: 9,nevents: 327000,nlumis: 327,
        DBSSample(dataset="/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"), # filesizeGB: 1.61,nfiles: 12,nevents: 869559,nlumis: 786,
        DBSSample(dataset="/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM"), # filesizeGB: 19.53,nfiles: 43,nevents: 9854000,nlumis: 9854,
        DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"), # filesizeGB: 0.39,nfiles: 5,nevents: 178000,nlumis: 178,
        DBSSample(dataset="/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"), # filesizeGB: 2.7,nfiles: 2,nevents: 1400000,nlumis: 1400,
        DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"), # filesizeGB: 16.13,nfiles: 31,nevents: 10339582,nlumis: 9943,
        DBSSample(dataset="/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM"), # filesizeGB: 20.88,nfiles: 23,nevents: 9898000,nlumis: 9898,
        DBSSample(dataset="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"), # filesizeGB: 144.13,nfiles: 109,nevents: 99388000,nlumis: 99388,
        DBSSample(dataset="/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM"), # filesizeGB: 18.23,nfiles: 31,nevents: 9524000,nlumis: 9524,
        DBSSample(dataset="/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"), # filesizeGB: 14.76,nfiles: 35,nevents: 5070989,nlumis: 5071,
        DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_M125_13TeV_powheg_pythia8_TuneCP5_PSweights/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"), # filesizeGB: 2.01,nfiles: 6,nevents: 971564,nlumis: 1880,
        ]

samples = samples_UL
