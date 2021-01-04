function calculateTip() {
	
	var billAmt = document.getElementById("billAmt").value;
	var serviceQual = document.getElementById("serviceQual").value;
	var numOfPeople = document.getElementById("peopleAmt").value;



	if(billAmt === "" || serviceQual == 0) {
		alert("Please Enter Values");
		return;
	}


	if(numOfPeople === "" || numOfPeople <= 1) {
		numOfPeople = 1;

		document.getElementById("each").style.display = "none";
	}

	else {
		document.getElementById("each").style.display = "block";
	}


	console.log(billAmt);
	console.log(serviceQual);
	console.log(numOfPeople);


	var total = (billAmt * serviceQual) / numOfPeople;

	total = Math.round(total * 100) / 100;

	total = total.toFixed(2);


	document.getElementById("totalTip").style.display = "block";
	document.getElementById("tip").innerHTML = total;
}



document.getElementById("totalTip").style.display = "none";
document.getElementById("each").style.display = "none";


document.getElementById("calculate").onclick = function() {
	calculateTip();
};