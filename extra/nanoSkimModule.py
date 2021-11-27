from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

ROOT.gROOT.SetBatch(True)

class nanoSkimProducer(Module):
    def __init__(self):
        print("Loading NanoCORE shared libraries...")
        ROOT.gSystem.Load("NanoTools/NanoCORE/libNANO_CORE.so")
        header_files = ["ElectronSelections", "MuonSelections", "TauSelections", "Config"]
        for header_file in header_files:
            print("Loading NanoCORE {} header file...".format(header_file))
            ROOT.gROOT.ProcessLine(".L NanoTools/NanoCORE/{}.h".format(header_file))

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self._tchain = ROOT.TChain("Events")
        self._tchain.Add(inputFile.GetName())
        print(inputFile)
        if "UL16" in inputFile.GetName():
            ROOT.gconf.nanoAOD_ver = 8
        if "UL17" in inputFile.GetName():
            ROOT.gconf.nanoAOD_ver = 8
        if "UL18" in inputFile.GetName():
            ROOT.gconf.nanoAOD_ver = 8
        ROOT.nt.Init(self._tchain)
        ROOT.gconf.GetConfigs(ROOT.nt.year())
        print("year = {}".format(ROOT.nt.year()))
        print("WP_DeepFlav_loose = {}".format(ROOT.gconf.WP_DeepFlav_loose))
        print("WP_DeepFlav_medium = {}".format(ROOT.gconf.WP_DeepFlav_medium))
        print("WP_DeepFlav_tight = {}".format(ROOT.gconf.WP_DeepFlav_tight))
        pass

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        # print(event._entry)
        ROOT.nt.GetEntry(event._entry)
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        # taus = Collection(event, "Tau")
        # jets = Collection(event, "Jet")

        n_el = 0
        for i, lep in enumerate(electrons):
            if not (ROOT.nt.Electron_mvaFall17V2Iso_WP90()[i]): continue
            if not (lep.pt > 10): continue
            if not (abs(lep.eta) < 2.5): continue
            n_el += 1

        n_mu = 0
        for i, lep in enumerate(muons):
            if not (ROOT.nt.Muon_mediumId()[i]): continue
            if not (ROOT.nt.Muon_pfRelIso04_all()[i] < 0.25): continue
            if not (lep.pt > 10): continue
            if not (abs(lep.eta) < 2.4): continue
            n_mu += 1

        if n_el + n_mu == 4:
            return True
        else:
            return False

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

nanoSkimModuleConstr = lambda: nanoSkimProducer()
