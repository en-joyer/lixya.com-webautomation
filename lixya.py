from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

# Selenium WebDriver'ı başlat
driver = webdriver.Chrome('./drivers/chromedriver.exe')
driver.maximize_window()


# Siteye Git
print("Siteye gidiliyor...")
hedefUrl = "https://www.lixya.com/"
driver.get(hedefUrl)

# Giriş Yap Butonuna Tıkla
driver.find_element_by_css_selector("div[class='button-set'] a[class='btn btn-primary']").click()

# Kullanıcı değerini ve şifre değerini 'kullanici.txt' dosyasından alır.
with open('E:\\Kodlama\\playwright\\tests\\lixya\\kullanici.txt', 'r') as file:
    lines = file.readlines()
    kullanici = lines[0].strip()
    sifre = lines[1].strip()

# Alınan bilgileri doldurur.
print("Kullanıcı bilgileri dolduruluyor...")
driver.find_element_by_css_selector('input[placeholder="Email / Gsm *"]').send_keys(kullanici)
driver.find_element_by_css_selector("input[ng-model='login.sifreBox']").click()
driver.find_element_by_css_selector("input[ng-model='login.sifreBox']").send_keys(sifre)
driver.find_element_by_css_selector('.btn.btn-login').click()

# Sure Bekleme Fonksiyonu
def sureyiBekle():
    while True:
        suankiZaman = int(time.strftime("%S"))
        if suankiZaman == 59:
            break

sureyiBekle()

# Bekleme tamamlandı
print('Bekleme tamamlandı!')

# Sayfaları ve ürünleri al
print("Ürünler alınıyor...")

products = open('E:\\Kodlama\\playwright\\tests\\lixya\\products.txt', 'r', encoding="utf-8").readlines()

# Her bir sayfa için işlemleri gerçekleştir
print("Her bir sayfa için işlemler gerçekleştiriliyor...")
for i in range(5):
    print("Yeni bir sekme aç...")
    driver.execute_script("window.open()")
    print("Yeni pencere açma scripti çalıştırıldı.")
    driver.switch_to.window(driver.window_handles[-1])
    print("Sekme değiştiriliyor...")

    # Yeni sekmede siteye git
    print(f"Yeni sekme {i} için siteye gidiliyor...")
    driver.get(hedefUrl)

    urunler = products[i].strip().split('\n')  # Ürünleri ayır

    for j in range(len(urunler)):
        urun = urunler[j].strip()  # Ürünü al

        # Arama yap
        print(f"Yeni sekme {i}, Ürün {urun} için arama yapılıyor...")
        driver.find_element_by_xpath("//input[@id='src']").send_keys(urun)
        time.sleep(2)
        driver.find_element_by_xpath("//button[normalize-space()='ARA']").click()

        # İlk ürünü seç ve sepete ekle
        products_set_div = driver.find_element_by_class_name("product-set") 
        ilk_urun = products_set_div.find_element_by_tag_name("li")
        ilk_urun.click()
        driver.find_element_by_xpath("(//button[@class='basket'])[1]").click()

        print(f"Yeni sekme {i}, Ürün {urun} işlemleri tamamlandı.")

time.sleep(2)
def UrunBulunamadi():
    okbutonu = driver.find_element(By.CSS_SELECTOR, ".swal2-actions")
    if okbutonu.is_displayed():
        okbutonu.click()
    else:
        return
UrunBulunamadi()

# Sepete git
driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.headersepet").click()
time.sleep(2)

# Sepetteki ürünler (devredışı)

#sepetteki_urunler = driver.find_elements(By.CSS_SELECTOR, "div.list > ul > li")

#for urun in sepetteki_urunler:
#    urunclass = urun.find_element(By.XPATH, ".//div[@class='centered']/p")
#    urunismi = urunclass.text
#    adetclass = urun.find_element(By.XPATH, ".//div[@class='price']/span[@class='piece ng-binding']")
#    adetdeger = adetclass.text.replace('x', '').strip()
#    fiyatclass = urun.find_element(By.XPATH, ".//div[@class='price']/span[@class='money ng-binding']")
#    fiyatdeger = fiyatclass.text.replace('TL', '').strip()
#    fiyatdeger = float(fiyatdeger)
#
#    print(f"{urunismi} - {adetdeger} - {fiyatdeger}")