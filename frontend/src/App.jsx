import react from "react"
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import Sidebar from './components/Sidebar.jsx';
import Header from './components/Header.jsx';
import ProtectedLayout from "./components/ProtectedLayout.jsx";
import ProtectedRoute from "./components/ProtectedRoute"
import AnalysisPage from './pages/AnalysisPage.jsx';
import DocumentsPage from "./pages/Documents.jsx";
import Settings from './pages/Settings';
import Login from "./pages/Login"
import Register from "./pages/Register"
import NotFound from "./pages/NotFound"
import './styles/App.css';

import protectedRoute from "./components/ProtectedRoute";
function Logout() {
  localStorage.clear()
  return <Navigate to="/login" />
}

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}

function App() {
  return (
    <div className="App">
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <ProtectedLayout>
                <AnalysisPage />
              </ProtectedLayout>
            </ProtectedRoute>
          }
        />
        <Route
          path="/analysis"
          element={
            <ProtectedRoute>
              <ProtectedLayout>
                <AnalysisPage />
              </ProtectedLayout>
            </ProtectedRoute>
          }
        />
        <Route
          path="/settings"
          element={
            <ProtectedRoute>
              <ProtectedLayout>
                <Settings />
              </ProtectedLayout>
            </ProtectedRoute>
          }
        />
        <Route
          path="/documents"
          element={
            <ProtectedRoute>
              <ProtectedLayout>
                <DocumentsPage />
              </ProtectedLayout>
            </ProtectedRoute>
          }
        />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/register" element={<RegisterAndLogout />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
    </div>
  );
}

export default App
