comandProblemPc ="Start-Process 'http://help/OTWG/Login.aspx?lang=ru&singleton=3&guestlogin=1&tzo=1000&id=25425475'"
comandSignature = "Start-Process 'https://confluence.sogaz.ru/pages/viewpage.action?pageId=297259051&preview=/297259051/297259063/%D0%98%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B8%20%D0%B2%20MS%20Outlook%202016.docx'"
comandClearTemp = r"Remove-Item C:\Users\$env:UserName\AppData\Local\Temp\* -Recurse -Force -ErrorAction SilentlyContinue"
comandNetCache = r"Remove-Item C:\Users\$env:UserName\AppData\Local\Microsoft\Windows\INetCache\* -Recurse -Force -ErrorAction SilentlyContinue"
comandCookies = r"Remove-Item C:\Users\$env:UserName\AppData\Local\Microsoft\Windows\INetCookies\* -Recurse -Force -ErrorAction SilentlyContinue"
comandClearEdge = r'Remove-Item "C:\Users\$env:UserName\AppData\Local\Microsoft\Edge\User Data\Default\Cache\*" -Recurse -Force -ErrorAction SilentlyContinue'
commandStopOutlook = "Stop-Process -Name OUTLOOK"
comandClearYandex = r'Remove-Item "C:\Users\$env:UserName\AppData\Local\Yandex\YandexBrowser\User Data\Default\Cache\*" -Recurse -Force -ErrorAction SilentlyContinue'
commandChangeCartridge = "Start-Process 'http://help/OTWG/Login.aspx?lang=ru&singleton=3&guestlogin=1&tzo=1000&id=25425395'"
commandAddNewPrinterSpp = "Start-Process 'http://help/OTWG/Login.aspx?lang=ru&singleton=3&guestlogin=1&tzo=1000&id=25425394'"
comandClearJava = r"Remove-Item C:\Users\$env:UserName\AppData\LocalLow\Sun\Java\Deployment\cache\* -Recurse -Force -ErrorAction SilentlyContinue"
commandRejectCitrixSpp = "Start-Process 'http://help/OTWG/Login.aspx?lang=ru&singleton=3&guestlogin=1&tzo=1000&id=25425387'"
commandBidRemote = "Start-Process 'http://help/OTWG/Login.aspx?lang=ru&singleton=3&guestlogin=1&tzo=1000&id=25425606'"