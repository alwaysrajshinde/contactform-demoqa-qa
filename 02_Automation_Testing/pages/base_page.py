# 02_Automation_Testing/pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException, JavascriptException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator, timeout=None):
        w = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return w.until(EC.visibility_of_element_located(locator))

    def remove_ads_iframes(self):
        """Remove obvious ad iframes that can intercept clicks (best-effort)."""
        try:
            self.driver.execute_script("""
                const frames = document.querySelectorAll('iframe[id^=\"google_ads_iframe\"], iframe[src*=\"safeframe\"], iframe[src*=\"ads\"]');
                frames.forEach(f => f.remove());
            """)
            # small pause to let layout stabilize
            time.sleep(0.3)
        except JavascriptException:
            pass

    def click(self, locator, timeout=None):
        """Robust click: wait -> try normal click -> JS click -> ActionChains click."""
        # remove ad iframes that commonly intercept clicks (best-effort)
        self.remove_ads_iframes()

        w = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            el = w.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            # fallback to presence
            el = self.find(locator)

        try:
            el.click()
            return
        except (ElementClickInterceptedException, StaleElementReferenceException):
            pass

        # Scroll into view then try JS click
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center', inline:'center'});", el)
            time.sleep(0.2)
            try:
                self.driver.execute_script("arguments[0].click();", el)
                return
            except JavascriptException:
                pass
        except JavascriptException:
            pass

        # Last resort: ActionChains move to element then click
        try:
            ActionChains(self.driver).move_to_element(el).click(el).perform()
            return
        except Exception:
            pass

        # If still not clicked, raise same interception error
        raise ElementClickInterceptedException("Unable to click element with locator: {}".format(locator))

    def type(self, locator, text):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False
