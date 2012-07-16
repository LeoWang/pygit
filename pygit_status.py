#! /usr/bin/python
# -*- coding: UTF-8 -*-

#################################################################
# Copyright (C) 2012 LEO
# FileName     : pygit_status.py
# Version      : 1.0
# Auther       : LeoWang
# Auther Email : leowang812@gmail.com
# Data         : 2012-07-15
# History      :
#                1.Data        : 2012-07-15
#                  Auther      : LeoWang
#                  Description :
#                                Create file
#################################################################

import pygit_class_def as cmdbaseclass
import pygit_command_excute as cmdexe

def opt_init():
    opt_dict = {}
    opt_dict["-s"] = cmdbaseclass.optclass("-s")
    opt_dict["--short"] = cmdbaseclass.optclass("--short")
    opt_dict["-b"] = cmdbaseclass.optclass("-b")
    opt_dict["--branch"] = cmdbaseclass.optclass("--branch")
    opt_dict["--porcelain"] = cmdbaseclass.optclass("--porcelain")
    opt_dict["-u"] = cmdbaseclass.optclass("-u")
    opt_dict["--untracked-files"] = cmdbaseclass.optclass("--untracked-files")
    opt_dict["--ignore-submodules"] = cmdbaseclass.optclass("--ignore-submodules")
    opt_dict["--ignored"] = cmdbaseclass.optclass("--ignored")
    opt_dict["-z"] = cmdbaseclass.optclass("-z")
    return opt_dict

class pycmdclass_status(cmdbaseclass.pycmdclass):
    def __init__(self):
        cmdbaseclass.pycmdclass.__init__(self,"status")
        self.opt_list = opt_init()

def pygit_status():
    pycmdclass_status_obj = pycmdclass_status()
    cmdexe.pygitcmd_exe(pycmdclass_status_obj)

def pygit_status_short():
    pycmdclass_status_obj = pycmdclass_status()
    pycmdclass_status_obj.opt_list["-s"].opt_valid = True
    cmdexe.pygitcmd_exe(pycmdclass_status_obj)
    print "git cmd name : "+pycmdclass_obj.pycmd_name

def main():
    pygit_status_short()

if __name__ == '__main__':
    main()
