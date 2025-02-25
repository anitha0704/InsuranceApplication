from service.insurance_policy_service import InsurancePolicyAPIService


""" Initialize the Application """
insurance_policy_api = InsurancePolicyAPIService()
app = insurance_policy_api.app
