

$( document ).on( 'click', '.nav-list li', function ( e ) {
    $( this ).addClass( 'active' ).siblings().removeClass( 'active' );
} );

var selector = '.nav li';

$(selector).on('click', function(){
    $(selector).removeClass('active');
    $(this).addClass('active');
});

$(function() {
    // Highlight current page in nav bar
    $('.nav, .navbar-nav li').each(function() {
        // Count the number of links to the current page in the <li>
        var matched_links = $(this).find('a[href]').filter(function() {
            return $(this).attr('href') == window.location.pathname;
        }).length;
        // If there's at least one, mark the <li> as active
        if (matched_links)
            $(this).addClass('active');
    });
});
It's also quite easy to add a click event to return false (or change the href attribute to #) for the current page, without changing the template/html markup:

        var matched_links = $(this).find('a[href]').filter(function() {
            var matched = $(this).attr('href') == window.location.pathname;
            if (matched)
                $(this).click(function() { return false; });
            return matched;
        }).length;