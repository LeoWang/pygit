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

class pycmdclass_status(cmdbaseclass.pycmdclass):
    def __init__(self):
        cmdbaseclass.pycmdclass.__init__(self,"status")
        self.opt_list = []

def pygit_status():
    pycmdclass_status_obj = pycmdclass_status()
    #pycmdclass_obj = cmdbaseclass.pycmdclass("status")
    #opt_obj_list = []
    #cmdexe.pygitcmd_exe(pycmdclass_obj,opt_obj_list)
    cmdexe.pygitcmd_exe(pycmdclass_status_obj)
                       # pycmdclass_status_obj.opt_list)

def pygit_status_short():
    pycmdclass_obj = cmdbaseclass.pycmdclass("status")
    print "git cmd name : "+pycmdclass_obj.pycmd_name
    opt_obj_list = []
    opt_obj = cmdbaseclass.optclass("-s","--short")
    opt_obj_list.append(opt_obj)
    cmdexe.pygitcmd_exe(pycmdclass_obj,opt_obj_list)

def main():
    pygit_status()

if __name__ == '__main__':
    main()
