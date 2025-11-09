import matplotlib.pyplot as plt



# x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# cite_y = ([0.245, 0.269, 0.273, 0.302, 0.300, 0.310, 0.326, 0.327, 0.305, 0.315, 0.058],[0.232, 0.249, 0.268, 0.291, 0.287, 0.284, 0.289, 0.296, 0.284, 0.290, 0.021],[0.511, 0.563, 0.580, 0.604, 0.598, 0.593, 0.586, 0.599, 0.583, 0.590, 0.290])
# blog_y = ([0.348, 0.342, 0.356, 0.370, 0.375, 0.438, 0.505, 0.523, 0.443, 0.259, 0.202],[0.226, 0.219, 0.229, 0.273, 0.253, 0.297, 0.365, 0.413, 0.361, 0.170, 0.136],[0.511, 0.501, 0.519, 0.562, 0.527, 0.596, 0.651, 0.675, 0.638, 0.454, 0.389])

fig = plt.figure(figsize=(22, 5), dpi=100)

# ax1, ax2, ax3 = fig.subplots(1,3,sharey=True)
plt.subplot(1,3,1)
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
plt.ylim(0.4,1)
# mu1_y = [0.9689,0.9795,0.9757,0.9917,0.9948,1.0,1.0,1.0,0.9983,0.9914,1.0]
# plt.plot(x, mu1_y, label='mu=0.1', linestyle='-', marker='o', color = 'blue' )
# mu2_y = [0.9834,0.9840,0.9896,0.9893,0.9921,0.9911,1.0,0.9930,0.9933,0.9898,0.9981]
# plt.plot(x, mu2_y, label='mu=0.2', linestyle='-', marker='v', color = 'green' )
# mu3_y = [0.9531,0.9672,0.9774,0.9863,0.9757,0.9911,0.9911,0.9927,1.0,0.9955,0.9887]
# plt.plot(x, mu3_y, label='mu=0.3', linestyle='-', marker='+', color = 'red' )
# mu4_y = [0.9790,0.9737,0.9738,0.9798,0.9680,0.9762,0.9784,0.9906,0.9866,0.9743,0.9561]
# plt.plot(x, mu4_y, label='mu=0.4', linestyle='-', marker='*', color = 'black' )
# mu5_y = [0.9522,0.9550,0.9593,0.9741,0.9619,0.9697,0.9870,0.9669,0.9794,0.9836,0.9849]
# plt.plot(x, mu5_y, label='mu=0.5', linestyle='-', marker='p', color = 'brown' )
# mu6_y = [0.9504,0.9524,0.9507,0.9594,0.9691,0.9483,0.9621,0.9581,0.9634,0.9699,0.4355]
# plt.plot(x, mu6_y, label='mu=0.6', linestyle='-', marker='^', color = 'pink' )
# mu7_y = [0.9416,0.9514,0.9498,0.9499,0.9533,0.9720,0.9721,0.9562,0.9775,0.9658,0.4565]
# plt.plot(x, mu7_y, label='mu=0.7', linestyle='-', marker='x', color = 'orange' )
mu1_y = [0.9689,0.9795,0.9757,0.9917,0.9948,1.0,1.0,1.0,0.9983,0.9914,1.0]
plt.plot(x, mu1_y, label='mu=0.1', linestyle='-', color = 'blue',linewidth=0.8 )
mu2_y = [0.9834,0.9840,0.9896,0.9893,0.9921,0.9911,1.0,0.9930,0.9933,0.9898,0.9981]
plt.plot(x, mu2_y, label='mu=0.2', linestyle='-', color = 'green',linewidth=0.8 )
mu3_y = [0.9531,0.9672,0.9774,0.9863,0.9757,0.9911,0.9911,0.9927,1.0,0.9955,0.9887]
plt.plot(x, mu3_y, label='mu=0.3', linestyle='-', color = 'red',linewidth=0.8 )
mu4_y = [0.9790,0.9737,0.9738,0.9798,0.9680,0.9762,0.9784,0.9906,0.9866,0.9743,0.9561]
plt.plot(x, mu4_y, label='mu=0.4', linestyle='-',  color = 'black',linewidth=0.8 )
mu5_y = [0.9522,0.9550,0.9593,0.9741,0.9619,0.9697,0.9870,0.9669,0.9794,0.9836,0.9849]
plt.plot(x, mu5_y, label='mu=0.5', linestyle='-', color = 'brown' ,linewidth=0.8)
mu6_y = [0.9504,0.9524,0.9507,0.9594,0.9691,0.9483,0.9621,0.9581,0.9634,0.9699,0.4355]
plt.plot(x, mu6_y, label='mu=0.6', linestyle='-', color = 'pink' ,linewidth=0.8)
mu7_y = [0.9416,0.9514,0.9498,0.9499,0.9533,0.9720,0.9721,0.9562,0.9775,0.9658,0.4565]
plt.plot(x, mu7_y, label='mu=0.7', linestyle='-', color = 'lightblue' ,linewidth=0.8)

