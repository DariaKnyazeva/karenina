module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    sass: {
      options: {
        includePaths: ['bower_components/foundation/scss']
      },
      dist: {
        options: {
          outputStyle: 'compressed'
        },
        files: {
          'static/css/viewsite.css': 'scss/viewsite.scss'
        }
      }
    },

    watch: {
      grunt: { files: ['Gruntfile.js'] },

      sass: {
        files: 'scss/**/*.scss',
        tasks: ['sass']
      }
    },

    bgShell: {
      _defaults: {
        bg: true
      },
      runDjango: {
        cmd: 'tox -e dev -- runserver 0.0.0.0:8000'
      }
    }
  });

  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-bg-shell');

  grunt.registerTask('build', ['sass']);
  grunt.registerTask('serve', ['bgShell:runDjango', 'build', 'watch']);
  grunt.registerTask('default', ['build','watch']);
}
