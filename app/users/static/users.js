$(document).ready(function(){
		// ---> Login <---
		$( "#login" ).on( "click",function() {
 			
 			data =  JSON.stringify({  	 
 						'email':'root@gmail.com', //$("#email").val(),
 						'password': 'root'// $("#password").val(),
 					})
 			alert(data)
 			$.ajax({
 				url: 'http://127.0.0.1:8000/api/token/',
 				type: 'POST',
 				contentType:"application/json",
 				dataType:"json",
				data: data,
				success: function(resp){
					alert('success')
					localStorage.setItem("access",  "Bearer " + resp['access'])
					localStorage.setItem("refresh", "Bearer " + resp['refresh'])
				},
				error: function(err){
					alert('failed')
				}
 			})
		});
		// ---> Login End<---
		$( "#access" ).on( "click",function() {
			headerParams = {'Authorization': localStorage.getItem('access')};
		    obj = {
		        type: 'GET',
		        url: 'http://127.0.0.1:8000/register/',
		        headers: headerParams,
		    	data: [],
		    	dataType: 'json',
		    	processData: false,
		    	success: function(data) {
		        	alert('access success');
		    	},
		    	error: function(err){
		    		alert('access fail')
		    	}

			};
		  	jQuery.ajax(obj);
		 })


	});