plt.xlabel('α')
plt.ylabel('NMI')

plt.subplot(1,3,2)
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
plt.ylim(0.2,1)
# mu1_y = [0.9615,0.9529,0.9507,0.9767,0.9925,1.0,1.0,1.0,0.9920,0.9903,1.0]
# plt.plot(x, mu1_y, label='mu=0.1', linestyle='-', marker='o', color = 'blue' )
# mu2_y = [0.9777,0.9816,0.9894,0.9880,0.9903,0.9824,1.0,0.9903,0.9928,0.9884,0.9975]
# plt.plot(x, mu2_y, label='mu=0.2', linestyle='-', marker='v', color = 'green' )
# mu3_y = [0.9490,0.9458,0.9768,0.9871,0.9631,0.9899,0.9900,0.9895,1.0,0.9960,0.9858]
# plt.plot(x, mu3_y, label='mu=0.3', linestyle='-', marker='+', color = 'red' )
# mu4_y = [0.9720,0.9547,0.9730,0.9776,0.9576,0.9635,0.9607,0.9769,0.9831,0.9644,0.9381]
# plt.plot(x, mu4_y, label='mu=0.4', linestyle='-', marker='*', color = 'black' )
# mu5_y = [0.9434,0.9496,0.9408,0.9446,0.9490,0.9540,0.9814,0.9345,0.9646,0.9774,0.7080]
# plt.plot(x, mu5_y, label='mu=0.5', linestyle='-', marker='p', color = 'brown' )
# mu6_y = [0.9402,0.9360,0.9435,0.9554,0.9685,0.9376,0.9596,0.9499,0.9487,0.9486,0.2339]
# plt.plot(x, mu6_y, label='mu=0.6', linestyle='-', marker='^', color = 'pink' )
# mu7_y = [0.9342,0.9317,0.9481,0.9447,0.9523,0.9768,0.9718,0.9490,0.9709,0.9400,0.2621]
# plt.plot(x, mu7_y, label='mu=0.7', linestyle='-', marker='x', color = 'orange' )
mu1_y = [0.9615,0.9529,0.9507,0.9767,0.9925,1.0,1.0,1.0,0.9920,0.9903,1.0]
plt.plot(x, mu1_y, label='mu=0.1', linestyle='-',  color = 'blue' ,linewidth=0.8)
mu2_y = [0.9777,0.9816,0.9894,0.9880,0.9903,0.9824,1.0,0.9903,0.9928,0.9884,0.9975]
plt.plot(x, mu2_y, label='mu=0.2', linestyle='-', color = 'green',linewidth=0.8 )
mu3_y = [0.9490,0.9458,0.9768,0.9871,0.9631,0.9899,0.9900,0.9895,1.0,0.9960,0.9858]
plt.plot(x, mu3_y, label='mu=0.3', linestyle='-', color = 'red' ,linewidth=0.8)
mu4_y = [0.9720,0.9547,0.9730,0.9776,0.9576,0.9635,0.9607,0.9769,0.9831,0.9644,0.9381]
plt.plot(x, mu4_y, label='mu=0.4', linestyle='-', color = 'black' ,linewidth=0.8)
mu5_y = [0.9434,0.9496,0.9408,0.9446,0.9490,0.9540,0.9814,0.9345,0.9646,0.9774,0.7080]
plt.plot(x, mu5_y, label='mu=0.5', linestyle='-', color = 'brown' ,linewidth=0.8)
mu6_y = [0.9402,0.9360,0.9435,0.9554,0.9685,0.9376,0.9596,0.9499,0.9487,0.9486,0.2339]
plt.plot(x, mu6_y, label='mu=0.6', linestyle='-', color = 'pink' ,linewidth=0.8)
mu7_y = [0.9342,0.9317,0.9481,0.9447,0.9523,0.9768,0.9718,0.9490,0.9709,0.9400,0.2621]
plt.plot(x, mu7_y, label='mu=0.7', linestyle='-', color = 'lightblue' ,linewidth=0.8)
plt.xlabel('α')
plt.ylabel('ARI')


