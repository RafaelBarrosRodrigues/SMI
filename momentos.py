import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
from pyparsing import line

plt.rcParams.update({'font.size': 24})
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams['font.sans-serif'] = ['Ubuntu Mono']

lTime = 0 #editar
lastTime = str(lTime) 
path_1 = 'postProcessing/forces/'+lastTime+'/moment.dat'

# time_avg = 1240
blank_iterations = 0

fig = plt.figure(figsize=(16, 8))

ax1 = fig.add_subplot(1,1,1)

#ax3 = fig.add_subplot(2,2,3)

# graph 0
graph_data = open(path_1, 'r').read()
lines = graph_data.split('\n')
# line = lines[6]
# print(line)
# lista = line.split('\t')
# print(lista)
for j in range(4+blank_iterations):
    lines[j] = []
xs = []
mx = []
my = []
mz = []
for line in lines:
	if len(line) > 1:
            line = line.split()
            # print(line)
            xs.append(int(line[0]))
            Ft = float(line[1])/1000
            mx.append(float(Ft))
            
            
ax1.clear()
ax1.plot(xs, mx, 'darkblue', linestyle="-", linewidth=4, ) #label=r'Pressão [kPa]'

t_lim = 1

time_avg = xs[-t_lim]

def Average(lst):
    return sum(lst) / len(lst)

flow_avg = Average(mx[-t_lim:])

ax1.plot([time_avg,xs[-1]],[flow_avg,flow_avg],'-r',linewidth=2,label=r'Average Torque = '+'{:.2f}'.format(flow_avg) +'[kN.m]')
#ax1.plot([time_avg,xs[-1]],[flow_avg,flow_avg],'-r',linewidth=2,label=r'Pressão média = '+'{:.2f}'.format(flow_avg) +'[kPa]')


ax1.grid(True, linestyle='-.')

#ax1.set_ylim(100, 200)
# ax1.set_xlim(0, 1)


ax1.set_xlabel(r'Iteration')
ax1.set_ylabel(r'Torque in x [kN.m]')
# plt.title('Torque(x) em função das iterações')
ax1.legend()
plt.savefig('momento_x.png', dpi=fig.dpi)
# plt.show()




