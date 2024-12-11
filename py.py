import random
import string
import requests

# Rastgele bir e-posta adresi oluştur
def random_email():
    domains = ["gmail.com", "yahoo.com", "hotmail.com"]
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(domains)
    return f"{name}@{domain}"

def send_email():
    url = "https://cpfree.org/log"  #
    email = random_email()
    payload = {
        "email": email,
        "password": "fucker1233020"  
    }
    
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print(f"E-posta gönderildi: {email}")
    else:
        print(f"Başarısız! Durum Kodu: {response.status_code}")

for _ in range(10): 
    send_email()
  
