# Copyright (c) 2024, Saranesh and contributors
# For license information, please see license.txt

import frappe, random
from frappe import _
from frappe.model.document import Document


class AirplaneTicket(Document):
    def validate(self):
        total_amount, add_ons = 0, []
        
        for add_on in self.add_ons:
            if add_on.item not in add_ons:
                add_ons.append(add_on.item)
                total_amount += add_on.amount
            else:
                self.add_ons.remove(add_on)
            
        self.total_amount = float(self.flight_price) + total_amount
        
    def before_insert(self):
        self.validate_seat_capacity()
        
        self.seat = f"{random.randint(1, 99)}{random.choice(['A', 'B', 'C', 'D', 'E'])}"
        
    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw(_("The Passenger has not been Boarded!"))
            
        frappe.db.set_value("Airplane Flight", self.flight, "status", "Completed")
        
    def validate_seat_capacity(self):
        capacity = int(frappe.db.sql(
            """
            SELECT
                ta.capacity
            FROM
                `tabAirplane Flight` taf
            INNER JOIN `tabAirplane` ta ON
                ta.name = taf.airplane
            WHERE
                taf.name = %s
            """, (self.flight)
        )[0][0])
        
        tickets_booked = frappe.db.count("Airplane Ticket", {"docstatus": 1, "flight": self.flight})
        
        if tickets_booked >= capacity:
            frappe.throw("Maximum Flight Capacity Reached")