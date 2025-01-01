import xmlrpc.client

ODOO_URL = "http://odoo-server:8069"
DB = "my_db"
USERNAME = "admin"
PASSWORD = "password"

def get_odoo_client():
    """
    Tworzy połączenie z Odoo.
    """
    common = xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/common")
    uid = common.authenticate(DB, USERNAME, PASSWORD, {})
    models = xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/object")
    return uid, models

def create_or_update_partner(partner_data):
    """
    Tworzy lub aktualizuje partnera w Odoo.
    """
    uid, models = get_odoo_client()
    existing_partner = models.execute_kw(
        DB, uid, PASSWORD,
        'res.partner', 'search_read',
        [[['email', '=', partner_data['email']]]], {'limit': 1}
    )
    if existing_partner:
        partner_id = existing_partner[0]['id']
        models.execute_kw(DB, uid, PASSWORD, 'res.partner', 'write', [[partner_id], partner_data])
    else:
        models.execute_kw(DB, uid, PASSWORD, 'res.partner', 'create', [partner_data])
