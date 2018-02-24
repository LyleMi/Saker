"use strict";

var app = angular.module("pocer", ["ui.router"]);

app.run(["$rootScope", function($rootScope) {}]);

app.config(["$stateProvider", "$urlRouterProvider", function($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise("/log");

    $stateProvider
        .state("notfound", {
            url: "/notfound",
            templateUrl: "static/templates/404.html",
        })
        .state("log", {
            url: "/log",
            templateUrl: "static/templates/log.html",
        })
        .state("blist", {
            url: "/blist",
            templateUrl: "static/templates/blist.html",
        })
        .state("rule", {
            url: "/rule",
            templateUrl: "static/templates/rule.html",
        })
        .state("intro", {
            url: "/intro",
            templateUrl: "static/templates/intro.html",
        })
        .state("config", {
            url: "/config",
            templateUrl: "static/templates/config.html",
        });

}]);