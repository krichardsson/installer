#!/usr/bin/python

host = 'host'
deployableArtfacts = 'deployableArtfacts'
environment = 'environment'
serverType = 'serverType'
installer = 'installer'
deployer = 'deployer'
logicalPartition = 'logicalPartition'
restarter = 'restarter'

ar_mts = 'MTS'
ar_fakexp = 'FakeXPH'
ar_mts_spec = 'MTS-spec'
ar_PML_backend = "PML-backend"
ar_webcounseling_app = "Webcounseling-App"

env_dev = 'dev'
env_sys = 'sys'
env_int = 'int'


host_dev_mts = 'dev_mts.maxm.se'
host_dev_linda = 'utvzon02.maxm.se'

host_sys_mts = 'sys_mts.maxm.se'
host_sys_linda = 'utvzon03.maxm.se'
host_sys_be = 'utvzon03.maxm.se'

host_int_mts = 'int_mts.maxm.se'
host_int_be_1 = 'lindaappserver1.maxm.se'
host_int_be_2 = 'lindaappserver2.maxm.se'
host_int_fe_1 = 'lindaappserver3.maxm.se'
host_int_fe_2 = 'lindaappserver4.maxm.se'

host_stage_mts = 'stage_mts.maxm.se'
host_stage_be_1 = 'lindaappserver5.maxm.se'
host_stage_be_2 = 'lindaappserver6.maxm.se'
host_stage_fe_1 = 'lindaappserver7.maxm.se'
host_stage_fe_2 = 'lindaappserver8.maxm.se'

in_jboss_base = {}
in_jboss_shifted = {}
in_fitnesse = {}
in_activeMq = {}

dp_jboss_base = {}
dp_jboss_shifted = {}
dp_fitesse = {}

rs_jboss_base = {}
rs_jboss_shift = {}
rs_fitnesse = {}
rs_activeMq = {}

lo_cluster1 = 'cluster1'
lo_cluster2 = 'cluster2'
lo_cluster1And2 = 'cluster1And2'
lo_mts = 'mts'
lo_fitnesse = 'fitnesse'
lo_activeMq = 'activeMq'

st_jboss_be = {
    deployableArtfacts:[ar_PML_backend],
    deployer:dp_jboss_base,
    installer:in_jboss_base,
    logicalPartition:{lo_cluster1, lo_cluster1And2},
    restarter:rs_jboss_base
}
st_jboss_fe = {
    deployableArtfacts:[ar_webcounseling_app],
    deployer:dp_jboss_base,
    installer:in_jboss_base,
    logicalPartition:{lo_cluster2, lo_cluster1And2},
    restarter:rs_jboss_base
}
st_jboss_fe_shift = {
    deployableArtfacts:[ar_webcounseling_app],
    deployer:dp_jboss_shifted,
    installer:in_jboss_shifted,
    logicalPartition:{lo_cluster2, lo_cluster1And2},
    restarter:rs_jboss_shift
}
st_jboss_mts_test = {
    deployableArtfacts:[ar_mts, ar_fakexp],
    deployer:dp_jboss_base,
    installer:in_jboss_base,
    logicalPartition:{lo_mts},
    restarter:rs_jboss_base
}
st_jboss_mts = {
    deployableArtfacts:[ar_mts],
    deployer:dp_jboss_base,
    installer:in_jboss_base,
    logicalPartition:{lo_mts},
    restarter:rs_jboss_base
}
st_fitnesse = {
    deployableArtfacts:[ar_mts_spec],
    deployer:dp_fitesse,
    installer:in_fitnesse,
    logicalPartition:{lo_fitnesse},
    restarter:rs_fitnesse
}
st_activeMq = {
    deployableArtfacts:[],
    deployer:"Can not deploy on activeMq",
    installer:in_activeMq,
    logicalPartition:{lo_activeMq},
    restarter:rs_activeMq
}

environments = {
    'dev':[
        {host:host_dev_mts,   serverType:st_activeMq},
        {host:host_dev_mts,   serverType:st_jboss_mts_test},
        {host:host_dev_mts,   serverType:st_fitnesse},
        {host:host_dev_linda, serverType:st_jboss_be},
        {host:host_dev_linda, serverType:st_jboss_fe_shift},
        ],

    'sys':[
        {host:host_sys_mts,   serverType:st_activeMq},
        {host:host_sys_mts,   serverType:st_jboss_mts_test},
        {host:host_sys_mts,   serverType:st_fitnesse},
        {host:host_sys_linda, serverType:st_jboss_be},
        {host:host_sys_linda, serverType:st_jboss_fe_shift},
        ],

    'int':[
        {host:host_int_mts,   serverType:st_activeMq},
        {host:host_int_mts,   serverType:st_jboss_mts_test},
        {host:host_int_mts,   serverType:st_fitnesse},
        {host:host_int_be_1,  serverType:st_jboss_be},
        {host:host_int_be_2,  serverType:st_jboss_be},
        {host:host_int_fe_1,  serverType:st_jboss_fe},
        {host:host_int_fe_2,  serverType:st_jboss_fe},
        ],

    'stage':[
        {host:host_stage_mts,   serverType:st_activeMq},
        {host:host_stage_mts,   serverType:st_jboss_mts_test},
        {host:host_stage_mts,   serverType:st_fitnesse},
        {host:host_stage_be_1,  serverType:st_jboss_be},
        {host:host_stage_be_2,  serverType:st_jboss_be},
        {host:host_stage_fe_1,  serverType:st_jboss_fe},
        {host:host_stage_fe_2,  serverType:st_jboss_fe},
        ],
}


def getEnvironments() :
    return environments.keys()

def getArtifacts() :
    result = set()
    for environment in environments.itervalues():
        for serverConf in environment:
            result|=set(serverConf[serverType][deployableArtfacts])
    return result

def getLogiclaPartitions() :
    result = set()
    for environment in environments.itervalues():
        for serverConf in environment:
            result|=set(serverConf[serverType][logicalPartition])
    return result;

def getDeployTargets(env, artifact) :
    result = []
    for serverConf in environments[env]:
        if artifact in serverConf[serverType][deployableArtfacts]:
            result.append(serverConf)

    return result

def getInstallTargets(env, partition) :
    result = []
    for serverConf in environments[env]:
        if partition in serverConf[serverType][logicalPartition]:
            result.append(serverConf)

    return result
