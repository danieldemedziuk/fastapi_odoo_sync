from celery import Celery
from app.nav_client import fetch_nav_data
from app.odoo_client import create_or_update_partner

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def fetch_and_sync_data():
    """
    Pobiera dane z NAV i zapisuje je w Odoo.
    """
    skip = 0
    top = 100
    while True:
        data = fetch_nav_data(skip=skip, top=top)
        if not data:
            break
        for record in data['value']:
            partner_data = {
                'name': record['Name'],
                'email': record.get('Email', ''),
                'phone': record.get('Phone', ''),
            }
            create_or_update_partner(partner_data)
        skip += top
