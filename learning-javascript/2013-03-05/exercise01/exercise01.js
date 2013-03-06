var riga;
riga='';

for(var i=1; i<=10; i++){
	for(var j=1; j<=10; j++){
		if (j===1) {
			riga=i*j;
		} else{
		riga=riga + '\t' + i*j;
		};
	};
	console.log(riga);
};