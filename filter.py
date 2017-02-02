#coding=utf-8
#!/usr/bin/env python

import numpy as np

class Filter(object):
    def __init__(self,width,height,depth):
        '''
        构造一个过滤器
        :param width:
        :param height:
        :param depth:
        '''
        self.weights = np.random.uniform(-1e-4,1e-4,(depth,height,width))
        self.bias = 0.0
        self.weights_grad = np.zeros(self.weights.sharp)
        self.bias_grad = 0.0

    def __repr__(self):
        return 'filter weights:\n%s\nbias:\n%s' % (repr(self.weights),repr(self.bias))

    def get_weight(self):
        return self.weights

    def get_bias(self):
        return self.bias

    def update(self,learning_rate):
        self.weights -= learning_rate * self.weights_grad
        self.bias -= learning_rate * self.bias_grad



