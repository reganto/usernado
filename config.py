import os.path

ROOT = os.path.dirname(os.path.abspath(__file__))
add_path = lambda *args: os.path.join(ROOT, *args)

SETTINGS = dict(
        template_path=add_path('templates'),
        cookie_secret=os.urandom(16),
        )