plt.subplot(1,3,3)
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
plt.ylim(0.5,1)
# mu1_y = [0.977,0.983,0.983,0.985,0.995,1.0,1.0,1.0,0.985,0.985,1.0]
# plt.plot(x, mu1_y, label='mu=0.1', linestyle='-', marker='o', color = 'blue',linewidth=0.1 )
# mu2_y = [0.981,0.982,0.982,0.983,0.984,0.985,1.0,0.985,0.985,0.984,0.999]
# plt.plot(x, mu2_y, label='mu=0.2', linestyle='-', marker='v', color = 'green',linewidth=0.1 )
# mu3_y = [0.952,0.959,0.973,0.98,0.968,0.983,0.983,0.985,1.0,0.985,0.982]
# plt.plot(x, mu3_y, label='mu=0.3', linestyle='-', marker='+', color = 'red' ,linewidth=0.1)
# mu4_y = [0.969,0.978,0.974,0.98,0.967,0.972,0.968,0.985,0.969,0.967,0.976]
# plt.plot(x, mu4_y, label='mu=0.4', linestyle='-', marker='*', color = 'black',linewidth=0.1 )
# mu5_y = [0.94,0.951,0.963,0.98,0.966,0.966,0.989,0.957,0.981,0.985,0.865]
# plt.plot(x, mu5_y, label='mu=0.5', linestyle='-', marker='p', color = 'brown' ,linewidth=0.1)
# mu6_y = [0.933,0.931,0.939,0.944,0.956,0.944,0.953,0.95,0.955,0.944,0.531]
# plt.plot(x, mu6_y, label='mu=0.6', linestyle='-', marker='^', color = 'pink' ,linewidth=0.1)
# mu7_y = [0.928,0.934,0.939,0.938,0.943,0.965,0.965,0.942,0.965,0.944,0.552]
# plt.plot(x, mu7_y, label='mu=0.7', linestyle='-', marker='x', color = 'orange',linewidth=0.1 )
mu1_y = [0.977,0.983,0.983,0.985,0.995,1.0,1.0,1.0,0.985,0.985,1.0]
plt.plot(x, mu1_y, label='mu=0.1', linestyle='-', color = 'blue',linewidth=0.8 )
mu2_y = [0.981,0.982,0.982,0.983,0.984,0.985,1.0,0.985,0.985,0.984,0.999]
plt.plot(x, mu2_y, label='mu=0.2', linestyle='-', color = 'green',linewidth=0.8 )
mu3_y = [0.952,0.959,0.973,0.98,0.968,0.983,0.983,0.985,1.0,0.985,0.982]
plt.plot(x, mu3_y, label='mu=0.3', linestyle='-',  color = 'red' ,linewidth=0.8)
mu4_y = [0.969,0.978,0.974,0.98,0.967,0.972,0.968,0.985,0.969,0.967,0.976]
plt.plot(x, mu4_y, label='mu=0.4', linestyle='-',  color = 'black',linewidth=0.8)
mu5_y = [0.94,0.951,0.963,0.98,0.966,0.966,0.989,0.957,0.981,0.985,0.865]
plt.plot(x, mu5_y, label='mu=0.5', linestyle='-', color = 'brown' ,linewidth=0.8)
mu6_y = [0.933,0.931,0.939,0.944,0.956,0.944,0.953,0.95,0.955,0.944,0.531]
plt.plot(x, mu6_y, label='mu=0.6', linestyle='-', color = 'pink' ,linewidth=0.8)
mu7_y = [0.928,0.934,0.939,0.938,0.943,0.965,0.965,0.942,0.965,0.944,0.552]
plt.plot(x, mu7_y, label='mu=0.7', linestyle='-', color = 'lightblue',linewidth=0.8)
plt.xlabel('α')
plt.ylabel('ACC')


plt.legend(loc='upper center', bbox_to_anchor=(-0.7, 1.1),
          fancybox=True, shadow=True, ncol=7, frameon=False)
# plt.savefig('D:\CodeData\PaperCode\image\LFR-α',dpi=300)
plt.savefig("D:\Research Direction\Paper\SVG\\LFR-α.svg", dpi=300,format="svg")
# plt.show()

