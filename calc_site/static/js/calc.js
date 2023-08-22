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

function update_calc_examp(id_var, name_var) {
  var quantity  = $('#calc_examp span#' + id_var + '[name="enter"]');
  var cost  = $('#calc_examp span#' + id_var + '[name="cost"]');
  var price_cost  = $('#calc_examp span#' + id_var + '[name="price_cost"]');
  
  if(name_var == "increase"){
    quantity.text(Number(quantity.text()) + 1);
    cost.text(Number(quantity.text()) * Number(price_cost.text()));
  }
  
  if(name_var == "decrease" && quantity.text() > 0){
    quantity.text(Number(quantity.text()) - 1);
    cost.text(Number(quantity.text()) * Number(price_cost.text()));
  }
}
