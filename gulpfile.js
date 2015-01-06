var gulp = require('gulp');
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');

gulp.task('watch', function() {
  gulp.start('sass');
  gulp.watch('./performanceplatformselfserve/static/stylesheets/*.scss', ['sass']);
});

gulp.task('sass', function () {
  gulp.src('./performanceplatformselfserve/static/stylesheets/application.scss')
    .pipe(sourcemaps.init())
    .pipe(sass())
    .pipe(sourcemaps.write())
    .pipe(gulp.dest('./performanceplatformselfserve/static/stylesheets/'));
});