#!/usr/bin/python
import argparse
import conf

parser = argparse.ArgumentParser(description='This script deploys an artifact on a server')
parser.add_argument('-e', dest='environment', choices=conf.getEnvironments(), required=True)
parser.add_argument('-a', dest='artifact', choices=conf.getArtifacts(), required=True)
parser.add_argument('-v', dest='version', required=False)

args = parser.parse_args()

for target in conf.getDeployTargets(args.environment, args.artifact):
    print target
print


