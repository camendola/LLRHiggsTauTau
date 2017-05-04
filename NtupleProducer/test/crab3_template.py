# TEMPLATE used for automatic script submission of multiple datasets

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'GluGluToRadionToHHTo2B2Tau_M-750'
config.General.workArea = 'DefaultCrab3Area'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'analyzer.py' # to produce LLR ntuples or EnrichedMiniAOD according to the RunNtuplizer bool
config.JobType.sendExternalFolder = True #Needed until the PR including the Spring16 ele MVA ID is integrated in CMSSW/cms-data.

config.section_("Data")
config.Data.inputDataset = '/GluGluToRadionToHHTo2B2Tau_M-750_narrow_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 10000 #number of events per jobs # 18K FOR SINGLE ELE, 10k for others
config.Data.totalUnits = -1 #number of event
config.Data.outLFNDirBase = '/store/user/camendol/HHNtuples/GluGluToRadionToHHTo2B2Tau_M-750'
config.Data.publication = True
config.Data.outputDatasetTag = 'GluGluToRadionToHHTo2B2Tau_M-750'

config.section_("Site")
config.Site.storageSite = 'T2_FR_GRIF_LLR'

