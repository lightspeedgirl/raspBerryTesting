from gpiozero import LEDBoard
from time import sleep
leds=LEDBoard(23,24,25,4)
bincounter = 1
while bincounter <= 15:
        myTempString="000"+str(bin(bincounter))[2:]
        leds.value=(int(myTempString[-4]),int(myTempString[-3]),int(myTempString[-2]),int(myTempString[-1]))
        sleep(1)
        bincounter+=1
