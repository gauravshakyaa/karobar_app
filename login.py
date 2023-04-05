import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

isLogin = True


class Login:

    @staticmethod
    def login_to_dashboard():
        desired_caps = {
            # "deviceName": "RF8M703BZXW",  # device name for s10 phone
            "deviceName": "A00000K580160801364",  # device name for nokia phone
            "platformName": "Android",
            "appPackage": "com.bytecaretech.merokarobar",
            "appActivity": "com.bytecaretech.merokarobar.MainActivity",
            "platformVersion": "11",
            "noReset": True
            # "app": "C:/Users/acer/Downloads/Karobar.apk"
            # "automationName": "UiAutomator2"
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        language_continue = driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Continue"]')

        language_continue.click()

        time.sleep(1)
        for i in range(1, 4):
            driver.swipe(600, 700, 100, 700, 150)

        time.sleep(1)
        button_next = driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Get Started"]')
        button_next.click()

        time.sleep(2)

        phoneNo_textbox = driver.find_element(By.XPATH,
                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                              '/android'
                                              '.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                              '.FrameLayout'
                                              '/android.view.View/android.view.View/android.view.View/android.view.View'
                                              '/android.view.View/android.widget.EditText')
        phoneNo_textbox.click()
        phoneNo_textbox.send_keys('9222222222')

        def click_done():
            # tap on a specific location on the screen using coordinates
            x = 577  # the x-coordinate of the location
            y = 1173  # the y-coordinate of the location
            # touch = TouchAction(driver).tap(x=x, y=y).perform()
            touch = TouchAction(driver)
            touch.tap(x=x, y=y).perform()

            click_done()

            get_loginOTP = driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Get Login OTP"]')
            get_loginOTP.click()

            time.sleep(2)

            enter_otp = driver.find_element(By.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                            '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                            '/android.view.View/android.view.View/android.view.View/android.view.View'
                                            '/android.view.View[2]/android.widget.EditText')
            enter_otp.click()
            enter_otp.send_keys('123456')

            driver.implicitly_wait(3)
            # verify_phone_number = driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Verify Phone
            # Number"]')
            #
            # verify_phone_number.click()

            select_singleUser = driver.find_element(By.XPATH, '//android.view.View[@content-desc = "Single User"]')

            select_singleUser.click()

            singleUser_continue = driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="CONTINUE"]')

            singleUser_continue.click()

            # select_personalKhata = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH,
            # "//android.view.View[" "@content-desc" "='Personal" "Khata']")))
            #
            time.sleep(7)

            select_personal_khata = driver.find_element(By.XPATH, '//android.view.View[@content-desc="Personal Khata"]')

            select_personal_khata.click()

            personal_khata_continue = driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="CONTINUE"]')

            personal_khata_continue.click()

            allow_permission = driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button')

            allow_permission.click()

            time.sleep(4)


Login.login_to_dashboard()
