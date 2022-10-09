import time
am = "and mouth and "
ee = "and eyes and ears"
kt = "knees and toes"
ac = "arms and chins"
ll = "legs and lips"
name = input("Hi! What's your name? ")
print("ah nice to meet you " +name)
qn = input("I want to sing you a song, can I?")
if qn == "yes" or "Yes" or " yes" or "ok":
    print("Great! OK let me get ready")
    print(" ")
    time.sleep(3)
# this allows the program to be in a loop = for i in range(number of times it loops)
    for i in range(2):
        print("head and shoulders " +kt)
        time.sleep(2)
        print(kt)
        time.sleep(3)
    print(ee)
    time.sleep(3)
    print(am +"nose")
    time.sleep(3)
    print("head and shoulders " +kt)
    time.sleep(3)
    print(kt)
    print(" ")
    time.sleep(4)
    for i in range(2):
        print("feet and tummies " +ac)
        time.sleep(2)
        print(ac)
        time.sleep(3)
    print(ee)
    time.sleep(3)
    print(am +"shins")
    time.sleep(3)
    print("feet and tummies " +ac)
    time.sleep(3)
    print(ac)
    time.sleep(3)
    print(" ")
    for i in range(2):
        print("hands and fingers " +ll)
        time.sleep(2)
        print(ll)
        time.sleep(3)
    print(ee)
    time.sleep(3)
    print(am +"hips")
    time.sleep(3)
    print("feet and tummies " +ac)
    time.sleep(3)
    print(ac)
    time.sleep(5)
    print(" ")
    print("So... did you like it?? ^^")
else:
    print("Ok, have a good day!")