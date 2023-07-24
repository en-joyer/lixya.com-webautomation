# Automated Product Addition Selenium Code

<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)
[![QA HUNT - Academy](https://img.shields.io/badge/QA_HUNT-Academy-blue?style=for-the-badge)](https://)

</div>

This project was created as part of the weekly project in QA Hunt. You can find the details in Turkish in the DOCX.

This code utilizes the Selenium library to perform web browser automation. It navigates to a specific website, logs in with user credentials, and then searches for specific products and adds them to the cart.

## Requirements
- Python 3.x
- Selenium library
- ChromeDriver (compatible version with Chrome browser)



## Installation
1. Download and install Python 3 from the official website: [Python Downloads](https://www.python.org/downloads/)
2. Install the Selenium library:

```bash
  pip install selenium
```
Download

```bash
  git clone https://github.com/en-joyer/lixya.com-webautomation
```

Go to Project Folder

```bash
  cd lixya.com-webautomation
```

3. Download ChromeDriver from the official website: [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
4. Extract the ChromeDriver file to a suitable directory and remember its path.
5. Copy the code to a Python file (e.g., `auto_product_add.py`).

## Usage
1. Create a text file named `kullanici.txt` and enter the username and password on separate lines.

```
username
password
```
Example
```
example@example.com
123456
```

2. Create a text file named `products.txt` and list the products you want to add, with each product on a separate line.
```
product1
product2
product3
```
3. Update the file paths (`kullanici.txt`, `products.txt`) with the appropriate paths.
4. Run the Python file:
```
python lixya.py
```

5. The code will launch the Chrome browser, navigate to the specified website, log in, search for products, and add them to the cart.

> **Note:** Ensure that the compatible versions of the Chrome browser and ChromeDriver are installed. Update the ChromeDriver file path in the line `driver = webdriver.Chrome('./drivers/chromedriver.exe')`.

This code provides a basic example of automating the process of adding products to a web browser. You can customize and enhance the code according to your needs.
