var riga;
var n;

for(var i=1; i<=10; i++){
	for(var j=1; j<=10; j++){
		if (i===j) {
			n=1;
		}else{
			n=0;
		};
		if (j===1){
			riga=n;
		}else{
		riga=riga + ',\t' + n;
		};
	}
	console.log(riga);
}
