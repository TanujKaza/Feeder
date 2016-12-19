function display_form_1(element_id,t){
	var x = document.getElementById("midsem_feed");
	if(x.style.display == "none"){
		x.style.display = "inline";
	}
	else  x.style.display = "none";

	var y = document.getElementById("deadline-toggle");
	y.setAttribute("action", "/"+element_id+"/add_deadline/midsem/");

	if (t.firstChild.data == "Add Midsem Date") {
	    t.firstChild.data = "Don't Add Midsem Date";
	} else {
	    t.firstChild.data = "Add Midsem Date";
	}
}

function display_form_2(element_id,t){
	var x = document.getElementById("midsem_feed");
	if(x.style.display == "none") x.style.display = "inline";
	else  x.style.display = "none";
	var y = document.getElementById("deadline-toggle");
	y.setAttribute("action", "/"+element_id+"/add_deadline/endsem/");

	if (t.firstChild.data == "Add Endsem Date") {
	    t.firstChild.data = "Don't Add Endsem Date";
	} else {
	    t.firstChild.data = "Add Endsem Date";
	} 
}

function move_feedback(element_id){
	window.location.href = '/feedback/'+element_id+'/';
}

function add_osquestion(element_id){
	var x = document.getElementById("feedback_id");
	var y = document.getElementById("add_oquestion_form");
	x.value = element_id;
	y.setAttribute("action", "/add_oquestion/"+element_id+"/");
}

function set_objective(){
	var x = document.getElementById("feedback_type");
	x.value = "objective";
}

function set_subjective(){
	var x = document.getElementById("feedback_type");
	x.value = "subjective";
}

function cancel_course(){
	window.location.href = '/sysmain/';
}

function add_course(){
	window.location.href = '/addCourse/';
}

function register(element_id){
	window.location.href = '/register/'+element_id+'/';
}

function register_done(){
	window.location.href = '/sysmain/';
}