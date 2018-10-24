$(document).ready(function(){
	$(".main-page-navbar").hide();

	var width = $(window).width();
	var height = $(window).height();
	$(window).scroll(function(){
		if (width < 560){
			if ($(this).scrollTop() > 50) {
	            $('.main-page-navbar').show();
	        } else {
	            $('.main-page-navbar').hide();
	        }
		}
		else{
			if ($(this).scrollTop() > 300) {
	            $('.main-page-navbar').show();
	        } else {
	            $('.main-page-navbar').hide();
	        }
		};
    });

    $('.link-0').click(function(){
    	$('html, body').animate({
		    scrollTop: $("#carouselControls").offset().top
		}, 1000);
    });

    $('.link-1').click(function(){
    	$('html, body').animate({
		    scrollTop: $("#who-we-are").offset().top
		}, 1000);
    });

    $('.link-2').click(function(){
    	$('html, body').animate({
		    scrollTop: $("#our-services").offset().top
		}, 1000);
    });

    $('.link-3').click(function(){
    	$('html, body').animate({
		    scrollTop: $("#our-contacts-location").offset().top
		}, 1000);
    });

    $('.link-4').click(function(){
    	$('html, body').animate({
		    scrollTop: $("#latest-posts").offset().top
		}, 1000);
    });
});