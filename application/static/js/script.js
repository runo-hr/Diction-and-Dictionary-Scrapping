var survey_options = document.getElementById('survey_options');
var add_more_fields = document.getElementById('add_more_fields');
var remove_fields = document.getElementById('remove_fields');
var counter = 1;

add_more_fields.onclick = function(){
    counter++;
	var newField = document.createElement('input');
	let txt = "page_";
	let txt1 = txt.concat(counter);
	newField.setAttribute('type','text');
	newField.setAttribute('name',txt1);
	newField.setAttribute('class','survey_options');
	newField.setAttribute('siz',50);
	newField.setAttribute('placeholder','Add url');
	survey_options.appendChild(newField);
}

remove_fields.onclick = function(){
	var input_tags = survey_options.getElementsByTagName('input');
	if(input_tags.length > 1) {
		survey_options.removeChild(input_tags[(input_tags.length) - 1]);
		counter--
	}
}