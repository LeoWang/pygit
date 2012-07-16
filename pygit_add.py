#! /usr/bin/python
# -*- coding: UTF-8 -*-

#################################################################
# Copyright (C) 2012 LEO
# FileName     : pygit_add.py
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

class pycmdclass_add(cmdbaseclass.pycmdclass):
    def __init__(self,paras):
        cmdbaseclass.pycmdclass.__init__(self,"add",paras)
        self.opt_list = {}

def pygit_add():
    pycmdclass_add_obj = pycmdclass_add(".")
    cmdexe.pygitcmd_exe(pycmdclass_add_obj)

def main():
    pygit_add()

if __name__ == '__main__':
    main()
