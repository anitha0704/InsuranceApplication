import React, { useState, useEffect } from "react";
import axios from "axios";
import "./InsuranceList.css";

const API_BASE_URL = "insurancepolicymanagement-api-production.up.railway.app";

const InsuranceList = () => {
  const [policies, setPolicies] = useState([]);
  const [search, setSearch] = useState("");
  const [error, setError] = useState({ message: "", status: null });
  const [filters, setFilters] = useState({
    policy_type: "",
    min_premium: "",
    max_premium: "",
    min_coverage: "",
  });

  const fetchPolicies = async () => {
    try {
      setError({ message: "", status: null });
      const response = await axios.get(`${API_BASE_URL}/policies/`);
      setPolicies(response.data.response);
    } catch (error) {
      setError({
        status: error.response?.data?.detail?.status,
        message: error.response?.data?.detail?.message,
      });
    }
  };

  const handleSearch = async () => {
    if (!search.trim()) {
      fetchPolicies();
      return;
    }

    try {
      setError({ message: "", status: null });
      const response = await axios.get(`${API_BASE_URL}/policies/search/${encodeURIComponent(search)}`);
      setPolicies(response.data.response);
    } catch (error) {
      setError({
        status: error.response?.data?.detail?.status,
        message: error.response?.data?.detail?.message || "Error filtering policies.",
      });
    }
  };

  const handleFilter = async () => {
    try {
      const processedFilters = {};
      setError({ message: "", status: null });
      Object.entries(filters).forEach(([key, value]) => {
        if (value !== "" && value !== null) {
          processedFilters[key] = value;
        }
      });

      const queryParams = new URLSearchParams(processedFilters).toString();
      const response = await axios.get(`${API_BASE_URL}/policies/filter/?${queryParams}`);
      console.log("response filters:", response)
      setPolicies(response.data.response);
    } catch (error) {
      setError({
        status: error.response?.data?.detail?.status,
        message: error.response?.data?.detail?.message || "Error filtering policies.",
      });
    }
  };
  
  const handleSearchChange = (e) => {
    const value = e.target.value;
  
    if (!isNaN(value) && value.trim() !== "") {
      alert("Invalid input: Only numbers are not allowed.");
      return;
    }
  
    setSearch(value);
  };

  return (
    <div className="container">
      <h2>Insurance Policies</h2>

      {/* Search Input */}
      <div className="search-box">
        <input
          type="text"
          placeholder="Search all or Search by name..."
          value={search}
          onChange={handleSearchChange}
        />
        <button onClick={handleSearch}>Search</button>
      </div>

      {/* Filters */}
      <div className="filter-box">
        <select
          onChange={(e) => setFilters({ ...filters, policy_type: e.target.value })}>
          <option value="">Select Policy Type</option>
          <option value="Health">Health</option>
          <option value="Vehicle">Vehicle</option>
          <option value="Term Life">Term Life</option>
          <option value="Business">Business</option>
          <option value="Travel">Travel</option>
        </select>

        <input
          type="number"
          placeholder="Min Premium"
          step="500"
          onChange={(e) => setFilters({ ...filters, min_premium: e.target.value })}
        />
        <input
          type="number"
          placeholder="Max Premium"
          step="500"
          onChange={(e) => setFilters({ ...filters, max_premium: e.target.value })}
        />
        <input
          type="number"
          placeholder="Minimum Coverage"
          step="1000"
          onChange={(e) => setFilters({ ...filters, min_coverage: e.target.value })}
        />
        <button onClick={handleFilter}>Apply Filters</button>
      </div>

      {/* Policies Table */}
      {!error.message ? (
        <table>
          <thead>
            <tr>
              <th>Policy Name</th>
              <th>Type</th>
              <th>Premium</th>
              <th>Coverage</th>
            </tr>
          </thead>
          <tbody>
            {policies?.length > 0 ? (
              policies.map((policy) => (
                <tr key={policy.id}>
                  <td>{policy.name}</td>
                  <td>{policy.type}</td>
                  <td>Rs.{policy.premium}</td>
                  <td>Rs.{policy.coverage}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="4">No policies found.</td>
              </tr>
            )}
          </tbody>
        </table>
      ) : (
        <div className="error-message">
          <strong>Error {error.status}:</strong> {error.message}
        </div>
      )}
    </div>
  );
};

export default InsuranceList;
