//Team [] -- Isaac Jon and Mohammed Uddin
//SoftDev1 pd6
//K#28 -- Sequential Progression
//2018-12-19

var fibonacci = function(n) {
  if(n == 0)
    return 0;
  if(n < 2)
    return 1;
  else
    return fibonacci(n-2) + fibonacci(n-1);
}

var gcd = function(a, b) {
  if(a == 0)
    return b;
  return gcd(b%a, a);
}

var listOfStudents = ["George", "Bob", "Nina", "Elizabeth", "John", "Charlie"];

var randomStudent = function() {
  randNum = parseInt((Math.random() * listOfStudents.length))
  return listOfStudents[randNum];
}