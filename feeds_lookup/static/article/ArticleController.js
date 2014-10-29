
'use strict';

var article_app = angular.module('article', []);
article_app.controller('ArticleController', function() {
    this.qty = 1;

    this.items = [
        { 'name': 'Scuba Diving Kit', 'id': 7297510 },
        { 'name': 'Snorkel', 'id': '0278916' },
        { 'name': 'Wet Suit', 'id': '2389017' },
        { 'name': 'Beach Towel', 'id': 1000983 }
    ];


  });

angular.bootstrap(document.getElementById("app2"),['article']);
