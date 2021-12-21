import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO site Pudim não está acessível no momento\033[m')
print('\033[32mO site Pudim está acessível agora\033[m\033[m')
print('O codigo do site é: ', end='')
print(site.read())