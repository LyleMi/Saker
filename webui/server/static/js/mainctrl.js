app.controller("mainctrl",
    function($scope, $rootScope, $state, HttpService) {

        $scope.data = {
            logs: [],
            blists: [],
            rules: [],
            newIPRule: {
                ip: "",
                allow: "",
                comment: ""
            },
            newHTTPRule: {
                key: "",
                value: "",
                rtype: "",
                allow: "",
            },
            changeIPRule: {},
            changeHTTPRule: {},
        }

        $scope.getAll = function(type) {
            HttpService.get(type, {}, function(response) {
                $scope.data[type + 's'] = response.data;
            }, function(err) {
                if (err.data.msg) {
                    alert(err.data.msg);
                } else {
                    alert("很抱歉，发生了未知错误");
                }
            });
        };

        $scope.delete = function(type, uid) {
            console.log(type, uid);
            HttpService.delete(type, {
                uid: uid
            }, function(response) {
                $scope.getAll(type);
            }, function(err) {
                if (err.data.msg) {
                    alert(err.data.msg);
                } else {
                    alert("很抱歉，发生了未知错误");
                }
            });
        };

        $scope.change = function(type, uid) {
            if (type == "rule") {
                for (let r in $scope.data.rules) {
                    if ($scope.data.rules[r].uid == uid) {
                        $scope.data.changeHTTPRule = JSON.parse(JSON.stringify($scope.data.rules[r]));
                        $scope.data.changeHTTPRule.allow = $scope.data.rules[r].allow ? "1" : "0";
                        break;
                    }
                }
                $('#changeHttpRuleModal').modal();
            } else if (type == 'blist') {
                for (let r in $scope.data.blists) {
                    if ($scope.data.blists[r].uid == uid) {
                        $scope.data.changeIPRule = JSON.parse(JSON.stringify($scope.data.blists[r]));
                        $scope.data.changeIPRule.allow = $scope.data.blists[r].allow ? "1" : "0";
                        break;
                    }
                }
                $('#changeRuleModal').modal();
            }
        }

        $scope.changeHTTPRule = function() {
            HttpService.put("rule", $scope.data.changeHTTPRule, function(response) {
                $scope.getAll("rule");
            }, function(err) {
                if (err.data.msg) {
                    alert(err.data.msg);
                } else {
                    alert("很抱歉，发生了未知错误");
                }
            });
            $scope.data.changeHTTPRule = {};
            $('#changeHttpRuleModal').modal('hide');
        }

        $scope.changeIPRule = function() {
            HttpService.put("blist", $scope.data.changeIPRule, function(response) {
                $scope.getAll("blist");
            }, function(err) {
                if (err.data.msg) {
                    alert(err.data.msg);
                } else {
                    alert("很抱歉，发生了未知错误");
                }
            });
            $scope.data.changeIPRule = {};
            $('#changeRuleModal').modal('hide');
        }

        $scope.openIPRuleModel = function() {
            $('#ruleModal').modal();
        };

        $scope.addIPRule = function(seq = 0) {
            $('#ruleModal').modal('hide');
            HttpService.post("blist", {
                ip: $scope.data.newIPRule.ip,
                allow: $scope.data.newIPRule.allow,
                comment: $scope.data.newIPRule.comment,
                seq: seq
            }, function(response) {
                $scope.getAll("blist");
                $scope.data.newIPRule = {
                    ip: "",
                    allow: "",
                    comment: ""
                };
            }, function(err) {
                if (err.data.msg) {
                    alert(err.data.msg);
                } else {
                    alert("很抱歉，发生了未知错误");
                }
            });
        };

        $scope.openHTTPRuleModel = function() {
            $('#httpRuleModal').modal();
        };

        $scope.addHTTPRule = function(seq = 0) {
            $('#httpRuleModal').modal('hide');
            HttpService.post("rule", {
                key: $scope.data.newHTTPRule.key,
                value: $scope.data.newHTTPRule.value,
                rtype: $scope.data.newHTTPRule.rtype,
                allow: $scope.data.newHTTPRule.allow,
                seq: seq
            }, function(response) {
                $scope.getAll("rule");
                $scope.data.newHTTPRule = {
                    key: "",
                    value: "",
                    rtype: "",
                    allow: "",
                };
            }, function(err) {
                if (err.data.msg) {
                    alert(err.data.msg);
                } else {
                    alert("很抱歉，发生了未知错误");
                }
            });
        };
    }
);