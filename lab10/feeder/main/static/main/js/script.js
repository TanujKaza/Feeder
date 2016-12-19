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