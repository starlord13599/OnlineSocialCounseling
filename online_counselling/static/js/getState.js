var country_select = document.getElementById('country-select');
var state_select = document.getElementById('state-select');

country_select.addEventListener('change',function(){
	var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     data = JSON.parse(this.responseText);
     x = document.getElementsByClassName('state-options');
     y = x.length;
     for(i=0;i<y;i++){
     	x[0].remove();
     }
     for(i=0;i<data.length;i++){
	    var child = document.createElement('option');
	    child.setAttribute('value',data[i]['id']);
	    child.setAttribute('class','state-options');
	    child.innerHTML = data[i]['state_name'];
	    state_select.appendChild(child);
	 }
    }
  };
  xhttp.open("GET", "/administration/get-states/" + String(this.value), true);
  xhttp.send();
})