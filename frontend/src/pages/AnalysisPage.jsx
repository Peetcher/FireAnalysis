import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import '../styles/Analysis.css';
import Documents from "../components/Documents.jsx";
import Analysis from "../components/Analysis.jsx";

function AnalysisPage() {

    return (
        <div className='analysis-page'>
            <div >
                <Analysis />
            </div>
        </div>

    );
}

export default AnalysisPage;
