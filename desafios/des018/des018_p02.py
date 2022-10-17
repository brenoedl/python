import urllib.error
import urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('O site pudim não está acessivel no momento.')
else:
    print('Comseguui acessar o site pudim com sucesso!')
