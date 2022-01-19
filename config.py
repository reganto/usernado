import secrets
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SETTINGS = dict(

        # Directory containing template files.
        template_path=BASE_DIR / 'templates',

        # Directory from which static files will be served.
        static_path=BASE_DIR / 'static',

        # Used by RequestHandler.get_secure_cookie and set_secure_cookie to sign cookies.
        cookie_secret=secrets.token_bytes(),

        # Automatically restart the server when a source file is modified. 
        autoreload=True,
        )
