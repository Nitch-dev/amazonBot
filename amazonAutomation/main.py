import pyautogui
import time
from pyautogui import ImageNotFoundException

def Vpn():
    print("connecting VPN")
    vpnX,vpnY = pyautogui.locateCenterOnScreen("vpnIcon.png") #to open the VPN
    time.sleep(2)
    pyautogui.click(vpnX,vpnY)
    time.sleep(3)
    try:
        vpnX,vpnY = pyautogui.locateCenterOnScreen("vpn.png")
    except:
        print("didnt found vpn")
    try:
        vpnX,vpnY = pyautogui.locateCenterOnScreen("vpn2.png")
    except:
        print("didnt found vpn")
    
    time.sleep(2)
    pyautogui.click(vpnX,vpnY)
    time.sleep(2)
    pyautogui.write("canada")
    time.sleep(3)
    greenX,greenY = pyautogui.locateCenterOnScreen("vpnCon.png")
    time.sleep(2)
    pyautogui.click(greenX,greenY)
    print("connected Vpn")

def AdsPower():
    print("making new browser profile")
    profileX,profileY = pyautogui.locateCenterOnScreen("newprofile.png")
    time.sleep(2)
    pyautogui.click(profileX,profileY)
    print("clicked the new profile")
    time.sleep(5)
    firX,firY = pyautogui.locateCenterOnScreen("firefox.png")
    time.sleep(2)
    pyautogui.click(firX,firY) 
    time.sleep(4)
    okX,okY = pyautogui.locateCenterOnScreen("ok.png")
    time.sleep(3)
    pyautogui.click(okX,okY)
    time.sleep(10)
    print("browser is made")
    openX,openY = pyautogui.locateCenterOnScreen("open.png")
    pyautogui.click(openX,openY)
    time.sleep(10)
    print("browser is loded!!")

def extenstionAdd():
    time.sleep(5)
    pyautogui.write("https://chromewebstore.google.com/detail/captcha-solver-auto-recog/ifibfemgeogfhoebkmokieepdoobkbpo")
    time.sleep(3)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.press("right",10)
    time.sleep(2)
    installX,installY = pyautogui.locateCenterOnScreen("chrome.png")
    time.sleep(2)
    pyautogui.click(installX,installY)
    time.sleep(2)
    pyautogui.press("right",1)
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(10)
    pyautogui.click(259,285)
    time.sleep(2)
    pyautogui.write("08b3c81f87dab62bace38fc7be0095f8")
    time.sleep(2)
    installX,installY = pyautogui.locateCenterOnScreen("login.png")
    time.sleep(2)
    pyautogui.click(installX,installY)
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.hotkey("ctrl","w")



def login(): #on 2nd tab
    print("login")
    pyautogui.hotkey("ctrl","t")
    time.sleep(5)
    pyautogui.write("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    pyautogui.press("enter")
    time.sleep(6)
    pyautogui.write("ThorstenHertzog456409809@yahoo.com")
    time.sleep(4)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.write("RNPHDW1292")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)
    return "ok"


def loginMail(): #on firt tab
    print("login Mail")
    pyautogui.hotkey("f6")
    time.sleep(5)
    pyautogui.write("https://login.yahoo.com/?.src=ym&lang=en-GB&done=https%3A%2F%2Fmail.yahoo.com%2Fd%2Ffolders%2F1%3F.intl%3Dde%26.lang%3Dde-DE%26.partner%3Dnone%26.src%3Dfp%26guce_referrer%3DaHR0cHM6Ly9sb2dpbi55YWhvby5jb20v%26guce_referrer_sig%3DAQAAAC7DrbyDJEYOPCzqUCinTRpaHDiUgoc3IHYd8e7az_rN1tl6AVV6XADkkMZiSt1ch5k5U5_-zcdjCop-5-1A15tIsIRSA4Ln10VFQfIPocOTrFVBx5gxx_HWOHWTA0xiBENGHsBskCg9JE8MeRNJyI7ywIryrLLP_guyjIdFHQOw&.partner=none")
    pyautogui.press("enter")
    time.sleep(6)
    pyautogui.write("ThorstenHertzog456409809@yahoo.com")
    time.sleep(4)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.write("NitchAccount4")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)
    return "ok"



def otpPage():
    print("checking captcha page")  
    time.sleep(10)
    try: 
        print("idk if found or not")
        if pyautogui.locateCenterOnScreen("otpPage.png") is not None:
            print("captcha page was found")
            time.sleep(15)
            captX,captY = pyautogui.locateCenterOnScreen("capt.png") #clicking the otp solve button to solve otp
            time.sleep(2)
            pyautogui.click(captX,captY)
            time.sleep(15)
            shopX,shopY = pyautogui.locateCenterOnScreen("shop.png") #clicking the otp solve button to solve otp
            time.sleep(2)
            pyautogui.click(shopX,shopY) #click the continuue shopping button  
            print("i think i did captcha")
            if pyautogui.locateCenterOnScreen("otpPage.png") is not None: 
                print("captcha was not solved")
                otpPage() #capthca was not solved
            print("ok")
            return "ok"
    except ImageNotFoundException:
        print("no")   
             

def EmailCode():
    pyautogui.hotkey("alt","1") #yahoo tab
    time.sleep(2)
    pyautogui.hotkey("ctrl","r")
    time.sleep(5)
    print("refreshed now clicking the mail")
    pyautogui.click(592,365)
    print("finding the image")
    time.sleep(5)

    try:
        print("trying to find the image")
        x,y = pyautogui.locateCenterOnScreen("otp.png")
        time.sleep(2)
        print("going to text")
        pyautogui.moveTo(x,y+55)
        time.sleep(4)
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()
        time.sleep(3)
        pyautogui.hotkey("ctrl","c")
        time.sleep(3)
    except:
        print("didnt find the email")
    pyautogui.hotkey("alt","2")
    time.sleep(3)
    pyautogui.click(548,332) #clicking the otp input
    time.sleep(2)
    pyautogui.hotkey('ctrl',"v")
    time.sleep(2)
    pyautogui.write("enter")




#------------ main Program ------------------------------------

#Vpn()
#AdsPower()
extenstionAdd()
loginMail()
login()
# check if the otp page is there or not
otpPage()
print("otp page was done or was not found")
time.sleep(5)
EmailCode()
print("login Done")
