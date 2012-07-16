#! /usr/bin/python
# -*- coding: UTF-8 -*- 

#################################################################
# Copyright (C) 2012 LEO
# FileName     : pygit_class_def.py
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

class pycmdclass(object):
    """ The Base Class of the Python Cmd.
    """

    def __init__(self, pycmd_name="", pycmd_paras=[]):
        """Initialize the object."""
        self.pycmd_name = pycmd_name
        self.pycmd_paras = pycmd_paras


class optclass(object):
    """ The Base Class of the Python Cmd Option.
    """

    def __init__(self, opt_name="", opt_para_value="", opt_valid=False):
        """Initialize the object."""
        self.opt_name= opt_name
        self.opt_para_value = opt_para_value
        self.opt_valid = opt_valid
