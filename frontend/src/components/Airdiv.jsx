import React, { useState, useEffect } from 'react';
import api from "../django_main"

const AirDivisionsList = () => {
    const [airDivisions, setAirDivisions] = useState([]);

    useEffect(() => {
        api.get('/main/airdivisions/')
            .then(response => {
                setAirDivisions(response.data);
            })
            .catch(error => {
                console.error("There was an error fetching the data!", error);
            });
    }, []);

    return (
        <div>
            <h1>Air Divisions</h1>
            <ul>
                {airDivisions.map(division => (
                    <li key={division.code}>{division.caption}</li>
                ))}
            </ul>
        </div>
    );
};

export default AirDivisionsList; // Экспортируем компонент AirDivisionsList
