import React, {useState} from "react";
import InsuranceList from "./components/InsuranceList";
import "./App.css";

function App() {
  const [activePage, setActivePage] = useState("home");
  return (
    <div className="app-container">
      <aside className="sidebar">
        <h2>Navigation</h2>
        <ul>
          <li onClick={() => setActivePage("dashboard")}>Dashboard</li>
          <li onClick={() => setActivePage("policies")}>Policies</li>
          <li onClick={() => setActivePage("claims")}>Claims</li>
          <li onClick={() => setActivePage("settings")}>Settings</li>
        </ul>
      </aside>

      <div className="main-content">
        {activePage === "home" ? (
          <div className="welcome-message">
            <h1>Welcome to Insurance Policy Management</h1>
            <p>
              Discover the best insurance policies tailored to your needs.  
              <br />
              Click on the <strong>Dashboard</strong> to explore our powerful tools  
              that help you compare, filter, and find the perfect policy effortlessly!
            </p>
          </div>
        ) : activePage === "dashboard" ? (
          <>
            <h1 className="header">Insurance Policy Management</h1>
            <InsuranceList />
          </>
        ) : (
          <h1>Coming Soon...</h1>
        )}
      </div>
    </div>
  );
}

export default App;
