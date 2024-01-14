import matplotlib.pyplot as plt

x_axis = ["D1", "D2", "D6", "D9"]

flash_fc1x10 = [337053/1024.0, 337405/1024.0, 338045/1024.0, 339757/1024.0]

flash_fc10_50 = [340061/1024.0, 340413/1024.0, 340893/1024.0, 343885/1024.0]

flash_fc10_10 = [343965/1024.0, 344317/1024.0, 344957/1024.0, 346669/1024.0]


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