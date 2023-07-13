frappe.pages['declaration-details'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Declaration Details',
        single_column: true
    });

	// frappe.require("/assets/my_module/css/my_page.css");
	// then add this to hooks.py
	// app_include_js = "assets/js/my_module.min.js"

    // Get company name from URL
    var declarationid = frappe.utils.get_url_arg('declaration');

    function fetchHTML() {
        frappe.call({
            method: 'my_app.my_app.page.declaration_details.declaration_details.get_page_content',
            args: { 'declarationid': declarationid},
            callback: function(response) {
                $(wrapper).find('.layout-main').html(response.message);
            }
        });
    }

    fetchHTML();

    $(wrapper).on('submit', '#update-form', function(e) {
        e.preventDefault();
    
        // get the selected document and the file
        var docname = $(this).data('declaration-detail-name');
        var file = $(this).find('input[type=file]')[0].files[0];
        
        if (file) {
            console.log('file not null')
            // upload the file
            let data = new FormData();
            data.append('file', file);
            data.append('doctype', 'MyAppDeclarationDetails');
            data.append('docname', docname);
            data.append('is_private', 0);  // or 1 for a private file
            // console.log("filename: ", file)
            $.ajax({
                type: 'POST',
                url: '/api/method/my_app.my_app.page.declaration_details.declaration_details.upload_file2',
                data: data,
                processData: false,
                contentType: false,
                headers: {
                    'X-Frappe-CSRF-Token': frappe.csrf_token
                },
                success: function(data) {
                    console.log('data returned on success: ', data)
                    alert("File uploaded successfully");
                },
                error: function(error) {
                    console.error("Error uploading file", error);
                }
            });
            
        }
    });


}