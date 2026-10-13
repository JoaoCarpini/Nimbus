from previsao import buscarPrevisao
from regra import avaliarPrevisao

previsao = buscarPrevisao()
result = avaliarPrevisao(previsao)

print(result)