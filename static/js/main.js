"use strict"
$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
	            letters : $('#text_box').val(),
                len : $('#number_box').val()
            },
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {
            $('#rezultat').text(data.result).show();			
		});

		event.preventDefault();

	});
});