# Copyright (c) 2023, Publishehr and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class MyAppDeclarationDetails(Document):
	def on_submit(self):
		print("ON SAVE")
