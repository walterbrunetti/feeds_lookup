'use strict';

var articleControllers = angular.module('articleControllers', []);

articleControllers.controller("ArticleController", ['$scope', '$routeParams', 'ArticleSearch', function($scope, $routeParams, ArticleSearch) {

    
    $scope.search = function search() {
        $scope.articles = ArticleSearch.query({query: $scope.search_query}, function(data) {
            $scope.articles = data.results;
        });
    };

    $scope.search_query = "";

}]);


articleControllers.controller("ArticleDetailController", ['$scope', '$routeParams', 'Article', function($scope, $routeParams, Article) {
    alert($routeParams.id);
    $scope.article = Article.query({id: $routeParams.id});

}]);

