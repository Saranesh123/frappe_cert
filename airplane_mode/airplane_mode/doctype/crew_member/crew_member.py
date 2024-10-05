# Copyright (c) 2024, Saranesh and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CrewMember(Document):
	def before_save(self):
		self.full_name = " ".join([self.first_name, self.last_name])