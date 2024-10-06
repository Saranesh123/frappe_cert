# Copyright (c) 2024, Saranesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.contacts.address_and_contact import (
    delete_contact_and_address,
    load_address_and_contact,
)


class Tenant(Document):
    def before_save(self):
        self.full_name = " ".join([self.first_name, self.last_name])
        
    def after_insert(self):
        self.update_address_link()
        self.update_contact_link()
        
    def update_address_link(self):
        address = frappe.get_doc("Address", self.address)
        address_link_names = [x.link_name for x in address.links]
        if self.name not in address_link_names:
            address.append("links", {
				"link_doctype": self.doctype,
				"link_name": self.name
			})
            
            address.save(ignore_permissions=True)
            
    def update_contact_link(self):
        contact = frappe.get_doc("Contact", self.contact)
        contact_link_names = [x.link_name for x in contact.links]
        if self.name not in contact_link_names:
            contact.append("links", {
				"link_doctype": self.doctype,
				"link_name": self.name
			})
            
            contact.save(ignore_permissions=True)
        
    def onload(self):
        load_address_and_contact(self)