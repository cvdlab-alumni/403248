/********************************************************
*********************** EXERCISE 4 **********************
********************************************************/

//global variables
var map;
var settlement;
var lake;

//lake position
var dXlake;
var dYlake;

//lake dimensions
var xLake = 2.2;
var yLake = 2;
var zLake = 0.1;

//settlements positions
var dYflat1;
var dYflat1;
var dYflat2;
var dYflat2;

//house dimension (random modification of heigh)
var xHouse = 0.2;
var yHouse= 0.2;
var zHouse = 0.2;

// distance between houses
var distanceX=0.5;
var distanceY=0.5;

// settlement number of houses
var contHouseX=3;
var contHouseY=2;

//boolean variables
var foundLake;
var foundSettlement1 = false;
var foundSettlement2 = false;

//forest
var forest=[];

//number of trees
var cont=50;


/*      SETTLEMENT FUNCTION
**
**      return a settlement 
**
**      input= distance between houses in coordinates X and Y, number of houses 
**
*/

function settlementDraw(distanceX,distanceY, contHouseX, contHouseY) {
		settlX = STRUCT( REPLICA(contHouseX)([houseDrawRandom(xHouse,yHouse,zHouse*(Math.random()+1)), T([0])([distanceX])]));
		var houseMatrix = []
		for (var i = 0;i < contHouseY; i++) {
			houseMatrix.push(settlX);
			houseMatrix.push(T([1])([distanceY]))
              houseMatrix.push(S([2])([Math.random()+0.5]))
		};
		settlement = STRUCT(houseMatrix);
		return settlement;
}

// draw one house
function houseDrawRandom(x,y,z){
    var points = [[0,0],[x,0],[0,z],[x,z],[x/2,z+z*0.5]];
    var cells = [[0,1,2],[1,3,2],[2,3,4]];
    var single_house = SIMPLICIAL_COMPLEX(points)(cells);
    single_house = R([1,2])([PI/2])(EXTRUDE([y])(single_house));
    return rgb(255,255,224)(single_house);
}
}
// draw the lake
function lakeDraw(x,y,z){
    return rgb(0,191,255)(CUBOID([x,y,z]));
}
// colour objects
function rgb(r,g,b){
  return COLOR([r/255, g/255, b/255]);
}

// draw one tree
function treeDrawRandom(rdmrCy,rdmhCy,rdmrCo,rdmhCo,slice){
        function cylinder(rdmrCy,rdmhCy,slice) {
            var cyl = EXTRUDE([rdmhCy])(DISK([rdmrCy])(slice));
            return cyl;
            }
        var domain = DOMAIN([[0,1],[0,2*PI]])([1,slice]);
        var profile = BEZIER(S0)([[0,0,rdmhCo],[rdmrCo,0,0]]);
        var mapping = ROTATIONAL_SURFACE(profile);
        var conoA = MAP(mapping)(domain);
        var conoB = DISK([rdmrCo])(slice);
        var cono = rgb(0,100,0) (T([2])([rdmhCy])(STRUCT([conoA,conoB])));
        var tronco = rgb(128,128,0)(cylinder(rdmrCy,rdmhCy,slice));
        var scaleRandom=Math.round(2*Math.random()+0.5);
return S([0,1,2])([scaleRandom,scaleRandom,scaleRandom])(STRUCT([tronco,cono]));
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
        var domain = DOMAIN([[0,x],[0,y]])([100,100]);
        var mapping = function (v) {
                                var x = v[0];
                                var y = v[1];
                                var z = Math.abs(SIN(x) + SIN(y) +(0.1*Math.random()-0.1));
                                var lakeRandom=Math.round(Math.random());
                                var alberoRandom=Math.round(Math.random());
                                var m = [x,y,z];
                                        if(z<0.2){
                                                m = [x,y,0];
                                        }
                                        if(y>1 && m[2]===0 && !foundLake && lakeRandom){
                                             foundLake=true;
                                             dXlake=x;
                                             dYlake=y;
                                             lake=T([0,1])([dXlake,dYlake])(lakeDraw(xLake,yLake,zLake));
                                        }
                                        if(y>2 && x<2 && 1<z && cont>0 && alberoRandom){
                                            cont--;
                                            forest.push(T([0,1,2])([x,y,z])(treeDrawRandom(0.015,0.06,0.04,0.1,12)));
                                        }
                                        if(m[2]===0 && x>1 && y>4  && !foundSettlement1){
                                        	 dXflat1=x;
                                        	 dYflat1=y;
                                        	 foundSettlement1=true;
                                             settlement1=T([0,1])([dXflat1,dYflat1])(settlementDraw(distanceX,distanceY, contHouseX,contHouseX));
                                        }
                                        if(m[2]===0 && x>2 && y>7.5  && !foundSettlement2){
                                        	 dXflat2=x;
                                        	 dYflat2=y;
                                        	 foundSettlement2=true;
                                             settlement2=T([0,1])([dXflat2,dYflat2])(settlementDraw(distanceX,distanceY, contHouseX,contHouseY));
                                        }
                                return m;
                                }
        var model = MAP(mapping)(domain);
        return model;
        }

