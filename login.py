import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

isLogin = True


class Login:

    def __init__(self, device_name, platform_name, app_package, app_activity, platform_version, no_reset):
        self.device_name = device_name
        self.platform_name = platform_name
        self.app_package = app_package
        self.app_activity = app_activity
        self.platform_version = platform_version
        self.no_reset = no_reset

        # Start the Appium driver
        desired_caps = {

            "deviceName": self.device_name,  # device name for nokia phone
            "platformName": self.platform_name,
            "appPackage": self.app_package,
            "appActivity": self.app_activity,
            "platformVersion": self.platform_version,
            "noReset": self.no_reset
        }
        # desired_caps = {
        #     # "deviceName": "RF8M703BZXW",  # device name for s10 phone
        #     "deviceName": "A00000K580160801364",  # device name for nokia phone

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def wait_for_element(self, locator, timeout=10):
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def select_language(self, language):
        # Click continue button. English is the default selected language.

        select_language_locator = (By.XPATH, f'//android.widget.ImageView[@content-desc="{language}"]')
        hello = self.wait_for_element(select_language_locator)

        language_continue = self.driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='Continue']")
        language_continue.click()

    def login(self, phonenum):
        # Swipe the slogan page
        for i in range(1, 4):
            self.driver.swipe(600, 700, 100, 700, 150)
        time.sleep(1)

        # Click get started button after swiping
        button_next = self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Get Started"]')
        button_next.click()
        time.sleep(2)

        phone_textbox = self.driver.find_element(By.XPATH,
                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android'
                                                 '.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                                 '.FrameLayout'
                                                 '/android.view.View/android.view.View/android.view.View/android.view'
                                                 '.View'
                                                 '/android.view.View/android.widget.EditText')
        phone_textbox.click()
        phone_textbox.send_keys(phonenum)

        def click_done():
            # tap on a specific location on the screen using coordinates
            x = 577  # the x-coordinate of the location
            y = 1173  # the y-coordinate of the location
            # touch = TouchAction(driver).tap(x=x, y=y).perform()
            touch = TouchAction(self.driver)
            touch.tap(x=x, y=y).perform()

        click_done()

        get_loginOTP = self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Get Login OTP"]')
        get_loginOTP.click()

        time.sleep(2)

        enter_otp = self.driver.find_element(By.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                             '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                             '/android.view.View/android.view.View/android.view.View/android.view.View'
                                             '/android.view.View[2]/android.widget.EditText')
        enter_otp.click()
        enter_otp.send_keys('123456')

        self.driver.implicitly_wait(3)
        # verify_phone_number = driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Verify Phone
        # Number"]')
        #
        # verify_phone_number.click()

        select_singleUser = self.driver.find_element(By.XPATH, '//android.view.View[@content-desc = "Single User"]')

        select_singleUser.click()

        singleUser_continue = self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="CONTINUE"]')

        singleUser_continue.click()

        # select_personalKhata = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH,
        # "//android.view.View[" "@content-desc" "='Personal" "Khata']")))
        #
        time.sleep(7)

        select_personalKhata = self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="Personal Khata"]')

        select_personalKhata.click()

        personalKhata_continue = self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="CONTINUE"]')

        personalKhata_continue.click()

        allow_permission = self.driver.find_element(By.ID,
                                                    'com.android.permissioncontroller:id/permission_allow_button')

        allow_permission.click()

        time.sleep(4)


appium_driver = Login('RF8M703BZXW', 'Android', 'com.bytecaretech.merokarobar',
                      'com.bytecaretech.merokarobar.MainActivity', '12', False)

appium_driver.select_language('English')
