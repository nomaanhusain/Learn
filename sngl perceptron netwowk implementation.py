import numpy as np
class NeuralNetwork():
    def __init__(self):
        np.random.seed(1)
        self.synaptic_wt=2*np.random.random((3,1)) -1

    def sigmoid(self,x):
        return 1/(1+ np.exp(-x))

    def sigmoid_derivative(self,x):
        return x*(1-x)
    def train(self,trn_in,trn_out,iter):
        for itr in range(70000):
            output=self.think(trn_in)
            error=trn_out-output

            adj=np.dot(trn_in.T, error * self.sigmoid_derivative(output))
            self.synaptic_wt+=adj

    def think(self,inputs):
        inputs=inputs.astype(float)
        output=self.sigmoid(np.dot(inputs,self.synaptic_wt))
        return output[0]

if __name__=="__main__":
    neuralnet=NeuralNetwork()
    trn_data= np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
    trn_output=np.array([[0,1,1,0]]).T
    print("##### Neural Network Model Data #####")
    print('   Random synaptic weights are :')
    print(neuralnet.synaptic_wt)
    print("   Traning for new weights ........")
    neuralnet.train(trn_data,trn_output,50000)

    print("   Synaptic weights after training")
    print(neuralnet.synaptic_wt)
    print("###### End of Model Generation #####")
    A=str(input("Input 1: "))
    B=str(input("Input 2: "))
    C=str(input("Input 3: "))
    print("New Situation : ", A ,B ,C)
    print()
    print("Output : ",int(neuralnet.think(np.array([A ,B ,C]))))