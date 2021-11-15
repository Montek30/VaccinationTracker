$(document).ready(function(){
	// VACCINE SPOTTER FOR COWIN API
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

	// VACCINE SPOTTER FOR DATABASE SEARCH
	$("#searchbtn_v2").click(function(e) {
		e.preventDefault();

		$("table.table").html("");
		$("#error").html("");
		
		user_id = $("#user_id").val()
		var formData = {
	    	search_value: $("#pin").val(),
	    	search_method: "pincode",
	    	version: 2
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
			    $("table.table").append("<tr><th>NAME</th><th>POSTCODE</th><th>ADDRESS</th><th>VACCINE</th><th>AVAILABLE DOSE</th><th>BOOK APPOINTMENT</th></tr>");
	    		$.each(data['data'], function(i, data){
	    			append_str = "<tr><td>" + data.vaccine_centre_name + "</td><td>" + data.postcode + "</td><td>" + data.address + "</td><td>" + data.vaccine_name + "</td><td>"+ data.count +"</td>"
			    	
			    	if(data.count>0){
			    		append_str += "<td><input type='button' onClick=bookAppointment("+data.vaccine_id+","+data.vaccine_centre_id+","+user_id+") value='Book' /></td>"
			    	}else{
			    		append_str += "<td>Not Available</td>"
			    	}

			    	append_str += "</tr>"

			    	$("table.table").append(append_str);
				})
	    	}
	    });
	});
});


function bookAppointment(vaccine_id, vaccine_centre_id, user_id){
	
	$("#error").html("");
	var formData = {
    	vaccine_id: vaccine_id,
    	vaccine_centre_id: vaccine_centre_id,
    	user_id: user_id
    };

    $.ajax({
    	type: "POST",
        url: "/vaccine/booking",
        data: formData,
        dataType: "json",
    }).done(function (data) {
    	
    	if(data['status'] == 0){
	    	$("#error").html(data['message'])	
	    }else{
			alert("Success")
		}
    	//do handling here
    	console.log(data)
    });
}