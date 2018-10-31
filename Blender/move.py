import bge

ctl = bge.logic.getCurrentController().owner

#esquerda
praesq = ctl.sensors["Esq"]
praesqm = ctl.sensors["MouseEsq"]

#cima
pracima = ctl.sensors["Cima"]
pracimam = ctl.sensors["MouseCima"]

#direita
pradir = ctl.sensors["Dir"]
pracdirm = ctl.sensors["MouseDir"]

#baixo
prabaixo = ctl.sensors["Baixo"]
prabaixom = ctl.sensors["MouseBaixo"]

if praesq.positive or praesqm.positive:
    ctl.worldPosition[0] -= 0.1
elif pracima.positive or pracimam.positive:
    ctl.worldPosition[1] -= 0.3
elif pradir.positive or pradirm.positive:
    ctl.worldPosition[0] -= 0.1
elif prabaixo.positive or prabaixom.positive:
    ctl.worldPosition[1] -= 0.3