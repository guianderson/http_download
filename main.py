import urllib.request, urllib.error
from urllib import request

resp = request.urlopen("http://ftp.cptec.inpe.br/goes/goes16/glm/2020/09/16/")
data = resp.read()
html = data.decode("UTF-8")
print(html)

arquivo = input("Nome do arquivo que deseja fazer download: ")
url = "http://ftp.cptec.inpe.br/goes/goes16/glm/2020/09/16/" + arquivo
print(url)
urllib.request.urlretrieve(url, arquivo)


