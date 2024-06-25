import torch

class Softmax:
    def __init__(self):
        pass
    
    def softmax_stable(self, x):
        exps = torch.exp(x - torch.max(x))
        return exps / exps.sum()
    
    def softmax(self, x):
        exps = torch.exp(x)
        return exps / exps.sum()
      

# Test
data = torch.tensor([1,2,3])
softmax = Softmax()
print(softmax.softmax(data))
print(softmax.softmax_stable(data))