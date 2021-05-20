"use strict"
$(document).ready(function() {

	// $('form').on('submit', function(event) {
  $('button').click(function(){
		$.ajax({
			data : {
	            letters : $('#text_box').val(),
                len : this.id
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