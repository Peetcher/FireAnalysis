import React, { useState, useEffect } from 'react';
import {MapContainer, TileLayer, Marker, Popup, CircleMarker} from 'react-leaflet';
import L from 'leaflet';
import api from "../django_main.js";
import 'leaflet/dist/leaflet.css';

const icon = new L.Icon({
  iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
});

const FiresMap = (fires) => {

    if (!fires || fires.fires.length === 0) {
        return <div>Loading...</div>; // You can customize this message or add a spinner
    }

  return (
    <MapContainer center={[56.3159, 96.0359]} zoom={5} style={{ height: "70vh", width: "100%" }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      {fires.fires.map(fire => (
        <CircleMarker
          key={fire.id}
          center={[fire.latitude, fire.longitude]}
          radius={Math.sqrt(fire.detection_area) * 10}
          fillColor="red"
          color="red"
          weight={1}
          fillOpacity={0.6}
        >
          <Popup>
            <div>
              <h3>{fire.fire_number.number}</h3>
              <p>{fire.state.caption}</p>
              <p>Region: {fire.fire_number.region.caption}</p>
              <p>Date: {fire.fire_date}</p>
            </div>
          </Popup>
        </CircleMarker>
      ))}
    </MapContainer>
  );
};

export default FiresMap;