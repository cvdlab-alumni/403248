'''
Created on 11/mag/2013

@author: mcannaviccio
'''
from pyplasm import *

#===============================================================================
# FUNZIONI
#===============================================================================

def DOMAIN2D(domains1D):
        def aux(q):
                a = q[0]
                b = q[1]
                c = q[2]
                d = q[3]
                return [ [ a, b, d ], [ d, b, c ] ]
        dd = PROD([ domains1D[0], domains1D[1] ])
        complex = UKPOL(dd)
        points = complex[0]
        cells = CAT(AA(aux)(complex[1]))
        return MKPOL([ points, cells, None ])

def curveHermite(c1):
    dom = domain(1, 22)
    return MAP(CUBICHERMITE(S1)(c1))(dom);

def supHermite(p1,p2,t1,t2):
    dom = DOMAIN2D([domain(1, 12),domain(1, 12)])
    curva1 = CUBICHERMITE(S1)(p1)
    curva2 = CUBICHERMITE(S1)(p2)
    return MAP(CUBICHERMITE(S2)([curva1,curva2,t1,t2]))(dom)

def quadDomain(l, p):
    semiDomain = domain(l,p)
    return PROD([semiDomain,semiDomain]);

def domain(l, p):
    domain = INTERVALS(l)(p)
    return domain;

def cerchio(r):
    def cerchio0(p):
        a=p[0]
        return [r*SIN(a), r*COS(a)]
    return cerchio0;

def pieceOfCircle(alpha, r , R):
    dom=DOMAIN2D([domain(alpha, 64),T(1)(r)(domain(R-r, 1))])
    def mapping(v):
            a=v[0]
            r=v[1]
            return [r*COS(a), r*SIN(a)]
    model=MAP(mapping)(dom)
    return model

dominioCircolare=DOMAIN2D([domain(1, 20),domain(2*PI, 32)])

#===============================================================================
#===============================================================================
# # EXERCISE 02
#===============================================================================
#===============================================================================

#===============================================================================
# LATERALE Z
#===============================================================================
#linee esterne
a1Z=[[0,5.5],[1,2.3],[0,-4],[1,0]]
a2Z=[[1,2.3],[4,2],[0,0],[0,0]]
bZ=[[4,2],[10,1.5],[0,14],[-3,-13]]
cZ=[[10,1.5],[21,1.5],[0,0],[0,0]]
dZ=[[21,1.5],[27,2],[0,14],[0,-13]]
eZ=[[27,2],[29.3,2.3],[0,0],[0,2]]
fZ=[[29.3,2.3],[29.3,3],[29.7,3],[29.7,3.5]]
gZ=[[29.7,3.5],[29,4.5],[4,2],[0,0]]
hZ=[[29,4.5],[29.2,5.5],[0,0],[0,0]]
iZ=[[29.2,5.5],[27,7.5],[6,0],[-1,0]]
lZ=[[27,7.5],[20.5,8.5],[-1,1],[-1,0]]
mZ=[[20.5,8.5],[20,8.2],[-2,-1],[0,0]]
nZ=[[20,8.2],[16,11],[0,0.5],[-2.5,1.5]]
oZ=[[16,11],[9,11.5],[-4,3],[-2,-1]]
pZ=[[9,11.5],[4,9],[-2,0],[0,0]]
qZ=[[4,9],[2.7,9],[0,0],[0,0]]
r1Z=[[2.8,8.8],[1.1,9.5],[0,1],[-3,0]]
r2Z=[[1.1,9.5],[2,8.8],[1,-0.5],[0,-1]]
r3Z=[[1.1,9.5],[1.6,8.9],[1,-0.5],[0,-1]]
sZ=[[0,5.5],[0.5,6],[1,6.2],[0.9,6.7],[1.2,7.7],[1.4,8],[1.2,8.2],[1.5,9]]

