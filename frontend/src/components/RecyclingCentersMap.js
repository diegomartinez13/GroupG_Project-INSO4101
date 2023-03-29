import React from "react";
import { MapContainer, TileLayer, Marker, Popup, useMap } from "react-leaflet";
import { Card, CardHeader } from "@mui/material";

const start = [18.1995, -67.1448];

const RecyclingCentersMap = () => {
    
    const recyclingCenters = [
      {
        name: "Recycling Center 1",
        location: [18.1995, -67.1448],
      },
      {
        name: "Recycling Center 2",
        location: [37.7747, -122.407],
      },
      {
        name: "Recycling Center 3",
        location: [37.7791, -122.4158],
      },
    ];

    const isSmallScreen = window.innerWidth < 900;
    console.log(isSmallScreen);
  
    function MyMap() {
      const map = useMap();
      map.invalidateSize(); // fix for Leaflet map not rendering properly on initial load
      return null;
    }
  
    return (
        <>
        <CardHeader title="Recycling Centers" />
        <Card sx={{borderRadius: 2}  }>
            
      <div style={{ height: isSmallScreen ? "60vh" : "calc(100vh - 240px)" }}>
        
        <MapContainer center={start} zoom={13} style={{ height: "100%" } }>
          <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
          {recyclingCenters.map((markers) => (
            <Marker key={markers.name} position={markers.location} >
              <Popup>{markers.name}</Popup>
            </Marker>
          ))}
          <MyMap />
        </MapContainer>
      </div>
      </Card>
        </>
        
    );
  };
  
  export default RecyclingCentersMap;