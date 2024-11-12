import control as ct
import matplotlib.pyplot as plt
import scipy
# Define the transfer function
num = [0, 4 ,60]
den = [1, 3, 5]
tf = ct.TransferFunction(num, den)
print(tf)

inv = 



# Compute the step response
# time, response = ct.step_response(tf)

# v = ct.step_info(tf)
# print(v)

# a , b = ct.step_response(tf)
# plt.plot(a,b)
# plt.show()
