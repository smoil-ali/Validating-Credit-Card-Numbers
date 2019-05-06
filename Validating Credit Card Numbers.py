import re

def seq_hyp_checker(str):
    list3=str.split("-")
    str="".join(list3)
    list1 = []
    tval = ""
    for x in str:
        if x not in list1:
            list1.append(x)
            tval = x
            tval += "+"
            y = re.findall(tval, str)
            list2 = list(map(lambda x: len(x), y))
            if max(list2) >= 4:
                return False
    return True


def seq_checker(str):
    list1 = []
    tval = ""
    for x in str:
        if x not in list1:
            list1.append(x)
            tval = x
            tval += "+"
            y = re.findall(tval, str)
            list2 = list(map(lambda x: len(x), y))
            if max(list2)>=4:
                return False
    return True

def start_checker(str):
    val1,val2,val3="^4","^5","^6"
    y=re.findall(val1,str)
    if y==[]:
        y=re.findall(val2,str)
        if y==[]:
            y=re.findall(val3,str)
            if y==[]:
                return False
            else:
                return True
        else:
            return True
    else:
        return True

def check_len(str):
    if len(str)==16:
        return True
    elif len(str)==19:
        return True
    else:
        return False
def check_digits(str):
    if str.isdigit():
        return True
    else:
        return False

def check_separte(str):
    if " " in str or "_" in str:
        return True
    else:
        return False
def check_hyphen_pos(str):
    if str[4]=="-":
        if str[9]=="-":
            if str[14]=="-":
                return True
            else:
                return False
        else:
            return False
    else:
        return False
def check_hyphen(str):
    if "-" in str:
        return True
    else:
        return False

if __name__ == '__main__':
    N=int(input())
    for x in range(N):
        str=input()
        if not check_len(str):
            print("Invalid")
            continue
        if check_separte(str):
            print("Invalid")
            continue
        if not start_checker(str):
            print("Invalid")
            continue
        if check_hyphen(str):
            if not check_hyphen_pos(str):
                print("Invalid")
                continue
            elif not seq_hyp_checker(str):
                print("Invalid")
                continue
            else:
                print("Valid")
                continue
        elif not check_digits(str):
            print("Invalid")
            continue
        elif not seq_checker(str):
            print("Invalid")
            continue
        else:
            print("Valid")









