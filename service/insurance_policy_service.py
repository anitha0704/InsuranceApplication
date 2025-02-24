from typing import Optional, List
from fastapi import FastAPI, Query
from dao.insurance_policy_dao import InsurancePolicyDAO
from fastapi.middleware.cors import CORSMiddleware
from config import POLICIES_BASE_URL, SEARCH_URL, FILTER_URL

class InsurancePolicyAPI:
    def __init__(self):
        self.app = FastAPI()
        self.dao = InsurancePolicyDAO()
        self.setup_cors()
        self.add_routes()

    def setup_cors(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["http://localhost:3000"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def add_routes(self):
        self.app.get(POLICIES_BASE_URL)(self.get_all_insurance_policies)
        self.app.get(SEARCH_URL)(self.get_policies_by_name)
        self.app.get(FILTER_URL)(self.filter_policies)

    def get_all_insurance_policies(self):
        result = self.dao.get_all_policy()
        print("all_policies", result)
        return {"response": result}

    def get_policies_by_name(self, name: str):
        result = self.dao.get_policy_by_name(name)
        print("policies_by_name", result)
        return {"response": result}

    def filter_policies(
        self,
        policy_type: Optional[List[str]] = Query(None, description="Filter by policy type"),
        min_premium: Optional[float] = Query(None, description="Minimum premium"),
        max_premium: Optional[float] = Query(None, description="Maximum premium"),
        min_coverage: Optional[float] = Query(None, description="Minimum coverage amount"),
        sort_by_premium: Optional[str] = Query(None, description="Sort by premium (asc/desc)"),
        limit: int = Query(10, description="Number of results per page"),
        offset: int = Query(0, description="Starting index for pagination")
    ):
        result = self.dao.get_filtered_policies(
            policy_type, min_premium, max_premium, min_coverage, sort_by_premium, limit, offset
        )
        return {"response": result, "limit": limit, "offset": offset}
