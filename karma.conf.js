module.exports = function(config){
  config.set({

    basePath : './',

    files : [
      //ANGULAR_SCENARIO,
      //ANGULAR_SCENARIO_ADAPTER,
      'django_test/static/bower_components/angular/angular.js',
      'django_test/static/bower_components/angular-route/angular-route.js',
      'django_test/static/bower_components/angular-mocks/angular-mocks.js',
      'django_test/static/feeds/*.js'
    ],

    autoWatch : true,

    frameworks: ['jasmine'],

    browsers : ['Chrome'],

    plugins : [
            'karma-chrome-launcher',
            'karma-firefox-launcher',
            'karma-jasmine',
            'karma-junit-reporter'
            ],

    junitReporter : {
      outputFile: 'test_out/unit.xml',
      suite: 'unit'
    },

    singleRun :true

  });
};
