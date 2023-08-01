import numpy as np;



#value of 0
qubitMatrix= np.array([[0],[1]]);

#X gate/Bit-flip/Not
Xgate = np.array([
[0,1],
[1,0]]
);


def circuitCalc(qubit,gate):
    #return np.multiply(qubit,gate)
    return gate@qubit



print(circuitCalc(qubitMatrix,Xgate))
#print(qubitMatrix)


