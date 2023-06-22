import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, nbinom, expon
from statsmodels.distributions.empirical_distribution import ECDF

# Informacoes Gerais sobre a Captura

dados_usuario = pd.read_table("captura.dat", encoding="UTF-8")
print(dados_usuario)

# Renomeando colunas de bits
dados_usuario = dados_usuario.rename(columns={"V1": "tempo", "V2": "num_pac", "V3": "tam_med_pac", "V4": "bytes"})

# Marcando linhas: total de tempo (30 min e 60 min) de cada arquivo leva a aprox. 25 linhas para cada segundo
# e depois considerando agrupamento a cada 5 segundos
tempo = np.repeat(np.arange(1, 361), repeats=125)
dados_usuario["tempo"] = tempo[:414]

# Criar DataFrame
dados = pd.DataFrame({"tempo": dados_usuario["tempo"][:414], "usuario_B": dados_usuario["bytes"]})

print(dados_usuario.shape[0])

# Analise de Bytes

print(dados["usuario_B"].describe())

# Intervalo de confianca para media de bytes
error = norm.ppf(0.95) * dados["usuario_B"].std() / np.sqrt(dados.shape[0])
left = dados["usuario_B"].mean() - error
right = dados["usuario_B"].mean() + error
print("Intervalo de confianca Usuario - 95%")
print("[", left, ",", right, "]")

# Histograma
plt.hist(dados["usuario_B"], bins="auto")
plt.xlabel("Bytes")
plt.ylabel("Frequencia")
plt.title("Usuario")
plt.show()

# Scatterplot
plt.plot(dados["tempo"], dados["usuario_B"], color="blue", label="Usuario")
plt.xlabel("Tempo")
plt.ylabel("Bytes")
plt.title("Scatterplot")
plt.legend()
plt.show()

# Ajustes de distribuicoes
sns.kdeplot(dados["usuario_B"])
plt.title("Densidade")
plt.show()

ecdf = ECDF(dados["usuario_B"])
plt.step(ecdf.x, ecdf.y)
plt.title("Empirical cumulative distribution function")
plt.show()

# fit_norm = norm.fit(dados["usuario_B"])
# ks_norm = kstest(dados["usuario_B"], "norm", args=(fit_norm[0], fit_norm[1]))

# Analise de Pacotes Para Trafego do Usuario

# Numero de pacotes

print(dados_usuario["tam_med_pac"].describe())
print(dados_usuario["num_pac"].describe())

# Intervalo de confianca para media de pacotes
error = norm.ppf(0.95) * dados_usuario["num_pac"].std() / np.sqrt(dados_usuario.shape[0])
left = dados_usuario["num_pac"].mean() - error
right = dados_usuario["num_pac"].mean() + error
print("Intervalo de confianca - 95%")
print("[", left, ",", right, "]")

# Histograma
plt.hist(dados_usuario["num_pac"], bins="auto")
plt.xlabel("Pacotes")
plt.ylabel("Frequencia")
plt.title("Numero de Pacotes")
plt.show()

# Scatterplot
plt.plot(dados_usuario["tempo"], dados_usuario["num_pac"], color="red")
plt.xlabel("Tempo")
plt.ylabel("Pacotes")
plt
