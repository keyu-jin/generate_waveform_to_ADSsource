import os
from tqdm import tqdm
import pathlib
import math
import numpy as np

def gaussian(x,H,A,x0,sigma):#可直接输入numpy数组
    return H + A*np.exp(-(x - x0)**2 / (2*sigma**2))

directory = r'E:\learningNeedSoftware\EDA\ADS\sw\bin\time_reflection_wrk'
filename = 'guassian_pulse'
extendname = '.tim'

start_time = 0
stop_time = 30e-9
timestep = 10e-15

dc = 0 #信号直流偏置
sigma = math.sqrt(2*math.log(2,math.e))/(0.35*math.pi) * 1e-9 #信号方差 #1.0708035721673005e-09
Amp = 1 #信号最大振幅
mu = 10e-9 #信号延时


filepath = pathlib.Path(directory)/(filename + extendname)
time = np.arange(start_time,stop_time,timestep)
x = gaussian(time,dc,Amp,mu,sigma)

with tqdm(total=len(time),desc='processing') as pbar:
    with filepath.open(mode='w',encoding='utf-8') as f:
        f.write('BEGIN ' + 'TIMEDATA' + '\n')
        f.write('% time(s)' + '\t' + 'Amp(V)\n')
        for t,output in zip(time,x):
            #output = gaussian(time,dc,Amp,mu,sigma)
            f.write('\t' + str(t) + '\t' + str(output) + '\n')
            pbar.update(1)
        f.write('END')

print(f'file: {filepath.name} has been created at {filepath.parent}')