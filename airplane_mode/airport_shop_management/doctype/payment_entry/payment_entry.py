# Copyright (c) 2024, Saranesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import get_first_day, get_last_day


class PaymentEntry(Document):
    def before_insert(self):
        self.set_dates()
        
        if frappe.db.exists("Payment Entry", {"docstatus": 1, "start_date": self.start_date, "end_date": self.end_date}):
            frappe.throw("Rent Payment done for this month!")
            
    def before_save(self):
        self.set_dates()
            
    def set_dates(self):
        self.start_date = get_first_day(self.start_date)
        self.end_date = get_last_day(self.start_date)