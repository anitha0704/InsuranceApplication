import unittest

from fastapi.testclient import TestClient

from service.insurance_policy_service import InsurancePolicyAPIService


class FakeInsurancePolicyDAO:
    def __init__(self):
        self.fake_result = [
            {"id": 1, "name": "Health Insurance Plan", "type": "Health", "premium": 500, "coverage": 25000}]

    def get_all_policy(self):
        return self.fake_result

    def get_policy_by_name(self, name):
        if name == "Health Insurance Plan":
            return self.fake_result
        return []

    def get_filtered_policies(self, policy_type, min_premium, max_premium, min_coverage):
        if policy_type and "Life" in policy_type:
            return [{"id": 2, "name": "Life Insurance", "type": "Life", "premium": 1000, "coverage": 25000}]
        return []


class TestInsurancePolicyAPIService(unittest.TestCase):
    def setUp(self):
        self.service = InsurancePolicyAPIService()
        self.service.dao = FakeInsurancePolicyDAO()
        self.client = TestClient(self.service.app)

    def assert_ok(self, expected_status_code):
        self.assertEqual(expected_status_code, 200)

    def assert_not_ok(self, expected_status_code):
        self.assertEqual(expected_status_code, 404)

    def assert_equal_error_message(self, response, error_message):
        expected_error_msg = response.get("detail").get("message")
        self.assertEqual(expected_error_msg, error_message)

    def test_get_all_insurance_policies(self):
        response = self.client.get("/policies")

        self.assert_ok(response.status_code)
        self.assertIn("response", response.json())

    def test_get_policies_by_name_found(self):
        response = self.client.get("/policies/search/Health Insurance Plan")

        self.assert_ok(response.status_code)
        self.assertIn("response", response.json())

    def test_filter_policies_found(self):
        response = self.client.get("/policies/filter?policy_type=Life")

        self.assert_ok(response.status_code)
        self.assertIn("response", response.json())

    def test_get_policies_by_name_not_found(self):
        response = self.client.get("/policies/search/unknown")
        actual_error_msg = "No Insurance Policies Found for Name: unknown"

        self.assert_not_ok(response.status_code)
        self.assert_equal_error_message(response.json(), actual_error_msg)

    def test_filter_policies_not_found(self):
        response = self.client.get("/policies/filter?policy_type=Unknown")
        actual_error_msg = "No Insurance Policies Found for the selected filters"

        self.assert_not_ok(response.status_code)
        self.assert_equal_error_message(response.json(), actual_error_msg)

    def test_filter_invalid_premium_range(self):
        response = self.client.get("/policies/filter?min_premium=1000&max_premium=500")
        actual_error_msg = "min_premium cannot be greater than max_premium"

        self.assert_not_ok(response.status_code)
        self.assert_equal_error_message(response.json(), actual_error_msg)


if __name__ == "__main__":
    unittest.main()
