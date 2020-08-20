import sklearn.metrics
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import pandas as pd
import networkx as nx
import matplotlib
import pickle
import sklearn.ensemble
import sklearn.neural_network
import datetime


def count_classification_metrics(y_true, y_pred):
    metrics = {}
    averages = ['micro', 'macro', 'weighted']
    name = 'test'

    metrics[f'{name}_accuracy'] = sklearn.metrics.accuracy_score(y_true, y_pred)
    for average in averages:
        metrics[f'{name}_f1_{average}'] = sklearn.metrics.f1_score(y_true, y_pred, average=average)
        metrics[f'{name}_recall_{average}'] = sklearn.metrics.recall_score(y_true, y_pred,
                                                           average=average)
        metrics[f'{name}_precision_{average}'] = sklearn.metrics.precision_score(y_true, y_pred,
                                                              average=average)
        
#         for i in list(set(y_true)):
#             metrics[f'{name}_f1_class_{i}_{average}'] = sklearn.metrics.f1_score(y_true, y_pred,
#                                                            average=average,
#                                                            labels=[i])
#             metrics[f'{name}_precision_class_{i}_{average}'] = sklearn.metrics.precision_score(y_true, y_pred,
#                                                                   average=average,
#                                                                   labels=[i])
#             metrics[f'{name}_recall_class_{i}_{average}'] = sklearn.metrics.recall_score(y_true, y_pred,
#                                                                average=average,
#                                                                labels=[i])
    return metrics


def count_confusion_matrix(y_true, y_pred):
    return sklearn.metrics.confusion_matrix(y_true, y_pred)


def plot_confusion_matrix(y_test, y_pred):
    conf_matrix = sklearn.metrics.confusion_matrix(y_true=y_test, y_pred=y_pred)
    conf_matrix = np.around(conf_matrix.astype('float') / conf_matrix.sum(axis=1)[:, np.newaxis], decimals=2)

    fig, ax = plt.subplots(figsize=(8,8))   
    ax = sns.heatmap(conf_matrix, cmap="PiYG", annot=True, center=0)
    
    
def get_next_params(params):
    new_params = {}
    res = list(itertools.product(*params.values()))
    for values in res:
        for key, value in zip(itertools.cycle(params.keys()), values):
            new_params[key] = value

        yield(new_params)
        
        
def uncover_nodes(G, nodes_to_uncover):
    attrs = {}
    for node in nodes_to_uncover:
        attrs[node] = {'class': G.nodes[node]['true_class']}
    nx.set_node_attributes(G, attrs)
    
    
def print_nodes(G):
    for node in G.nodes:
        print(node, G.nodes[node])
        
        
def set_class_node_attribute(G, node, neighbour, class_name):
     if class_name in G.nodes[neighbour]:
        true_class = int(G.nodes[neighbour][class_name])
        if f'num_{true_class}' in G.nodes[node]:
            new_value = G.nodes[node][f'num_{true_class}'] + 1
        else:
            new_value = 1
        nx.set_node_attributes(G, {node: {f'num_{true_class}': new_value}})

        
def set_node_attribute(G, node, neighbour):
    set_class_node_attribute(G, node, neighbour, 'class')
    set_class_node_attribute(G, node, neighbour, 'pred_class')
    
    
def set_all_class_node_attrs(G):
    for node in G.nodes:
        nx.set_node_attributes(G, {node: {'num_0': 0, 'num_1': 0, 'num_2': 0}})

    for node in G.nodes:
        for source, dest in G.edges(node):
            if source == node:
                set_node_attribute(G, node, dest)
#             elif dest == node:
#                 set_node_attribute(G, node, source)


def remove_unimportant_columns(df: pd.DataFrame):
    columns_to_drop = ['class', 'true_class', 'pred_class']

    for column in columns_to_drop:
        if column in df.columns:
            df = df.drop(columns=column)
    return df


def create_df(G, idxs):
    df_train = pd.DataFrame()
    df_test = pd.DataFrame()
    for node in G.nodes:
        if node in idxs:
            df_train = df_train.append(G.nodes[node], ignore_index=True)
        else:
            df_test = df_test.append(G.nodes[node], ignore_index=True)

    df_train.set_index('node', drop=True, inplace=True)
    df_test.set_index('node', drop=True, inplace=True)
    
    labels_train = df_train['class']
    df_train = remove_unimportant_columns(df_train)

    labels_test = df_test['true_class']
    df_test = remove_unimportant_columns(df_test)
    
    return df_train, labels_train, df_test, labels_test


def get_y_true_pred(G):
    y_true = []
    y_pred = []
    for node in G.nodes:
        if 'pred_class' in G.nodes[node]:
    #         print(node, G.nodes[node]['true_class'], int(G.nodes[node]['pred_class'][0]))
            y_true.append(G.nodes[node]['true_class'])
            y_pred.append(int(G.nodes[node]['pred_class']))
    return y_true, y_pred