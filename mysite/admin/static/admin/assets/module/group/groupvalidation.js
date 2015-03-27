/**
 * Created by Gavin on 2015/3/27.
 */
var GroupFormValidation = function () {

    // validation using icons
    var handleValidation = function() {
        // for more info visit the official plugin documentation:
            // http://docs.jquery.com/Plugins/Validation

            var form2 = $('#form_sample_2');
            var error2 = $('.alert-danger', form2);
            var success2 = $('.alert-success', form2);
            var $modal = $('#user-edit-modal');

            form2.validate({
                errorElement: 'span', //default input error message container
                errorClass: 'help-block help-block-error', // default input error message class
                focusInvalid: false, // do not focus the last invalid input
                ignore: "",  // validate all fields including form hidden input
                rules: {
                    username: {
                        minlength: 2,
                        maxlength: 50,
                        required: true
                    },
                    email: {
                        required: true,
                        email: true
                    },
                    phone: {
                        required: true
                    },
                    password: {
                        required: true
                    },
                    repassword: {
                        required: true,
                        equalTo: "#j_password"
                    },
                },

                invalidHandler: function (event, validator) { //display error alert on form submit
                    success2.hide();
                    error2.show();
                    Metronic.scrollTo(error2, -200);
                },

                errorPlacement: function (error, element) { // render error placement for each input type
                    var icon = $(element).parent('.input-icon').children('i');
                    icon.removeClass('fa-check').addClass("fa-warning");
                    icon.attr("data-original-title", error.text()).tooltip({'container': icon});
                },

                highlight: function (element) { // hightlight error inputs
                    $(element)
                        .closest('.form-group').removeClass("has-success").addClass('has-error'); // set error class to the control group
                },

                unhighlight: function (element) { // revert the change done by hightlight

                },

                success: function (label, element) {
                    var icon = $(element).parent('.input-icon').children('i');
                    $(element).closest('.form-group').removeClass('has-error').addClass('has-success'); // set success class to the control group
                    icon.removeClass("fa-warning").addClass("fa-check");
                },

                submitHandler: function (form) {
                    //success2.show();
                    //error2.hide();


                    $modal.modal('loading');
                    console.log($(form).serializeArray())

                    $.ajax({
                        url:'/admin/user/update/',
                        type:'post',
                        data: $(form).serializeArray(),
                        success:function(data){
                            data = $.parseJSON(data);
                            if(data.success){
                                setTimeout(function(){

                                      $modal.load('/admin/user/edit/'+data.pk+'/', '', function(){
                                          error2.hide();
                                          $modal.modal('loading')
                                      .find('.modal-body')
                                        .prepend('<div class="alert alert-info fade in">' +
                                          'Updated!<button type="button" class="close" data-dismiss="alert">&times;</button>' +
                                        '</div>');
                                    });
                                  }, 1000);
                            }else{
                                setTimeout(function(){
                                      $modal.modal('loading');
                                        error2.show();
                                  }, 1000);
                            }
                        }
                    });
                }
            });
    }


    return {
        //main function to initiate the module
        init: function () {
            handleValidation();

        }

    };

}();
