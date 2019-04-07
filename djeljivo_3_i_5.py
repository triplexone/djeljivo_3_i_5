cnt3 = 0
cnt5 = 0
cnt35 = 0

while True:
    broj = int(input("Unesi broj djeljiv sa 3 ili 5: "))

    if broj % 3 == 0 and broj % 5 == 0:
        cnt35 += 1
    elif broj % 3 == 0:
        cnt3 += 1
    elif broj % 5 == 0:
        cnt5 += 1
    else:
        print("\nUnesena su " + str(cnt3) + " broja djeljiva sa 3.")
        print("Unesena su " + str(cnt5) + " broja djeljiva sa 5.")
        print("Unesena su " + str(cnt35) + " broja djeljiva sa 3 i 5.")
        break

