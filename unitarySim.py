#outputs the matrix representing the quantum circuit
#Does the same thing as IBM qiskit's 'unitary_simulator'

import numpy as np;
import math;


#X gate/Bit-flip/Not
Xgate = np.array([
[0,1],
[1,0]]
);



#Z gate/Phase-flip
Zgate = np.array([
[1,0],
[0,1]]
);

#H gate/Hadamard
Hgate = np.array([
    [1/math.sqrt(2), 1/math.sqrt(2)],
    [1/math.sqrt(2), -1/math.sqrt(2)]
]);

#T gate (missing the imaginary part bc its not letting me put it)
Tgate = np.array([
    [1,0],
    [0,0+math.exp(math.pi/4(1j))]
])

qubitMatrix = np.array([
    [1,0],
    [0,1]
])


def circuitCalc(qubit,gate):
    return gate@qubit

while(True):
    gate = input("Which quantum gate would you like to apply to your single qubit circuit (X, Z, H, T): ");

    if(gate=="X"):
        qubitMatrix = circuitCalc(qubitMatrix,Xgate);
    elif(gate=="Z"):
        qubitMatrix = circuitCalc(qubitMatrix,Zgate);
    elif(gate=="H"):
        qubitMatrix = circuitCalc(qubitMatrix,Hgate);
    else:
        qubitMatrix = circuitCalc(qubitMatrix,Tgate);


    while(True):
        cont = input("Would you like to apply another gate to your quantum circuit? (Y/N): ");

        if(cont=="Y" or cont=="N"):
            break;

    if(cont=="N"):
        print(qubitMatrix)
        break;


#print(qubitMatrix)