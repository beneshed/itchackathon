$(document).ready(function () {
	// get_subpage = $.get("_requests.html", function(data) {
	// 	requests_request = $.ajax({
	// 		url: "penis/helps",
	// 		type: "GET"
	// 	})
	// 	requests_request.done(function (data) 
	// 	{
	// 		for(var i == 0; i++; i < len(data)) {
	// 			$(".mount_point").append(data);
	// 		}
	// 	});
	// });

	get_subpage = $.get("_requests.html", function(data) {
		var counter = 0;
		dom_class = "request_" + counter 
		// Check return parameters and set some other stuff
		$(data).addClass(dom_class)
		$(".mount_point").append(data)


	})

	$("#decline_request").click(function () {

	})
	$("#accept_request").click(function () {
		$(".request_content").addClass("request_dont_show");
		// $.ajax({
		// 	url: "//Hook To Bens API, JOB ACCEPTED",
		// 	type: "PUT",
		// 	data: {
		// 		provider: user_id
		// 	}
		// })
	})
	$("#cancel_request").click(function () {
		$(".request_content_second").addClass("request_dont_show");
		$.ajax({
			url: "//Hook to Bens API, JOB CANCELLED",
			type: "PUT",
			data: {
				provider: user_id
			}
		})
	})
	$("#complete_request").click(function () {
		$(".request_content_first").addClass("request_dont_show");
		$(".request_content_second").addClass("request_dont_show");
		$.ajax({
			url: "//Hook to API, JOB IS DONE",
			type: "PUT",
			data: {
				provider: user_id
			}
		})
	})
})