#linee interne
t1Z=[[1.5,9],[2.2,8.4],[11.5,8.4]]
t2Z=[[2.2,8.4],[1.6,6.7]]
t3Z=[[1.6,6.7],[0,5.5],[0,-3],[-3,0]]
uZ=[[1.2,8.2],[1.8,8],[1.3,6.4],[1,6.2]]
v1Z=[[10.1,2.5],[20.5,2.5],[21.2,2.8]]
v2Z=[[10.1,2.3],[21,2.3]]
v3Z=[[10,7],[12,7]]
v4Z=[[14,7],[22,6.8]]
z1Z=[[11,8.4],[10.5,10.2]]
z2Z=[[11.2,8.4],[10.7,10.2]]
z3Z=[[10.5,10.2],[15.5,10.4],[1.5,2],[3,-2]]
z4Z=[[10.7,10.2],[15.5,10.2],[1.5,2],[3,-2]]
z5Z=[[15.5,10.4],[18.5,8.2]]
z6Z=[[15.5,10.2],[18.3,8.2]]
x1Z=[[19,8.2],[15,11],[0,0],[-3,1]]
x2Z=[[15,11],[9.2,11],[-2,1],[-2.5,-1]]
x3Z=[[9.2,11],[4.4,8.6],[-2,-1],[0,0]]
x4Z=[[4.4,8.6],[4,9]]
x5Z=[[15.9,11.1],[15.5,10.8]]
x6Z=[[4.4,8.6],[4,9]]
x7Z=[[9,10.9],[8.3,11.3]]
y1Z=[[11.2,8.4],[18.5,8.2]]
y2Z=[[11.2,8.4],[12.2,2.5],[-2,0],[1,-1]]
y3Z=[[18.5,8.2],[18.5,2.5],[2,-1],[-2,1]]
w1Z=[[18.5,8.2],[28,5.5],[9,0],[0,-6]]
w2Z=[[29.2,5.5],[27.8,5.4]]
w3Z=[[27.8,5.4],[27.4,4.3],[-1,0],[1,0]]
w4Z=[[27.4,4.3],[29,4.5],[0,-0.5],[0,0.5]]
kZ=[[1.2,6.5],[5.1,4.5],[8,0],[16,0]]
k2Z=[[29.3,2.3],[29.5,3]]

paraurtiPosterioreZZZ=curveHermite(a1Z)
paraurtiPosterioreSottoZZZ=curveHermite(a2Z)
parafangoPosterioreZZZ=curveHermite(bZ)
paraurtiLateraleZZZ=curveHermite(cZ)
parafangoAnterioreZZZ=curveHermite(dZ)
paraurtiAnterioreZZZ=curveHermite(eZ)
portaFendinebbiaFrontaleZZZ=POLYLINE(fZ)
portaFaroAnterioreZZZ=curveHermite(gZ)
faroAnterioreZZZ=curveHermite(hZ)
cofanoGrandeZZZ=curveHermite(iZ)
cofanoMustangZZZ=curveHermite(lZ)
cofanoPiccoloZZZ=curveHermite(mZ)
parabrezzaZZZ=curveHermite(nZ)
tettoSuperioreZZZ=curveHermite(oZ)
tettoPosterioreZZZ=curveHermite(pZ)
portabagagliSuperioreZZZ=curveHermite(qZ)
pinnaZZZ=STRUCT([curveHermite(r1Z),curveHermite(r2Z),curveHermite(r3Z)])
portabagagliPosterioreZZZ=POLYLINE(sZ)
portabagagliEsternoZZZ=STRUCT([POLYLINE(t1Z),POLYLINE(t2Z),curveHermite(t3Z)])
targaZZZ=POLYLINE(uZ)
gonnaLateraleZZZ=STRUCT([POLYLINE(v1Z),POLYLINE(v2Z)])
rigaLateraleZZZ=STRUCT([POLYLINE(v3Z),POLYLINE(v4Z)])
finestrinoZZZ=STRUCT([POLYLINE(z1Z),POLYLINE(z2Z),curveHermite(z3Z),curveHermite(z4Z),POLYLINE(z5Z),POLYLINE(z6Z)])
lineaTettoZZZ=STRUCT([curveHermite(x1Z),curveHermite(x2Z),curveHermite(x3Z),POLYLINE(x4Z),POLYLINE(x5Z),POLYLINE(x6Z),POLYLINE(x7Z)])
sportelloZZZ=STRUCT([POLYLINE(y1Z),curveHermite(y2Z),curveHermite(y3Z)])
cofanoDavantiEfaroZZZ=STRUCT([curveHermite(w1Z),POLYLINE(w2Z),curveHermite(w3Z),curveHermite(w4Z)])
lineaParaurtiPosterioreZZZ=curveHermite(kZ)
tappoSerbatoioZZZ=T([1,2])([4,7])(MAP(cerchio(0.6))(domain(2*PI,36)))
fendinebbiaAnterioreZZZ=POLYLINE(k2Z)


