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

function update_examp_total_sum() {
  var examp_total_cost = $('.calc_examp_cost_span_1');
  var column_cost =   $('#calc_examp .calc_examp_cost')
  var sum = 0
  for (let i = 0; i < column_cost.length; i++) {
    sum += Number(column_cost[i].innerText)
  }
  examp_total_cost.text(sum)
}

function update_calc_examp(id_var, name_var) {
  var level_work = $('input[name="complexity"]:checked').val();
  var quantity  = $('#calc_examp span#' + id_var + '[name="enter"]');
  var cost  = $('#calc_examp span#' + id_var + '[name="cost"]');
  var price_cost  = $('#calc_examp span#' + id_var + '[name="price_cost"]');


  if(name_var == "increase"){
    quantity.text(Number(quantity.text()) + 1);
    cost.text(Number(quantity.text()) * Number(price_cost.text()) + (Number(quantity.text()) * Number(level_work) ) );
  }
  
  if(name_var == "decrease" && quantity.text() > 0){
    quantity.text(Number(quantity.text()) - 1);
    cost.text(Number(quantity.text()) * Number(price_cost.text()) + (Number(quantity.text()) * Number(level_work) )  );
  }

  update_examp_total_sum()

}

function update_calc_examp_def(id_var, name_var) {
  var level_work = $('input[name="complexity"]:checked').val();
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

  update_examp_total_sum()

}


