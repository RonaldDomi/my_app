import frappe
# import base64
# from frappe.utils.file_manager import save_file

@frappe.whitelist()
def get_page_content(declarationid):
    declaration_details = frappe.get_all('MyAppDeclarationDetails', filters={'declarationid': declarationid}, fields=['*'])
    
    declaration = frappe.get_doc('MyAppCompanyDeclarationType', declaration_details[0].declarationid)
    for detail in declaration_details:
        detail["declarationtype_name"] = declaration.declarationtype_name

    # print("Declarations Details after update", declaration_details)
    return frappe.render_template('my_app/page/declaration_details/declaration_details.html', { 'declaration_details': declaration_details })

@frappe.whitelist()
def upload_file():
    print("UPLOAD FILE")
    print(frappe.request.files)
    print(frappe.request.form)
    print(frappe.request.form.get("doctype"))
    # print(frappe.request.files['docname'])
    if 'file' in frappe.request.files:
        file = frappe.request.files['file']
        print("filename: ", file.filename)
        docname = frappe.request.form.get("docname")
        doctype = frappe.request.form.get('doctype')
        is_private = frappe.request.form.get('is_private')

        # Get the file from the FormData object
        doc = frappe.get_doc(doctype, docname)

        # Create a new File document and link it to the document
        attached_file = frappe.get_doc({
            "doctype": "File",
            "file_name": file.filename,
            "attached_to_doctype": doctype,
            "attached_to_name": docname,
            "is_private": is_private
        })
        attached_file.save()

        # Link the File document with the doc
        doc.append('declarationdetail_file', {
            'file': attached_file.name
        })
        doc.save()

        return "File uploaded successfully"
    else:
        return "No file in request"



@frappe.whitelist()
def upload_file3():
    # print(frappe.request.files['docname'])
    if 'file' in frappe.request.files:
        print("UPLOAD FILE")
        print(frappe.request.files)
        print(frappe.request.form)
        print(frappe.request.form.get("doctype"))
        my_file = frappe.request.files['file']
        print("filename: ", my_file.filename)
        docname = frappe.request.form.get("docname")
        doctype = frappe.request.form.get('doctype')
        is_private = frappe.request.form.get('is_private')
        print("doctype: ", doctype)
        print("docname: ", docname)

        # Get the file from the FormData object
        doc = frappe.get_doc(doctype, docname)

        # file_doc = frappe.get_doc({
        #     "doctype": "File",
        #     "file_name": my_file.filename,
        #     "attached_to_doctype": doctype,
        #     "attached_to_name": docname,
        #     "is_private": is_private
        # })
        # print("file_doc: ", file_doc)
        print("my_file: ", my_file)
        # print("my_file.url: ", my_file.file_url)
        # file_doc.save()
        # Use Frappe's inbuilt file uploader to save the file.
        file_doc = frappe.upload_file(my_file.filename, my_file.read(), doctype, docname, is_private)
        print("file_doc: ", file_doc)
        print("file_doc filename: ", file_doc.file_name)
        print("file_doc url: ", file_doc.file_url)
        # doc.declarationdetail_file = file_doc 
        doc.declarationdetail_file = file_doc.file_url

        # doc.declarationdetail_file = file_data
        # doc.file_url = file_url

        # Save the updated document
        doc.save()

        return "File uploaded successfully"
    else:
        return "No file in request"

@frappe.whitelist()
def upload_file2():
    # print(frappe.request.files['docname'])
    if 'file' in frappe.request.files:
        print("UPLOAD FILE")
        print(frappe.request.files)
        print(frappe.request.form)
        print(frappe.request.form.get("doctype"))
        my_file = frappe.request.files['file']
        print("filename: ", my_file.filename)
        docname = frappe.request.form.get("docname")
        doctype = frappe.request.form.get('doctype')
        is_private = frappe.request.form.get('is_private')
        print("doctype: ", doctype)
        print("docname: ", docname)

        # Get the file from the FormData object
        doc = frappe.get_doc(doctype, docname)

        file_doc = frappe.get_doc({
            "doctype": "File",
            "file_name": my_file.filename,
            "attached_to_doctype": doctype,
            "attached_to_name": docname,
            "is_private": is_private
        })
        print("file_doc: ", file_doc)
        print("filename doctype: ", file_doc.file_name)
        print("my_file: ", my_file)
        print("my_file.url: ", my_file.file_url)
        file_doc.save()
        print("file url: ", file_doc.file_url)
        # Use Frappe's inbuilt file uploader to save the file.
        # file_doc = frappe.upload_file(my_file.filename, my_file.read(), doctype, docname, is_private)
        # doc.declarationdetail_file = file_doc 
        doc.declarationdetail_file = file_doc.file_url

        # doc.declarationdetail_file = file_data
        # doc.file_url = file_url

        # Save the updated document
        doc.save()

        return "File uploaded successfully"
    else:
        return "No file in request"