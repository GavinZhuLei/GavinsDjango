/**
 * Created by 磊 on 2015/3/18.
 */
var UserUIExtendedModals = function () {


    return {
        //main function to initiate the module
        init: function () {

            // general settings
            $.fn.modal.defaults.spinner = $.fn.modalmanager.defaults.spinner =
              '<div class="loading-spinner" style="width: 200px; margin-left: -100px;">' +
                '<div class="progress progress-striped active">' +
                  '<div class="progress-bar" style="width: 100%;"></div>' +
                '</div>' +
              '</div>';

            $.fn.modalmanager.defaults.resize = true;

            //dynamic demo:
            $('.dynamic .demo').click(function(){
              var tmpl = [
                // tabindex is required for focus
                '<div class="modal hide fade" tabindex="-1">',
                  '<div class="modal-header">',
                    '<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>',
                    '<h4 class="modal-title">Modal header</h4>',
                  '</div>',
                  '<div class="modal-body">',
                    '<p>Test</p>',
                  '</div>',
                  '<div class="modal-footer">',
                    '<a href="#" data-dismiss="modal" class="btn btn-default">Close</a>',
                    '<a href="#" class="btn btn-primary">Save changes</a>',
                  '</div>',
                '</div>'
              ].join('');

              $(tmpl).modal();
            });

            //ajax demo:
            var $modal = $('#user-edit-modal');
            var $groupModal = $('#user-group-modal')

            $('#j-adduser').on('click', function(){
              // create the backdrop and wait for next modal to be triggered
              $('body').modalmanager('loading');

              setTimeout(function(){
                  $modal.load('/admin/user/edit/0/', '', function(){
                  $modal.modal();
                });
              }, 500);
            });

            $('#datatable_ajax').delegate('.btn-editable','click',function(){
                console.log('this')
                $('body').modalmanager('loading');
                var editId = $(this).attr('data-id');
                  setTimeout(function(){
                      $modal.load('/admin/user/edit/'+editId+'/', '', function(){
                      $modal.modal();
                    });
                  }, 500);
            });

            /**
             * 选择用户组
             */
            $('#datatable_ajax').delegate('.btn-editgroup','click',function(){
                $('body').modalmanager('loading');
                var currentId = $(this).attr('data-id');
                setTimeout(function(){
                      $groupModal.load('/admin/user/group/'+currentId+'/', '', function(){
                      $groupModal.modal();
                    });
                }, 500);
            });


            $modal.on('click', '.update', function(){

                $('#form_sample_2').submit();
            });
        }

    };

}();
