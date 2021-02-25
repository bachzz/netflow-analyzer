import pandas as pd

df_0 = pd.read_csv("./dataset/snmp_normal_0.csv")
df_1 = pd.read_csv("./dataset/snmp_normal_1.csv")
df_2 = pd.read_csv("./dataset/snmp_normal_2.csv")
df_3 = pd.read_csv("./dataset/snmp_attack.csv")

df_0["class"] = 'normal'
df_1["class"] = 'normal'
df_2["class"] = 'normal'
df_3["class"] = 'attack'

df_full = df_0.append(df_1, ignore_index=True)
df_full = df_full.append(df_2, ignore_index=True)
df_full = df_full.append(df_3, ignore_index=True)

print(df_full)

df_full.to_csv("df_full.csv", index=False)