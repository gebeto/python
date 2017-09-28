var products = document.getElementsByClassName('card');

function priceFilter(priceFrom, priceTo) {
	for (var i = 0; i <= products.length; i++) {
		if (products[i]) {
			if (parseFloat(products[i].getAttribute('price')) < priceFrom) {
				products[i].style.display = 'none';
			} else if (parseFloat(products[i].getAttribute('price')) > priceTo) {
				products[i].style.display = 'none';
			} else {
				products[i].style.display = 'block';
			}
		}
	}
}

$('#price').on('change', function(ev){
	// console.log(ev);
	priceFilter(ev.value.newValue[0], ev.value.newValue[1])
});

$('.dropdown-menu>li>a').on('click', function(){
	$('input[name=url]').val(this.innerText);
	return false;
});