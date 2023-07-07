frappe.pages['company-declarations'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Company Declarations',
        single_column: true
    });

	// frappe.require("/assets/my_module/css/my_page.css");
	// then add this to hooks.py
	// app_include_js = "assets/js/my_module.min.js"

    // Get company name from URL
    var companyid = frappe.utils.get_url_arg('company');

    function fetchHTML() {
        frappe.call({
            method: 'my_app.my_app.page.company_declarations.company_declarations.get_page_content',
            args: { 'companyid': companyid},
            callback: function(response) {
                $(wrapper).find('.layout-main').html(response.message);
            }
        });
    }

    fetchHTML();


    $(wrapper).on('click', '#my_appLinkFirstPage', function() {
        window.location.href = '/app/fcustom-page';
    });

	// Add event listener for the Go to Other Page button
	$(wrapper).on('click', '#my_appLinkDeclarationDetails', function() {
		var declarationname = $(this).data('declaration-name');
		// console.log("company name: ", companyname);
		window.location.href = '/app/declaration-details?declaration='+declarationname;
	});
}