import torch
import matplotlib.pyplot as plt

x = torch.linspace(-10, 10, 100)
y = x**2 + 2*x + 45

plt.plot(x.numpy(), y.numpy())
plt.title("y = x^2 + 2x + 45")
plt.xlabel("x")
plt.ylabel("y")
plt.show()