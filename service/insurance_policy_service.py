from typing import Optional, List
from fastapi import FastAPI, Query, HTTPException
from dao.insurance_policy_dao import InsurancePolicyDAO
from fastapi.middleware.cors import CORSMiddleware
from config import POLICIES_BASE_URL, SEARCH_URL, FILTER_URL

class InsurancePolicyAPIService:
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
        try:
            result = self.dao.get_all_policy()
            if not result:
                raise HTTPException(status_code=404, detail="No policies found")
            return {"response": result}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fetching policies: {str(e)}")

    def get_policies_by_name(self, name: str):
        try:
            if not name.strip():
                raise HTTPException(status_code=400, detail="Policy name cannot be empty")
            result = self.dao.get_policy_by_name(name)
            if not result:
                raise HTTPException(status_code=404, detail=f"No policies found for name: {name}")
            return {"response": result}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error searching policies: {str(e)}")


    def filter_policies(
        self,
        policy_type: Optional[List[str]] = Query(None, description="Filter by policy type"),
        min_premium: Optional[float] = Query(None, description="Minimum premium"),
        max_premium: Optional[float] = Query(None, description="Maximum premium"),
        min_coverage: Optional[float] = Query(None, description="Minimum coverage amount"),
        limit: int = Query(10, description="Number of results per page"),
        offset: int = Query(0, description="Starting index for pagination")
    ):
        try:
            if min_premium and max_premium and min_premium > max_premium:
                raise HTTPException(status_code=400, detail="min_premium cannot be greater than max_premium")

            result = self.dao.get_filtered_policies(
                policy_type, min_premium, max_premium, min_coverage, limit, offset
            )
            if not result:
                raise HTTPException(status_code=404, detail="No policies match the given filters")

            return {"response": result, "limit": limit, "offset": offset}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error filtering policies: {str(e)}")