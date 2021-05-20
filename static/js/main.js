"use strict"
$(document).ready(function() {

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
            
            if(data.result.length > 1)
              document.getElementById("mesaj_rezultat").innerHTML = "Solutiile sunt:";
            else
              document.getElementById("mesaj_rezultat").innerHTML = "Nu exista solutii";

		});

		event.preventDefault();

	});
});