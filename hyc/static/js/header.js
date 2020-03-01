var selector = 'ul.nav > li'

$(document).ready(function () {
    $(selector).click(function (e) {
        e.preventDefault();
        $(selector).removeClass('active');
        $(this).addClass('active');
    });
});