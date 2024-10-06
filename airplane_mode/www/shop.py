import frappe

def get_context(context):
    context.shops = frappe.get_list("Shop", {"status": "available"}, ["image", "shop_number", "airport"])
    
    context.company = "All Services Served"
    
    return context