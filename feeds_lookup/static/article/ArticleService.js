
var articleServices = angular.module('articleServices', ['ngResource']);

articleServices.factory('Article', ['$resource',
    function($resource){
        return $resource('/api/articles/:id', {}, {query: {method:'GET'}
    });
}]);


articleServices.factory('ArticleSearch', ['$resource',
    function($resource){
        return $resource('/api/articles/:query', {}, {query: {method:'GET'}
    });
}]);
