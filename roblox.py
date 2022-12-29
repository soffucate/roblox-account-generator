from selenium import webdriver
from os import system
import sys
import string, random, time
from playsound import playsound
from typing import Union
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import random
import os
import subprocess
import time
title = f"if u need help dm me on discord squeazzy#0381"
system("title " + title)
def CountingNIggers():
 for i in range(90):
   time.sleep(1)
   print("bypassing ratelimit" + i)
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
wtf = "n"
bot = False
print('')
print(f'skidded gen from github by vilintaskidder (u can skid it too LOOL)')
print('')
print(f"{bcolors.WARNING}Advanced options and tools? (n for fast start) y/n{bcolors.ENDC}")
faststart = input()
print("")
if faststart == "y":
	print(f"{bcolors.WARNING}Type custom bot names (Empty for none){bcolors.ENDC}")
	customuser = input()
	print("")
	print(f"{bcolors.WARNING}Wanna friend request spam an account? y/n{bcolors.ENDC}")
	raid = input()
	print("")
	if raid == "y":
		print(f"{bcolors.WARNING}Paste the link to the account (ex. https://www.roblox.com/users/414153224/profile){bcolors.ENDC}")
		user = input()
		print("")
	print(f"{bcolors.WARNING}Run in manual mode? y/n{bcolors.ENDC}")
	manual = input()
	print("")
	print(f"{bcolors.WARNING}Enable roblox group botter? y/n{bcolors.ENDC}")
	groupbot = input()
	print("")
elif faststart == "a":
	print(f"{bcolors.FAIL}ARE YOU SURE TO RUN FULL SETTINGS DEBUGGER? (y/n){bcolors.ENDC}")
	wtf = input()
	print("")
	if wtf == "y":
		print(f"{bcolors.WARNING}Type custom bot names (Empty for none){bcolors.ENDC}")
		customuser = input()
		print("")
		print(f"{bcolors.WARNING}Wanna friend request spam an account? y/n{bcolors.ENDC}")
		raid = input()
		print("")
		if raid == "y":
			print(f"{bcolors.WARNING}Paste the link to the account (ex. https://www.roblox.com/users/5346316134/profile){bcolors.ENDC}")
			user = input()
			print("")
		print(f"{bcolors.WARNING}Run in manual mode? y/n{bcolors.ENDC}")
		manual = input()
		print("")
		print(f"{bcolors.WARNING}Enable roblox group botter? y/n{bcolors.ENDC}")
		groupbot = input()
		print("")
		print(f"{bcolors.WARNING}Cooldown? (integer){bcolors.ENDC}")
		cd = input()
		print("")
		print(f"{bcolors.WARNING}Bot variable? (y/n){bcolors.ENDC}")
		bot = input()
		print("")
		if bot == "y":
			bot = True
		else: bot = False

	else: pass
elif faststart != "a" and faststart != "y":
	manual = "n"
	raid = "n"
	groupbot = "n"
	customuser = "squeazzy" #Change if nigga
	print(f"{bcolors.WARNING}Fast starting...{bcolors.ENDC}")
	print("")

if groupbot == "y":
	groupbot = True
	print(f"{bcolors.WARNING}Send link to the group you want to bot{bcolors.ENDC}")
	group = input()
	print("")
	print(f"{bcolors.WARNING}Type message to spam on wall (Empty for none){bcolors.ENDC}")
	spammsg = input()
	print("")
else:
	groupbot = False
	spammsg = False

if spammsg == "" or spammsg == " " or spammsg == False:
	wallspam = False
else:
	wallspam = True

if manual == "y" and wtf != "y":
		GENERATION_COOLDOWN = 3
		manual = True
		counter = 7
elif wtf != "y":
		GENERATION_COOLDOWN = 70
		manual = False
elif wtf == "y":
	GENERATION_COOLDOWN = cd

if raid == "y":
	raid = True
else:
	raid = False

# Default = True
FOCUS_ON_REVERSE_CHECKING = True

closeddriver = False
thefucknigga = False
options = Options()
options.add_argument('log-level=3')
options.add_extension("solver.crx")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
if manual == False:
		options.add_argument('headless')
		options.add_argument('window-size=1920x1080')
		options.add_argument("disable-gpu")
PATH = 'C:/Path/To/Chromedriver/Projects/RobloxAccountGenerator/chromedriver'

def closeDriver(drvr: webdriver.Chrome):
	drvr.close()
	drvr.quit()
def waitForElementAppear(strategy, locator, driver, timeout=10) -> Union[WebElement, bool]:
	try:
		element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((strategy, locator)))
	except (TimeoutException, NoSuchElementException):
		return False
	return element
def waitForElementClickable(strategy, locator, driver, timeout=10) -> Union[WebElement, bool]:
	try:
		element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((strategy, locator)))
	except (TimeoutException, NoSuchElementException):
		return False
	return element
