import React from "react";
import { Bar, Line, Pie } from 'react-chartjs-2';
import {
  Chart,
  CategoryScale,
  LinearScale,
  BarElement,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  TimeScale
} from 'chart.js';
import 'chart.js/auto';
import "../styles/Charts.css"

Chart.register(CategoryScale, LinearScale, BarElement, PointElement, LineElement, Title, Tooltip, Legend, ArcElement, TimeScale);

const Dashboards = ({ fires }) => {
  // Количество пожаров по причинам
  if (!fires || fires.length === 0) {
        return <div>Loading...</div>; // You can customize this message or add a spinner
  }

  const causes = {};
  fires.forEach(fire => {
    const cause = fire.cause.caption;
    if (causes[cause]) {
      causes[cause]++;
    } else {
      causes[cause] = 1;
    }
  });

  const causeData = {
    labels: Object.keys(causes),
    datasets: [{
      label: 'Количество пожаров по причинам',
      data: Object.values(causes),
      backgroundColor: 'rgba(75, 192, 192, 0.6)',
      borderColor: 'rgba(75, 192, 192, 1)',
      borderWidth: 1,
    }]
  };

   // Динамика пожаров по датам
  const fireDates = {};
  fires.forEach(fire => {
    const date = new Date(fire.fire_date).toLocaleDateString();
    if (fireDates[date]) {
      fireDates[date]++;
    } else {
      fireDates[date] = 1;
    }
  });

  const fireDateData = {
    labels: Object.keys(fireDates),
    datasets: [{
      label: 'Динамика пожаров по датам',
      data: Object.values(fireDates),
      backgroundColor: 'rgba(255, 99, 132, 0.6)',
      borderColor: 'rgba(255, 99, 132, 1)',
      borderWidth: 1,
      fill: false,
    }]
  };

  // Количество пожаров по типу
  const fireKinds = {};
  fires.forEach(fire => {
    const kind = fire.fire_number.fire_kind.caption;
    if (fireKinds[kind]) {
      fireKinds[kind]++;
    } else {
      fireKinds[kind] = 1;
    }
  });

  const fireKindData = {
    labels: Object.keys(fireKinds),
    datasets: [{
      label: 'Количество пожаров по типу',
      data: Object.values(fireKinds),
      backgroundColor: 'rgba(54, 162, 235, 0.6)',
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 1,
    }]
  };

   // Количество пожаров по лесничествам
  const fireForestries = {};
  fires.forEach(fire => {
    const forestry = fire.fire_number.forestry.caption;
    if (fireForestries[forestry]) {
      fireForestries[forestry]++;
    } else {
      fireForestries[forestry] = 1;
    }
  });

  const fireForestryData = {
    labels: Object.keys(fireForestries),
    datasets: [{
      label: 'Количество пожаров по лесничествам',
      data: Object.values(fireForestries),
      backgroundColor: 'rgba(255, 159, 64, 0.6)',
      borderColor: 'rgba(255, 159, 64, 1)',
      borderWidth: 1,
    }]
  };
  // // Количество пожаров по регионам
  // const regions = {};
  // fires.forEach(fire => {
  //   const region = fire.fire_number.region.caption;
  //   if (regions[region]) {
  //     regions[region]++;
  //   } else {
  //     regions[region] = 1;
  //   }
  // });
  //
  // const regionData = {
  //   labels: Object.keys(regions),
  //   datasets: [{
  //     label: 'Количество пожаров по регионам',
  //     data: Object.values(regions),
  //     backgroundColor: 'rgba(255, 159, 64, 0.6)',
  //     borderColor: 'rgba(255, 159, 64, 1)',
  //     borderWidth: 1,
  //   }]
  // };

  return (
    <div className="charts">
      <div className="chart-container">
          <h3>Количество пожаров по причинам</h3>
          <Pie data={causeData} />
      </div>
      <div className="chart-container">
          <h3>Динамика пожаров</h3>
          <Line data={fireDateData} />
      </div>
      <div className="chart-container">
          <h3>Количество пожаров по типу</h3>
          <Bar data={fireKindData} />
      </div>
      {/*<div className="chart-container">*/}
      {/*  <h3>Пожары по регионам</h3>*/}
      {/*</div>*/}
      <div className="chart-container">
        <h3>Количество пожаров по лесничествам</h3>
        <Bar data={fireForestryData} />
      </div>
    </div>
  );
};
export default Dashboards