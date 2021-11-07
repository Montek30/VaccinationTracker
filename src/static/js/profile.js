$(document).ready(function(){

	$("#searchbtn").click(function(e) {
		e.preventDefault();

		$("table.table").html("");
		$("#error").html("");

		var formData = {
	    	date: $("#date").val(),
	    	search_value: $("#pin").val(),
	    	search_method: "pincode",
	    };

	    $.ajax({
	    	type: "GET",
	        url: "/vaccine_centre/search",
	        data: formData,
	        dataType: "json",
	    }).done(function (data) {

	    	//do handling here
	    	if(data['status'] == 0){
	    		$("#error").html(data['message'])	
	    	}else{
			    $("table.table").append("<tr><th>NAME</th><th>ADDRESS</th><th>AVAILABLE DOSE 1</th><th>AVAILABLE DOSE 2</th></tr>");
	    		$.each(data['data'], function(i, data){
			    	$("table.table").append("<tr><td>" + data.name + "</td><td>" + data.address + "</td><td>" + data.available_capacity_dose1 + "</td><td>" + data.available_capacity_dose2 + "</td></tr>");
				})
	    	}
	    });

	});
});