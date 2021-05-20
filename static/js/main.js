"use strict"
$(document).ready(function() {
  document.getElementById("mesaj_rezultat").style.display = "none";

            // $('#mesaj_rezultat').style.display ="none";	
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
  document.getElementById("mesaj_rezultat").style.display = "block";

		});

		event.preventDefault();

	});
});