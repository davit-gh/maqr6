var PriceManipulator = (function(el){
	var price = 0;
	var lastBdPrice = 0, lastBthPrice = 0,
		lastExtra = 0;
	var manageBedrooms = function(bdrNum){
		lastBdPrice = bdrNum * 1000;
		price = lastBdPrice + lastBthPrice + lastExtra;		
	}

	var manageBathrooms = function(bthrNum){
		lastBthPrice = bthrNum * 1500;
		price = lastBdPrice + lastBthPrice + lastExtra;
	}

	var manageExtras = function(extra){
		var extras = {
			'oven': 2000,
			'fridge': 5000,
			'basement': 9000
		};
		var val = $(extra).val();
		if($(extra)[0].checked){
			lastExtra += extras[val];
		} else {
			lastExtra -= extras[val];
		}
		price = lastBdPrice + lastBthPrice + lastExtra;
	}

	var getPrice = function(){
		return price;
	}

	return {
		bdroom: manageBedrooms,
		bthroom: manageBathrooms,
		extras: manageExtras,
		price: getPrice
	}
})();

function addToPrice(el){
	var el_id = $(el).attr('id'),
		num = $(el).val();
	if(el_id === 'id_bedroomNumber'){
		PriceManipulator.bdroom(num);
	} else if (el_id === 'id_bathroomNumber'){
		PriceManipulator.bthroom(num);
	} else {

	}
	$('#id_cost').val(PriceManipulator.price());
	
}

function addToPriceExtras(el){
	PriceManipulator.extras(el);
	$('#id_cost').val(PriceManipulator.price());
}
