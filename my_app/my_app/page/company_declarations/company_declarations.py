import frappe

@frappe.whitelist()
def get_page_content(companyid):
    company_declarations = frappe.get_all('MyAppCompanyDeclarationType', filters={'companyid': companyid}, fields=['*'])
    print("CompanyDeclarations: ", company_declarations)
    
    company = frappe.get_doc('MyAppCompany', company_declarations[0].companyid)
    print("company got: ", company)
    for declaration in company_declarations:
        declaration["companyname"] = company.companyname  # Assuming 'company_name' is a field in your Company DocType

    print("Company Declarations after update", company_declarations)
    return frappe.render_template('my_app/page/company_declarations/company_declarations.html', { 'company_declarations': company_declarations })