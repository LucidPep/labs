import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.read_csv('UNSW_NB15_training-set.csv')# Читаем исходную выборку
print(df.columns)

df = df.drop(['id', 'attack_cat', 'proto', 'service', 'state'], axis=1)# Убираем качественные значения и id за ненадобностью

cols = ['dur', 'spkts', 'dpkts', 'sbytes',
       'dbytes', 'rate', 'sttl', 'dttl', 'sload', 'dload', 'sloss', 'dloss',
       'sinpkt', 'dinpkt', 'sjit', 'djit', 'swin', 'stcpb', 'dtcpb', 'dwin',
       'tcprtt', 'synack', 'ackdat', 'smean', 'dmean', 'trans_depth',
       'response_body_len', 'ct_srv_src', 'ct_state_ttl', 'ct_dst_ltm',
       'ct_src_dport_ltm', 'ct_dst_sport_ltm', 'ct_dst_src_ltm',
       'is_ftp_login', 'ct_ftp_cmd', 'ct_flw_http_mthd', 'ct_src_ltm',
       'ct_srv_dst', 'is_sm_ips_ports', 'label']

dfx = df.loc[:, cols].values# Все значения, кроме label
dfy = df.loc[:, ['label']].values# Только значения label

print(dfx, dfy)

ss = StandardScaler()# Инициализация StandardScaler
df0 = ss.fit_transform(dfx.copy())# Масштабируем данные из dfx

print(df0)

pca = PCA(n_components=2)# Инициализация метода главных компонент
df1 = pca.fit_transform(df0.copy())# Строим главные компоненты

print(df1)
stage1_df = pd.DataFrame(data=df1, columns=['pc1', 'pc2'])# Формируем датафрейм с двумя главными компонентами
stage2_df = pd.concat([stage1_df, df[['label']]], axis=1)

print(stage1_df)

plt.figure()
plt.scatter(stage1_df['pc1'], stage1_df['pc2'], c=dfy, edgecolor='black', lw=.4, cmap='jet', alpha=.1)
plt.xlabel("Первая компонента")
plt.ylabel("Вторая компонента")
plt.axis('equal')
plt.show()

df2 = pca.inverse_transform(stage1_df.copy())
print(df2)

df2 = pd.DataFrame(data=df2, columns=['dur', 'spkts', 'dpkts', 'sbytes',
       'dbytes', 'rate', 'sttl', 'dttl', 'sload', 'dload', 'sloss', 'dloss',
       'sinpkt', 'dinpkt', 'sjit', 'djit', 'swin', 'stcpb', 'dtcpb', 'dwin',
       'tcprtt', 'synack', 'ackdat', 'smean', 'dmean', 'trans_depth',
       'response_body_len', 'ct_srv_src', 'ct_state_ttl', 'ct_dst_ltm',
       'ct_src_dport_ltm', 'ct_dst_sport_ltm', 'ct_dst_src_ltm',
       'is_ftp_login', 'ct_ftp_cmd', 'ct_flw_http_mthd', 'ct_src_ltm',
       'ct_srv_dst', 'is_sm_ips_ports', 'label'])

plt.matshow(pca.components_[0:2, 0:39])
cb = plt.colorbar()
plt.gca().xaxis.tick_bottom()
plt.yticks(range(len(stage2_df.columns) - 1), stage2_df.iloc[:, :-1].columns)
plt.xticks(range(len(df.columns) - 1), df.iloc[:, :-1].columns)
plt.show()

features = pd.DataFrame(data=pca.components_, columns=['dur', 'spkts', 'dpkts', 'sbytes',
       'dbytes', 'rate', 'sttl', 'dttl', 'sload', 'dload', 'sloss', 'dloss',
       'sinpkt', 'dinpkt', 'sjit', 'djit', 'swin', 'stcpb', 'dtcpb', 'dwin',
       'tcprtt', 'synack', 'ackdat', 'smean', 'dmean', 'trans_depth',
       'response_body_len', 'ct_srv_src', 'ct_state_ttl', 'ct_dst_ltm',
       'ct_src_dport_ltm', 'ct_dst_sport_ltm', 'ct_dst_src_ltm',
       'is_ftp_login', 'ct_ftp_cmd', 'ct_flw_http_mthd', 'ct_src_ltm',
       'ct_srv_dst', 'is_sm_ips_ports', 'label'])

#print(pcadf)


print('!!!!', pca.components_)

print("Наименее информативные признаки:")
for feature in features:
    if (-0.06 < features[feature][0] < 0.06) and (-0.08 < features[feature][1] < 0.08):
        print(feature)