profiloZZZ=STRUCT([paraurtiPosterioreZZZ,paraurtiPosterioreSottoZZZ,parafangoPosterioreZZZ,paraurtiLateraleZZZ,
                parafangoAnterioreZZZ,paraurtiAnterioreZZZ,portaFendinebbiaFrontaleZZZ,portaFaroAnterioreZZZ,faroAnterioreZZZ,
                cofanoGrandeZZZ,cofanoMustangZZZ,cofanoPiccoloZZZ,parabrezzaZZZ,tettoSuperioreZZZ,tettoPosterioreZZZ,portabagagliSuperioreZZZ,pinnaZZZ,
                portabagagliPosterioreZZZ,portabagagliEsternoZZZ,targaZZZ,gonnaLateraleZZZ,rigaLateraleZZZ,finestrinoZZZ,lineaTettoZZZ,sportelloZZZ,cofanoDavantiEfaroZZZ,
                lineaParaurtiPosterioreZZZ,tappoSerbatoioZZZ,fendinebbiaAnterioreZZZ])

profiloZZZruotato=S(2)(0.85)(T([1,3])([8,-30])(R([1,3])(PI/2)(profiloZZZ)))
#VIEW(profiloZZZruotato)

#===============================================================================
# PROFILO DAVANTI X
#===============================================================================

#linee esterne
a1X=[[0,2.3],[4,2.3]]
a2X=[[4,2.3],[5.2,6],[2,1],[0,2]]
a3X=[[5.2,6],[4.9,6.2]]
a4X=[[5.1,6.1],[4.8,7],[0,2],[-0.5,0]]
b1X=[[4.8,7],[5.3,7],[0,0],[0,0]]
b2X=[[5.3,7],[5.3,7.8],[0.5,0],[-0.5,0]]
b3X=[[5.3,7.8],[4.5,7.8],[0,0],[0,0]]
b4X=[[4.5,7.8],[4.3,7.6],[-0.5,-0.5],[0,0]]
cX=[[4.3,7.6],[3.2,9.8],[0,0],[-1,1]]
d1X=[[3.2,9.8],[0,10.2],[-2,1],[-2,0]]

#linee interne

d2X=[[3.35,9.5],[0,10],[-2,1],[-2,0]]
e1X=[[3.35,9.5],[4.2,7.1]]
e2X=[[4.2,7.1],[0,7.7],[-1,2],[-2,0]]
fX=[[4.2,7.1],[3.7,5.5],[0,5.5]]
g1X=[[3.7,5.5],[4.2,4.5],[2,-1],[0,-2]]
g2X=[[4.2,4.5],[2.3,5.5],[-3.8,0],[0,3.8]]
h1X=[[2,5.5],[0,4.4],[1,-3.5],[-3,0]]
h2X=[[2,5.5],[0,5.5],[0,0],[0,0]]
i1X=[[4.3,4],[0,4]]
i2X=[[4.2,3.8],[0,3.8]]
i3X=[[4.2,3.8],[4.5,5.7],[0,0],[-1,2]]
f1X=[[0,3.5],[3,3.5],[0,0],[0,0]]
f2X=[[0,2.6],[3,3.5],[8,0],[0,3]]
r1X=[[5,4.5],[5,1]]
r2X=[[3.5,2.3],[3.5,1]]
r3X=[[3.5,1],[5,1],[0,-1],[0,1]]

