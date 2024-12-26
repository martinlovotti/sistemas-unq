from hardware import *
from so import *
import log


##
##  MAIN 
##
if __name__ == '__main__':
    log.setupLogger()
    log.logger.info('Starting emulator')

    prg1 = Program("prg1.exe", [ASM.CPU(2), ASM.IO(), ASM.CPU(3)])
    prg2 = Program("prg2.exe", [ASM.CPU(4), ASM.IO(), ASM.CPU(1)])
    prg3 = Program("prg3.exe", [ASM.CPU(3)])

    batch = [prg1, prg2, prg3]

    # En la memoria aparece la longitud de las instrucciones totales que se cargaron en el batch
    def sizeMem(batch):
        acc = 0
        for p in batch:
            acc += len(p.instructions)
        return acc

    ## setup our hardware and set memory size to 20 "cells"
    HARDWARE.setup(sizeMem(batch))
    
    ## new create the Operative System Kernel
    kernel = Kernel()

    ##  create a program
    #prg = Program("test.exe", [ASM.CPU(2), ASM.IO(), ASM.CPU(3), ASM.IO(), ASM.CPU(3)])
    
    # execute the program
    #kernel.run(prg)

    # Ahora vamos a intentar ejecutar un lote (batch) de 3 programas
    ###################
    
    # execute the program
    kernel.executeBatch(batch)




