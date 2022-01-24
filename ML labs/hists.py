import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import argrelextrema

df = pd.read_csv('UNSW_NB15_training-set.csv')  # Загружаем исходную выборку

qualless = df.drop(['attack_cat', 'proto', 'service', 'state'], axis=1)
quanless = df.drop(['id', 'dur', 'spkts', 'dpkts', 'sbytes',
                    'dbytes', 'rate', 'sttl', 'dttl', 'sload', 'dload', 'sloss', 'dloss',
                    'sinpkt', 'dinpkt', 'sjit', 'djit', 'swin', 'stcpb', 'dtcpb', 'dwin',
                    'tcprtt', 'synack', 'ackdat', 'smean', 'dmean', 'trans_depth',
                    'response_body_len', 'ct_srv_src', 'ct_state_ttl', 'ct_dst_ltm',
                    'ct_src_dport_ltm', 'ct_dst_sport_ltm', 'ct_dst_src_ltm',
                    'is_ftp_login', 'ct_ftp_cmd', 'ct_flw_http_mthd', 'ct_src_ltm',
                    'ct_srv_dst', 'is_sm_ips_ports', 'label'], axis=1)

print(qualless)
print(quanless)
"""q1 = ['id', 'dur', 'spkts', 'dpkts', 'sbytes',
       'dbytes', 'rate', 'sttl', 'dttl', 'sload', 'dload', 'sloss', 'dloss',
       'sinpkt', 'dinpkt', 'sjit', 'djit', 'swin', 'stcpb', 'dtcpb', 'dwin',
       'tcprtt', 'synack', 'ackdat', 'smean', 'dmean', 'trans_depth',
       'response_body_len', 'ct_srv_src', 'ct_state_ttl', 'ct_dst_ltm',
       'ct_src_dport_ltm', 'ct_dst_sport_ltm', 'ct_dst_src_ltm',
       'is_ftp_login', 'ct_ftp_cmd', 'ct_flw_http_mthd', 'ct_src_ltm',
       'ct_srv_dst', 'is_sm_ips_ports', 'label']

q2 = ['attack_cat', 'proto', 'service', 'state']"""
# Количественные данные

print(len(qualless))
min_k = 0.55 * len(qualless) ** 0.4
max_k = 1.25 * len(qualless) ** 0.4

k_bins = int((min_k + max_k) // 2)
if k_bins % 2 == 0:
    k_bins += 1

print(min_k, max_k, k_bins)

i = 1
for column in qualless.columns:
    for_mins = qualless[column].to_numpy()
    minimums = argrelextrema(for_mins, np.less)
    print('Локальные минимумы: ', for_mins[minimums])
    plt.figure()
    plt.hist(qualless[column], bins=k_bins, density=True, color='skyblue')
    #plt.savefig('hists\\{0}_hist_{1}'.format(i, column + '.png'))
    sns.kdeplot(data=qualless, x=column, color='red')
    #sns.scatterplot(data=qualless, x=column, y='id')
    plt.savefig('hists\\{0}_{1}'.format(i, column + '.png'))
    plt.close('all')
    i += 1


j = len(qualless.columns)
for column in quanless:
    plt.figure()
    plt.hist(quanless[column], density=True)
    plt.savefig('hists\\{0}_{1}'.format(j, column + '.png'))
    j += 1