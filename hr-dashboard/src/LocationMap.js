import React, { useState, useCallback, useRef, useEffect } from "react";
import {
  GoogleMap,
  useJsApiLoader,
  DrawingManager,
  Polygon,
} from "@react-google-maps/api";

const center = { lat: 24.7136, lng: 46.6753 }; // Riyadh

const mapContainerStyle = {
  width: "100%",
  height: "500px",
};

const LocationMap = () => {
  const { isLoaded } = useJsApiLoader({
    googleMapsApiKey: process.env.REACT_APP_GOOGLE_MAPS_API_KEY,
    libraries: ["drawing"],
  });

  const [polygonPath, setPolygonPath] = useState([]);
  const polygonRef = useRef(null);

  const onPolygonComplete = useCallback((polygon) => {
    const path = polygon
      .getPath()
      .getArray()
      .map((latLng) => ({
        lat: latLng.lat(),
        lng: latLng.lng(),
      }));

    setPolygonPath(path);
    polygon.setMap(null); // Remove temporary drawn polygon
  }, []);

  const onEdit = () => {
    const nextPath = polygonRef.current
      ?.getPath()
      ?.getArray()
      .map((latLng) => ({
        lat: latLng.lat(),
        lng: latLng.lng(),
      }));

    if (nextPath) {
      setPolygonPath(nextPath);
      console.log("Updated polygon path:", nextPath);
    }
  };

  useEffect(() => {
    if (polygonRef.current) {
      const path = polygonRef.current.getPath();
      window.google.maps.event.addListener(path, "set_at", onEdit);
      window.google.maps.event.addListener(path, "insert_at", onEdit);
      window.google.maps.event.addListener(path, "remove_at", onEdit);
    }
  }, [polygonPath]);

  if (!isLoaded) return <div>Loading...</div>;

  return (
    <GoogleMap
      mapContainerStyle={mapContainerStyle}
      center={center}
      zoom={13}
    >
      <DrawingManager
        onPolygonComplete={onPolygonComplete}
        options={{
          drawingControl: true,
          drawingControlOptions: {
            position: window.google.maps.ControlPosition.TOP_CENTER,
            drawingModes: ["polygon"],
          },
        }}
      />

      {polygonPath.length > 0 && (
        <Polygon
          path={polygonPath}
          editable={true}
          draggable={true}
          onLoad={(polygon) => (polygonRef.current = polygon)}
          options={{
            fillColor: "#2196F3",
            fillOpacity: 0.3,
            strokeColor: "#0D47A1",
            strokeOpacity: 0.8,
            strokeWeight: 2,
          }}
        />
      )}
    </GoogleMap>
  );
};

export default LocationMap;
