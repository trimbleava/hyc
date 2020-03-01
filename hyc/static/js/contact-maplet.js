var map = L.map( 'hyc-loc-map', {
    center: [20.0, 5.0],
    minZoom: 2,
    zoom: 2
});

L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    subdomains: ['a','b','c']
}).addTo( map );

var myURL = jQuery( 'script[src$="contact-maplet.js"]' ).attr( 'src' ).replace( 'contact-maplet.js', '' )
console.log(STATIC_URL, "Hello, world!");


var myIcon = L.icon({
  iconUrl: STATIC_URL + 'images/pin24.png',
  iconRetinaUrl: STATIC_URL + 'images/pin48.png',
  iconSize: [29, 24],
  iconAnchor: [9, 21],
  popupAnchor: [0, -14]
})

for ( var i=0; i < markers.length; ++i )
{
 L.marker( [markers[i].lat, markers[i].lng], {icon: myIcon} )
  .bindPopup( '<a href="' + markers[i].url + '" target="_blank">' + markers[i].name + '</a>' )
  .addTo( map );
}