import frappe
# from frappe.website.doctype.sweb_form.web_form import WebForm

def get_context(context):
    # modify context as needed
    return context

# class CustomWebForm(WebForm):
#     def save(self, ignore_permissions=False):
#         # Get the existing document to update
#         existing_doc = frappe.get_doc(self.doc.doctype, self.doc.name)
#         print("GOT HERE")
#         # Update the fields
#         # existing_doc.fieldname1 = self.doc.fieldname1
#         # existing_doc.fieldname2 = self.doc.fieldname2

#         # Save the changes
#         existing_doc.save(ignore_permissions=ignore_permissions)

#         return existing_doc