paraurtiXXX=STRUCT([POLYLINE(a1X),curveHermite(a2X),POLYLINE(a3X),curveHermite(a4X)])
specchiettoXXX=STRUCT([curveHermite(b1X),curveHermite(b2X),curveHermite(b3X),curveHermite(b4X)])
finestrinoXXX=curveHermite(cX)
tettinoXXX=STRUCT([curveHermite(d1X),curveHermite(d2X)])
parabrezzaXXX=STRUCT([POLYLINE(e1X),curveHermite(e2X)])
cofanoXXX=POLYLINE(fX)
faroXXX=STRUCT([curveHermite(g1X),curveHermite(g2X)])
grigliaSopraXXX=COLOR(BLACK)(SKELETON(1)(supHermite(h1X,h2X,[0,0],[0,0])))
grigliaSottoXXX=COLOR(BLACK)(SKELETON(1)(supHermite(f1X,f2X,[0,0],[0,0])))
paraurtiBassoXXX=STRUCT([POLYLINE(i1X),POLYLINE(i2X),curveHermite(i3X)])
ruotaXXX=STRUCT([POLYLINE(r1X),POLYLINE(r2X),curveHermite(r3X)])

profiloDxXXX=S(1)(1.3)(STRUCT([paraurtiXXX,specchiettoXXX,finestrinoXXX,tettinoXXX,parabrezzaXXX,
                     cofanoXXX,faroXXX,grigliaSopraXXX,paraurtiBassoXXX,grigliaSottoXXX,ruotaXXX]))
                       
profiloSxXXX=R([1,3])(PI)(profiloDxXXX)
profiloXXX=STRUCT([profiloDxXXX,profiloSxXXX])

#VIEW(profiloXXX)

#===============================================================================
# PROFILO SUPERIORE Y
#===============================================================================

#linee esterne
aY=[[0,0.5],[6,3.5],[12,0],[2,2]]
bY=[[6,3.5],[6,8.3],[5.7,8.8],[5.7,11.5]]
cY=[[5.7,11.5],[6.2,11.7],[6.4,12],[6.4,12.5],[5.3,12],[5.4,11.8]]
dY=[[5.7,12.2],[5.7,20],[6,20.5],[6,25],[5.7,25.5],[5.3,29]]
eY=[[5.3,29],[0,30.2],[0,4],[-2,0]]

#linee interne

f1Y=[[5,10.2],[0,8],[0,-2],[-7,0]]
f2Y=[[4,13.5],[0,13.2],[0,-1],[0,0]]
f3Y=[[4,13.5],[4.9,9.9]]
g1Y=[[5,10.2],[4.2,19],[-1,9],[2,15]]
g2Y=[[4.2,19],[5,19],[0,1],[2,-2]]
g3Y=[[5,10.2],[5,19]]
hY=[[4,13.5],[4,20],[-1,7],[1,4]]
i1Y=[[4,20],[4.2,26],[1,4],[-0.5,3]]
i2Y=[[5,27.7],[0,28.5],[-1,1],[-5,0]]
i3Y=[[4.2,26],[0,27],[-1,1],[-5,0]]
i4Y=[[4.1,22],[0,22]]
lY=[[4.2,26],[4.2,27.9]]
m1Y=[[5,27.7],[5,29]]
m2Y=[[5,29],[0,29.6],[-1,1],[-5,0]]
n1Y=[[5,19],[5.7,19],[0,1],[0,-1]]
n2Y=[[5,10.4],[5.7,9.8],[1,0],[0,-1]]
n3Y=[[5,19],[4.2,26],[0,8],[-1,3]]


