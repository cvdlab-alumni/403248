function fromLarToObj(v,fv){
	var numberVertices = v.length;
	var numberFaces = fv.length;
	var result = "";

	for (var i = 0; i < numberVertices; i++){
		if(v[i][2] !== undefined)
			result += 'V ' + '{' + v[i][0] + ' ' + v[i][1] + ' '+  v[i][2] + '}' + '\n'; 
		else
		    result += 'V ' + '{' + v[i][0] + ' ' + v[i][1] + ' 0'+ '}' + '\n';
	};

	result+="\n";

	for (var i = 0; i < numberFaces; i++){
		var vertexIndex = fv[i].length;
		result += 'FV ' + '{' ;
		for (var j = 0; j < vertexIndex; j++) {
			if(vertexIndex-1 !== j)
				result +=  fv[i][j] + ' '; 
			else 
				result +=  fv[i][j] + '}' + '\n';

		};
	};
	return result; 
}


v = [	[0,6],
 		[0,0],
 		[3,0],
 		[6,0],
 		[0,3,5],
 		[3,3,4],
 		[6,3],
 		[6,6],
 		[3,6]		];

fv = [	[5,6,7,8],
	 	[0,5,8],
	 	[0,4,5],
	 	[1,2,4,5],
	 	[2,3,5,6],
	 	[0,8,7],
	 	[3,6,7],
	 	[1,2,3],
	 	[0,1,4]		];

var model = fromLarToObj(v,fv);
console.log(model);