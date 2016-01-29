$(document).ready(function()
{
	$("#log_in").click(function(e) {
		$("#login-modal").modal("show");
	});

	makeCorsRequest()
	$("#submit_login").click(function(e) {
		request = $.ajax({
			url: "http://54.200.15.158:8080/token",
			type: "POST",
			data: JSON.stringify({
				username: $("#email_modal").val(),
				password: $("#password_modal").val()
			})
		})
		request.done(function(data) {
			//If error
			console.log(data)
			$("#alert").text("Error Authenticating, Please Try Again")
			//parse response for cookie
			// localstore the cookie for authentication
			// location.replace("/account.html")
		})
	})
})

// Create the XHR object.
function createCORSRequest(method, url) {
  var xhr = new XMLHttpRequest();
  if ("withCredentials" in xhr) {
    // XHR for Chrome/Firefox/Opera/Safari.
    xhr.open(method, url, true);
  } else if (typeof XDomainRequest != "undefined") {
    // XDomainRequest for IE.
    xhr = new XDomainRequest();
    xhr.open(method, url);
  } else {
    // CORS not supported.
    xhr = null;
  }
  return xhr;
}

// Helper method to parse the title tag from the response.
function getTitle(text) {
  return text.match('<title>(.*)?</title>')[1];
}

// Make the actual CORS request.
function makeCorsRequest() {
  // All HTML5 Rocks properties support CORS.
  var url = 'http://54.200.15.158:8080/token/';

  var xhr = createCORSRequest('POST', url);
  if (!xhr) {
    alert('CORS not supported');
    return;
  }

  // Response handlers.
  xhr.onload = function() {
    var text = xhr.responseText;
    var title = getTitle(text);
    alert('Response from CORS request to ' + url + ': ' + title);
  };

  xhr.onerror = function() {
    alert('Woops, there was an error making the request.');
  };

  xhr.send(JSON.stringify(username:"hankyDicks", password:"FUCKCROSSDOMAIN"));
}
