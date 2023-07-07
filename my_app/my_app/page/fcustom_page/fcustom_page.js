
frappe.pages['fcustom-page'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Company List',
        single_column: true
    });

	// frappe.require("/assets/my_module/css/my_page.css");
	// then add this to hooks.py
	// app_include_js = "assets/js/my_module.min.js"

    function fetchHTML() {
        frappe.call({
            method: 'my_app.my_app.page.fcustom_page.fcustom_page.get_page_content',
            args: {},
            callback: function(response) {
                $(wrapper).find('.layout-main').html(response.message);
            }
        });
    }

    fetchHTML();

    // // Add event listener for the Go to Other Page button
    // $(wrapper).on('click', '#my_appLinkUploadPage', function() {
    //     window.location.href = '/app/upload';
    // });

    // Add event listener for the Go to Other Page button
    $(wrapper).on('click', '#my_appLinkCompanyDeclarations', function() {
        var companyname = $(this).data('company-name');
        // console.log("company name: ", companyname);
        window.location.href = '/app/company-declarations?company='+companyname;
    });

     // Add event listener for the Add Company button
    $(wrapper).on('click', '#my_appAddCompanyButton', function() {
        var newCompanyName = $('#my_appNewCompanyName').val();    

        frappe.call({
            method: 'my_app.my_app.page.fcustom_page.fcustom_page.add_company',
            args: {
                'companyname': newCompanyName
            },
            callback: function(response) {
                fetchHTML();
                $('#my_appNewCompanyName').val('');  // clear the input field
            }
        });
    });

     // Add event listener for the Delete Company button
    $(wrapper).on('click', '.my_appDeleteCompanyButton', function(event) {
        // as to not trigger the card event to go the company details

        event.stopPropagation()
        var companyname = $(this).data('company-name');
        console.log("companyname: ", companyname);
        frappe.call({
            method: 'my_app.my_app.page.fcustom_page.fcustom_page.delete_company',
            args: {
                'companyname': companyname
            },
            callback: function(response) {
                fetchHTML();
            }
        });
    });
}