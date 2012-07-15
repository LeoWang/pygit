#! /usr/bin/python
# -*- coding: UTF-8 -*-

#################################################################
# Copyright (C) 2012 LEO
# FileName     : pygit_command_excute.py
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
import os
import sys

str_space = " "

def pygitcmd_exe(pygitcmd_obj,opt_list):

    git_cmd_str = "git"+str_space+pygitcmd_obj.pycmd_name
    
    for opt in opt_list:
        git_cmd_str += str_space+opt.opt_short_name+str_space+opt.opt_para_value
    print "git cmd string : "+git_cmd_str

    #execute cmd
    os.system(git_cmd_str)

    exit(0)
