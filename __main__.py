#!/usr/bin/env python
# AUTHOR: WRS
# 

def run_main(**kwargs):
    pass

if __name__ == '__main__':
    import yaml
    namelist = yaml.load(open('options.yaml', 'r'))
    run_main(**namelist)
