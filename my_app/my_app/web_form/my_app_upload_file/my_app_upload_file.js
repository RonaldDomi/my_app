// inside your_form_name.js
frappe.ready(function() {

    // Bind the submit button click event
    $('.submit-btn').on('click', function() {
        updateDeclaration();
    });

    // Function to update the declaration document
    function updateDeclaration() {
        var formValues = $('.web-form').serializeArray();
        console.log("formValues: ", formValues);
        // var declaration = $('input[name="myapp_declaration"]').val();

        // frappe.call({
        //     method: 'my_custom_module.my_custom_module.doctype.my_app_declaration_details.my_app_declaration_details.update_declaration',
        //     args: {
        //         declaration: declaration,
        //         form_values: formValues
        //     },
        //     callback: function(response) {
        //         if (response.message) {
        //             frappe.show_alert('Declaration details updated successfully.');
        //         }
        //     }
        // });
    }
});