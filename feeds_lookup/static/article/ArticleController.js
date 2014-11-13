'use strict';

var articleControllers = angular.module('articleControllers', []);

articleControllers.controller("ArticleController", ['$scope', 'Article', function($scope, Article) {

    $scope.articles = Article.query(function(data) {
        $scope.articles = data.results;
    });
    $scope.article = Article.query({id: 1});

    $scope.items = [
        { 'name': 'Scuba Diving Kit', 'id': 7297510 },
        { 'name': 'Snorkel', 'id': '0278916' },
        { 'name': 'Wet Suit', 'id': '2389017' },
        { 'name': 'Beach Towel', 'id': 1000983 }
    ];
}]);


articleControllers.controller("ArticleDetailController", ['$scope', '$routeParams', 'Article', function($scope, $routeParams, Article) {
    alert($routeParams.id);
    $scope.article = Article.query({id: $routeParams.id});

}]);

