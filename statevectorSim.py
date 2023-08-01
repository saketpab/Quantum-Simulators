#outputs the state vector
#does the same thing as IBM qiskit's statevector simulator, except it outputs the statevextor in a different form 

import numpy as np;
import math;

cont="";


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
    [0,math.exp(1*(math.pi/4))]
])

#input value of the bit, which can be 0 or 1
qubitValue = input("Enter the starting value of your qubit (0 or 1): ");

while(True):
    if(qubitValue == "0"):
        qubitMatrix= np.array([[1],[0]]);
        break;
    elif(qubitValue=="1"):
        qubitMatrix = np.array([[0],[1]]);
        break;
    else:
        qubitValue = input("Enter the starting value of your qubit (0 or 1): ");


def circuitCalc(qubit,gate):
    return gate@qubit

#

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
    
    #print(qubitMatrix[0][0].type())
    





    while(True):
        cont = input("Would you like to apply another gate to your quantum circuit? (Y/N): ");

        if(cont=="Y" or cont=="N"):
            break;

    if(cont=="N"):
        num = round(qubitMatrix[0][0],3)
        print(qubitMatrix)
        print(num, end="")
        print("|0> ", end="")
        print("+ ", end="")
        print(round(qubitMatrix[1][0],3), end="")
        print("|1>")
        break;




    














       










