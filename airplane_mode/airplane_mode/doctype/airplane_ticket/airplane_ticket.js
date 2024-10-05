// Copyright (c) 2024, Saranesh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
        if (frm.doc.docstatus == 0) {
            frm.add_custom_button(__("Assign Seat"), () => {
                let d = new frappe.ui.Dialog({
                    title: 'Assign Seat',
                    fields: [
                        {
                            label: "Seat",
                            fieldname: "seat",
                            fieldtype: "Data",
                            reqd: 1
                        },
                    ],
                    size: "small",
                    primary_action_label: "Assign Seat",
                    primary_action(values) {
                        frm.set_value("seat", values.seat);
                        d.hide();
                    }
                });
                
                d.show();
            }, __("Actions"))
        }
	},
});
