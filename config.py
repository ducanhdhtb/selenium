import random, string
#the url of the website need to test
BASE_URL = 'http://automationpractice.com'
#BASE_URL = 'https://testing.perseed.eu'
OPERATING_SYSTEM = 'windows'  
#random chuoi
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))
   
#account to login the system to execute tests
CUSTOMER_EMAIL = randomword(10)+"@gmail.com"
CUSTOMER_FIRSTNAME = "Nguyen"
CUSTOMER_LASTNAME = "Duc Anh"
CUSTOMER_PASSWORD = "ducanasdh123"
FIRSTNAME = "anh"
LASTNAME = "duc"
COMPANY = "QSoft"
ADDRESS1 = "Ho Tung Mau"
ADDRESS2 = "Vinh CITY"
CITY = "Ha Noi"
POSTCODE = "10000"

