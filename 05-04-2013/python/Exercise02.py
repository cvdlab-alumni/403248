from pyplasm import *

#function for round pillars
def roundPillar():
    pillar = CYLINDER([1.25,26])(36)
    centeredPillar = T([1,2])([1.25,1.25])(pillar)
    return centeredPillar

#function GRID    
GRID = COMP([INSR(PROD),AA(QUOTE)])

#pillars 0
roundPillars0 = STRUCT(NN(5)([roundPillar(),T([1])([27.5])]))
roundPillars0a = T([2])([50])(roundPillar())
roundPillars0b = T([1,2])([110,50])(roundPillar())
squarePillars0 = GRID([[-13.75, 2.5, -11.25, 2.5, -25, 2.5, -25, 2.5, -25], [-50, 2.5, -12.5], [-1,25]])
pillars0 = STRUCT([squarePillars0,roundPillars0,roundPillars0a,roundPillars0b])

#pillars 1
squarePillarsLine1AA = GRID([[2.5,-25,2.5],[2.5],[-27,49]])#fila sotto
squarePillarsLine1AB = GRID([[-2.5,-25,-2.5,-25,2.5,-25,2.5,-25,2.5],[2.5],[-27,24]])#fila sotto
squarePillarsLine1BA = GRID([[2.5,-25,2.5],[-50,2.5],[-27,49]])#fila sopra
squarePillarsLine1BB = GRID([[-2.5,-25,-2.5,-25,2.5,-25,-2.5,-25,2.5],[-50,2.5],[-27,24]])#fila sopra
roundPillar1t = T([1,2,3])([2.5+25+2.5+25+2.5+25+1.25,50+1.25,27])(CYLINDER([1.25,24])(36))
pillars1 = STRUCT([squarePillarsLine1AA,squarePillarsLine1AB,squarePillarsLine1BA,squarePillarsLine1BB,roundPillar1t])

#pillars 2
squarePillars2a = GRID([[-55, 2.5, -52.5, 2.5], [2.5, -62.5], [-52, 24, -26]])
squarePillars2b = GRID([[-55, 2.5, -25, 2.5, -25, 2.5], [-50, 2.5, -12.5], [-52, 24, -26]])
pillars2 = STRUCT([squarePillars2a,squarePillars2b])

#pillars 3
smallSquarePillars3a = GRID([[1.25, -111.25], [1.25, -62.5], [-77, 23, -2]])
smallSquarePillars3b = GRID([[1.25, -26.25, 1.25], [-51.25, 1.25], [-77, 23, -2]])
squarePillars3a = GRID([[-55, 2.5, -52.5, 2.5],[2.5, -47.5, 2.5],[-77, 23, -2]])
squarePillars3b = GRID([[-55, 2.5, -25, 2.5, -25, 2.5],[-50, 2.5],[-77, 23, -2]])
pillars3 = STRUCT([squarePillars3a,squarePillars3b,smallSquarePillars3a,smallSquarePillars3b])

#the groups of pillars are organized in a STRUCT
pillars = STRUCT ([pillars0,pillars1,pillars2,pillars3])

#function for semiCircle floor 0
def semiCircle(r):
    
    def semiCircle(p):
            alpha = p[0]
            b = p[1]
            a = [b*COS(alpha), b*SIN(alpha)] 
            return a
        
    dom = PROD([INTERVALS(PI)(36), INTERVALS(r)(1)])
    cerchioO = MAP(semiCircle)(dom)
    semiPlan = PROD([cerchioO, Q(1)])
    return semiPlan


#floor 0
semiPlan0a = GRID([[-13.75, 71.25], [-22, 43], [1]])
semiPlan0b = GRID([[-85, 12.5, -15], [-42, 23], [1]])
semiPlan0c = GRID([[-13.75, 12.5],[-18, 4],[1]])
semiPlan0d = T([1,2])([97.5, 53.5])(R([1,2])(-PI/2)(semiCircle(11.5)))
semiPlan0e = T([1,2])([20, 18])(R([1,2])(-PI)(semiCircle(6.25)))
floor0 = STRUCT([semiPlan0a,semiPlan0b,semiPlan0c,semiPlan0d,semiPlan0e])

#floor 1
hpart11 = GRID([[2.5,8.57],[50,3.5,9,2.5],[-1,-25,1]])
hpart12 = GRID([[-2.5,-8.57,40.22],[50,3.50,-9,2.5],[-1,-25,1]])
hpart14 = GRID([[-2.5,-8.57,-31.65,-4.58,3.99],[-50,-3.5,9],[-1,-25,1]])
hpart15 = GRID([[-2.5,-8.57,-31.65,-8.57,8.57],[65],[-1,-25,1]])
hpart16 = GRID([[-2.5,-8.57,-31.65,-8.57,-8.57,52.64],[65],[-1,-25,1]])
floor1 = STRUCT([hpart11,hpart12,hpart14,hpart15,hpart16])

#floor 2
hpart21 = GRID([[2.5,5.71],[65],[-1,-25,-1,-24,1]])
hpart22 = GRID([[-2.5,-5.71,37.14],[2.5,-51,-9,2.5],[-1,-25,-1,-24,1]])
hpart23 = GRID([[-2.5,-5.71,-37.14,13.57],[2.5],[-1,-25,-1,-24,1]])
verts = [[58.92,0],[45.35,51],[45.35,65],[58.92,65]]
cells = [[1,2,3,4]]
hpart24 = MKPOL([verts,cells,None])
hpart24_3D = T([3])([1+25+1+24])(PROD([hpart24,Q(1)]))
hpart25 = GRID([[-2.5,-5.71,-37.14,-13.57,53.53],[65],[-1,-25,-1,-24,1]])
floor2 = STRUCT([hpart21,hpart22,hpart23,hpart24_3D,hpart25])

#floor 3
hpart31 = GRID([[2.5],[65],[-1,-25,-1,-24,-1,-24,1]])
hpart32 = GRID([[2.5,25,2.5,25],[2.5,61.25,1.25],[-1,-25,-1,-24,-1,-24,1]])
hpart33 = GRID([[-2.5,-25,-2.5,-25,2.5],[65],[-1,-25,-1,-24,-1,-24,1]])
hpart34 = GRID([[-2.5,-25,-2.5,-25,2.5,34.58],[54.75,-9,1.25],[-1,-25,-1,-24,-1,-24,1]])
hpart35 = GRID([[-2.5,-25,-2.5,-25,2.5,-34.58,20.42],[65],[-1,-25,-1,-24,-1,-24,1]])
floor3 = STRUCT([hpart31,hpart32,hpart33,hpart34,hpart35])

#floor 4
hpart41 = GRID([[2.5],[65],[-1,-25,-1,-24,-1,-24,-1,-23,2]])
hpart42 = GRID([[2.5,25,2.5,25],[2.5,-41.18,21.32],[-1,-25,-1,-24,-1,-24,-1,-23,2]])
hpart43 = GRID([[-2.5,-25,-2.5,-25,2.5,25,2.5,25,2.5],[65],[-1,-25,-1,-24,-1,-24,-1,-23,2]])
floor4 = STRUCT([hpart41,hpart42,hpart43])

#the base of the building
buildingBase = T([1,2])([-9,-12])(COLOR(GREEN)(T([3])([-2])(GRID([[130],[90],[2]]))))

#the groups of floors are organized in a STRUCT
floors = STRUCT([floor0,floor1,floor2,floor3,floor4,buildingBase])

VIEW([pillars, floors])
