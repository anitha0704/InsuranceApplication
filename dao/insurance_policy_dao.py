from typing import Optional, List

import os
import psycopg2 as pg
from dotenv import load_dotenv
load_dotenv()

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._establish_connection()
        return cls._instance

    def _establish_connection(self):
        try:
            self.conn = pg.connect(
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT")
            )
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(f"Database Connection Error: {e}")
            self.conn = None
            self.cursor = None

    def get_cursor(self):
        return self.cursor

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        DatabaseConnection._instance = None


class InsurancePolicyDAO:
    def __init__(self):
        self.db = DatabaseConnection()
        self.cursor = self.db.get_cursor()

    def get_all_policy(self):
        query =f"""
            SELECT
                json_build_object(
                    'id', id,
                    'name', name,
                    'type', type,
                    'premium', premium,
                    'coverage', coverage
                ) AS policies
            FROM insurance_policies
            ORDER BY id;
         """
        self.cursor.execute(query)
        return [row[0] for row in self.cursor.fetchall()]

    def get_policy_by_name(self, name:str):
        query = f"""
            SELECT
                json_build_object(
                    'id', id,
                    'name', name,
                    'type', type,
                    'premium', premium,
                    'coverage', coverage
                ) AS policies
            FROM insurance_policies
            WHERE name ILIKE '%{name}%'
            ORDER BY id;
        """
        self.cursor.execute(query)
        return [row[0] for row in self.cursor.fetchall()]

    def get_filtered_policies(
                self,
                policy_types: Optional[List[str]],
                min_premium: Optional[float],
                max_premium: Optional[float],
                min_coverage: Optional[float],
                sort_by_premium: Optional[str],
                limit: int = 10,
                offset: int =0
        ):
            query = """ SELECT
                json_build_object(
                    'id', id,
                    'name', name,
                    'type', type,
                    'premium', premium,
                    'coverage', coverage
                ) AS policies
            FROM insurance_policies 
            WHERE 1=1
            """
            params = []

            if policy_types:
                placeholders = ", ".join(["%s"] * len(policy_types))
                query += f" AND type IN ({placeholders})"
                params.extend(policy_types)

            if min_premium is not None:
                query += " AND premium >= %s"
                params.append(min_premium)

            if max_premium is not None:
                query += " AND premium <= %s"
                params.append(max_premium)

            if min_coverage is not None:
                query += " AND coverage >= %s"
                params.append(min_coverage)

            if sort_by_premium:
                if sort_by_premium.lower() == "asc":
                    query += " ORDER BY premium ASC"
                elif sort_by_premium.lower() == "desc":
                    query += " ORDER BY premium DESC"

            query += " LIMIT %s OFFSET %s"
            params.extend([limit, offset])
            self.cursor.execute(query, tuple(params))
            return [row[0] for row in self.cursor.fetchall()]

    def close_db_connection(self):
        self.db.close_connection()