paraurtiAnterioreYYY=curveHermite(aY)
fiancataAnterioreYYY=POLYLINE(bY)
specchiettoYYY=POLYLINE(cY)
fiancataPosterioreYYY=POLYLINE(dY)
portabagagliYYY=curveHermite(eY)
parabrezzaYYY=STRUCT([curveHermite(f1Y),curveHermite(f2Y),POLYLINE(f3Y)])
finestrinoYYY=STRUCT([curveHermite(g1Y),curveHermite(g2Y),POLYLINE(g3Y)])
tettinoSuperioreYYY=curveHermite(hY)
tettinoPosterioreYYY=STRUCT([curveHermite(i1Y),curveHermite(i2Y),curveHermite(i3Y),POLYLINE(i4Y)])
portabagagliSuperioreYYY=POLYLINE(lY)
spoilerYYY=STRUCT([POLYLINE(m1Y),curveHermite(m2Y)])
sportelloYYY=STRUCT([curveHermite(n1Y),curveHermite(n2Y),curveHermite(n3Y)])

profiloDxYYY=STRUCT([paraurtiAnterioreYYY,fiancataAnterioreYYY,specchiettoYYY,fiancataPosterioreYYY,portabagagliYYY,
                     parabrezzaYYY,finestrinoYYY,tettinoSuperioreYYY,tettinoPosterioreYYY,portabagagliSuperioreYYY,spoilerYYY,
                     sportelloYYY])   
profiloSxYYY=R([1,3])(PI)(profiloDxYYY)
profiloYYY=COLOR(BLACK)(STRUCT([profiloDxYYY,profiloSxYYY]))
profiloYYYruotato=S(1)(1.2)(T(2)(10)(R([2,3])(-PI/2)(profiloYYY)))
#VIEW(profiloYYY)

exercise02=COLOR(BLACK)(STRUCT([profiloXXX,profiloZZZruotato,profiloYYYruotato]))
#VIEW(exercise02)

#===============================================================================
#===============================================================================
# # EXERCISE 03
#===============================================================================
#===============================================================================

#===============================================================================
# RUOTA 3D
#===============================================================================

puntiProfilo1=[[5.5,0,0],[6,0,0],[0,0,0],[0,0,0]]
puntiProfilo2=[[5.5,0,5],[6,0,5],[0,0,0],[0,0,0]]
puntiProfilo3=[[6,0,0],[6,0,5],[6,0,0],[-6,0,0]]
profiloGomma1=CUBICHERMITE(S1)(puntiProfilo1)
profiloGomma2=CUBICHERMITE(S1)(puntiProfilo2)
profiloGomma3=CUBICHERMITE(S1)(puntiProfilo3)
gomma1=MAP(ROTATIONALSURFACE(profiloGomma1))(dominioCircolare)
gomma2=MAP(ROTATIONALSURFACE(profiloGomma2))(dominioCircolare)
gomma3=MAP(ROTATIONALSURFACE(profiloGomma3))(dominioCircolare)
gomma=COLOR(BLACK)(STRUCT([gomma1,gomma2,gomma3]))

puntiProfiloCerchioEsterno1=[[4.5,0,1],[5,0,0],[0,0,0],[0,0,0]]
puntiProfiloCerchioEsterno2=[[4.5,0,4],[5,0,5],[0,0,0],[0,0,0]]
puntiProfiloCerchioEsterno4=[[5,0,0],[5.5,0,0],[0,0,0],[0,0,0]]
puntiProfiloCerchioEsterno5=[[5,0,5],[5.5,0,5],[0,0,0],[0,0,0]]
puntiProfiloCerchioEsterno3=[[4.5,0,4],[4.5,0,1],[-0.5,0,0],[0.5,0,0]]

