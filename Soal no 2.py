from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inisialisasi driver Selenium, misalnya menggunakan Chrome
driver = webdriver.Chrome()

# waktu tunggu
driver.implicitly_wait(60)

# Langkah 1: Open browser dan direct ke URL
driver.get('https://www.saucedemo.com/')

# fullscreen
driver.maximize_window()

# Langkah 2: Get value username (standard_user) dan password nya
username_input = driver.find_element(By.ID, 'user-name')
password_input = driver.find_element(By.ID, 'password')

# Langkah 3: Simpan value kedalam variable
username_input.send_keys('standard_user')
password_input.send_keys('secret_sauce')

print ('Login successfully')

time.sleep(1)
# Langkah 4: Submit form login
login_button = driver.find_element(By.ID, 'login-button')
login_button.click()

time.sleep(1)
# Langkah 5: Get harga barang (Sauce Labs Backpack) dan simpan dalam variable
product_name = "Sauce Labs Backpack"  # Nama produk yang ingin dicari
product_price_element = driver.find_element(By.XPATH, f"(//div[normalize-space()='$29.99'])[1]")
product_price = product_price_element.text

print ("Price : ", '$29.99')

time.sleep(2)
# Langkah 6: Checkout barang (Sauce Labs Backpack) dan verifikasi harga ketika proses checkout
cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
cart_button.click()

print ("Barang dimasukkan ke keranjang")

time.sleep(2)
# Lanjutkan ke halaman checkout
checkout_button = driver.find_element(By.ID, "shopping_cart_container")
checkout_button.click()

time.sleep(1)
# Verifikasi harga ketika proses checkout
checkout_product_price_element = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]")
checkout_product_price = checkout_product_price_element.text


time.sleep(2)
# Verifikasi apakah harga sama dengan yang di halaman awal
assert checkout_product_price == product_price, "Harga pada proses checkout tidak sesuai dengan harga awal."

print ('Harga pada proses checkout tidak sesuai dengan harga awal. Karena, Harga awal + tax')

time.sleep(2)
# Lanjutkan ke halaman checkout
checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()

time.sleep(1)
# Langkah 7: Lanjutkan proses checkout sampai selesai
first_name_input = driver.find_element(By.ID, "first-name")
last_name_input = driver.find_element(By.ID, "last-name")
postal_code_input = driver.find_element(By.ID, "postal-code")

print ('Lengkapi data pengiriman anda')

time.sleep(2)
# Isi informasi pembayaran dan alamat pengiriman
first_name_input.send_keys("John")
last_name_input.send_keys("Doe")
postal_code_input.send_keys("12345")

time.sleep(2)
# Klik tombol continue
continue_button = driver.find_element(By.ID, "continue")
continue_button.click()

print ('Checkout Successfully')

time.sleep(2)
# Klik tombol finish untuk menyelesaikan pembelian
finish_button = driver.find_element(By.ID, "finish")
finish_button.click()


input()
driver.quit()