def waitForElementDisappear(strategy, locator, driver, timeout=10) -> Union[WebElement, bool]:
	try:
		element = WebDriverWait(driver, timeout).until_not(EC.presence_of_element_located((strategy, locator)))
	except (TimeoutException, NoSuchElementException):
		return False
	return element
def generateUserPass(chars=string.ascii_lowercase+string.digits):
	length = random.randint(10, 14)
	if customuser == None or customuser == "n":
		length = random.randint(10, 14)
		user = ""
	else:
		length = random.randint(8, 12)
		user = customuser
	passwordLength = 16
	password = ""
	for i in range(length):
		char = random.choice(chars)
		user += char.upper() if random.randint(0,1) == 1 else char if char.isalpha() else char
	for i in range(passwordLength):
		char = random.choice(chars)
		password += char.upper() if random.randint(0,1) == 1 else char if char.isalpha() else char
	# password = user[::-1]
	return { "username": user, "password": password }


def main():
        try:
                driver = webdriver.Chrome(options=options)
                drivers = [driver]

                for driver in reversed(drivers):
                        # driver: webdriver.Chrome
                        driver.get('https://www.roblox.com/')

                for driver in drivers:
                        # Accept Cookies
                        print(f"{bcolors.OKGREEN}\nStarted generating an account.{bcolors.ENDC}")
                        if cookieButton := waitForElementClickable(By.CLASS_NAME, "btn-cta-lg", driver, 4):
                                cookieButton.click()
                                print(f"{bcolors.WARNING}Cookies accepted{bcolors.ENDC}")
                        print("wait")
                        CountingNIggers()
                        print("Done!")
                        #time.sleep(90)
                        


                        # Initialize elements
                        try:
                                months = Select(driver.find_element(By.ID, "MonthDropdown"))
                                days = Select(driver.find_element(By.ID, "DayDropdown"))
                                years = Select(driver.find_element(By.ID, "YearDropdown"))
                                username = driver.find_element(By.ID, "signup-username")
                                password = driver.find_element(By.ID, "signup-password")
                                femaleButton = driver.find_element(By.ID, "FemaleButton")
                                maleButton = driver.find_element(By.ID, "MaleButton")
                                submitButton = waitForElementClickable(By.ID, "signup-button", driver)
                        except NoSuchElementException:
                                print(f"{bcolors.FAIL}Unable to locate element.{bcolors.ENDC}")
                                thefucknigga = True
                                return closeDriver(driver)
                        except TimeoutException:
                                print(f"{bcolors.FAIL}Timed out to locate elements.{bcolors.ENDC}")
                                thefucknigga = True
                                return closeDriver(driver)

                        # Fill in the Form
                        # Birthday
                        try:
                                months.select_by_value('Jul')
                                days.select_by_value('09')
                                years.select_by_value('2000')
                        except:
                                print(f"{bcolors.FAIL}Unable to fill birthday.{bcolors.ENDC}")
                                thefucknigga = True
                                return closeDriver(driver)

                        # Credentials
                        credentials = generateUserPass()
                        username.send_keys(credentials["username"])
                        password.send_keys(credentials["password"])

                        # Gender
                        femaleButton.click() if random.randint(0,1) == 1 else maleButton.click()

                        # Submit the Form
                        try:
                                time.sleep(0.2)
                                submitButton.click()
                                time.sleep(0.2)
                                submitButton.click()
                                time.sleep(0.2)
                                submitButton.click()
                        except: pass

                        # Username validation
                        if usernameWarning := driver.find_element(By.ID, "signup-usernameInputValidation"):
                                retries = 0
                                while usernameWarning.text == "Username not appropriate for Roblox.":
                                        if retries == 3:
                                                print(f"{bcolors.FAIL}Error 602: Username not appropriate for Roblox - max. retries (3) exceeded. Could not fetch account information.{bcolors.ENDC}")
                                                return closeDriver(driver)
                                        retries += 1

                                        credentials = generateUserPass()
                                        username.clear()
                                        password.clear()
                                        time.sleep(0.3)
                                        username.send_keys(credentials["username"])
                                        password.send_keys(credentials["password"])
                                        time.sleep(0.3)
                                        submitButton.click()


                        # Handling captcha and awaiting menu
                        captchaSuccess = False

                        if waitForElementAppear(By.CLASS_NAME, "icon-nav-settings", driver, 7):
                                captchaSuccess = True
                                print(f"{bcolors.OKGREEN}No Captcha!{bcolors.ENDC}")
                        else:
                                # FunCaptcha or Menu loading too long
                                if waitForElementAppear(By.CLASS_NAME, "modal-modern-challenge-captcha", driver, 4):
                                        print(f"{bcolors.FAIL}Captcha met!{bcolors.ENDC}")
                                        if manual == False:
                                                return closeDriver(driver)

                                        # If captcha was solved
                                        if waitForElementDisappear(By.CLASS_NAME, "modal-modern-challenge-captcha", driver, 20):
                                                captchaSuccess = True
                                        else:
                                                captchaSuccess = False
                                                if captchaSuccess == False and manual == False:
                                                        return closeDriver(driver)

                                # Checking if menu is loading too long
                                elif waitForElementAppear(By.CLASS_NAME, "icon-nav-settings", driver, 3):
                                        captchaSuccess = True
                                else:
                                        captchaSuccess = False
                                        print(f"{bcolors.FAIL}Error 603: Timeout exceeded.{bcolors.ENDC}")
                                        thefucknigga = True


                        if captchaSuccess == True:
                                print(f"{bcolors.OKGREEN}Fetched account information{bcolors.ENDC}")
                                with open("altsrblx.txt", "a", encoding="utf-8") as f:
                                        f.write(f"{credentials['username']}:{credentials['password']}\n")
                        else:
                                print(f"{bcolors.FAIL}Error 601: Could not fetch account information.{bcolors.ENDC}")

                        if raid == False and bot == False:
                                return closeDriver(driver)
                                closeddriver = True
                        else:
                                closeddriver = False

                        if raid == True or bot == True:
                                driver.get(user)

                        if raid == True:
                                if waitForElementAppear(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/ul[2]/li[1]/button", driver, 3):
                                        fadd = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/ul[2]/li[1]/button')
                                        fadd.click()
                                        time.sleep(0.4)
                                        fadd.click()
                                        time.sleep(0.2)
                                        fadd.click()
                                        time.sleep(0.1)
                                        print(f"{bcolors.WARNING}Sent friend request!{bcolors.ENDC}")
                                        if raid == True and bot == False and groupbot == False:
                                                return closeDriver(driver)

                        if bot == True:
                                if waitForElementClickable(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/div/div[1]/div/div[3]/button", driver):
                                        followa = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/ul[2]/li[1]/button')
                                        followa.click()
                                        if waitForElementAppear(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/div/div[1]/div/div[3]/div/div[2]/div/ul/li[2]/button", driver):
                                                followb = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[2]/div/div[1]/div/div[3]/div/div[2]/div/ul/li[2]/button')
                                                followb.click()
                                        time.sleep(1)
                                        print(f"{bcolors.WARNING}Followed!{bcolors.ENDC}")


                        if groupbot == True:
                                try:
                                        driver.get(group)
                                except:
                                        print(f"{bcolors.FAIL}Can't load group page!{bcolors.ENDC}")
                        try:
                                if groupbot == True:
                                        if waitForElementClickable(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[3]/div/button", driver):
                                                time.sleep(0.1)
                                                try:
                                                        botterr = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[3]/div/button')
                                                        botterr.click()
                                                        time.sleep(1)
                                                        print(f"{bcolors.WARNING}Joined group!{bcolors.ENDC}")
                                                except:
                                                        print(f"{bcolors.FAIL}Failed to find button to join!{bcolors.ENDC}")
                                                if wallspam == True:
                                                        try:
                                                                time.sleep(1)
                                                                driver.get(group)
                                                                wall = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div/div[2]/div/group-wall/div/div[2]/div[1]/div/textarea')
                                                                wall.send_keys(spammsg)
                                                                time.sleep(0.2)
                                                        except:
                                                                print(f"{bcolors.FAIL}Failed to spam the wall!{bcolors.ENDC}")
                                                        try:
                                                                if waitForElementAppear(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div/div[2]/div/group-wall/div/div[2]/div[1]/button', driver):
                                                                        postbutton = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div/div[2]/div/group-wall/div/div[2]/div[1]/button')
                                                                        postbutton.click()
                                                        except:
                                                                print(f"{bcolors.FAIL}Failed to press button to send!{bcolors.ENDC}")
                                                                pass
                                                        else:
                                                                try:
                                                                        driver.get(group)
                                                                        time.sleep(1)
                                                                        postbutton = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div/div[2]/div/group-wall/div/div[2]/div[1]/button')
                                                                        postbutton.click()
                                                                except:
                                                                        print(f"{bcolors.FAIL}Failed the retry!{bcolors.ENDC}")
                        except:
                                print(f"{bcolors.FAIL}Failed to spam (global)!{bcolors.ENDC}")
                                pass

                if closeddriver == False:
                        return closeDriver(driver)
        except:
                pass


while True:
	main()
	print(f"{bcolors.WARNING}Loaded!{bcolors.ENDC}")
	if thefucknigga == False:
			if manual == True and counter > 0:
				counter = counter - 1
				time.sleep(GENERATION_COOLDOWN)
			elif manual == True and counter == 0:
				print(f"{bcolors.WARNING}Bypassing the antibot!{bcolors.ENDC}")
				time.sleep(61)
				print(f"{bcolors.WARNING}Bypassed the antibot!{bcolors.ENDC}")
				counter = 7
			else:
				time.sleep(GENERATION_COOLDOWN)
			thefucknigga = False
	if thefucknigga == True:
			time.sleep(2)
			thefucknigga = False
