from typing import Optional, List

from fastapi import FastAPI, Query
from dao.insurance_policy_dao import InsurancePolicyDAO
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

dao = InsurancePolicyDAO()

@app.get("/policies/")
def get_all_insurance_policies():
   result = dao.get_all_policy()
   print("all_policies", result)
   return {"response": result}

@app.get("/policies/search/{name}")
def get_policies_by_name(name: str):
   result = dao.get_policy_by_name(name)
   print("policies_by_name", result)
   return {"response": result}

@app.get("/policies/filter/")
def filter_policies(
    policy_type: Optional[List[str]] = Query(None, description="Filter by policy type (e.g., Term Life, Health)"),
    min_premium: Optional[float] = Query(None, description="Minimum premium amount"),
    max_premium: Optional[float] = Query(None, description="Maximum premium amount"),
    min_coverage: Optional[float] = Query(None, description="Minimum coverage amount"),
    sort_by_premium: Optional[str] = Query(None, description="Sort by premium (asc/desc)"),
    limit: int = Query(10, description="Number of results per page"),
    offset: int = Query(0, description="Starting index for pagination")
):
    """Filter policies by type, premium range, and coverage amount"""
    result = dao.get_filtered_policies(policy_type, min_premium, max_premium, min_coverage, sort_by_premium, limit, offset)
    print("policies_by_filters", result)
    return {"response": result, "limit": limit, "offset": offset}