'''fig = plt.figure(figsize=(22, 5), dpi=100)

# ax1, ax2, ax3 = fig.subplots(1,3,sharey=True)
plt.subplot(1,3,1)
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
plt.ylim(0.5,1)
# mu1_y = [1.0,1.0,0.9888,0.9938,1.0,1.0,1.0,1.0,0.9922,0.9909,1.0]
# plt.plot(x, mu1_y, label='mu=0.1', linestyle='-', marker='o', color = 'blue' )
# mu2_y = [0.9936,0.9887,0.9949,0.9910,1.0,0.9942,1.0,0.9923,0.9891,0.9928,1.0]
# plt.plot(x, mu2_y, label='mu=0.2', linestyle='-', marker='v', color = 'green' )
# mu3_y = [0.9839,0.9824,0.9820,0.9842,0.9946,0.9859,0.9869,0.9893,0.9850,0.9946,0.9858]
# plt.plot(x, mu3_y, label='mu=0.3', linestyle='-', marker='+', color = 'red' )
# mu4_y = [0.9903,0.9751,0.9714,0.9803,0.9767,0.9818,0.9918,0.9840,0.9848,0.9796,0.9783]
# plt.plot(x, mu4_y, label='mu=0.4', linestyle='-', marker='*', color = 'black' )
# mu5_y = [0.9759,0.9792,0.9711,0.9668,0.9786,0.9797,0.9764,0.9674,0.9736,0.9764,0.9667]
# plt.plot(x, mu5_y, label='mu=0.5', linestyle='-', marker='p', color = 'brown' )
# mu6_y = [0.9609,0.9509,0.9584,0.9695,0.9695,0.9506,0.9571,0.9512,0.9560,0.9578,0.9611]
# plt.plot(x, mu6_y, label='mu=0.6', linestyle='-', marker='^', color = 'pink' )
# mu7_y = [0.9576,0.9527,0.9556,0.9683,0.9572,0.9704,0.9661,0.9650,0.9571,0.9602,0.9675]
# plt.plot(x, mu7_y, label='mu=0.7', linestyle='-', marker='x', color = 'orange' )
mu1_y = [1.0,1.0,0.9888,0.9938,1.0,1.0,1.0,1.0,0.9922,0.9909,1.0]
plt.plot(x, mu1_y, label='mu=0.1', linestyle='-',color = 'blue' ,linewidth=0.8)
mu2_y = [0.9936,0.9887,0.9949,0.9910,1.0,0.9942,1.0,0.9923,0.9891,0.9928,1.0]
plt.plot(x, mu2_y, label='mu=0.2', linestyle='-',  color = 'green' ,linewidth=0.8)
mu3_y = [0.9839,0.9824,0.9820,0.9842,0.9946,0.9859,0.9869,0.9893,0.9850,0.9946,0.9858]
plt.plot(x, mu3_y, label='mu=0.3', linestyle='-', color = 'red' ,linewidth=0.8)
mu4_y = [0.9903,0.9751,0.9714,0.9803,0.9767,0.9818,0.9918,0.9840,0.9848,0.9796,0.9783]
plt.plot(x, mu4_y, label='mu=0.4', linestyle='-', color = 'black',linewidth=0.8 )
mu5_y = [0.9759,0.9792,0.9711,0.9668,0.9786,0.9797,0.9764,0.9674,0.9736,0.9764,0.9667]
plt.plot(x, mu5_y, label='mu=0.5', linestyle='-', color = 'brown' ,linewidth=0.8)
mu6_y = [0.9609,0.9509,0.9584,0.9695,0.9695,0.9506,0.9571,0.9512,0.9560,0.9578,0.9611]
plt.plot(x, mu6_y, label='mu=0.6', linestyle='-', color = 'pink' ,linewidth=0.8)
mu7_y = [0.9576,0.9527,0.9556,0.9683,0.9572,0.9704,0.9661,0.9650,0.9571,0.9602,0.9675]
plt.plot(x, mu7_y, label='mu=0.7', linestyle='-', color = 'lightblue' ,linewidth=0.8)

plt.xlabel('β')
plt.ylabel('NMI')

plt.subplot(1,3,2)
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
plt.ylim(0.5,1)
# mu1_y = [1.0,1.0,0.9833,0.9915,1.0,1.0,1.0,1.0,0.9906,0.9850,1.0]
# plt.plot(x, mu1_y, label='mu=0.1', linestyle='-', marker='o', color = 'blue' )
# mu2_y = [0.9905,0.9831,0.9943,0.9863,1.0,0.9929,1.0,0.9911,0.9894,0.9923,1.0]
# plt.plot(x, mu2_y, label='mu=0.2', linestyle='-', marker='v', color = 'green' )
# mu3_y = [0.9792,0.9811,0.9725,0.9777,0.9935,0.9818,0.9836,0.9883,0.9785,0.9935,0.9819]
# plt.plot(x, mu3_y, label='mu=0.3', linestyle='-', marker='+', color = 'red' )
# mu4_y = [0.9868,0.9532,0.9538,0.9724,0.9583,0.9744,0.9896,0.9814,0.9712,0.9592,0.9703]
# plt.plot(x, mu4_y, label='mu=0.4', linestyle='-', marker='*', color = 'black' )
# mu5_y = [0.9718,0.9743,0.9614,0.9563,0.9746,0.9769,0.9632,0.9517,0.96,0.9631,0.9539]
# plt.plot(x, mu5_y, label='mu=0.5', linestyle='-', marker='p', color = 'brown' )
# mu6_y = [0.9417,0.9389,0.9445,0.9661,0.9662,0.9470,0.9556,0.9430,0.9457,0.9504,0.9641]
# plt.plot(x, mu6_y, label='mu=0.6', linestyle='-', marker='^', color = 'pink' )
# mu7_y = [0.9527,0.9379,0.9475,0.9628,0.9477,0.9644,0.9660,0.9564,0.9474,0.9570,0.9694]
# plt.plot(x, mu7_y, label='mu=0.7', linestyle='-', marker='x', color = 'orange' )
mu1_y = [1.0,1.0,0.9833,0.9915,1.0,1.0,1.0,1.0,0.9906,0.9850,1.0]
plt.plot(x, mu1_y, label='mu=0.1', linestyle='-',color = 'blue',linewidth=0.8 )
mu2_y = [0.9905,0.9831,0.9943,0.9863,1.0,0.9929,1.0,0.9911,0.9894,0.9923,1.0]
plt.plot(x, mu2_y, label='mu=0.2', linestyle='-',color = 'green' ,linewidth=0.8)
mu3_y = [0.9792,0.9811,0.9725,0.9777,0.9935,0.9818,0.9836,0.9883,0.9785,0.9935,0.9819]
plt.plot(x, mu3_y, label='mu=0.3', linestyle='-', color = 'red' ,linewidth=0.8)
mu4_y = [0.9868,0.9532,0.9538,0.9724,0.9583,0.9744,0.9896,0.9814,0.9712,0.9592,0.9703]
plt.plot(x, mu4_y, label='mu=0.4', linestyle='-',color = 'black',linewidth=0.8 )
mu5_y = [0.9718,0.9743,0.9614,0.9563,0.9746,0.9769,0.9632,0.9517,0.96,0.9631,0.9539]
plt.plot(x, mu5_y, label='mu=0.5', linestyle='-',color = 'brown' ,linewidth=0.8)
mu6_y = [0.9417,0.9389,0.9445,0.9661,0.9662,0.9470,0.9556,0.9430,0.9457,0.9504,0.9641]
plt.plot(x, mu6_y, label='mu=0.6', linestyle='-',color = 'pink',linewidth=0.8 )
mu7_y = [0.9527,0.9379,0.9475,0.9628,0.9477,0.9644,0.9660,0.9564,0.9474,0.9570,0.9694]
plt.plot(x, mu7_y, label='mu=0.7', linestyle='-', color = 'lightblue',linewidth=0.8 )
plt.xlabel('β')
plt.ylabel('ARI')


plt.subplot(1,3,3)
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
plt.ylim(0.5,1)
# mu1_y = [1.0,1.0,0.985,0.985,1.0,1.0,1.0,1.0,0.985,0.985,1.0]
# plt.plot(x, mu1_y, label='mu=0.1', linestyle='-', marker='o', color = 'blue' )
# mu2_y = [0.985,0.979,0.985,0.985,1.0,0.985,1.0,0.985,0.985,0.985,1.0]
# plt.plot(x, mu2_y, label='mu=0.2', linestyle='-', marker='v', color = 'green' )
# mu3_y = [0.971,0.983,0.97,0.97,0.985,0.977,0.985,0.972,0.976,0.985,0.969]
# plt.plot(x, mu3_y, label='mu=0.3', linestyle='-', marker='+', color = 'red' )
# mu4_y = [0.985,0.964,0.965,0.966,0.969,0.97,0.978,0.97,0.969,0.969,0.961]
# plt.plot(x, mu4_y, label='mu=0.4', linestyle='-', marker='*', color = 'black' )
# mu5_y = [0.966,0.97,0.96,0.97,0.969,0.977,0.976,0.96,0.968,0.968,0.957]
# plt.plot(x, mu5_y, label='mu=0.5', linestyle='-', marker='p', color = 'brown' )
# mu6_y = [0.945,0.935,0.942,0.952,0.958,0.937,0.949,0.943,0.946,0.941,0.955]
# plt.plot(x, mu6_y, label='mu=0.6', linestyle='-', marker='^', color = 'pink' )
# mu7_y = [0.948,0.938,0.94,0.952,0.949,0.946,0.959,0.957,0.945,0.945,0.964]
# plt.plot(x, mu7_y, label='mu=0.7', linestyle='-', marker='x', color = 'orange' )
mu1_y = [1.0,1.0,0.985,0.985,1.0,1.0,1.0,1.0,0.985,0.985,1.0]
plt.plot(x, mu1_y, label='mu=0.1', linestyle='-',color = 'blue',linewidth=0.8 )
mu2_y = [0.985,0.979,0.985,0.985,1.0,0.985,1.0,0.985,0.985,0.985,1.0]
plt.plot(x, mu2_y, label='mu=0.2', linestyle='-', color = 'green' ,linewidth=0.8)
mu3_y = [0.971,0.983,0.97,0.97,0.985,0.977,0.985,0.972,0.976,0.985,0.969]
plt.plot(x, mu3_y, label='mu=0.3', linestyle='-',  color = 'red',linewidth=0.8 )
mu4_y = [0.985,0.964,0.965,0.966,0.969,0.97,0.978,0.97,0.969,0.969,0.961]
plt.plot(x, mu4_y, label='mu=0.4', linestyle='-',  color = 'black' ,linewidth=0.8)
mu5_y = [0.966,0.97,0.96,0.97,0.969,0.977,0.976,0.96,0.968,0.968,0.957]
plt.plot(x, mu5_y, label='mu=0.5', linestyle='-', color = 'brown',linewidth=0.8 )
mu6_y = [0.945,0.935,0.942,0.952,0.958,0.937,0.949,0.943,0.946,0.941,0.955]
plt.plot(x, mu6_y, label='mu=0.6', linestyle='-',  color = 'pink',linewidth=0.8 )
mu7_y = [0.948,0.938,0.94,0.952,0.949,0.946,0.959,0.957,0.945,0.945,0.964]
plt.plot(x, mu7_y, label='mu=0.7', linestyle='-',  color = 'lightblue' ,linewidth=0.8)
plt.xlabel('β')
plt.ylabel('ACC')


plt.legend(loc='upper center', bbox_to_anchor=(-0.7, 1.1),
          fancybox=True, shadow=True, ncol=7, frameon=False)
# plt.savefig('D:\CodeData\PaperCode\image\LFR-β',dpi=300)
plt.savefig("D:\Research Direction\Paper\SVG\\LFR-β.svg", dpi=300,format="svg")
# plt.show()'''

