function update_cell(id, count) {
  // update cost sum line if  quantity edit
  price =  document.getElementById("pricelist").rows[id].cells[2].textContent;
  data = Number(price) * Number(count);
  document.getElementById("pricelist").rows[id].cells[6].textContent = data;
  
  // when update line this func  update tota_cost
  var table = document.querySelector('#pricelist');
  var quantity = table.querySelectorAll('#sum_work');
  total_cost = 0;
  for (var i = 0; i < quantity.length; i++) {
      total_cost += Number(quantity[i].textContent);
  }
  total.innerHTML = total_cost;
}


//  if you whant use button this code for you

//start

// var sumBtn = document.querySelector('#plus');

// sumBtn.onclick = function() {
//   var table = document.querySelector('#pricelist');
//   var tds = table.querySelectorAll('input');
//   var quantity = table.querySelectorAll('span');
//   var sum = 0;
//   for (var i = 0; i < tds.length; i++) {
//     sum += Number(tds[i].value) * Number(quantity[i].innerHTML) ;
//     total.innerHTML = sum;
//   }
// }

//end