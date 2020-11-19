import browser_cookie3
import requests
import sys
import json   
import time
print('get your cookie')
cj = browser_cookie3.chrome(domain_name='.target.com')
cookie = ''
for i, c in enumerate(cj):
    if i != len(cj) - 1:
    	cookie += c.name+'='+c.value+'; '
    else:
    	cookie += c.name+'='+c.value
print('getted your cookie')

count = 0
stop_process = False
header = {
	'content-type': 'application/json',
	'cookie': cookie
	}
body = {"cart_type":"REGULAR",
"channel_id":"10",
"shopping_context":"DIGITAL",
"cart_item": {"tcin":"81114595" # 81114595 ps5 80790841 xbox series x 21 81114477 #ps5 controller 81114596 ps5 digital
,"quantity":1,
"item_channel_id":"10"},
"fulfillment":{"fulfillment_test_mode":"grocery_opu_team_member_test"}}
body = json.dumps(body)
while True :
	print(count)
	count += 1
	if count > 960:
		print('more than 960 time, out')
		sys.exit()
		break
	print('try to add into cart')
	response = requests.post("https://carts.target.com/web_checkouts/v1/cart_items?field_groups=CART%2CCART_ITEMS%2CSUMMARY&key=feaf228eb2777fd3eee0fd5192ae7107d6224b39", data = body, headers= header)
	res = response.text
	res = json.loads(res)
	if 'cart_id' in res:
		break
	else:
		print('failed to add into cart')
		time.sleep(30)
print('step 2')

body = json.dumps({"cart_type":"REGULAR"})
while True:
	count += 1
	print('try to move to checkout')
	if count > 1060:
		print('more than 1060 times try')
		sys.exit()
		break
	response = requests.post('https://carts.target.com/web_checkouts/v1/pre_checkout?field_groups=ADDRESSES%2CCART%2CCART_ITEMS%2CDELIVERY_WINDOWS%2CPAYMENT_INSTRUCTIONS%2CPICKUP_INSTRUCTIONS%2CPROMOTION_CODES%2CSUMMARY&key=feaf228eb2777fd3eee0fd5192ae7107d6224b39',data = body, headers= header)
	res = response.text
	res = json.loads(res)
	if 'cart_id' in res:
		print('success move to checkout')
		break
	else:
		print('try one more time move to checkout')
		time.sleep(5)
print('begin checkout')

body = json.dumps({"cart_type":"REGULAR","channel_id":10})
while True:
	count += 1
	if count > 1080:
		print('more than 1080 times try')
		sys.exit()
	url = 'https://carts.target.com/web_checkouts/v1/checkout?field_groups=ADDRESSES%2CCART%2CCART_ITEMS%2CDELIVERY_WINDOWS%2CPAYMENT_INSTRUCTIONS%2CPICKUP_INSTRUCTIONS%2CPROMOTION_CODES%2CSUMMARY&key=feaf228eb2777fd3eee0fd5192ae7107d6224b39'
	response = requests.post(url,data = body, headers= header)
	res = response.text
	res = json.loads(res)
	if 'orders' in res:
		print(res)
		print('success!!')
		break
	else:
		print('failed checkout, try one more times, try 10 times')
		time.sleep(5)
print('done')
