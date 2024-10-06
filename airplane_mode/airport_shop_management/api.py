import frappe
from frappe.utils import today

def send_email_reminder():
    shop_settings = frappe.get_single("Shop Settings")
    if shop_settings.send_rent_reminders:
            shop_contract = frappe.db.sql(
                """
                SELECT
                    email,
                    tenant_name,
                    rent_amount
                FROM
                    `tabShop Contract`
                WHERE
                    docstatus = 1
                    AND is_active = 1
                    AND contract_start_date < %s
                    AND contract_end_date > %s
                """, (today(), today()), as_dict=1
            )
            
            sender = frappe.get_value("Email Account", shop_settings.email, "email_id")
            
            for shop in shop_contract:
                msg = f"Dear {shop.tenant_name},<br><br>Your Rent Payment is due on {today()}"
                frappe.sendmail(recipients=[shop.email], message=msg, subject="Rent Payment Reminder", sender=sender)
    
def change_shop_status():
    contracts = frappe.get_list("Shop Contract", {"is_ative": 1, "contract_end_date": ("<", today())}, ["name", "shop"])
    
    for contract in contracts:
        frappe.db.set_value("Shop Contract", contract.name, "is_active", 0)
        frappe.db.set_value("Shop", contract.shop, "status", "Available")