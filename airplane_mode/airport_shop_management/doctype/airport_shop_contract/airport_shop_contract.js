// Copyright (c) 2024, Saranesh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airport Shop Contract", {
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
					link_doctype: "Airport Tenant",
					link_name: frm.doc.tenant,
				},
			};
		});

        frm.set_query("contact", () => {
			return {
				filters: {
					link_doctype: "Airport Tenant",
					link_name: frm.doc.tenant,
				},
			};
		});

        frm.set_query("shop", () => {
			return {
				filters: {
					airport: frm.doc.airport,
				},
			};
		});
    },
});
