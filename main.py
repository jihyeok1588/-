print("The Love Calculator is calculating your score...")
name1 = input("What is your name?") # What is your name?
name2 = input("What is their name?") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name = name1 + name2

name_count_T = name.count("T")
name_count_t = name.count("t")
name_count_Tt = int(name_count_T + name_count_t)

name_count_R = name.count("R")
name_count_r = name.count("r")
name_count_Rr = int(name_count_R + name_count_r)

name_count_U = name.count("U")
name_count_u = name.count("u")
name_count_Uu = int(name_count_U + name_count_u)

name_count_E = name.count("E")
name_count_e = name.count("e")
name_count_Ee = int(name_count_E + name_count_e)

name_count_L = name.count("L")
name_count_l = name.count("l")
name_count_Ll = int(name_count_L + name_count_l)

name_count_O = name.count("O")
name_count_o = name.count("o")
name_count_Oo = int(name_count_O + name_count_o)

name_count_V = name.count("V")
name_count_v = name.count("v")
name_count_Vv = int(name_count_V + name_count_v)

name_count_E = name.count("E")
name_count_e = name.count("e")
name_count_Ee_1 = int(name_count_E + name_count_e)

score1 = (name_count_Tt + name_count_Rr + name_count_Uu + name_count_Ee)
score2 = (name_count_Ll + name_count_Oo + name_count_Vv + name_count_Ee_1)
score = str(score1) + str(score2)
print(type(score))
score_int = int(score)
print(type(score_int))

if score_int < 10 or score_int > 90:
    print(f"Your score is {score_int}, you go together like coke and mentos.")
elif 40 < score_int < 50:
    print(f"Your score is {score_int}, you are alright together.")
else:
    print(f"Your score is {score_int}.")