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

var fib2 = function(n){ //code from Bill Ni's comment on Dynamic Programming QAF post
	var window = [0, 1];

	if(n < 2){
		return window[n];
	}else{
		var inc = 2;
		while(inc <= n){
			window[inc % 2] = window[(inc + 1) % 2] + window[inc % 2];
			inc++;
		}
	return window[(inc - 1) % 2];
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
	var list = document.getElementById("fiblist2");	
	var item = document.createElement("li");
	item.innerHTML = fib2(list.childElementCount);
	list.appendChild(item);
}

var fb = document.getElementById("fb");
fb.addEventListener("click",addFib);

var fb2 = document.getElementById("fb2");
fb2.addEventListener("click",addFib2);





