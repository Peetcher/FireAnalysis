import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import SideBarMenu from "./SideBarMenu.jsx";
import '../styles/Sidebar.css';

function Sidebar() {
  const location = useLocation();

  return (
    <div className="sidebar">
      <SideBarMenu/>
    </div>
  );
}

export default Sidebar;
