from typing import Optional, List

from dao.database_connection import DatabaseConnection


class InsurancePolicyDAO:
    def __init__(self):
        self.db = DatabaseConnection()
        self.cursor = self.db.get_cursor()

    def construct_json_result(self, result):
        result_in_json_format = [
            {"id": row[0], "name": row[1], "type": row[2], "premium": row[3], "coverage": row[4]}
            for row in result
        ]
        return result_in_json_format

    def get_all_policy(self):
        """Fetch all insurance policies"""
        query = """
            SELECT id, name, type, premium, coverage 
            FROM insurance_policies
            ORDER BY premium;
        """
        self.cursor.execute(query)
        return self.construct_json_result(self.cursor.fetchall())

    def get_policy_by_name(self, name: str):
        """Search for policies by name (case-insensitive search)"""
        query = """
            SELECT id, name, type, premium, coverage 
            FROM insurance_policies
            WHERE LOWER(name) LIKE LOWER(?)
            ORDER BY premium;
        """
        self.cursor.execute(query, (f"%{name}%",))
        return self.construct_json_result(self.cursor.fetchall())

    def get_filtered_policies(
            self,
            policy_types: Optional[List[str]],
            min_premium: Optional[float],
            max_premium: Optional[float],
            min_coverage: Optional[float]
    ):
        """Filter policies based on multiple criteria"""
        query = """
            SELECT id, name, type, premium, coverage 
            FROM insurance_policies 
            WHERE 1=1
        """
        params = []

        if policy_types:
            placeholders = ", ".join(["?"] * len(policy_types))
            query += f" AND type IN ({placeholders})"
            params.extend(policy_types)

        if min_premium is not None:
            query += " AND premium >= ?"
            params.append(min_premium)

        if max_premium is not None:
            query += " AND premium <= ?"
            params.append(max_premium)

        if min_coverage is not None:
            query += " AND coverage >= ?"
            params.append(min_coverage)

        query += " ORDER BY premium ASC"

        self.cursor.execute(query, tuple(params))
        return self.construct_json_result(self.cursor.fetchall())

    def close_db_connection(self):
        self.db.close_connection()
