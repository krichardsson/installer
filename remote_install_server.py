#!/usr/bin/python
import argparse
import conf

parser = argparse.ArgumentParser(description='This script installs a server')
parser.add_argument('-e', dest='environment', choices=conf.getEnvironments(), required=True)
parser.add_argument('-l', dest='logicalPartition', choices=conf.getLogiclaPartitions(), required=True)
parser.add_argument('-v', dest='version', required=False)

args = parser.parse_args()

for target in conf.getInstallTargets(args.environment, args.logicalPartition):
    print target
print


