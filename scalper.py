import time
import selenium 
import webdriver
# for using chrome
browser = webdriver.Chrome('C:/bin/chromedriver')
# amazon 3080 link
#browser.get("https://www.amazon.com/ASUS-Graphics-DisplayPort-Axial-Tech-2-9-Slot/dp/B08J6GMWCQ/ref=sr_1_3?dchild=1&keywords=rtx+3080&qid=1614349732&sr=8-3")
browser.get("https://www.amazon.com/FIODIO-Mechanical-Anti-ghosting-Quick-Response-Multimedia/dp/B086168SJT/ref=pb_d_jfyfob_6?pd_rd_w=VXh1D&pf_rd_p=a382c7b7-9811-48d0-be9b-920b2354e052&pf_rd_r=7FH05KN815A0YP5F1HQM&pd_rd_r=921b99c9-092a-4548-8027-eb4acdcab726&pd_rd_wg=z0tC1&pd_rd_i=B086168SJT&psc=1")


#purchaseable page
#

buyButton = False

while not buyButton:
    try:
        #if this works then the button is not open
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-disabled")

        print("Button isnt ready yet")

        time.sleep(1)
        browser.refresh()

    except:
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")
        print("Button was clicked")
        addToCartBtn.click()
        buyButton = True

