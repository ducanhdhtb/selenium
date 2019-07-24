import random, string
#the url of the website need to test
BASE_URL = 'http://automationpractice.com'
#BASE_URL = 'https://testing.perseed.eu'
OPERATING_SYSTEM = 'windows'  
#random string
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))
   
# Account to login the system to execute tests
CUSTOMER_EMAIL = randomword(10)+"@gmail.com"
CUSTOMER_FIRSTNAME = "testname"
CUSTOMER_LASTNAME = "testlastname"
CUSTOMER_PASSWORD = "ducanh123"
FIRSTNAME = "Mr"
LASTNAME = "Shine"
CUSTOMER_COMPANY = "QSoft"
CUSTOMER_ADDRESS1 = "Ho Tung Mau"
CUSTOMER_ADDRESS2 = "My Dinh"
CUSTOMER_CITY = "Ha Noi"
CUSTOMER_POSTCODE = "10000"
CUSTOMER_INFOR = "this is test information"
CUSTOMER_PHONE = "028 7108 7108"
CUSTOMER_PHONE_MOBILE = "0357653027"
CUSTOMER_ALIAS  = "thanks best!"
# Test login
EMAIL_LOGIN = "anhndsmartit@gmail.com"
PASSWORD_LOGIN = "ducanh123"
EMAIL_LOGIN_FAILED = "anhndsmartit"
PASSWORD_LOGIN_FAILED = "123"

