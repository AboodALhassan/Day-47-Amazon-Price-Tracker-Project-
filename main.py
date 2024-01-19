from bs4 import BeautifulSoup
import requests
import lxml
import smtplib


AMAZON_URL = "https://www.amazon.com/dp/B0C1GSNLHW/ref=sspa_dk_detail_1?pd_rd_i=B0C1GSNLHW&pd_rd_w=XvrAT&content-id=amzn1.sym.eb7c1ac5-7c51-4df5-ba34-ca810f1f119a&pf_rd_p=eb7c1ac5-7c51-4df5-ba34-ca810f1f119a&pf_rd_r=J89AZYC5HE1GW4A7NEJ8&pd_rd_wg=kvVVw&pd_rd_r=3009222f-754a-4edf-871e-cf6e92d64a52&s=kitchen&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw&th=1"
MY_EMAIL = "aboodalhassan699@gmail.com"
MY_PASSWORD = "ek4m54n4npw4jks"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=AMAZON_URL, headers=headers)
amazon_web_page = response.text

soup = BeautifulSoup(amazon_web_page, "lxml")

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()

if price_as_float < 100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                           to_addrs="abdelrahmanalhassan95@yahoo.com",
                           msg=f"Subject:Amazon Price Alert!\n\n"
                               f"{title} is now {price}\n{AMAZON_URL}".encode("utf-8"))
