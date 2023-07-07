import frappe


@frappe.whitelist()
def get_page_content():
    context = {}
    uploads = frappe.get_all('MyAppDeclarationUpload', fields=["file"])
    
    context = {"uploads": uploads}
    print(context)
    return frappe.render_template('my_app/page/upload/upload.html', context)
 
@frappe.whitelist()
def upload_file():
    print("UPLOAD FILE")
    if 'file' in frappe.request.files:
        # file = frappe.request.files['file']
        # file_content = file.read()  # read the file content
        # # ... now you can process the file_content as per your requirements
        return "File uploaded successfully"
    else:
        return "No file in request"