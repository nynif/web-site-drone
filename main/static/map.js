const copy = "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a>";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const layer = L.tileLayer(url, { attribution: copy }).on('tileload', function(e) {
    e.tile.alt = 'Carte interactive de la région SUD PACA France ';
});

const map = L.map("map", { 
    layers: [layer],
    center: [43.297559, 5.391289],
    zoom: 4,
    zoomControl: false,
    scrollWheelZoom: false,
    dragging: false,
    // doubleClickZoom: false,
});

map.panTo([43.297559, 5.391289], 4)
map.flyTo([43.297559, 5.391289], 9)