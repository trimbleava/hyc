
function initMap() {
    var uluru = {lat: 26.670459, lng: -80.161208};

    var map = new google.maps.Map(document.getElementById('hyc-loc-map'), {
        zoom: 4,
        center: uluru,
        scrollwheel: false
    });

    var marker = new google.maps.Marker({
        position: uluru,
        map: map
    });
}
