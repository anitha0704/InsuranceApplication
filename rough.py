from fastapi import FastAPI, Query, Depends
from typing import List, Optional
from dao.insurance_policy_dao import InsurancePolicyDAO

app = FastAPI()

dao = InsurancePolicyDAO()

@app.get("/policies/")
def get_all_policies():
    """Fetch all insurance policies"""
    result = dao.get_all_policy()
    return {"response": result}


@app.get("/policies/search/")
def search_policies_by_name(name: str):
    """Search policies by name (partial matches included)"""
    result = dao.get_policy_by_name(name)
    return {"response": result}


@app.get("/policies/filter/")
def filter_policies(
    policy_type: Optional[List[str]] = Query(None, description="Filter by policy type (e.g., Term Life, Health)"),
    min_premium: Optional[float] = Query(None, description="Minimum premium amount"),
    max_premium: Optional[float] = Query(None, description="Maximum premium amount"),
    min_coverage: Optional[float] = Query(None, description="Minimum coverage amount"),
    sort_by_premium: Optional[str] = Query(None, description="Sort by premium (asc/desc)")
):
    """Filter policies by type, premium range, and coverage amount"""
    result = dao.get_filtered_policies(policy_type, min_premium, max_premium, min_coverage, sort_by_premium)
    return {"response": result}
