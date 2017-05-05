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

function validateEmail($email) {
  var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
  return emailReg.test( $email );
}

function verifyEmail(el){
	if(!validateEmail($(el).val())){
		$(el).parent().addClass("has-error");
		if(!$("#email_label").length){
			$(el).after('<label id="email_label" for="id_email" class="alert alert-danger">Email is not valid</label>');
		}
	} else if($(el).parent().hasClass("has-error")){
		$(el).parent().removeClass("has-error");
		$("#email_label").remove();
	}
}
https://api.jquery.com/remove/
$(function(){
	$('#id_bathroomNumber option[selected=""]').attr('disabled','disabled');
	$('#id_bedroomNumber option[selected=""]').attr('disabled','disabled');
});