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

def pygitcmd_exe(pygitcmd_obj):

    git_cmd_str = "git"+str_space+pygitcmd_obj.pycmd_name
    
    for opt in pygitcmd_obj.opt_list.values():
        if opt.opt_valid == True:
            git_cmd_str += str_space+opt.opt_name
            if 0 != len(opt.opt_para_value):
                git_cmd_str += str_space+opt.opt_para_value

    for para in pygitcmd_obj.pycmd_paras:
        git_cmd_str += str_space+para

    print "git cmd string : "+git_cmd_str

    #execute cmd
    os.system(git_cmd_str)

    exit(0)
