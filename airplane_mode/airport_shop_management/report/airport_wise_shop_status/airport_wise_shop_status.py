# Copyright (c) 2024, Saranesh and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	columns = [
		_("Airport") + ":Link/Airport: 150",
  		_("Available") + ":Int: 150",
		_("Occupied") + ":Int: 150",
		_("Total") + ":Int: 150",
	]
 
	data = frappe.db.sql(
		"""
		SELECT
			airport,
			SUM(IF(status = 'Available', 1, 0)) available,
			SUM(IF(status = 'Occupied', 1, 0)) occupied,
			COUNT(name) total
		FROM
			`tabShop`
		GROUP BY
			airport
  		"""
	)
 
	return columns, data
