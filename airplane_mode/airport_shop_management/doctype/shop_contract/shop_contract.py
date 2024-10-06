# Copyright (c) 2024, Saranesh and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class ShopContract(Document):
    def before_submit(self):
        self.is_active = 1
        frappe.db.set_value("Shop", self.shop, "status", "Occupied")
        
    def on_cancel(self):
        frappe.db.set_value("Shop", self.shop, "status", "Available")