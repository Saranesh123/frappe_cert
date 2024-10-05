# Copyright (c) 2024, Saranesh and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	columns = [
		_("Airline") + ":Link/Airline: 150",
		_("Revenue") + ":Currency: 200",
	]
 
	data = frappe.db.sql(
		"""
		SELECT
			ta2.name airline,
			SUM(tat.total_amount) revenue
		FROM
			`tabAirplane` ta
		LEFT JOIN `tabAirline` ta2 ON
			ta2.name = ta.airline
		LEFT JOIN `tabAirplane Flight` taf ON
			taf.airplane = ta.name
			AND taf.docstatus = 1
		LEFT JOIN `tabAirplane Ticket` tat ON
			tat.flight = taf.name
			AND tat.docstatus = 1
		GROUP BY
			ta2.name
		ORDER BY
			ta2.name
		""", as_dict=True
		)
 
	report_summary = [
		{"value": sum(row.revenue for row in data if row.revenue), "label": "Total Revenue", "datatype": "Currency", "indicator": "Green"}
	]
 
	chart = {
		"data": {"labels": [x.airline for x in data], "datasets": [{"values": [x.revenue for x in data]}]},
		"type": "donut",
		"height": 300,
	}
 
	return columns, data, None, chart, report_summary