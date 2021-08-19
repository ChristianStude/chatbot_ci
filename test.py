import unittest
import main

# loading settings from .env file in root of project directory
from dotenv import load_dotenv
load_dotenv()

class grafanaTests(unittest.TestCase):
    """Tests for GeekTechStuff Grafana API Python"""

    def test_admin_name_is_string(self):
        admin_username = main.get_username()
        self.assertIs(type(admin_username),str)
    
    def test_admin_password_is_string(self):
        admin_password = main.get_password()
        self.assertIs(type(admin_password),str)
    
    def test_grafana_url_is_string(self):
        grafana_url = main.get_url()
        self.assertIs(type(grafana_url),str)
    
    def test_grafana_admin_url_is_string(self):
        admin_url = main.create_url()
        self.assertIs(type(admin_url),str)
    
if __name__ == '__main__':
    unittest.main()
