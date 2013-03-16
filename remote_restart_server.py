#!/usr/bin/python
import argparse
import conf

parser = argparse.ArgumentParser(description='This script restarts serves')
parser.add_argument('-e', dest='environment', choices=conf.getEnvironments(), required=True)
parser.add_argument('-l', dest='logicalPartition', choices=conf.getLogiclaPartitions(), required=True)

args = parser.parse_args()

for target in conf.getInstallTargets(args.environment, args.logicalPartition):
    print target
print


