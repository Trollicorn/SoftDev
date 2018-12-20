//[] -- Mohammed Uddin and Isaac Jon
//
//
//

var changeHeading = function(e) {
	h.innerHTML = this.innerHTML;
};

var removeItem = function(e) {
	this.remove();
};

var lis = document.getElementsByTagName("li");

for (var i = 0; i<lis.length; i++){
	lis[i].addEventListener('mouseover',changeHeading);
	lis[i].addEventListener('mouseout',function(){h.innerHTML="Hello World!"});
	lis[i].addEventListener('click',removeItem);
}

var addItem = function(e) {
	var list = document.getElementById("thelist");	
	var item = document.createElement("li");
	item.innerHTML = "WORD";
	item.addEventListener('mouseover',changeHeading);
	item.addEventListener('mouseout',function(){h.innerHTML="Hello World!"});
	item.addEventListener('click',removeItem);
	list.appendChild(item);
};

var button = document.getElementById("b");
button.addEventListener('click',addItem);

var fib = function(n) {
	if (n<2){
		return 1;
	}
	else {
		return fib(n-1) + fib(n-2);
	}
};


var addFib = function(e) {
	console.log(e);
	var list = document.getElementById("fiblist");	
	var item = document.createElement("li");
	item.innerHTML = fib(list.childElementCount);
	list.appendChild(item);
};

var addFib2 = function(e) {
	console.log(e);
}

var fb = document.getElementById("fb");
fb.addEventListener("click",addFib);


