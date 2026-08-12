import numpy as np

#activation function
def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1-s)

np.random.seed(42)

#weights

w1 = np.random.randn(2,4)*0.1
b1 = np.zeros((1,4))

w2 = np.random.randn(4,1)*0.1
b2 = np.zeros((1,1))

x = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])

y = np.array([[0],
              [1],
              [1],
              [0]])

learning_rate = 0.1

for epoch in range(500000):

    #forward pass

    #layer 1  
    z1 = x @ w1+b1
    a1 = sigmoid(z1)

    #layer 2
    z2 = a1 @ w2+b2
    a2 = sigmoid(z2)

    #loss mse
    loss = np.mean((y-a2)**2)

    #backward pass

      #how much loss change wrt a2
    dloss_da2 = -2*(y-a2)/len(y)

      #how much did a2 change wrt z2
    da2_az2 = sigmoid_derivative(z2)

      #chain rule
    dz2 = dloss_da2 * da2_az2

      #how much did z2 change wrt to w2 and b2
    dw2 = a1.T @ dz2
    db2 = np.sum(dz2, axis=0, keepdims=True)

      #going back thru layer 1
    da1 = dz2 @ w2.T
    dz1 = da1 * sigmoid_derivative(z1)

      # how much z1 change wrt to w1 and b1
    dw1 = x.T @ dz1
    db1 = np.sum(dz1, axis=0, keepdims=True)

    w2 -= learning_rate*dw2
    b2 -= learning_rate*db2

    w1 -= learning_rate*dw1
    b1 -= learning_rate*db1

    if epoch % 1000 == 0:
        print(f"epoch {epoch:6d}| loss: {loss:.6f}")



print("\nfinal prediction:")
print(a2.round(3))
print("\n expected: ")
print(y)
