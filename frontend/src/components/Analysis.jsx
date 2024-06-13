import React, {useEffect, useState} from "react";
import Map from "../components/Map.jsx";
import Dashboards from "./dashboards.jsx";
import "../styles/Analysis.css"

import 'chart.js/auto';
import api from "../django_main.js";

const parseCoordinates = (coord) => {
  let  coordinate = parseFloat(coord);
  coordinate = (coordinate) / 10;
  return coordinate;
};


function Analysis(){

    const [fires, setFires] = useState([]);

    useEffect(() => {
        //console.log("Fetching fire data...");
        api.get('/main/fires_dinamics/?start_date=2016-05-01&end_date=2016-05-15')
            .then(response => {
                const firesData = response.data.map(fire => ({
                    ...fire,
                    latitude: parseCoordinates(fire.fire_number.latitude),
                    longitude: parseCoordinates(fire.fire_number.longitude),
                    detection_area: parseFloat(fire.fire_number.detection_area)
                }));
                console.log("Data fetched successfully:", firesData);
                setFires(firesData);
            })
            .catch(error => {
                console.error("There was an error fetching the data!", error);
            });
    }, []);

    return (
        <div className='analysis'>
            <div className="map"><Map fires={fires}/></div>
            <div className="dashboard"><Dashboards fires={fires}/></div>
        </div>
    );
}

export default Analysis