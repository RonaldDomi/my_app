import frappe

# @frappe.whitelist()
# def get_data():
#     doctype = 'tabMyAppCompany'
    
#     data = frappe.db.sql("""
#         SELECT * FROM `%s`
#     """ % doctype, as_dict=True)
#     dataNames = [companyObject.companyname for companyObject in data]
#     return dataNames

@frappe.whitelist()
def get_page_content():
    companies = frappe.get_all('MyAppCompany', fields=['*'])
    print("companies: ", companies)
    context = {
        "companies": companies,
    }
    return frappe.render_template('my_app/page/fcustom_page/fcustom_page.html', context)

@frappe.whitelist()
def add_company(companyname):
    company = frappe.get_doc({
        'doctype': 'MyAppCompany',
        'companyname': companyname
    })
    company.insert(ignore_permissions=True)

@frappe.whitelist()
def delete_company(companyname):
    frappe.delete_doc('MyAppCompany', companyname, ignore_permissions=True)
