import keyboard as kb
import random

def writeWords():
    hotkey = input("\033[1;35;40m\033[+] choose a hotkey [default: R]: ")
    if hotkey:
        print(f"\033[1;31;40m[+]\033[+] all set just press '{hotkey.upper()}' when ready!")
        with open("wordlist.txt", "r") as file:
            for word in file:
                kb.wait(hotkey)
                kb.write(word)
                kb.press("Enter")
    elif hotkey == "":
        print(f"\033[1;31;40m[+]\033[+] all set just press 'R' when ready!")
        with open("wordlist.txt", "r") as file:
            for word in file:
                kb.wait("r")
                kb.write(word)
                kb.press("Enter")
     elif hotkey.lower() == "none":
        with open("wordlist.txt", "r") as file:
            for count in range(5):
                print(f"starting in {count}..."
                sleep(1)
            for word in file:
                kb.write(word)
                kb.press("Enter")
    else:
        print(f"[+] {hotkey} is an invalid hotkey!")


def wordGen():
    number_of_words = int(input("\033[1;33;40m[+]\033[+] how many lines to generate?: "))
    letters_to_add = int(input("\033[1;33;40m[+]\033[+] how many letters for each line?: "))
    print("\033[1;31;40m\033[+] generating words...")
    num = 0
    word = ""
    chars = "abcdefghijklmnopqrstuvxyz!#%&/()=?@$€{[]}|`+ABCDEFGHIJKLMNOPQRSTUVXYZ"
    while num <= number_of_words: 
        for i in range(0,letters_to_add):
            word += random.choice(chars)
        with open("wordlist.txt", "a") as Wlist:
            Wlist.write(word)
            Wlist.write("\n")
            num += 1
            word = ""
    print("[+] words added!")
    writeWords()

        


if __name__ == "__main__":
    wordGen()
