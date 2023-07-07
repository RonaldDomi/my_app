frappe.pages['upload'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Upload Page',
        single_column: true
    });

	function fetchHTML() {
        frappe.call({
            method: 'my_app.my_app.page.upload.upload.get_page_content',
            args: { },
            callback: function(response) {
                $(wrapper).find('.layout-main').html(response.message);
            }
        });
    }

    fetchHTML();

    $(wrapper).on('submit', '#update-form', function(e) {
        e.preventDefault();
    
        // get the selected document and the file
        var docname = frappe.utils.get_url_arg('declarationd-detail');

        var file = $('#file-input')[0].files[0];
    
        // if (file) {
        if (true) {
            // upload the file
            let data = new FormData();
            data.append('file', file);
            data.append('doctype', 'MyAppDeclarationDetails');
            data.append('docname', docname);
            data.append('is_private', 0);  // or 1 for a private file

            $.ajax({
                type: 'POST',
                url: '/api/method/my_app.my_app.page.upload.upload.upload_file',
                data: data,
                processData: false,
                contentType: false,
                headers: {
                    'X-Frappe-CSRF-Token': frappe.csrf_token
                },
                success: function(data) {
                    alert("File uploaded successfully");
                },
                error: function(error) {
                    console.error("Error uploading file", error);
                }
            });
            
        }
    });

};