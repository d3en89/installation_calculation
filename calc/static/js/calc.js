// this code  enter sum when use button
var sumBtn = document.querySelector('#plus');
sumBtn.onclick = function() {
  var table = document.querySelector('#pricelist');
  var tds = table.querySelectorAll('input');
  var quantity = table.querySelectorAll('span')
  var sum = 0;
  for (var i = 0; i < tds.length; i++) {
    sum += Number(tds[i].value) * Number(quantity[i].innerHTML) ;
    total.innerHTML = sum;
  }
}

//
//var table = document.querySelector('#pricelist');
//var tds = table.querySelectorAll('input');
//var quantity = table.querySelectorAll('span')
//var sum = 0;
//for (var i = 0; i < tds.length - 1; i++) {
//	    sum += Number(tds[i].value) * Number(quantity[i].innerHTML) ;
//    total.innerHTML = sum;
//}

