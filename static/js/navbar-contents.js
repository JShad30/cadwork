// Adding and removing the classes
$(document).ready(function() {
	// If the user clicks the on the jobs link the options of upload and bid will appear
    $("#jobs-dropdown-link").on("click", function() {
		$("#jobs-dropdown").slideToggle("fast");
	});

	// If the mouse leaves the jobs dropdown link, then the dropdown menu will scroll up
	$("#jobs-dropdown-link").mouseleave(function() {
		$("#jobs-dropdown").slideUp("fast");
	});
	
	// The dropdown menu will also scroll up if the mouse leaves the jobs dropdown list
	$("#jobs-dropdown").mouseleave(function() {
		$("#jobs-dropdown").slideUp("fast");
	});
});

// Reset page when window size changes
$(window).resize(function() {
    location.reload(true)
});