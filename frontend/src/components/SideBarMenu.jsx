import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import '../styles/SideBarMenu.css';

function SideBarMenu() {
  const location = useLocation();

  return (
    <div className="SideBarMenu">
      <ul className="menu">
        <li className={location.pathname === '/analysis' ? 'active' : ''}>
          <Link to="/analysis">Анализ</Link>
        </li>
        <li className={location.pathname === '/documents' ? 'active' : ''}>
          <Link to="/documents">Документы</Link>
        </li>
        <li className={location.pathname === '/settings' ? 'active' : ''}>
          <Link to="/settings">Настройки</Link>
        </li>
      </ul>
    </div>
  );
}

export default SideBarMenu;