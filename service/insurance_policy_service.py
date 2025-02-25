from typing import Optional, List

from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from config import POLICIES_BASE_URL, SEARCH_URL, FILTER_URL
from dao.insurance_policy_dao import InsurancePolicyDAO


class InsurancePolicyAPIService:
    def __init__(self):
        self.app = FastAPI()
        self.dao = InsurancePolicyDAO()
        self._setup_cors()
        self._add_routes()

    def _setup_cors(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def _add_routes(self):
        self.app.get(POLICIES_BASE_URL)(self.get_all_insurance_policies)
        self.app.get(SEARCH_URL)(self.get_policies_by_name)
        self.app.get(FILTER_URL)(self.filter_policies)

    def _fetch_policies(self, fetch_function, *args, error_message: str):
        try:
            result = fetch_function(*args)
            if not result:
                raise HTTPException(status_code=404, detail={"status": 404, "message": error_message})
            return {"response": result}

        except HTTPException as http_error:
            raise http_error

        except Exception as e:
            raise HTTPException(status_code=500,
                                detail={"status": 500, "message": f"Error fetching policies:: {str(e)}"})

    def get_all_insurance_policies(self):
        return self._fetch_policies(self.dao.get_all_policy, error_message="No Insurance Policies Found")

    def get_policies_by_name(self, name: str):
        return self._fetch_policies(self.dao.get_policy_by_name, name,
                                    error_message=f"No Insurance Policies Found for Name: {name}")

    def filter_policies(
            self,
            policy_type: Optional[List[str]] = Query(None, description="Filter by policy type"),
            min_premium: Optional[float] = Query(None),
            max_premium: Optional[float] = Query(None),
            min_coverage: Optional[float] = Query(None, description="Minimum coverage amount")
    ):
        if min_premium and max_premium and min_premium > max_premium:
            raise HTTPException(status_code=404,
                                detail={"status": 404, "message": "min_premium cannot be greater than max_premium"})

        return self._fetch_policies(
            self.dao.get_filtered_policies,
            policy_type, min_premium, max_premium, min_coverage,
            error_message="No Insurance Policies Found for the selected filters"
        )
