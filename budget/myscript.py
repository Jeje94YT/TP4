import os

badhash = os.getenv('BAD_HASH')
goodhash = os.getenv('GOOD_HASH')

os.system(f"git bisect start {badhash} {goodhash}")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")

