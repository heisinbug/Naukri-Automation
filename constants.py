# Configuration and constants used in the script. Update values as needed.
import os

USERNAME = os.getenv("NAUKRI_USERNAME")
PASSWORD = os.getenv("NAUKRI_PASSWORD")
MOBILE = os.getenv("NAUKRI_MOBILE")
ORIGINAL_RESUME_PATH = "resumes/aryan_old.pdf"
MODIFIED_RESUME_PATH = "resumes/aryan_devops.pdf"

# Other constants
NAUKRI_LOGIN_URL = "https://www.naukri.com/nlogin/login"
NAUKRI_PROFILE_URL = "https://www.naukri.com/mnjuser/profile"