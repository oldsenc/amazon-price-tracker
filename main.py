import requests
import lxml
import smtplib
from bs4 import BeautifulSoup

EMAIL_ID = "YOUR EMAIL ID"
PASSWORD = "YOUR PASSWORD"

url = "https://www.amazon.in/2021-Apple-Bionic-Wi-Fi-256GB/dp/B09G95JT9X"

header = {
    "UserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0",
    "Accept-Language": "en-US,en-GB;q=0.9"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")

price = soup.find("span", class_="a-offscreen").get_text()
print(price)

price_without_currency = price.split("₹")[1]
print(price_without_currency)

price_as_float = float(price_without_currency.replace(",", ""))
print(price_as_float)
print(type(price_as_float))


title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 65000
if price_as_float < BUY_PRICE:
    message = f"{title} is now price."
    print(message)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL_ID, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ID,
            to_addrs=EMAIL_ID,
            msg=f"Subject:Amazon price alert!\n\n{message}\n{url}"
        )
