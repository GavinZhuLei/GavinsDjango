/**
 * Created by 磊 on 2015/3/18.
 */
var UserTableAjax = function () {

    var initPickers = function () {
        //init date pickers
        $('.date-picker').datepicker({
            rtl: Metronic.isRTL(),
            autoclose: true
        });
    }

    var handleRecords = function () {

        var grid = new Datatable();

        grid.init({
            src: $("#datatable_ajax"),
            onSuccess: function (grid) {
                // execute some code after table records loaded
                console.log("success")
            },
            onError: function (grid) {
                // execute some code on network or other general error
                console.log("error")
            },
            onDataLoad: function(grid) {
                // execute some code on ajax data load
                console.log("load")
            },
            loadingMessage: 'Loading...',
            dataTable: { // here you can define a typical datatable settings from http://datatables.net/usage/options

                // Uncomment below line("dom" parameter) to fix the dropdown overflow issue in the datatable cells. The default datatable layout
                // setup uses scrollable div(table-scrollable) with overflow:auto to enable vertical scroll(see: assets/global/scripts/datatable.js).
                // So when dropdowns used the scrollable div should be removed.
                //"dom": "<'row'<'col-md-8 col-sm-12'pli><'col-md-4 col-sm-12'<'table-group-actions pull-right'>>r>t<'row'<'col-md-8 col-sm-12'pli><'col-md-4 col-sm-12'>>",

                "bStateSave": true, // save datatable state(pagination, sort, etc) in cookie.

                "lengthMenu": [
                    [10, 20, 50, 100, 150, -1],
                    [10, 20, 50, 100, 150, "All"] // change per page values here
                ],
                "pageLength": 10, // default record count per page
                "ajax": {
                    "url": "/admin/user/data/", // ajax source
                    //"data":function(){
                    //
                    //}
                },
                "order": [
                    [1, "asc"]
                ]// set first column as a default sort by asc
            }
        });

        // handle group actionsubmit button click
        grid.getTableWrapper().on('click', '.table-group-action-submit', function (e) {

            e.preventDefault();
            var action = $(".table-group-action-input", grid.getTableWrapper());
            if (action.val() != "" && grid.getSelectedRowsCount() > 0) {
                grid.setAjaxParam("customActionType", "group_action");
                grid.setAjaxParam("customActionName", action.val());
                grid.setAjaxParam("id", grid.getSelectedRows());
                grid.getDataTable().ajax.reload();
                grid.clearAjaxParams();
            } else if (action.val() == "") {
                Metronic.alert({
                    type: 'danger',
                    icon: 'warning',
                    message: '请选择一个操作',
                    container: grid.getTableWrapper(),
                    place: 'prepend'
                });
            } else if (grid.getSelectedRowsCount() === 0) {
                Metronic.alert({
                    type: 'danger',
                    icon: 'warning',
                    message: '没有选中的记录',
                    container: grid.getTableWrapper(),
                    place: 'prepend'
                });
            }
        });

        var $modal = $('#user-edit-modal');
        var $groupModal = $('#user-group-modal')



        $('body').delegate('#user-edit-modal','hide.bs.modal',function(e){
            grid.getDataTable().ajax.reload();
        })

        $('#datatable_ajax').delegate('.btn-disable','click',function(e) {
            Metronic.blockUI({
                                message: 'Loading...',
                                target: $('#datatable_ajax'),
                                overlayColor: 'none',
                                cenrerY: true,
                                boxed: true
                            });

            console.log('disable')
            var pk = $(this).attr('data-id');
            console.log(pk)
            //grid.getDataTable().ajax.reload();

            $thisSateTd = $(this).parent().prev();

            $thisAction = $(this);

            $.ajax({
                url:'/admin/user/disable/'+pk+'/',
                type:'POST',
                success:function(data){
                    Metronic.unblockUI($('#datatable_ajax'));
                    data = $.parseJSON(data);
                    if(data.success){
                        //禁用成功
                        $thisSateTd.html('<span class="label label-sm label-default">禁用</span>');
                        $thisAction.removeClass('btn-disable').addClass('btn-enable').html('<i class="fa fa-unlock-alt"></i>启用');
                    }else{
                        alert('fail')
                    }
                }
            })
        });

        $('#datatable_ajax').delegate('.btn-enable','click',function(e) {
            Metronic.blockUI({
                                message: 'Loading...',
                                target: $('#datatable_ajax'),
                                overlayColor: 'none',
                                cenrerY: true,
                                boxed: true
                            });

            console.log('enable')
            var pk = $(this).attr('data-id');
            console.log(pk)
            //grid.getDataTable().ajax.reload();

            $thisSateTd = $(this).parent().prev();

            $thisAction = $(this);

            $.ajax({
                url:'/admin/user/enable/'+pk+'/',
                type:'POST',
                success:function(data){
                    Metronic.unblockUI($('#datatable_ajax'));
                    data = $.parseJSON(data);
                    if(data.success){
                        //禁用成功
                        $thisSateTd.html('<span class="label label-sm label-success">正常</span>');
                        $thisAction.removeClass('btn-enable').addClass('btn-disable').html('<i class="fa  fa-lock"></i>禁用');
                    }else{
                        alert('fail')
                    }
                }
            })
        });
    }



    return {

        //main function to initiate the module
        init: function () {

            initPickers();
            handleRecords();
        }

    };

}();

