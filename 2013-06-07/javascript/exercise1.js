/********************************************************
*********************** EXERCISE 1 **********************
********************************************************/

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
                                        if(z<0.2){
                                                return [v[0],v[1],0];
                                        }
                                return [x,y,z];
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
                                        if(z<0.2){
                                                return [v[0],v[1],0];
                                        }
                                return [x,y,z];
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
                                        if(z<0.2){
                                                return [v[0],v[1],0];
                                        }
                                return [x,y,z];
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
                                        if(z<0.2){
                                                return [v[0],v[1],0];
                                        }
                                return [x,y,z];
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
        if (n==0)
                return mapping1(2*PI,2*PI);
        else if (n==1)
                return mapping2(2*PI,2*PI);
        else if (n==2)
                return mapping3(2*PI,2*PI);
        else if (n==3)
                return mapping4(2*PI,2*PI);
}

var modelT=randomDTM();
var model=rgb(139,69,19) (modelT);
DRAW(model);