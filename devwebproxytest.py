from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType

class Settings:
    def __init__(self, port: int=8156, file: str=None):
        self.port = port
        self.file = file if (file!=None) else f"ProxyRecorder.har"

class Browser(webdriver.Chrome):
    def __init__(self, settings: Settings, debug: bool=False, manualseleniumproxy: bool=False,  **kwargs):
        print(f"Browser.__init__()")
        c = DesiredCapabilities.CHROME.copy()
        if manualseleniumproxy:
            p = Proxy()                                     
            p.proxy_type = ProxyType.MANUAL
            p.http_proxy = f"127.0.0.1:{settings.port}"
            p.add_to_capabilities(c)                      # comment this line for speed when testing
        c['acceptInsecureCerts'] = True
        kwargs.update(desired_capabilities=c)
        print(f'webdriver.Chrome().__init__({kwargs})')
        super().__init__(**kwargs)

    def faststop(self):
        self.__del__()

    def __del__(self):
        print(f"Browser.__del__()")
        return