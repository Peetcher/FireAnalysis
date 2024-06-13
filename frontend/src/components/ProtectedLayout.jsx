import React from 'react';
import Sidebar from './Sidebar.jsx';
import Header from './Header.jsx';
import '../styles/ProtectedLayout.css';

const ProtectedLayout = ({ children }) => {
  return (
    <div className="protected-layout">
      <Header />
      <div className="main">
        <Sidebar />
        <div className="content">
          {children}
        </div>
      </div>
    </div>
  );
}

export default ProtectedLayout;
