#! /usr/bin/python
# -*- coding: UTF-8 -*-

#################################################################
# Copyright (C) 2012 LEO
# FileName     : pygit_branch.py
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

def pygit_branch():
    pycmdclass_obj = cmdbaseclass.pycmdclass("branch")
    opt_obj_list = []
    cmdexe.pygitcmd_exe(pycmdclass_obj,opt_obj_list)

def main():
    pygit_branch()

if __name__ == '__main__':
    main()

