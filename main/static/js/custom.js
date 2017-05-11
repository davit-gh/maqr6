var PriceManipulator = (function(){
	const PPBD = 1000, PPBTH = 1500;
	const EXTRAS = {
			'oven': 2000,
			'fridge': 5000,
			'basement': 9000
		};
	var price;
	var bd = $('#id_bedroomNumber').val(), bth = $('#id_bathroomNumber').val(),
		ext = $('#id_extras');	
	var lastBdPrice = bd ? bd*PPBD : 0, lastBthPrice = bth ? bth*PPBTH : 0;
		
	var iterExtras = function(){
		var p = 0;
		$('#id_extras input').each(function(i,v){
			p += v.checked ? EXTRAS[$(v).val()] : 0; 
		});
		return p;
	}
	var lastExtra = iterExtras();
	var manageBedrooms = function(bdrNum){
		lastBdPrice = bdrNum * PPBD;
		price = lastBdPrice + lastBthPrice + lastExtra;	
	}

	var manageBathrooms = function(bthrNum){
		lastBthPrice = bthrNum * PPBTH;
		price = lastBdPrice + lastBthPrice + lastExtra;
	}

	var manageExtras = function(extra){		
		var val = $(extra).val();
			
		if($(extra)[0].checked){
			lastExtra += EXTRAS[val];
		} else {
			lastExtra -= EXTRAS[val];
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
		getprice: getPrice,
	}
})();


function addToPrice(el){
	var el_id = $(el).attr('id'),
		num = $(el).val();
	if(el_id === 'id_bedroomNumber'){
		PriceManipulator.bdroom(num);
	} else if (el_id === 'id_bathroomNumber'){
		PriceManipulator.bthroom(num);
	}
	$('#id_cost').val(PriceManipulator.getprice());
	
}

function addToPriceExtras(el){
	PriceManipulator.extras(el);
	$('#id_cost').val(PriceManipulator.getprice());
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


$(function(){
	$('#id_bathroomNumber option[selected=""]').attr('disabled','disabled');
	$('#id_bedroomNumber option[selected=""]').attr('disabled','disabled');
	
});