'''fig = plt.figure(figsize=(22, 5), dpi=100)

# ax1, ax2, ax3 = fig.subplots(1,3,sharey=True)
plt.subplot(1,3,1)
x = [16,32,64,128,256,512]
plt.ylim(0.5,1.01)
# mu1_y = [1.0,1.0,1.0,1.0,1.0,1.0]
# plt.plot(x, mu1_y, label='mu=0.1', linestyle='-', marker='o', color = 'blue' )
# mu2_y = [1.0,1.0,1.0,1.0,0.9906,0.9928]
# plt.plot(x, mu2_y, label='mu=0.2', linestyle='-', marker='v', color = 'green' )
# mu3_y = [1.0,0.9926,0.9929,0.9781,0.9851,0.9778]
# plt.plot(x, mu3_y, label='mu=0.3', linestyle='-', marker='+', color = 'red' )
# mu4_y = [0.9985,0.9981,0.9933,0.9888,0.9791,0.9732]
# plt.plot(x, mu4_y, label='mu=0.4', linestyle='-', marker='*', color = 'black' )
# mu5_y = [0.9903,0.9860,0.9736,0.9738,0.9687,0.9732]
# plt.plot(x, mu5_y, label='mu=0.5', linestyle='-', marker='p', color = 'brown' )
# mu6_y = [0.9841,0.9768,0.9605,0.9592,0.9578,0.9499]
# plt.plot(x, mu6_y, label='mu=0.6', linestyle='-', marker='^', color = 'pink' )
# mu7_y = [0.9778,0.9737,0.9597,0.9536,0.9581,0.9685]
# plt.plot(x, mu7_y, label='mu=0.7', linestyle='-', marker='x', color = 'orange' )
mu1_y = [1.0,1.0,1.0,1.0,1.0,1.0]
plt.plot(x, mu1_y, label='mu=0.1', linestyle='-',  color = 'blue' ,linewidth=0.8)
mu2_y = [1.0,1.0,1.0,1.0,0.9906,0.9928]
plt.plot(x, mu2_y, label='mu=0.2', linestyle='-', color = 'green' ,linewidth=0.8)
mu3_y = [1.0,0.9926,0.9929,0.9781,0.9851,0.9778]
plt.plot(x, mu3_y, label='mu=0.3', linestyle='-', color = 'red' ,linewidth=0.8)
mu4_y = [0.9985,0.9981,0.9933,0.9888,0.9791,0.9732]
plt.plot(x, mu4_y, label='mu=0.4', linestyle='-', color = 'black' ,linewidth=0.8)
mu5_y = [0.9903,0.9860,0.9736,0.9738,0.9687,0.9732]
plt.plot(x, mu5_y, label='mu=0.5', linestyle='-',  color = 'brown' ,linewidth=0.8)
mu6_y = [0.9841,0.9768,0.9605,0.9592,0.9578,0.9499]
plt.plot(x, mu6_y, label='mu=0.6', linestyle='-', color = 'pink' ,linewidth=0.8)
mu7_y = [0.9778,0.9737,0.9597,0.9536,0.9581,0.9685]
plt.plot(x, mu7_y, label='mu=0.7', linestyle='-',  color = 'lightblue',linewidth=0.8 )

plt.xlabel('d')
plt.ylabel('NMI')

plt.subplot(1,3,2)
x = [16,32,64,128,256,512]
plt.ylim(0.5,1.01)
# mu1_y = [1.0,1.0,1.0,1.0,1.0,1.0]
# plt.plot(x, mu1_y, label='mu=0.1', linestyle='-', marker='o', color = 'blue' )
# mu2_y = [1.0,1.0,1.0,1.0,0.9833,0.9895]
# plt.plot(x, mu2_y, label='mu=0.2', linestyle='-', marker='v', color = 'green' )
# mu3_y = [1.0,0.9922,0.9923,0.9687,0.9845,0.9638]
# plt.plot(x, mu3_y, label='mu=0.3', linestyle='-', marker='+', color = 'red' )
# mu4_y = [0.9981,0.9977,0.9931,0.9843,0.9621,0.9581]
# plt.plot(x, mu4_y, label='mu=0.4', linestyle='-', marker='*', color = 'black' )
# mu5_y = [0.9902,0.9837,0.9653,0.9489,0.9616,0.9591]
# plt.plot(x, mu5_y, label='mu=0.5', linestyle='-', marker='p', color = 'brown' )
# mu6_y = [0.9869,0.9806,0.9568,0.9550,0.9569,0.9407]
# plt.plot(x, mu6_y, label='mu=0.6', linestyle='-', marker='^', color = 'pink' )
# mu7_y = [0.9819,0.9664,0.9579,0.9452,0.9451,0.9490]
# plt.plot(x, mu7_y, label='mu=0.7', linestyle='-', marker='x', color = 'orange' )
mu1_y = [1.0,1.0,1.0,1.0,1.0,1.0]
plt.plot(x, mu1_y, label='mu=0.1', linestyle='-',color = 'blue',linewidth=0.8 )
mu2_y = [1.0,1.0,1.0,1.0,0.9833,0.9895]
plt.plot(x, mu2_y, label='mu=0.2', linestyle='-', color = 'green' ,linewidth=0.8)
mu3_y = [1.0,0.9922,0.9923,0.9687,0.9845,0.9638]
plt.plot(x, mu3_y, label='mu=0.3', linestyle='-',  color = 'red' ,linewidth=0.8)
mu4_y = [0.9981,0.9977,0.9931,0.9843,0.9621,0.9581]
plt.plot(x, mu4_y, label='mu=0.4', linestyle='-',  color = 'black' ,linewidth=0.8)
mu5_y = [0.9902,0.9837,0.9653,0.9489,0.9616,0.9591]
plt.plot(x, mu5_y, label='mu=0.5', linestyle='-',  color = 'brown' ,linewidth=0.8)
mu6_y = [0.9869,0.9806,0.9568,0.9550,0.9569,0.9407]
plt.plot(x, mu6_y, label='mu=0.6', linestyle='-',color = 'pink' ,linewidth=0.8)
mu7_y = [0.9819,0.9664,0.9579,0.9452,0.9451,0.9490]
plt.plot(x, mu7_y, label='mu=0.7', linestyle='-', color = 'lightblue' ,linewidth=0.8)
plt.xlabel('d')
plt.ylabel('ARI')


plt.subplot(1,3,3)
x = [16,32,64,128,256,512]
plt.ylim(0.5,1.01)
# mu1_y = [1.0,1.0,1.0,1.0,1.0,1.0]
# plt.plot(x, mu1_y, label='mu=0.1', linestyle='-', marker='o', color = 'blue' )
# mu2_y = [1.0,1.0,1.0,1.0,0.985,0.979]
# plt.plot(x, mu2_y, label='mu=0.2', linestyle='-', marker='v', color = 'green' )
# mu3_y = [1.0,0.984,0.984,0.97,0.969,0.97]
# plt.plot(x, mu3_y, label='mu=0.3', linestyle='-', marker='+', color = 'red' )
# mu4_y = [0.999,0.999,0.985,0.985,0.963,0.969]
# plt.plot(x, mu4_y, label='mu=0.4', linestyle='-', marker='*', color = 'black' )
# mu5_y = [0.994,0.991,0.976,0.968,0.953,0.971]
# plt.plot(x, mu5_y, label='mu=0.5', linestyle='-', marker='p', color = 'brown' )
# mu6_y = [0.987,0.975,0.962,0.948,0.944,0.931]
# plt.plot(x, mu6_y, label='mu=0.6', linestyle='-', marker='^', color = 'pink' )
# mu7_y = [0.982,0.974,0.962,0.96,0.946,0.943]
# plt.plot(x, mu7_y, label='mu=0.7', linestyle='-', marker='x', color = 'orange' )
mu1_y = [1.0,1.0,1.0,1.0,1.0,1.0]
plt.plot(x, mu1_y, label='mu=0.1', linestyle='-', color = 'blue' ,linewidth=0.8)
mu2_y = [1.0,1.0,1.0,1.0,0.985,0.979]
plt.plot(x, mu2_y, label='mu=0.2', linestyle='-', color = 'green' ,linewidth=0.8)
mu3_y = [1.0,0.984,0.984,0.97,0.969,0.97]
plt.plot(x, mu3_y, label='mu=0.3', linestyle='-', color = 'red' ,linewidth=0.8)
mu4_y = [0.999,0.999,0.985,0.985,0.963,0.969]
plt.plot(x, mu4_y, label='mu=0.4', linestyle='-',  color = 'black' ,linewidth=0.8)
mu5_y = [0.994,0.991,0.976,0.968,0.953,0.971]
plt.plot(x, mu5_y, label='mu=0.5', linestyle='-',  color = 'brown' ,linewidth=0.8)
mu6_y = [0.987,0.975,0.962,0.948,0.944,0.931]
plt.plot(x, mu6_y, label='mu=0.6', linestyle='-', color = 'pink' ,linewidth=0.8)
mu7_y = [0.982,0.974,0.962,0.96,0.946,0.943]
plt.plot(x, mu7_y, label='mu=0.7', linestyle='-',  color = 'lightblue' ,linewidth=0.8)
plt.xlabel('d')
plt.ylabel('ACC')


plt.legend(loc='upper center', bbox_to_anchor=(-0.7, 1.1),
          fancybox=True, shadow=True, ncol=7, frameon=False)
# plt.savefig('D:\CodeData\PaperCode\image\LFR-d',dpi=300)
plt.savefig("D:\Research Direction\Paper\SVG\\LFR-d.svg", dpi=300,format="svg")
# plt.show()'''