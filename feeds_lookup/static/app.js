'use strict';

var article_app = angular.module('article', ['ngRoute', 'article.controllers', 'article.services']);

article_app.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/', {
                templateUrl: '/static/article/assets/_articles.html',
                controller: 'ArticleController'
            }).
            when('/:id', {
                templateUrl: '/static/article/assets/_article_details.html',
                controller: 'ArticleDetailController'
            }).
            otherwise({
                redirectTo: '/'
            });
}]);


//angular.bootstrap(document.getElementById("article-app"),['article']);
