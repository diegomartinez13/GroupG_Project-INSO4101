import React, { useState, useEffect } from "react";
import { MapContainer, TileLayer, Marker, Popup, useMap } from "react-leaflet";
import { csv } from "d3-fetch";
import datas from "./recycling_centers.csv";
import L from "leaflet";

const MapWithCSVMarkers = () => {
  const [markers, setMarkers] = useState([]);
  const [userLocation, setUserLocation] = useState(null);
  const [mapSize, setMapSize] = useState({ width: "100%", height: "500px" });

  useEffect(() => {
    // Load the CSV file and parse its contents
    csv(datas).then((data) => {
      // Map the CSV rows to Marker components
      const newMarkers = data?.map((row) => (
        <Marker key={row.name} position={[row.latitude, row.longitude]}>
          <Popup>{row.name}</Popup>
        </Marker>
      ));
      setMarkers(newMarkers);
    });
  }, []);

  useEffect(() => {
    // Get the user's location
    navigator.geolocation.getCurrentPosition((position) => {
      setUserLocation([position.coords.latitude, position.coords.longitude]);
    });
  }, []);

  useEffect(() => {
    const handleResize = () => {
      setMapSize({ width: "100%", height: `${window.innerHeight * 0.7}px` });
    };
    window.addEventListener("resize", handleResize);

    return () => window.removeEventListener("resize", handleResize);
  }, []);

  return (
    <MapContainer center={[51.505, -0.09]} zoom={13} style={{ ...mapSize }}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
      {markers}
      {userLocation && <UserLocationMarker position={userLocation} />}
    </MapContainer>
  );
};

const UserLocationMarker = ({ position }) => {
  const map = useMap();

  useEffect(() => {
    // Create the marker
    const marker = L.marker(position, {
      icon: L.icon({
        iconUrl: "https://cdn0.iconfinder.com/data/icons/small-n-flat/24/678111-map-marker-512.png",
        iconSize: [48, 48],
      }),
    });

    // Create the circle
    const circle = L.circle(position, {
      radius: 80,
      color: "red",
      fillColor: "#3186cc",
      fillOpacity: 0.2,
    });

    // Add the marker and circle to the map
    marker.addTo(map);
    circle.addTo(map);

    // Set the map's view to the user's location
    map.setView(position, 13);

    return () => {
      // Remove the marker and circle from the map when the component unmounts
      marker.remove();
      circle.remove();
    };
  }, [map, position]);

  return null;
};

export default MapWithCSVMarkers;
