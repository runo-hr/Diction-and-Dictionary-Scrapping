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


var theParent = document.querySelector('#sections');
theParent.addEventListener("click", doSomething, false);

function doSomething(e){
    if (e.target !== e.currentTarget){
        var readMoreBtn = document.getElementById(e.target.id);
        var text = readMoreBtn.previousElementSibling
        text.classList.toggle('show-more');
        if (readMoreBtn.innerText === 'Show More'){
            readMoreBtn.innerText = 'Show Less';
        } else {
            readMoreBtn.innerText = 'Show More';
        }
     }
}



