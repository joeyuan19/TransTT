var timer;
var imgs;

function fadeImages(index) {
    clearTimeout(timer);
    $('.tt-logo-img-active').animate({opacity:0},function() {
        $(this).removeClass('tt-logo-img-active');
    });
    $('.tt-logo-img-'+index).animate({opacity:1},function() {
        $(this).addClass('tt-logo-img-active');
    });
    timer = setTimeout(function() {fadeImages((index+1)%imgs);},3000);
}

$(document).ready(function() {
    imgs = $('.tt-logo-bg-img').length;
    console.log($('.tt-logo').height());
    console.log($('.tt-logo').width());
    fadeImages(0);
});



