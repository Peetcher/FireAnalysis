import React, {useState} from 'react';
import '../styles/Header.css';

function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <header className="header">
      <div className="header-content">
        <div className="header-label">
          <h1>Анализ пожаров</h1>
        </div>
        <div className="user-menu">
          <button onClick={toggleMenu} className="user-button">Пользователь</button>
          {isMenuOpen && (
            <div className="user-dropdown">
              <p>Информация</p>
              <p>Выйти</p>
            </div>
          )}
        </div>
      </div>
    </header>
  );
}

export default Header;
