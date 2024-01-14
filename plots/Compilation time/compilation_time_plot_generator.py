import matplotlib.pyplot as plt

x_axis = ["D1", "D2", "D6", "D9"]

flash_fc1x10 = [15.3, 14.9, 15.4, 15.6]

flash_fc10_50 = [14.7, 14.8, 15.8, 15.1]

flash_fc10_10 = [14.2, 14.8, 14.4, 14.6]


fig, (ax1) = plt.subplots(1, figsize=(8, 3.5))
plt.yscale("linear")
ax1.plot(x_axis, flash_fc1x10, '^C0')
ax1.plot(x_axis, flash_fc1x10, 'C0')

ax1.plot(x_axis, flash_fc10_50, 'sC1')
ax1.plot(x_axis, flash_fc10_50, 'C1')

ax1.plot(x_axis, flash_fc10_10, 'oC2')
ax1.plot(x_axis, flash_fc10_10, 'C2')


ax1.grid(color ='grey', linestyle='-', linewidth = 0.25, alpha = 0.5)

plt.show()