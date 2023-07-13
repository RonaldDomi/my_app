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

    company_id = company.name  # Retrieve the ID of the newly created company

    declaration_types = ["Blerje", "Shitje"]
    for i in range(2):
        company_declaration = frappe.get_doc({
            'doctype': 'MyAppCompanyDeclarationType',
            'companyid': company_id,  # Link the CompanyDetails to the newly created company
            'declarationtype_name': declaration_types[i]
        })
        company_declaration.insert(ignore_permissions=True)

        # add current month
        current_date = frappe.utils.today()
        current_month = frappe.utils.formatdate(current_date, "MM")  # Format the date to retrieve the full month name
        declaration_details = frappe.get_doc({
            'doctype': 'MyAppDeclarationDetails',
            'declarationid': company_declaration.name,  # Link the CompanyDetails to the newly created company
            'declarationdetail_periodstart': current_month
        })
        declaration_details.insert(ignore_permissions=True)
        
        
        # add next month
        next_month = get_next_month()
        declaration_details_2 = frappe.get_doc({
            'doctype': 'MyAppDeclarationDetails',
            'declarationid': company_declaration.name,  # Link the CompanyDetails to the newly created company
            'declarationdetail_periodstart': next_month
        })
        declaration_details_2.insert(ignore_permissions=True)
        

    return company

@frappe.whitelist()
def delete_company(companyname):
    frappe.delete_doc('MyAppCompany', companyname, ignore_permissions=True)

def get_next_month():
    current_date = frappe.utils.today()
    current_month = int(current_date[5:7])
    current_year = int(current_date[:4])

    next_month = current_month + 1
    next_year = current_year

    if next_month > 12:
        next_month = 1
        next_year += 1

    next_month_formatted = "{:02d}.{}".format(next_month, next_year)

    return next_month_formatted