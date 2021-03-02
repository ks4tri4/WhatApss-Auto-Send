from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time
import os
text = "Hey, this message was sent using Selenium"
chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://web.whatsapp.com")
wait = WebDriverWait(driver, 10)
wait5 = WebDriverWait(driver, 5)


def pilihkontak(nama):
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(nama))
    user.click()
    print("kontak dipilih")
    time.sleep(0.5)


def kirimpesan(pesan):
    # Select the Input Box
    # "//div[@data-tab='6']" adalah identitas xpath untuk menulis pesan balasan
    # kadang ini dirubah oleh WA, jika tidak berjalan semestinya rubah kode tersebut dengan yang baru
    inp_xpath = "//div[@data-tab='6']"
    input_box = wait.until(
        EC.presence_of_element_located((By.XPATH, inp_xpath)))
    print("kontak dipilih")
    time.sleep(1)
    # Send message
    # target is your target Name and msgToSend is you message
    # + Keys.ENTER (Uncomment it if your msg doesnt contain '\n')
    input_box.send_keys(pesan)
    # Link Preview Time, Reduce this time, if internet connection is Good
    time.sleep(2)
    input_box.send_keys(Keys.ENTER)


print("Scan QR Code, And then Enter")
print("Logged In")
perintah = ""
while (perintah != "exit"):
    perintah = input("Masukkan Perintah: ")

    if(perintah == "exit"):
        print("Program Selesai")
        time.sleep(1.5)

    if (perintah == "kirim"):
        nama = input("Kontak yang akan dikirim pesan: ")
        try:
            pilihkontak(nama)
            pesan = input("tulis pesan -> ")
            kirimpesan(pesan)
            print("Successfully Send Message to : " + nama + '\n')
            time.sleep(0.5)

        except:
            # Menampilkan output
            print("Hello kontak dengan", nama, "tidak ditemukan")
            print("Good bye!")
            time.sleep(3)
            os.system("cls")

    if(perintah == "baca"):
        nama = input("Kontak yang akan diBaca Pesannya pesan: ")
        pilihkontak(nama, driver)
        for i in range(1, 3):
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
        msg_got = driver.find_elements_by_css_selector(
            "span._3-8er.selectable-text.copyable-text")
        print(type(msg_got))
        msg = [message.text for message in msg_got]
        print(type(msg))
        print(msg_got[0])
        # print "Semua Pesan: ada {} Pesan".format(len(msg_got))
        time.sleep(3)

    else:
        print("perintah yang anda masukkan tidak ada")
driver.close()
