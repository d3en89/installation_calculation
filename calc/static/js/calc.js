// this code  enter sum when use button
  var input = document.body.children[0];

    input.oninput = function() {
    document.getElementById('result').innerHTML = input.value;
};


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

function update_cell(id, count) {
  price =  document.getElementById("pricelist").rows[id].cells[2].textContent
  data = Number(price) * Number(count)
  document.getElementById("pricelist").rows[id].cells[6].textContent = data;
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

