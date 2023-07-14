var lat = document.getElementById("map").getAttribute('lat');
var lng = document.getElementById("map").getAttribute('lng');
console.log(lat)

const copy = "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a>";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const layer = L.tileLayer(url, { attribution: copy }).on('tileload', function(e) {
    e.tile.alt = 'Carte interactive de la région SUD PACA France ';
});

const map = L.map("map", { 
    layers: [layer],
    center: [lat, lng],
    zoom: 4,
    zoomControl: false,
    scrollWheelZoom: false,
    dragging: false,
    // doubleClickZoom: false,
});

map.panTo([lat, lng], 4)
map.flyTo([lat, lng], 9)