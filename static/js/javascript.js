// on load animation

window.addEventListener("load", function() {
    var tl = gsap.timeline()
    tl.to('.page-container', 0.1, { opacity: 1 }, '-=0.7')
    tl.to('.left-shutter', 1.5, { left: '-150vw', ease: 'power3' })
    tl.to('.right-shutter', 1.5, { left: '150vw', ease: 'power3' }, '-=1.5')
    tl.from('.wobble-onload', 1, { transform: 'scale(0.85)', ease: 'power3', opacity: 0, stagger: 0.1 }, '-=1.5')
    tl.from('.main-title', 1, { ease: 'power2' }, '-=1.5')
    tl.to('.mobile-navigation', 0.7, { top: '0px', opacity: 1, ease: 'power3' }, '-=1.5')
    setTimeout(function() {
        $('.loading-align-center').remove()
    });
});

// open all categories for a selected section.

$('#open-all-front').on('click', function() {
    $('#css').collapse('toggle');
    $('#js').collapse('toggle');
    $('#frame').collapse('toggle');
    $('#animation').collapse('toggle');
    $('#charts').collapse('toggle');
    $('#icons').collapse('toggle');
    $('#fonts').collapse('toggle');
    $('#forms').collapse('toggle');
    $('.front-plus').toggleClass('fa-plus-square');
    $('.front-plus').toggleClass('fa-minus-square');
    $('#illustrations').collapse('toggle');
    $('#photos').collapse('toggle');
    $('#svg').collapse('toggle');
    $('#inspiration').collapse('toggle');
});

$('#open-all-back').on('click', function() {
    $('#framework').collapse('toggle');
    $('#django').collapse('toggle');
    $('#modules').collapse('toggle');
    $('#database').collapse('toggle');
    $('#automation').collapse('toggle');
    $('#flask-modules').collapse('toggle');
    $('#django-modules').collapse('toggle');
});

$('.far').on('click', function() {
    $(this).toggleClass('fa-plus-square')
    $(this).toggleClass('fa-minus-square')
});

$('.toggle-nav').on('click', function() {
    var tl = gsap.timeline()
    if ($('.mobile-navigation').hasClass('closed')) {
        tl.to('.mobile-questionmark', 0.5, { transform: 'translate( -20vw, 0)' })
        tl.to('.nav-link-container', 0.5, { left: '40vw' }, '-=0.5');
        tl.to('.nav-backdrop', 0.05, { right: '0vw' }, '-=0.5');
        tl.to('.nav-backdrop', 1, { backdropFilter: 'blur(4px)', backgroundColor: 'rgba(0, 0, 0, 0.25)' }, '-=0.5');
        tl.from('.nav-button', 0.5, { left: '65vw', ease: 'power3', stagger: 0.05 }, '-=0.9');
        tl.from('.nav-button', 0.5, { transform: 'scaleY(0.5)', ease: 'power3', stagger: 0.05 }, '-=0.75');
        $('.mobile-navigation').toggleClass('closed');
    } else {
        tl.to('.mobile-questionmark', 0.5, { transform: 'translate( 0, 0)' })
        tl.to('.nav-link-container', 0.5, { left: '100vw' }, '-=0.5');
        tl.to('.nav-backdrop', 0.2, { backdropFilter: 'blur(0px)', backgroundColor: 'rgba(0, 0, 0, 0.0)' }, '-=0.5');
        tl.to('.nav-backdrop', 0.01, { right: '100vw' })
        $('.mobile-navigation').toggleClass('closed');
    }

});