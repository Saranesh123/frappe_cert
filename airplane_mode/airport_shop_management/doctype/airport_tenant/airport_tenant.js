// Copyright (c) 2024, Saranesh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airport Tenant", {
	address(frm) {
        frappe.call({
            method: "frappe.contacts.doctype.address.address.get_address_display",
            args: {
                address_dict: frm.doc.address,
            },
            callback: function (r) {
                frm.set_value("address_display", r.message);
            },
        });
	},

    setup(frm) {
        frm.set_query("address", () => {
			return {
				filters: {
					link_doctype: frm.doc.doctype,
					link_name: frm.doc.name,
				},
			};
		});

        frm.set_query("contact", () => {
			return {
				filters: {
					link_doctype: frm.doc.doctype,
					link_name: frm.doc.name,
				},
			};
		});
    },

    refresh(frm) {
        frappe.dynamic_link = {doc: frm.doc, fieldname: frm.doc.address, doctype: frm.doc.doctype};
        frm.toggle_display(['address_html','contact_html'], !frm.doc.__islocal);
        if(!frm.doc.__islocal) {
            frappe.contacts.render_address_and_contact(frm);
        } else {
            frappe.contacts.clear_address_and_contact(frm);
        }   
    }
});
