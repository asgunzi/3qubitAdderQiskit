# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:24:40 2020

@author: asgun
"""

from qiskit import *

qin = QuantumRegister(9)
qsum = QuantumRegister(3)

cout = ClassicalRegister(3)

qc = QuantumCircuit(qin, qsum, cout)

 

#Inicialização 
# se tem x, inicializa com 1
qc.x(qin[0])
# qc.x(qin[1])
qc.x(qin[2])
qc.x(qin[3])
# qc.x(qin[4])
qc.x(qin[5])
qc.x(qin[6])
qc.x(qin[7])
qc.x(qin[8])



#Circuito somador
for i in range(9):
    qc.cx(qin[i],qsum[0])

    if i>1 and i<8:
        qc.mct([qin[i+1],qsum[0],qsum[1]], qsum[2])

    if i<8:
        qc.ccx(qin[i+1],qsum[0],qsum[1])
    

qc.measure(qsum[:],cout[:])
        
#print(qc)
qc.draw(output = 'mpl')     
        
        
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=99)
result = job.result()
count =result.get_counts()
print(count)

