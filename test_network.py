#coding=utf-8
#!/usr/bin/env python

from network import *
from mnist_loader import *

def gradient_check(network,sample_feature,sample_label):
    '''
    梯度检查
    :param network: 神经网络
    :param sample_feature: 样本的特性
    :param sampe_label: 样本的标签
    :return:
    '''
    #计算网络误差
    network_error= lambda vec1,vec2:\
        0.5 * reduce(lambda a,b:a+b,
                     map(lambda v: (v[0] - v[1]) * (v[0] -v[1]) ,
                         zip(vec1,vec2)))

    #获得网络在当前样本下的每个连接的梯度
    network.get_gradient(sample_feature,sample_label)

    #对每个权重做梯度检查
    epsilon = 0.0001
    for conn in network.connections.connections:
        # 获得指定连接的梯度
        actual_gradient = conn.get_gradient()

        #增加一个很小的值，计算网络误差
        conn.weight +=epsilon
        error1 = network_error(network.predict(sample_feature),sample_label)

        #减少一个很小的值，计算网络误差
        conn.weight -= 2*epsilon
        error2 = network_error(network.predict(sample_feature),sample_label)

        #根据公式计算预期的梯度值
        except_gradient = (error2-error1) / (2* epsilon)

        #打印
        print 'excepted gradient: \t%f\nactual gradient: \t%f' %(
            except_gradient,actual_gradient)

def get_training_data_set():
    '''
    获得训练数据
    :return:
    '''
    image_loader = ImageLoader('mnist/train-images.idx3-ubyte',60000)
    label_loader = LabelLoader('mnist/train-labels.idx1-ubyte',60000)
    return image_loader.load(),label_loader.load()

def get_test_data_set():
    '''
    获得测试数据
    :return:
    '''
    image_loader = ImageLoader('mnist/t10k-images.idx3-ubyte', 10000)
    label_loader = LabelLoader('mnist/t10k-labels.idx1-ubyte', 10000)
    return image_loader.load(), label_loader.load()

def get_result(vec):
    #vec是一个10纬向量
    max_value_index = 0
    max_value = 0
    for index in range(len(vec)):
        if(vec[i]>max_value):
            max_value = vec[i]
            max_value_index = i
    return max_value_index

def evaluate(network,test_data_set,test_labels):
    '''
    测试神经网络的错误率
    :param network:
    :param test_data_set:
    :param test_labels:
    :return:
    '''
    correct = 0
    total = len(test_data_set)
    for i in range(total):
        label = get_result(test_labels[i])
        predict = get_result(network.predict(test_data_set[i]))
        if label == predict:
            correct +=1
    return float(correct)/float(total)

def train_and_evaluate():
    last_error_ratio = 1.0
    epoch = 0
    train_data_set,train_labels = get_training_data_set()
    test_data_set,test_labels = get_test_data_set()
    network = Network([784,300,10])
    while True:
        epoch += 10
        network.train(train_labels,train_data_set,0.1,10)
        error_ratio = evaluate(network,test_data_set,test_labels)
        print 'after apoch %d,error ratio is %f' % (epoch,error_ratio)

        if error_ratio > last_error_ratio:
            break
        else:
            last_error_ratio = error_ratio
def test_network():
    image_loader = ImageLoader('mnist/t10k-images.idx3-ubyte', 10)
    label_loader = LabelLoader('mnist/t10k-labels.idx1-ubyte', 10)
    input_vecs = image_loader.load()
    lables = label_loader.load()
    network = Network([784, 300, 10])
    for i in range(len(input_vecs)):
        gradient_check(network,input_vecs[i],lables[i])

if __name__ == '__main__':
    test_network()
    #train_and_evaluate()












