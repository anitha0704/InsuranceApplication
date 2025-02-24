import React, { useState, useEffect } from "react";
import axios from "axios";
import "./InsuranceList.css"; // Import CSS for styling

const API_URL = "http://localhost:8000";  // Ensure this matches FastAPI backend

const InsuranceList = () => {
  const [policies, setPolicies] = useState([]);
  const [search, setSearch] = useState("");
  const [filters, setFilters] = useState({
    policy_type: "",
    min_premium: "",
    max_premium: "",
    min_coverage: "",
  });

  // useEffect(() => {
  // }, [policies]);

  const fetchPolicies = async () => {
    try {
      const response = await axios.get(`${API_URL}/policies/`);
      setPolicies(response.data.response);
    } catch (error) {
      console.error("Error fetching policies:", error);
    }
  };

  const handleSearch = async () => {
    if (!search.trim()) {
      fetchPolicies();
      return;
    }

    try {
      const response = await axios.get(`${API_URL}/policies/search/${encodeURIComponent(search)}`);
      console.log("response name", response.data)
      setPolicies(response.data.response);
    } catch (error) {
      console.error("Error searching policies:", error);
    }
  };

  const handleFilter = async () => {
    try {
      const processedFilters = {};

      // Convert empty fields to null (FastAPI treats null as None)
      Object.entries(filters).forEach(([key, value]) => {
        if (value !== "" && value !== null) {
          processedFilters[key] = value;
        }
      });

      const queryParams = new URLSearchParams(processedFilters).toString();
      console.log("queryParams:", queryParams);

      const response = await axios.get(`${API_URL}/policies/filter/?${queryParams}`);
      console.log("response:", response.data);

      // setPolicies(response.data.response);
      // Ensure response is an array
      setPolicies(response.data.response);
    } catch (error) {
      console.error("Error filtering policies:", error);
    }
  };


  return (
    <div className="container">
      <h2>Insurance Policies</h2>

      {/* Search Input */}
      <div className="search-box">
        <input
          type="text"
          placeholder="Search by name..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
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
        </select>

        <input
          type="number"
          placeholder="Min Premium"
          onChange={(e) => setFilters({ ...filters, min_premium: e.target.value })}
        />
        <input
          type="number"
          placeholder="Max Premium"
          onChange={(e) => setFilters({ ...filters, max_premium: e.target.value })}
        />
        <button onClick={handleFilter}>Apply Filters</button>
      </div>

      {/* Policies Table */}
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
                <td>${policy.premium}</td>
                <td>${policy.coverage}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="4">No policies found.</td>
            </tr>
          )}
        </tbody>
        {/* <tbody>
          {policies.map((policy) => (
            <tr key={policy.id}>
              <td>{policy.policy_name}</td>
              <td>{policy.policy_type}</td>
              <td>${policy.premium_amount}</td>
              <td>${policy.coverage_amount}</td>
            </tr>
          ))}
        </tbody> */}
      </table>
    </div>
  );
};

export default InsuranceList;
