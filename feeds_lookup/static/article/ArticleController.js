
'use strict';

var article_app = angular.module('article', ['ngResource']);

article_app.factory("Post", function($resource) {
  return $resource("api/articles");
});


article_app.controller('ArticleController', function($scope) {
    this.qty = 1;

    this.items = [
        { 'name': 'Scuba Diving Kit', 'id': 7297510 },
        { 'name': 'Snorkel', 'id': '0278916' },
        { 'name': 'Wet Suit', 'id': '2389017' },
        { 'name': 'Beach Towel', 'id': 1000983 }
    ];


});


article_app.controller("PostIndexCtrl", function($scope, Post) {
  Post.get(function(data) {
    $scope.posts = data.results;
  });
});

angular.bootstrap(document.getElementById("app2"),['article']);
angular.bootstrap(document.getElementById("app3"),['article']);
