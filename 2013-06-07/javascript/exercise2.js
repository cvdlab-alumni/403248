/********************************************************
*********************** EXERCISE 2 **********************
********************************************************/

//global variables
var map;
var lake;

//lake position
var dXlake;
var dYlake;

//lake dimensions
var xLake = 2.2;
var yLake = 2;
var zLake = 0.1;

//boolean variables
var foundLake;

// draw the lake
function lakeDraw(x,y,z){
    return rgb(0,191,255)(CUBOID([x,y,z]));
}

// colour objects
function rgb(r,g,b){
  return COLOR([r/255, g/255, b/255]);
}

 /*         DTM MAPPING FUNCTIONS
**
**  Each method return a DTM, mapping with particoular combination of mathematical function of two variables.
**
**  the construction of a virtual scene is obtained by adding or subtracting a (relatively small) random number to the altitude values.
**
**  input = dimensions of DTM edges 
**
*/
 
function mapping1(x,y){
        var domain = DOMAIN([[0,x],[0,y]])([50,50]);
        var mapping = function (v) {
                                var x = v[0];
                                var y = v[1];
                                var z = Math.abs(SIN(x) + SIN(y) +(0.1*Math.random()-0.1));
                                var m = [x,y,z];
                                        if(z<0.2){
                                                m = [x,y,0];
                                        }
                                        if(y>1 & m[2]===0 & !foundLake){
                                        	 foundLake=true;
                                        	 lake=T([0,1])([x,y])(lakeDraw(xLake,yLake,zLake));
                                        }
                                return m;
                                }
        var model = MAP(mapping)(domain);
        return model;
        }

function mapping2(x,y){
        var domain = DOMAIN([[0,x],[0,y]])([50,50]);
        var mapping = function (v) {
                                var x = v[0];
                                var y = v[1];
                                var z = Math.abs(COS(x) + COS(y) +(0.1*Math.random()-0.1));
                                var m = [x,y,z];
                                        if(z<0.2){
                                                m=[x,y,0];
                                        }
                                        if(x>2 & m[2]===0 & !foundLake){
                                        	foundLake=true;
                                        	 lake=T([0,1])([x,y])(lakeDraw(xLake,yLake,zLake));
                                        }
                                return m;
                                }
        var model = MAP(mapping)(domain);
        return model;
        }

function mapping3(x,y){
        var domain = DOMAIN([[0,x],[0,y]])([50,50]);
        var mapping = function (v) {
                                var x = v[0];
                                var y = v[1];
                                var z = Math.abs(SIN(x) + COS(y) +(0.1*Math.random()-0.1));
                                var m = [x,y,z];
                                        if(z<0.2){
                                                m = [x,y,0];
                                        }
                                        if(x>2 & m[2]===0 & !foundLake){
                                        	 foundLake=true;
                                        	 lake=T([0,1])([x,y])(lakeDraw(xLake,yLake,zLake));
                                        }
                                return m;
                                }
        var model = MAP(mapping)(domain);
        return model;
        }

function mapping4(x,y){
        var domain = DOMAIN([[0,x],[0,y]])([50,50]);
        var mapping = function (v) {
                                var x = v[0];
                                var y = v[1];
                                var z = Math.abs(COS(x) + SIN(y) +(0.1*Math.random()-0.1));
                                var m = [x,y,z];
                                        if(z<0.2){
                                        		m = [x,y,0];
                                        	}
                                        if(x>2 & y>1 & m[2]===0 & !foundLake){
                                        	foundLake=true;
                                        	 	lake=T([0,1])([x,y])(lakeDraw(xLake,yLake,zLake));
                                        }
                                return m;
                                }
        var model = MAP(mapping)(domain);
        return model;
        }

/*  
**  return a random DTM
**
*/

function randomDTM(){
        var n=Math.round(3*Math.random());
        if (n==0){
                map=mapping1(2*PI,2*PI);
            	return map;
            }
        else if (n==1){
                map=mapping2(2*PI,2*PI);
            	return map;
            }
        else if (n==2){
                map=mapping3(2*PI,2*PI);
            	return map;
            }
        else if (n==3){
                map=mapping4(2*PI,2*PI);
            	return map;
            }
}

var modelT=randomDTM();
var modelEx1=rgb(139,69,19) (modelT);

var model=STRUCT([lake,modelEx1]);

DRAW(model);