profiloCerchioEsterno1=CUBICHERMITE(S1)(puntiProfiloCerchioEsterno1)
profiloCerchioEsterno2=CUBICHERMITE(S1)(puntiProfiloCerchioEsterno2)
profiloCerchioEsterno3=CUBICHERMITE(S1)(puntiProfiloCerchioEsterno3)
profiloCerchioEsterno4=CUBICHERMITE(S1)(puntiProfiloCerchioEsterno4)
profiloCerchioEsterno5=CUBICHERMITE(S1)(puntiProfiloCerchioEsterno5)
cerchioneEsterno1=MAP(ROTATIONALSURFACE(profiloCerchioEsterno1))(dominioCircolare)
cerchioneEsterno2=MAP(ROTATIONALSURFACE(profiloCerchioEsterno2))(dominioCircolare)
cerchioneEsterno3=MAP(ROTATIONALSURFACE(profiloCerchioEsterno3))(dominioCircolare)
cerchioneEsterno4=MAP(ROTATIONALSURFACE(profiloCerchioEsterno4))(dominioCircolare)
cerchioneEsterno5=MAP(ROTATIONALSURFACE(profiloCerchioEsterno5))(dominioCircolare)
cerchioneEsterno=COLOR(YELLOW)(STRUCT([cerchioneEsterno1,cerchioneEsterno2,cerchioneEsterno3,cerchioneEsterno4,cerchioneEsterno5]))

cerchioneInternoBase=pieceOfCircle(2*PI,1.8,2)
cerchioneInterno=T(3)(1)(COLOR(YELLOW)(PROD([cerchioneInternoBase,Q(2)])))

cerchionePiccoloBase=pieceOfCircle(2*PI,1.2,1.8)
cerchionePiccolo=T(3)(2)(COLOR(YELLOW)(PROD([cerchionePiccoloBase,Q(0.2)])))

r1a=[[4.5,0.8,1],[1.9,0.4,1],[-2,-2,-1.5],[-1,1,1.5]]
r2a=[[4.5,-0.8,1],[1.9,-0.4,1],[-2,2,-1.5],[-1,-1,1.5]]
r1b=[[4.5,0.8,2],[1.9,0.4,2],[-2,-2,-1.5],[-1,1,1.5]]
r2b=[[4.5,-0.8,2],[1.9,-0.4,2],[-2,2,-1.5],[-1,-1,1.5]]

raggio1a=supHermite(r1a,r2a,[0,0,0],[0,0,0])
raggio1b=supHermite(r1b,r2b,[0,0,0],[0,0,0])
raggio1c=supHermite(r1a,r1b,[0,0,0],[0,0,0])
raggio1d=supHermite(r2a,r2b,[0,0,0],[0,0,0])

raggio1=STRUCT([raggio1a,raggio1b,raggio1c,raggio1d])

raggio=COLOR(YELLOW)(STRUCT([raggio1,R([1,2])(PI/4),raggio1,R([1,2])(PI/4),raggio1,R([1,2])(PI/4),raggio1,R([1,2])(PI/4),
                                             raggio1,R([1,2])(PI/4),raggio1,R([1,2])(PI/4),raggio1,R([1,2])(PI/4),raggio1,R([1,2])(PI/4),]))
ruota3D=STRUCT([cerchioneInterno,cerchioneEsterno,gomma,raggio,cerchionePiccolo])

ruota3Dpos1=T([1,2,3])([8,2,-6])(R([1,3])(PI/2)(S([1,2,3])([0.3,0.3,0.3])(ruota3D)))
ruota3Dpos2=T([1,2,3])([-8,2,-6])(R([1,3])(-PI/2)(S([1,2,3])([0.3,0.3,0.3])(ruota3D)))
ruote3Danteriori=STRUCT([ruota3Dpos1,ruota3Dpos2])
ruote3Dposteriori=T(3)(-17)(ruote3Danteriori)
ruote3D=STRUCT([ruote3Danteriori,ruote3Dposteriori])
exercise03=STRUCT([exercise02,ruote3D])

VIEW(exercise03)







