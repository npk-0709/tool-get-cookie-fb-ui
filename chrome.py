from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import base64
import hashlib
import struct
import hmac
import time
class WebDriver:
    def __init__(self):
        self.__setup()

    def __setup(self):
        self.options = Options()
        self.options.add_experimental_option(
            'excludeSwitches', ['enable-logging'])
        self.options.add_experimental_option(
            "prefs", {"profile.default_content_setting_values.notifications": 2})
        self.options.add_argument('--headless')

    def startDriver(self):
        service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=self.options)
        return self.driver


def getFullCookie(driver: webdriver.Chrome):
    try:
        cookies = driver.execute_cdp_cmd('Network.getAllCookies', {})
        return '; '.join([cookie['name']+"="+cookie['value'] for cookie in cookies['cookies'] if str(cookie['name']) != 'test_cookie'])
    except:
        return False


def LoginFacebookCookie(driver: webdriver.Chrome, cookie, types="mbasic."):
    url = f"http://{types}facebook.com"
    driver.get(url)
    js = """javascript: void(function() {
                    function setCookie(t) {
                        var list = t.split("; ");
                        console.log(list);
                        for (var i = list.length - 1; i >= 0; i--) {
                            var cname = list[i].split("=")[0];
                            var cvalue = list[i].split("=")[1];
                            var d = new Date();
                            d.setTime(d.getTime() + (7 * 24 * 60 * 60 * 1000));
                            var expires = ";domain=.facebook.com;expires=" + d.toUTCString();
                            document.cookie = cname + "=" + cvalue + "; " + expires;
                        }
                    }
                    setCookie("__cookie__");
                    location.href = "__url__";
                })();
        """
    js = js.replace("__cookie__", cookie).replace("__url__", url)
    driver.execute_script(js)
    driver.get("https://mbasic.facebook.com/me")
    check = checkCheckpoint(driver.current_url)
    if check:
        return True, "susses"
    else:
        return False, check

def getAccesstokenEAAB(driver: webdriver.Chrome):
    try:
        driver.get("https://www.facebook.com/dialog/oauth?client_id=124024574287414&redirect_uri=fbconnect%3A%2F%2Fsuccess&scope=email%2Cpublish_actions%2Cpublish_pages%2Cuser_about_me%2Cuser_actions.books%2Cuser_actions.music%2Cuser_actions.news%2Cuser_actions.video%2Cuser_activities%2Cuser_birthday%2Cuser_education_history%2Cuser_events%2Cuser_games_activity%2Cuser_groups%2Cuser_hometown%2Cuser_interests%2Cuser_likes%2Cuser_location%2Cuser_notes%2Cuser_photos%2Cuser_questions%2Cuser_relationship_details%2Cuser_relationships%2Cuser_religion_politics%2Cuser_status%2Cuser_subscriptions%2Cuser_videos%2Cuser_website%2Cuser_work_history%2Cfriends_about_me%2Cfriends_actions.books%2Cfriends_actions.music%2Cfriends_actions.news%2Cfriends_actions.video%2Cfriends_activities%2Cfriends_birthday%2Cfriends_education_history%2Cfriends_events%2Cfriends_games_activity%2Cfriends_groups%2Cfriends_hometown%2Cfriends_interests%2Cfriends_likes%2Cfriends_location%2Cfriends_notes%2Cfriends_photos%2Cfriends_questions%2Cfriends_relationship_details%2Cfriends_relationships%2Cfriends_religion_politics%2Cfriends_status%2Cfriends_subscriptions%2Cfriends_videos%2Cfriends_website%2Cfriends_work_history%2Cads_management%2Ccreate_event%2Ccreate_note%2Cexport_stream%2Cfriends_online_presence%2Cmanage_friendlists%2Cmanage_notifications%2Cmanage_pages%2Cphoto_upload%2Cpublish_stream%2Cread_friendlists%2Cread_insights%2Cread_mailbox%2Cread_page_mailboxes%2Cread_requests%2Cread_stream%2Crsvp_event%2Cshare_item%2Csms%2Cstatus_update%2Cuser_online_presence%2Cvideo_upload%2Cxmpp_login&response_type=token")
        driver.find_element(By.NAME, "__CONFIRM__").click()
        driver.get("view-source:https://www.facebook.com/dialog/oauth?client_id=124024574287414&redirect_uri=https://www.instagram.com/accounts/signup/&&scope=email&response_type=token")
        access_token = driver.current_url.split("access_token=")[1]
        return access_token
    except: 
        return False


def Authenticator(code):
    intervals_no = int(time.time())//30
    key = base64.b32decode(code, True)
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = h[19] & 15
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    return h


def checkCheckpoint(data: str):
    if "27956" in data:
        return 956
    elif "282" in data:
        return 282
    elif "723" in data:
        return 723
    elif "login.php" in data:
        return "auth"
    return True


def isLogin(current_url: str):
    if "login.php" in current_url:
        return False
    return True


def LoginFacebookUserPass2Fa(driver: webdriver.Chrome, username: str, password: str, authen_2fa: str, delay_input: float = 0.3):

    driver.get('https://mbasic.facebook.com/login')
    for user in username:
        driver.find_element(By.NAME, 'email').send_keys(user)

        time.sleep(delay_input)
    for passs in password:
        driver.find_element(By.NAME, 'pass').send_keys(passs)
        time.sleep(delay_input)
    driver.find_element(By.NAME, 'pass').send_keys("\n")
    time.sleep(1)
    try:
        driver.find_element(By.NAME, 'pass')
        driver.quit()
        return False, "auth"
    except:
        try:
            code = Authenticator(authen_2fa.replace(" ", "").strip())
            driver.find_element(By.ID, 'approvals_code').send_keys(code)
            time.sleep(1)
            driver.find_element(By.ID, 'approvals_code').send_keys("\n")
            time.sleep(1)
            while True:
                try:
                    driver.find_element(
                        By.ID, 'approvals_code').send_keys(code)
                except:
                    break
            try:
                driver.find_element(By.NAME, 'submit[Continue]').click()
                time.sleep(0.3)
            except:
                pass
            try:
                driver.find_element(By.NAME, 'submit[Continue]').click()
                time.sleep(1)
                driver.find_element(By.NAME, 'submit[This was me]').click()
                time.sleep(1)
                driver.find_element(By.NAME, 'submit[Continue]').click()
            except:
                pass
        except:
            pass
    driver.get("https://mbasic.facebook.com/me")
    check = checkCheckpoint(driver.current_url)
    if check:
        return True, "susses"
    else:
        return False, check
