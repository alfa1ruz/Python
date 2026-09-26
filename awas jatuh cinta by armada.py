import sys
import time


def jalanin_lirik():
    lirik = [
        ("Awas nanti jatuh cinta", 0.1),
        ("Cinta kepada dirikuuuu", 0.1),
        ("Jangan-jangan ku jodohmu", 0.1),
        ("Kamu terlalu membenci", 0.1),
        ("Membenci dirikuuu iniii", 0.1),
        ("Awas nanti jatuh cinta padaku", 0.1),
    ]

    delay = [0.3, 0.3, 0.4, 1, 0.2, 0.4]

    print("\n== Awas Jatuh Cinta - Armada ==")
    time.sleep(2)

    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end="")
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print("")  
    print("\n// follow my github")


if __name__ == "__main__":
    jalanin_lirik()