function mapping2(x,y){
        var domain = DOMAIN([[0,x],[0,y]])([100,100]);
        var mapping = function (v) {
                                var x = v[0];
                                var y = v[1];
                                var z = Math.abs(COS(x) + COS(y) +(0.1*Math.random()-0.1));
                                var lakeRandom=Math.round(Math.random());
                                var alberoRandom=Math.round(Math.random());
                                var m = [x,y,z];
                                        if(z<0.2){
                                                m=[x,y,0];
                                        }
                                        if(x>2 && m[2]===0 && !foundLake && lakeRandom){
                                            foundLake=true;
                                            dXlake=x;
                                             dYlake=y;
                                             lake=T([0,1])([dXlake,dYlake])(lakeDraw(xLake,yLake,zLake));
                                        }
                                        if(y>2 && x<2 && 1<z && cont>0 && alberoRandom){
                                            cont--;
                                            forest.push(T([0,1,2])([x,y,z])(treeDrawRandom(0.015,0.06,0.04,0.1,12)));
                                        }
                                       if(y>2.8 && m[2]===0 && x>3  && !foundSettlement1){
                                        	 dXflat1=x;
                                        	 dYflat1=y;
                                        	 foundSettlement1=true;
                                              settlement1=T([0,1])([dXflat1,dYflat1])(settlementDraw(distanceX,distanceY, contHouseX,contHouseX));
                                        }
                                        if(m[2]===0 && x>2 && y>6  && !foundSettlement2){
                                        	 dXflat2=x;
                                        	 dYflat2=y;
                                        	 foundSettlement2=true;
                                             settlement2=T([0,1])([dXflat2,dYflat2])(settlementDraw(distanceX,distanceY, contHouseX,contHouseY));
                                        }
                                return m;
                                }
        var model = MAP(mapping)(domain);
        return model;
        }

function mapping3(x,y){
        var domain = DOMAIN([[0,x],[0,y]])([100,100]);
        var mapping = function (v) {
                                var x = v[0];
                                var y = v[1];
                                var z = Math.abs(SIN(x) + COS(y) +(0.1*Math.random()-0.1));
                                var lakeRandom=Math.round(Math.random());
                                var alberoRandom=Math.round(Math.random());
                                var m = [x,y,z];
                                        if(z<0.2){
                                                m = [x,y,0];
                                        }
                                        if(x>2 && m[2]===0 && !foundLake && lakeRandom){
                                             foundLake=true;
                                             dXlake=x;
                                             dYlake=y;
                                             lake=T([0,1])([dXlake,dYlake])(lakeDraw(xLake,yLake,zLake));
                                        }
                                        if(y>2 && x<2 && 1<z && cont>0 && alberoRandom){
                                            cont--;
                                            forest.push(T([0,1,2])([x,y,z])(treeDrawRandom(0.015,0.06,0.04,0.1,12)));
                                        }
                                        if(y>2.5 && m[2]===0 && x>1  && !foundSettlement1){
                                        	 dXflat1=x;
                                        	 dYflat1=y;
                                        	 foundSettlement1=true;
                                              settlement1=T([0,1])([dXflat1,dYflat1])(settlementDraw(distanceX,distanceY, contHouseX,contHouseX));
                                        }
                                        if(m[2]===0 && x>2 && y>6  && !foundSettlement2){
                                        	 dXflat2=x;
                                        	 dYflat2=y;
                                        	 foundSettlement2=true;
                                             settlement2=T([0,1])([dXflat2,dYflat2])(settlementDraw(distanceX,distanceY, contHouseX,contHouseY));
                                        }
                                return m;
                                }
        var model = MAP(mapping)(domain);
        return model;
        }

function mapping4(x,y){
        var domain = DOMAIN([[0,x],[0,y]])([100,100]);
        var mapping = function (v) {
                                var x = v[0];
                                var y = v[1];
                                var z = Math.abs(COS(x) + SIN(y) +(0.1*Math.random()-0.1));
                                var lakeRandom=Math.round(Math.random());
                                var alberoRandom=Math.round(Math.random());
                                var m = [x,y,z];
                                        if(z<0.2){
                                                m = [x,y,0];
                                            }
                                        if(x>2 && y>1 && m[2]===0 && !foundLake && lakeRandom){
                                                foundLake=true;
                                                dXlake=x;
                                                dYlake=y;
                                                lake=T([0,1])([dXlake,dYlake])(lakeDraw(xLake,yLake,zLake));
                                        }
                                         if(y>2 && x<2 && 1<z && cont>0 && alberoRandom){
                                            cont--;
                                            forest.push(T([0,1,2])([x,y,z])(treeDrawRandom(0.015,0.06,0.04,0.1,12)));
                                        }
                                        if(y>4.2 && m[2]===0 && x>4.8 && !foundSettlement1){
                                        	 dXflat1=x;
                                        	 dYflat1=y;
                                        	 foundSettlement1=true;
                                            settlement1=T([0,1])([dXflat1,dYflat1])(settlementDraw(distanceX,distanceY, contHouseX,contHouseX));
                                        }
                                        if(m[2]===0 && x>2 && y>7.5  && !foundSettlement2){
                                        	 dXflat2=x;
                                        	 dYflat2=y;
                                        	 foundSettlement2=true;
                                             settlement2=T([0,1])([dXflat2,dYflat2])(settlementDraw(distanceX,distanceY, contHouseX,contHouseY));
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
                map=mapping1(8,8);
                return map;
            }
        else if (n==1){
                map=mapping2(8,8);
                return map;
            }
        else if (n==2){
                map=mapping3(8,8);
                return map;
            }
        else if (n==3){
                map=mapping4(8,8);
                return map;
            }
}

var modelT=randomDTM();
var modelEx1=rgb(139,69,19)(modelT);
var foresta=STRUCT(forest);
var model=STRUCT([lake,modelEx1,foresta,settlement1,settlement2]);


DRAW(model);