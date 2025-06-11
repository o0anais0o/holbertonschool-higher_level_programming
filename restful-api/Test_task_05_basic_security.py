import unittest
from flask import Flask
from flask_jwt_extended import create_access_token
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from task_05_basic_security import app

class AdminOnlyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def get_jwt_headers(self, username, role):
        with self.app.app_context():
            token = create_access_token(identity=username, additional_claims={"role": role})
        return {"Authorization": f"Bearer {token}"}

    def test_admin_access_granted(self):
        headers = self.get_jwt_headers("admin", "admin")
        response = self.client.get('/admin-only', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Admin Access: Granted", response.data)

    def test_non_admin_access_denied(self):
        headers = self.get_jwt_headers("user", "user")
        response = self.client.get('/admin-only', headers=headers)
        self.assertEqual(response.status_code, 403)
        self.assertIn(b"Admin access required", response.data)

    def test_missing_jwt(self):
        response = self.client.get('/admin-only')
        self.assertEqual(response.status_code, 401)  # Missing Authorization header

if __name__ == '__main__':
    unittest.main()
