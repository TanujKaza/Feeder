function view_ass(element_id){
	window.location.href = '/view_ass/'+element_id+'/';
}

function edit_ass(element_id){
	window.location.href = '/edit_ass/'+element_id+'/';
}

function save_ass(element_id,assignment_id){
	window.location.href = '/save_ass/'+element_id+'/';
}

function add_ass(element_id){
	window.location.href = '/add_ass/'+element_id+'/';
}

function delete_ass(){
	var x = document.getElementById("assignment-id_del");
	window.location.href = '/delete_ass/'+x.value+'/';
}

function cancel_ass(){
	var x = document.getElementById("course-id_cal");
	window.location.href = '/cancel_ass/'+x.value+'/';
}

function view_feed(element_id){
	window.location.href = '/view/feedback/'+element_id+'/';
}

function view_questions(element_id){
	window.location.href = '/view/questions/'+element_id+'/';
}

function view_results(element_id){
	window.location.href = '/view/results/' + element_id+'/';
}

function add_feed(element_id){
	window.location.href = '/add/feedback/'+element_id+'/';
}

function set_objective(){
	var x = document.getElementById("feedback_type");
	x.value = "objective";
}

function add_oquestion(element_id){
	var x = document.getElementById("feedback_id");
	var y = document.getElementById("add_oquestion_form");
	x.value = element_id;
	y.setAttribute("action", "/add/question/"+element_id+"/");
}

function set_subjective(){
	var x = document.getElementById("feedback_type");
	x.value = "subjective";
}

function view_graph(element_id){
	window.location.href = '/view/graph/'+element_id+'/';
}

function view_answers(element_id){
	question_id = element_id.substring(0,element_id.indexOf("/"));
	feedback_id = element_id.substring(element_id.indexOf("/") + 1);
	window.location.href = '/view/subjective/'+question_id+'/'+feedback_id+'/';
}