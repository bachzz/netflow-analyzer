(function ($) {
	"use strict";
	$('.column100').on('mouseover',function(){
		var table1 = $(this).parent().parent().parent();
		var table2 = $(this).parent().parent();
		var verTable = $(table1).data('vertable')+"";
		var column = $(this).data('column') + ""; 

		$(table2).find("."+column).addClass('hov-column-'+ verTable);
		$(table1).find(".row100.head ."+column).addClass('hov-column-head-'+ verTable);
	});

	$('.column100').on('mouseout',function(){
		var table1 = $(this).parent().parent().parent();
		var table2 = $(this).parent().parent();
		var verTable = $(table1).data('vertable')+"";
		var column = $(this).data('column') + ""; 

		$(table2).find("."+column).removeClass('hov-column-'+ verTable);
		$(table1).find(".row100.head ."+column).removeClass('hov-column-head-'+ verTable);
	});
    

    /*Dropdown Menu*/
    $('.dropdown').click(function () {
            $(this).attr('tabindex', 1).focus();
            $(this).toggleClass('active');
            $(this).find('.dropdown-menu').slideToggle(300);
        });
        $('.dropdown').focusout(function () {
            $(this).removeClass('active');
            $(this).find('.dropdown-menu').slideUp(300);
        });
        $('.dropdown .dropdown-menu li').click(function () {
            $(this).parents('.dropdown').find('span').text($(this).text());
            $(this).parents('.dropdown').find('input').attr('value', $(this).attr('id'));
        });
    /*End Dropdown Menu*/


    $('.dropdown-menu li').click(function () {
      var input = $(this).parents('.dropdown').find('input').val() ;
      console.log(input);
    });


//    $('.radio-status-ok').click(function(){
//        console.log("ok clicked!");
//    })

    $('.agent-status').each(function(i, obj) {
        var new_src = "/static/images/ok.png";
        if($(this).children(".status").children(".toggle-radio").children(".radio-status-not-ok").is(':checked')){
            new_src = "/static/images/not_ok.png";
        }

        $(this).children(".screen").children("img").prop('src', new_src);
    });

    $( ".agent-status" ).change(function() {
        var new_src = "/static/images/ok.png";
        if($(this).children(".status").children(".toggle-radio").children(".radio-status-not-ok").is(':checked')){
            new_src = "/static/images/not_ok.png";
        }

        $(this).children(".screen").children("img").prop('src', new_src);
    });


})(jQuery);