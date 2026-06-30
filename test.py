import torch
from torch import nn
a = torch.__version__
print(a)
device = "cuda" if torch.cuda.is_available() else "illada kutta"
print(device)