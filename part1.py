

def element_type(a):

    #It returns the type of expression the element is.
    if isinstance(a,str):
        if a.isnumeric()==True:
            return 'integer_constant'
        elif a=='True' or a=='False':
            return 'boolean'
        else:
            return 'variable'
    elif isinstance(a,int):
        return 'integer_constant'


def search(a,A):
    # Search for an element in the list A.
    if A==[]:
        return False
    elif element_type(a)=='integer_constant' or element_type(a)=='boolean':
        l = len(A)
        j = 0
        S = False
        while j < l and (not S):
            if A[j] == a:
                S = True
            elif j<l and not S:
                j += 1
        return S

    elif element_type(a)=='variable':
        l = len(A)
        j = 0
        S = False
        while j < l and (not S):
            if A[j]==a:
                S = False
                j += 1
            elif A[j] != a:
                S = False
                j += 1
            elif a in A[j]:
                S = True
            elif j < l and not S:
                j += 1
        return S
a=[2,3,('x',5),1]
print(search(6,a))
print(search('x',a))



def search_index(a,A):
    # Returns the index value of the element a in the list A.
    if A==[]:
        return False
    elif element_type(a)=='integer_constant' or element_type(a)=='boolean':
        l = len(A)
        m = 0
        S = False
        while m < l and (not S):
            if A[m]==a:
                S = True
            elif m<l and not S:
                m += 1
        return m
    elif element_type(a)=='variable':
        l = len(A)
        m = 0
        S = False
        while m < l and (not S):
            if element_type(A[m]) == 'integer_constant' or element_type(A[m]) == 'boolean':
                S = False
                m += 1
            elif isinstance(A[m], tuple):
                if a in A[m]:
                    S = True
            elif m < l and not S:
                m += 1
        return m
a=[1,2,3,('x',5)]
print(5 in a[3])
print('x' == a[3])
print(search_index('x', a))
print(element_type(a[3]))
print(isinstance(a[3], tuple))



GARBAGE_LIST=[]
def interpret(B):
# This will be used to interpret the token_list.
    l=len(B)
    i=0
    GARBAGE_LIST=[]
    DATA_LIST=[]
    if not search(B[i],DATA_LIST) and element_type(B[i])=='variable':
        if ((i+2)<len(B) and (i+4)>len(B)) and element_type(B[i+2])=='integer_constant':
            if not search(B[i],DATA_LIST) and not search(B[i+2],DATA_LIST):
                DATA_LIST.append(int(B[i+2]))
                DATA_LIST.append((B[i],search_index(int(B[i+2]),DATA_LIST)))
                return DATA_LIST
            elif search(B[i],DATA_LIST) and not search(B[i+2],DATA_LIST):
                DATA_LIST.append(int(B[i+2]))
                DATA_LIST.append((B[i],search_index(int(B[i+2]),DATA_LIST)))
                return DATA_LIST
        elif ((i+2)<len(B) and (i+4)>len(B)) and (not search(B[i],DATA_LIST) and element_type(B[i+2])=='variable'):
            DATA_LIST.append((B[i+2],DATA_LIST[search_index(B[i],DATA_LIST)][1]))
            return DATA_LIST
        elif (i+4)<len(B) and element_type(B[i+2])=='integer_constant' and element_type(B[i+4])=='integer_constant':
            if not search(B[i],DATA_LIST) and not search(B[i+2],DATA_LIST) and not search(B[i+4],DATA_LIST):
                DATA_LIST.append(int(B[i+2]))
                DATA_LIST.append(int(B[i+4]))
                if B[i+3]=='+' and not search(int(B[i+2])+int(B[i+4]),DATA_LIST):
                    DATA_LIST.append(int(B[i+2])+int(B[i+4]))
                    DATA_LIST.append((B[i], search_index(int(B[i+2])+int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='+' and search(int(B[i+2])+int(B[i+4]),DATA_LIST):
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) + int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='-' and not search(int(B[i+2])-int(B[i+4]),DATA_LIST):
                    DATA_LIST.append(int(B[i+2])-int(B[i+4]))
                    DATA_LIST.append((B[i], search_index(int(B[i+2])-int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='-' and search(int(B[i+2])-int(B[i+4]),DATA_LIST):
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) - int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='*' and not search(int(B[i+2])*int(B[i+4]),DATA_LIST):
                    DATA_LIST.append(int(B[i+2])*int(B[i+4]))
                    DATA_LIST.append((B[i], search_index(int(B[i+2])*int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='*' and search(int(B[i+2])*int(B[i+4]),DATA_LIST):
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) * int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='/' and not search(int(B[i+2])/int(B[i+4]),DATA_LIST):
                    DATA_LIST.append(int(B[i+2])/int(B[i+4]))
                    DATA_LIST.append((B[i], search_index(int(B[i+2])/int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='/' and search(int(B[i+2])/int(B[i+4]),DATA_LIST):
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) / int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
            elif not search(B[i], DATA_LIST) and search(int(B[i+2]), DATA_LIST) and not search(int(B[i+4]), DATA_LIST):

                DATA_LIST.append(int(B[i+4]))
                if B[i + 3] == '+' and not search(int(B[i+2]) + int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) + int(B[i+4]))
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) + int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '+' and search(int(B[i+2]) + int(B[i+4]), DATA_LIST):
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) + int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '-' and not search(int(B[i+2]) - int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) - int(B[i+4]))
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) - int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '-' and search(int(B[i+2]) - int(B[i+4]), DATA_LIST):
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) - int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '*' and not search(int(B[i+2]) * int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) * int(B[i+4]))
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) * int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '*' and search(int(B[i+2]) * int(B[i+4]), DATA_LIST):
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) * int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '/' and not search(int(B[i+2]) / int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) / int(B[i+4]))
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) / int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '/' and search(int(B[i+2]) / int(B[i+4]), DATA_LIST):
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) / int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
            elif not search(B[i], DATA_LIST) and not search(int(B[i+2]), DATA_LIST) and search(int(B[i+4]), DATA_LIST):
                DATA_LIST.append(int(B[i+2]))
                if B[i + 3] == '+' and not search(int(B[i+2]) + int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) + int(B[i+4]))
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) + int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '+' and search(int(B[i+2]) + int(B[i+4]), DATA_LIST):
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) + int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '-' and not search(int(B[i+2]) - int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) - int(B[i+4]))
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) - int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '-' and search(int(B[i+2]) - int(B[i+4]), DATA_LIST):
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) - int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '*' and not search(int(B[i+2]) * int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) * int(B[i+4]))
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) * int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '*' and search(int(B[i+2]) * int(B[i+4]), DATA_LIST):
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) * int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '/' and not search(int(B[i+2]) / int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) / int(B[i+4]))
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) / int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '/' and search(int(B[i+2]) / int(B[i+4]), DATA_LIST):
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) / int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
            elif not search(B[i], DATA_LIST) and search(int(B[i+2]), DATA_LIST) and search(int(B[i+4]), DATA_LIST):

                if B[i + 3] == '+' and not search(int(B[i+2]) + int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) + int(B[i+4]))
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) + int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '+' and search(int(B[i+2]) + int(B[i+4]), DATA_LIST):
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) + int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '-' and not search(int(B[i+2]) - int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) - int(B[i+4]))
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) - int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '-' and search(int(B[i+2]) - int(B[i+4]), DATA_LIST):
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) - int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '*' and not search(int(B[i+2]) * int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) * int(B[i+4]))
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) * int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '*' and search(int(B[i+2]) * int(B[i+4]), DATA_LIST):
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) * int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '/' and not search(int(B[i+2]) / int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) / int(B[i+4]))
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) / int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '/' and search(int(B[i+2]) / int(B[i+4]), DATA_LIST):
                    DATA_LIST.append((B[i], search_index(int(B[i+2]) / int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST

        elif (i + 4) < len(B) and element_type(B[i + 2]) == 'variable' and element_type(B[i + 4]) == 'integer_constant':
            if not search(int(B[i + 4]), DATA_LIST):
                DATA_LIST.append(int(B[i + 4]))
                if B[i + 3] == '+':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] + int(B[i + 4]), DATA_LIST):
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] + int(B[i + 4]), DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] + int(B[i + 4]),
                                    DATA_LIST):
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] + int(B[i + 4]))
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] + int(B[i + 4]), DATA_LIST)))
                        return DATA_LIST
                elif B[i + 3] == '-':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] - int(B[i + 4]), DATA_LIST):
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] - int(B[i + 4]), DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] - int(B[i + 4]),
                                    DATA_LIST):
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] - int(B[i + 4]))
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] - int(B[i + 4]), DATA_LIST)))
                        return DATA_LIST
                elif B[i + 3] == '*':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] * int(B[i + 4]), DATA_LIST):
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] * int(B[i + 4]), DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] * int(B[i + 4]),
                                    DATA_LIST):
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] * int(B[i + 4]))
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] * int(B[i + 4]), DATA_LIST)))
                        return DATA_LIST
                if B[i + 3] == '/':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] / int(B[i + 4]), DATA_LIST):
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] / int(B[i + 4]), DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] / int(B[i + 4]),
                                    DATA_LIST):
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] / int(B[i + 4]))
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] / int(B[i + 4]), DATA_LIST)))
                        return DATA_LIST
            elif search(int(B[i + 4]), DATA_LIST):
                if B[i + 3] == '+':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] + int(B[i + 4]), DATA_LIST):
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] + int(B[i + 4]), DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] + int(B[i + 4]),
                                    DATA_LIST):
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] + int(B[i + 4]))
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] + int(B[i + 4]), DATA_LIST)))
                        return DATA_LIST
                elif B[i + 3] == '-':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] - int(B[i + 4]), DATA_LIST):
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] - int(B[i + 4]), DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] - int(B[i + 4]),
                                    DATA_LIST):
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] - int(B[i + 4]))
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] - int(B[i + 4]), DATA_LIST)))
                        return DATA_LIST
                elif B[i + 3] == '*':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] * int(B[i + 4]), DATA_LIST):
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] * int(B[i + 4]), DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] * int(B[i + 4]),
                                    DATA_LIST):
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] * int(B[i + 4]))
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] * int(B[i + 4]), DATA_LIST)))
                        return DATA_LIST
                if B[i + 3] == '/':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] / int(B[i + 4]), DATA_LIST):
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] / int(B[i + 4]), DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] / int(B[i + 4]),
                                    DATA_LIST):
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] / int(B[i + 4]))
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] / int(B[i + 4]), DATA_LIST)))
                        return DATA_LIST


        elif (i + 4) < len(B) and (element_type(B[i+2])=='boolean' and element_type(B[i+4])=='boolean'):
            if not search(B[i], DATA_LIST) and not search(eval(B[i+2]), DATA_LIST) and not search(eval(B[i+4]), DATA_LIST):
                DATA_LIST.append(eval(B[i+2]))
                DATA_LIST.append(eval(B[i+4]))
                if B[i+3]=='and' and not search(eval(B[i+2]) and eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append(eval(B[i+2]) and eval(B[i+4]))
                    DATA_LIST.append((B[i], search_index(eval(B[i+2]) and eval(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='and' and search(eval(B[i+2]) and eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append((B[i], search_index(eval(B[i+2]) and eval(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='or' and not search(eval(B[i+2]) or eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append(eval(B[i+2]) or eval(B[i+4]))
                    DATA_LIST.append((B[i], search_index(eval(B[i+2]) or eval(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='or' and search(eval(B[i+2]) or eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append((B[i], search_index(eval(B[i+2]) or eval(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
            elif not search(B[i],DATA_LIST) and search(eval(B[i+2]),DATA_LIST) and not search(eval(B[i+4]),DATA_LIST):
                DATA_LIST.append(eval(B[i+2]))
                if B[i+3]=='and' and not search(eval(B[i+2]) and eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append(eval(B[i+2]) and eval(B[i+4]))
                    DATA_LIST.append((B[i], search_index(eval(B[i+2]) and eval(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='and' and search(eval(B[i+2]) and eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append((B[i], search_index(eval(B[i+2]) and eval(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='or' and not search(eval(B[i+2]) or eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append(eval(B[i+2]) or eval(B[i+4]))
                    DATA_LIST.append((B[i], search_index(eval(B[i+2]) or eval(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='or' and search(eval(B[i+2]) or eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append((B[i], search_index(eval(B[i+2]) or eval(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
            elif not search(B[i], DATA_LIST) and not search(eval(B[i+2]), DATA_LIST) and search(eval(B[i+4]), DATA_LIST):
                DATA_LIST.append(eval(B[i+2]))
                if B[i+3]=='and' and not search(eval(B[i+2]) and eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append(eval(B[i+2]) and eval(B[i+4]))
                    DATA_LIST.append((B[i], search_index(eval(B[i+2]) and eval(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='and' and search(eval(B[i+2]) and eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append((B[i], search_index(B[i+2] and int(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='or' and not search(eval(B[i+2]) or eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append(eval(B[i+2]) or eval(B[i+4]))
                    DATA_LIST.append((B[i], search_index(eval(B[i+2]) or eval(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='or' and search(eval(B[i+2]) or eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append((B[i], search_index(eval(B[i+2]) or eval(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
            elif not search(B[i], DATA_LIST) and search(eval(B[i+2]), DATA_LIST) and search(eval(B[i+2]), DATA_LIST):
                if B[i+3]=='and' and not search(eval(B[i+2]) and eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append(eval(B[i+2]) and eval(B[i+4]))
                    DATA_LIST.append((B[i], search_index(eval(B[i+2]) and eval(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='and' and search(eval(B[i+2]) and eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append((B[i], search_index(eval(B[i+2]) and eval(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='or' and not search(eval(B[i+2]) or eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append(eval(B[i+2]) or eval(B[i+4]))
                    DATA_LIST.append((B[i], search_index(eval(B[i+2]) or eval(B[i+4]), DATA_LIST)))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='or' and search(eval(B[i+2]) or eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append((B[i], search_index(eval(B[i+2]) or eval(B[i+2]), DATA_LIST)))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    return DATA_LIST
        elif ((i + 2) < len(B) and (i + 4) > len(B)) and element_type(B[i + 2]) == 'variable':
            DATA_LIST.append((B[i], DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]))
            return DATA_LIST

    elif search(B[i],DATA_LIST) and element_type(B[i])=='variable':
        if ((i+2)<len(B) and (i+4)>len(B)) and element_type(B[i+2])=='integer_constant':
            if not search(int(B[i+2]),DATA_LIST):
                DATA_LIST.append(int(B[i+2]))
                GARBAGE_LIST.append(DATA_LIST[search_index(B[i],DATA_LIST)])
                DATA_LIST[search_index(B[i],DATA_LIST)]=(B[i],search_index(int(B[i+2]),DATA_LIST))
                return DATA_LIST
            elif search(int(B[i+2]),DATA_LIST):
                GARBAGE_LIST.append(DATA_LIST[search_index(B[i],DATA_LIST)])
                DATA_LIST[search_index(B[i],DATA_LIST)]=(B[i],search_index(int(B[i+2]),DATA_LIST))
                return DATA_LIST
        elif ((i+2)<len(B) and (i+4)>len(B)) and element_type(B[i+2])=='boolean':
            if not search(eval(B[i+2]),DATA_LIST):
                DATA_LIST.append(eval(B[i+2]))
                GARBAGE_LIST.append(DATA_LIST[search_index(B[i],DATA_LIST)])
                DATA_LIST[search_index(B[i],DATA_LIST)]=(B[i],search_index(eval(B[i+2]),DATA_LIST))
                return DATA_LIST
            elif search(eval(B[i+2]),DATA_LIST):
                GARBAGE_LIST.append(DATA_LIST[search_index(B[i],DATA_LIST)])
                DATA_LIST[search_index(B[i],DATA_LIST)]=(B[i],search_index(eval(B[i+2]),DATA_LIST))
                return DATA_LIST
        elif ((i+2)<len(B) and (i+4)>len(B)) and element_type(B[i+2])=='variable':
            DATA_LIST[search_index(B[i],DATA_LIST)]=(B[i],DATA_LIST[search_index(B[i+2],DATA_LIST)][1])

        elif (i+4)<len(B) and element_type(B[i+2])=='integer_constant' and element_type(B[i+4])=='integer_constant':

            if not search(int(B[i+2]),DATA_LIST) and not search(int(B[i+4]),DATA_LIST):
                DATA_LIST.append(int(B[i+2]))
                DATA_LIST.append(int(B[i+4]))

                if B[i+3]=='+' and not search(int(B[i+2])+int(B[i+4]),DATA_LIST):
                    DATA_LIST.append(int(B[i+2])+int(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)]=(B[i],search_index(int(B[i+2])+int(B[i+4]),DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='+' and search(int(B[i+2])+int(B[i+4]),DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) + int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='-' and not search(int(B[i+2])-int(B[i+4]),DATA_LIST):
                    DATA_LIST.append(int(B[i+2])-int(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) - int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='-' and search(int(B[i+2])-int(B[i+4]),DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) - int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='*' and not search(int(B[i+2])*int(B[i+4]),DATA_LIST):
                    DATA_LIST.append(int(B[i+2])*int(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) * int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='*' and search(int(B[i+2])*int(B[i+4]),DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) * int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='/' and not search(int(B[i+2])/int(B[i+4]),DATA_LIST):
                    DATA_LIST.append(int(B[i+2])/int(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) / int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='/' and search(int(B[i+2])/int(B[i+4]),DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) / int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST

            elif search(int(B[i+2]), DATA_LIST) and (not search(int(B[i+4]), DATA_LIST)):

                DATA_LIST.append(int(B[i+4]))
                if B[i + 3] == '+' and (not search(int(B[i+2]) + int(B[i+4]), DATA_LIST)):
                    DATA_LIST.append(int(B[i+2]) + int(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) + int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '+' and search(int(B[i+2]) + int(B[i+4]), DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) + int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '-' and not search(int(B[i+2]) - int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) - int(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) - int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST

                elif B[i + 3] == '-' and search(int(B[i+2]) - int(B[i+4]), DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) - int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '*' and not search(int(B[i+2]) * int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) * int(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) * int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '*' and search(int(B[i+2]) * int(B[i+4]), DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) * int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '/' and not search(int(B[i+2]) / int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) / int(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) / int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '/' and search(int(B[i+2]) / int(B[i+4]), DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) / int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
            elif (not search(int(B[i+2]), DATA_LIST)) and search(int(B[i+4]), DATA_LIST):
                DATA_LIST.append(int(B[i+2]))
                if B[i + 3] == '+' and not search(int(B[i+2]) + int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) + int(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) + int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '+' and search(int(B[i+2]) + int(B[i+4]), DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) + int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '-' and not search(int(B[i+2]) - int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) - int(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) - int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '-' and search(int(B[i+2]) - int(B[i+4]), DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) - int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '*' and not search(int(B[i+2]) * int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) * int(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) * int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '*' and search(int(B[i+2]) * int(B[i+4]), DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) * int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '/' and not search(int(B[i+2]) / int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) / int(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) / int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '/' and search(int(B[i+2]) / int(B[i+4]), DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) / int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
            elif search(int(B[i+2]), DATA_LIST) and search(int(B[i+4]), DATA_LIST):

                if B[i + 3] == '+' and not search(int(B[i+2]) + int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) + int(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) + int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '+' and search(int(B[i+2]) + int(B[i+4]), DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) + int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '-' and not search(int(B[i+2]) - int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) - int(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) - int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '-' and search(int(B[i+2]) - int(B[i+4]), DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) - int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '*' and not search(int(B[i+2]) * int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) * int(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) * int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '*' and search(int(B[i+2]) * int(B[i+4]), DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) * int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '/' and not search(int(B[i+2]) / int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]) / int(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) / int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
                elif B[i + 3] == '/' and search(int(B[i+2]) / int(B[i+4]), DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(int(B[i+2]) / int(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(int(B[i+2]))
                    GARBAGE_LIST.append(int(B[i+4]))
                    return DATA_LIST
        elif (i + 4) < len(B) and element_type(B[i+2])=='boolean' and element_type(B[i+4])=='boolean':
            if (not search(eval(B[i+2]), DATA_LIST)) and (not search(eval(B[i+4]), DATA_LIST)):
                DATA_LIST.append(eval(B[i+2]))
                DATA_LIST.append(eval(B[i+4]))
                if B[i+3]=='and' and not search(eval(B[i+2]) and eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append(eval(B[i+2]) and eval(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(eval(B[i+2]) and eval(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='and' and search(eval(B[i+2]) and eval(B[i+4]),DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(eval(B[i+2]) and eval(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='or' and not search(eval(B[i+2]) or eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append(eval(B[i+2]) or eval(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(eval(B[i+2]) or eval(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='or' and search(eval(B[i+2]) or eval(B[i+4]),DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(eval(B[i+2]) or eval(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
            elif search(eval(B[i+2]),DATA_LIST) and (not search(eval(B[i+4]),DATA_LIST)):
                DATA_LIST.append(eval(B[i+2]))
                if B[i+3]=='and' and not search(eval(B[i+2]) and eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append(eval(B[i+2]) and eval(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(eval(B[i+2]) and eval(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='and' and search(eval(B[i+2]) and eval(B[i+4]),DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(eval(B[i+2]) and eval(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='or' and not search(eval(B[i+2]) or eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append(eval(B[i+2]) or eval(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(eval(B[i+2]) or eval(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='or' and search(eval(B[i+2]) or eval(B[i+4]),DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(eval(B[i+2]) or eval(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
            elif (not search(eval(B[i+2]), DATA_LIST)) and search(eval(B[i+4]), DATA_LIST):
                DATA_LIST.append(eval(B[i+2]))
                if B[i+3]=='and' and not search(eval(B[i+2]) and eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append(eval(B[i+2]) and eval(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(eval(B[i+2]) and eval(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='and' and search(eval(B[i+2]) and eval(B[i+4]),DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(eval(B[i+2]) and eval(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='or' and not search(eval(B[i+2]) or eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append(eval(B[i+2]) or eval(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(eval(B[i+2]) or eval(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='or' and search(eval(B[i+2]) or eval(B[i+4]),DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(eval(B[i+2]) or eval(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
            elif search(eval(B[i+2]), DATA_LIST) and search(eval(B[i+4]), DATA_LIST):
                if B[i+3]=='and' and not search(eval(B[i+2]) and eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append(eval(B[i+2]) and eval(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(eval(B[i+2]) and eval(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='and' and search(eval(B[i+2]) and eval(B[i+4]),DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(eval(B[i+2]) and eval(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='or' and not search(eval(B[i+2]) or eval(B[i+4]),DATA_LIST):
                    DATA_LIST.append(eval(B[i+2]) or eval(B[i+4]))
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(eval(B[i+2]) or eval(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
                elif B[i+3]=='or' and search(eval(B[i+2]) or eval(B[i+4]),DATA_LIST):
                    DATA_LIST[search_index(B[i], DATA_LIST)] = (B[i], search_index(eval(B[i+2]) or eval(B[i+4]), DATA_LIST))
                    GARBAGE_LIST.append(eval(B[i+2]))
                    GARBAGE_LIST.append(eval(B[i+4]))
                    return DATA_LIST
        elif ((i + 2) < len(B) and (i + 4) > len(B)) and element_type(B[i+2])=='variable':
            DATA_LIST.append((B[i],DATA_LIST[search_index(B[i+2],DATA_LIST)][1]))
            return DATA_LIST

        elif (i + 4) < len(B) and element_type(B[i+2])=='variable' and element_type(B[i+4])=='integer_constant':
            if not search(int(B[i+4]),DATA_LIST):
                DATA_LIST.append(int(B[i+4]))
                if B[i+3]=='+':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]+int(B[i+4]), DATA_LIST):
                        DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]+int(B[i+4]),DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]+int(B[i+4]), DATA_LIST):
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]+int(B[i+4]))
                        DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]+int(B[i+4]), DATA_LIST)))
                        return DATA_LIST
                elif B[i+3]=='-':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]-int(B[i+4]), DATA_LIST):
                        DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]-int(B[i+4]),DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]-int(B[i+4]), DATA_LIST):
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]-int(B[i+4]))
                        DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]-int(B[i+4]), DATA_LIST)))
                        return DATA_LIST
                elif B[i+3]=='*':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]*int(B[i+4]), DATA_LIST):
                        DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]*int(B[i+4]),DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]*int(B[i+4]), DATA_LIST):
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]*int(B[i+4]))
                        DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]*int(B[i+4]), DATA_LIST)))
                        return DATA_LIST
                if B[i+3]=='/':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]/int(B[i+4]), DATA_LIST):
                        DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]/int(B[i+4]),DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]/int(B[i+4]), DATA_LIST):
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]/int(B[i+4]))
                        DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]/int(B[i+4]), DATA_LIST)))
                        return DATA_LIST
            elif search(int(B[i+4]),DATA_LIST):
                if B[i+3]=='+':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]+int(B[i+4]), DATA_LIST):
                        DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]+int(B[i+4]),DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]+int(B[i+4]), DATA_LIST):
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]+int(B[i+4]))
                        DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]+int(B[i+4]), DATA_LIST)))
                        return DATA_LIST
                elif B[i+3]=='-':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]-int(B[i+4]), DATA_LIST):
                        DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]-int(B[i+4]),DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]-int(B[i+4]), DATA_LIST):
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]-int(B[i+4]))
                        DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]-int(B[i+4]), DATA_LIST)))
                        return DATA_LIST
                elif B[i+3]=='*':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]*int(B[i+4]), DATA_LIST):
                        DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]*int(B[i+4]),DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]*int(B[i+4]), DATA_LIST):
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]*int(B[i+4]))
                        DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]*int(B[i+4]), DATA_LIST)))
                        return DATA_LIST
                if B[i+3]=='/':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]/int(B[i+4]), DATA_LIST):
                        DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]/int(B[i+4]),DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]/int(B[i+4]), DATA_LIST):
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]/int(B[i+4]))
                        DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]/int(B[i+4]), DATA_LIST)))
                        return DATA_LIST
        elif (i + 4) < len(B) and element_type(B[i+2])=='variable' and element_type(B[i+4])=='boolean':
            if search(eval(B[i+4]),DATA_LIST):
                if B[i+3]=='and':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]] and eval(B[i + 4]),DATA_LIST):
                        DATA_LIST.append((B[i], search_index(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] and eval(B[i + 4]),DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]] and eval(B[i + 4]),DATA_LIST):
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]] and eval(B[i + 4]))
                        DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]] and eval(B[i+4]),DATA_LIST)))
                        GARBAGE_LIST.append(eval(B[i+4]))
                        return DATA_LIST
                elif B[i+3]=='or':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]] or eval(B[i + 4]),DATA_LIST):
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] or eval(B[i + 4]))
                        DATA_LIST.append((B[i], search_index(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] or eval(B[i + 4]),DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]] or eval(B[i + 4]),DATA_LIST):
                        DATA_LIST.append(eval(B[i+4]))
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]] or eval(B[i + 4]))
                        DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]] or eval(B[i+4]),DATA_LIST)))
                        GARBAGE_LIST.append(eval(B[i+4]))
                        return DATA_LIST

            elif search(eval(B[i+4]),DATA_LIST):
                DATA_LIST.append(eval(B[i+4]))
                if B[i+3]=='and':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]] and eval(B[i + 4]),DATA_LIST):
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] and eval(B[i + 4]))
                        DATA_LIST.append((B[i], search_index(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] and eval(B[i + 4]),DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]] and eval(B[i + 4]),DATA_LIST):
                        DATA_LIST.append(eval(B[i+4]))
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]] and eval(B[i + 4]))
                        DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]] and eval(B[i+4]),DATA_LIST)))
                        GARBAGE_LIST.append(eval(B[i+4]))
                        return DATA_LIST
                elif B[i+3]=='or':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]] or eval(B[i + 4]),DATA_LIST):
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] or eval(B[i + 4]))
                        DATA_LIST.append((B[i], search_index(DATA_LIST[DATA_LIST[search_index(B[i + 2], DATA_LIST)][1]] or eval(B[i + 4]),DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]] or eval(B[i + 4]),DATA_LIST):
                        DATA_LIST.append(eval(B[i+4]))
                        DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]] or eval(B[i + 4]))
                        DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]] or eval(B[i+4]),DATA_LIST)))
                        GARBAGE_LIST.append(eval(B[i+4]))
                        return DATA_LIST

        elif (i + 4) < len(B) and element_type(B[i+2])=='integer_constant' and element_type(B[i+4])=='variable':
            if B[i+3]=='+':
                if search(DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]]+int(B[i+2]), DATA_LIST):
                    DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]]+int(B[i+2]),DATA_LIST)))
                    return DATA_LIST
                elif not search(DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]]+int(B[i+2]), DATA_LIST):
                    DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]]+int(B[i+2]))
                    DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]]+int(B[i+2]), DATA_LIST)))
                    return DATA_LIST
            elif B[i+3]=='-':
                if search(int(B[i+2])-DATA_LIST[DATA_LIST[search_index(int(B[i+4]),DATA_LIST)][1]], DATA_LIST):
                    DATA_LIST.append((B[i],search_index(int(B[i+2])-DATA_LIST[DATA_LIST[search_index(int(B[i+4]),DATA_LIST)][1]],DATA_LIST)))
                    return DATA_LIST
                elif not search(int(B[i+2])-DATA_LIST[DATA_LIST[search_index(int(B[i+4]),DATA_LIST)][1]], DATA_LIST):
                    DATA_LIST.append(int(B[i+2])-DATA_LIST[DATA_LIST[search_index(int(B[i+4]),DATA_LIST)][1]])
                    DATA_LIST.append((B[i],search_index(int(B[i+2])-DATA_LIST[DATA_LIST[search_index(int(B[i+4]),DATA_LIST)][1]], DATA_LIST)))
                    return DATA_LIST
            elif B[i+3]=='*':
                if search(DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]]*int(B[i+2]), DATA_LIST):
                    DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]]*int(B[i+2]),DATA_LIST)))
                    return DATA_LIST
                elif not search(DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]]*int(B[i+2]), DATA_LIST):
                    DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]]*int(B[i+2]))
                    DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]]*int(B[i+2]), DATA_LIST)))
                    return DATA_LIST
            if B[i+3]=='/':
                if search(int(B[i+2])/DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]], DATA_LIST):
                    DATA_LIST.append((B[i],search_index(int(B[i+2])/DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]],DATA_LIST)))
                    return DATA_LIST
                elif not search(int(B[i+2])/DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]], DATA_LIST):
                    DATA_LIST.append(int(B[i+2])/DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]])
                    DATA_LIST.append((B[i],search_index(int(B[i+2])/DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]], DATA_LIST)))
                    return DATA_LIST

        elif (i + 4) < len(B) and element_type(B[i + 2]) == 'boolean' and element_type(B[i + 4]) == 'variable':
            if search(eval(B[i + 4]), DATA_LIST):
                if B[i + 3] == 'and':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] and eval(B[i + 2]),DATA_LIST):
                        DATA_LIST.append(
                            DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] and eval(B[i + 2]))
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] and eval(B[i + 2]),
                            DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] and eval(B[i + 2]),DATA_LIST):
                        DATA_LIST.append(eval(B[i + 2]))
                        DATA_LIST.append(
                            DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] and eval(B[i + 2]))
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] and eval(B[i + 2]),
                            DATA_LIST)))
                        GARBAGE_LIST.append(eval(B[i + 2]))
                        return DATA_LIST
                elif B[i + 3] == 'or':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] or eval(B[i + 2]),DATA_LIST):
                        DATA_LIST.append(
                            DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] or eval(B[i + 2]))
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] or eval(B[i + 2]),
                            DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] or eval(B[i + 2]),DATA_LIST):
                        DATA_LIST.append(eval(B[i + 2]))
                        DATA_LIST.append(
                            DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] or eval(B[i + 2]))
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] or eval(B[i + 2]),
                            DATA_LIST)))
                        GARBAGE_LIST.append(eval(B[i + 2]))
                        return DATA_LIST

            elif search(eval(B[i + 2]), DATA_LIST):
                DATA_LIST.append(eval(B[i + 2]))
                if B[i + 3] == 'and':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] and eval(B[i + 2]),DATA_LIST):
                        DATA_LIST.append(
                            DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] and eval(B[i + 2]))
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] and eval(B[i + 2]),
                            DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] and eval(B[i + 2]),DATA_LIST):
                        DATA_LIST.append(eval(B[i + 2]))
                        DATA_LIST.append(
                            DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] and eval(B[i + 2]))
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] and eval(B[i + 2]),
                            DATA_LIST)))
                        GARBAGE_LIST.append(eval(B[i + 2]))
                        return DATA_LIST
                elif B[i + 3] == 'or':
                    if search(DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] or eval(B[i + 2]),DATA_LIST):
                        DATA_LIST.append(
                            DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] or eval(B[i + 2]))
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] or eval(B[i + 2]),
                            DATA_LIST)))
                        return DATA_LIST
                    elif not search(DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] or eval(B[i + 2]),DATA_LIST):
                        DATA_LIST.append(eval(B[i + 2]))
                        DATA_LIST.append(
                            DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] or eval(B[i + 2]))
                        DATA_LIST.append((B[i], search_index(
                            DATA_LIST[DATA_LIST[search_index(B[i + 4], DATA_LIST)][1]] or eval(B[i + 2]),
                            DATA_LIST)))
                        GARBAGE_LIST.append(eval(B[i + 2]))
                        return DATA_LIST

        elif (i+4)<len(B) and element_type(B[i+2])=='variable' and element_type(B[i+4])=='variable':
            if element_type(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]])=='integer_constant' and element_type(DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]])=='integer_constant':
                if B[i+3]=='+':
                    DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]+DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]])
                    DATA_LIST.append((B[i],search_index(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]+DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]],DATA_LIST)))
                    return DATA_LIST
                elif B[i+3]=='-':
                    DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]-DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]])
                    DATA_LIST.append((B[i],DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]-DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]]))
                    return DATA_LIST
                elif B[i+3]=='*':
                    DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]*DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]])
                    DATA_LIST.append((B[i],DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]*DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]]))
                    return DATA_LIST
                elif B[i+3]=='/':
                    DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]/DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]])
                    DATA_LIST.append((B[i],DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]/DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]]))
                    return DATA_LIST
            elif element_type(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]])=='boolean' and element_type(DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]])=='boolean':
                if B[i+3]=='and':
                    DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]] and DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]])
                    DATA_LIST.append((B[i],DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]] and DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]]))
                    return DATA_LIST
                elif B[i+3]=='or':
                    DATA_LIST.append(DATA_LIST[DATA_LIST[search_index(B[i+2], DATA_LIST)][1]] or DATA_LIST[DATA_LIST[search_index(B[i+4], DATA_LIST)][1]])
                    DATA_LIST.append((B[i],DATA_LIST[DATA_LIST[search_index(B[i+2], DATA_LIST)][1]] or DATA_LIST[DATA_LIST[search_index(B[i+4], DATA_LIST)][1]]))
                    return DATA_LIST

        # Code for >,<,>=,<=,!=.
        elif (i+4)<len(B) and element_type(B[i+2])=='integer_constant' and element_type(B[i+4])=='integer_constant':
            if B[i+3]=='<':
                if not search(int(B[i+2]),DATA_LIST):
                    if not search(int(B[i+4]),DATA_LIST):
                        DATA_LIST.append(int(B[i+2]))
                        DATA_LIST.append(int(B[i+4]))
                    elif search(int(B[i+4]),DATA_LIST):
                        DATA_LIST.append(int(B[i+2]))
                elif search(int(B[i+2]),DATA_LIST):
                    if not search(int(B[i+4]),DATA_LIST):
                        DATA_LIST.append(int(B[i+4]))
                    elif search(int(B[i+4]),DATA_LIST):
                        DATA_LIST=DATA_LIST
                DATA_LIST.append(int(B[i+2]))
                DATA_LIST.append(int(B[i+4]))
                DATA_LIST.append(int(B[i+2])<int(B[i+4]))
                DATA_LIST.append((B[i],search_index(int(B[i+2])<int(B[i+4]),DATA_LIST)))
                return DATA_LIST
            elif B[i+3]=='<=':
                if not search(int(B[i+2]),DATA_LIST):
                    if not search(int(B[i+4]),DATA_LIST):
                        DATA_LIST.append(int(B[i+2]))
                        DATA_LIST.append(int(B[i+4]))
                    elif search(int(B[i+4]),DATA_LIST):
                        DATA_LIST.append(int(B[i+2]))
                elif search(int(B[i+2]),DATA_LIST):
                    if not search(int(B[i+4]),DATA_LIST):
                        DATA_LIST.append(int(B[i+4]))
                    elif search(int(B[i+4]),DATA_LIST):
                        DATA_LIST=DATA_LIST
                DATA_LIST.append(int(B[i+2])<=int(B[i+4]))
                DATA_LIST.append((B[i],search_index(int(B[i+2])<=int(B[i+4]),DATA_LIST)))
                return DATA_LIST
            elif B[i+3]=='>':
                if not search(int(B[i+2]),DATA_LIST):
                    if not search(int(B[i+4]),DATA_LIST):
                        DATA_LIST.append(int(B[i+2]))
                        DATA_LIST.append(int(B[i+4]))
                    elif search(int(B[i+4]),DATA_LIST):
                        DATA_LIST.append(int(B[i+2]))
                elif search(int(B[i+2]),DATA_LIST):
                    if not search(int(B[i+4]),DATA_LIST):
                        DATA_LIST.append(int(B[i+4]))
                    elif search(int(B[i+4]),DATA_LIST):
                        DATA_LIST=DATA_LIST
                DATA_LIST.append(int(B[i+2])>int(B[i+4]))
                DATA_LIST.append((B[i],search_index(int(B[i+2])>int(B[i+4]),DATA_LIST)))
                return DATA_LIST
            elif B[i+3]=='>=':
                if not search(int(B[i+2]),DATA_LIST):
                    if not search(int(B[i+4]),DATA_LIST):
                        DATA_LIST.append(int(B[i+2]))
                        DATA_LIST.append(int(B[i+4]))
                    elif search(int(B[i+4]),DATA_LIST):
                        DATA_LIST.append(int(B[i+2]))
                elif search(int(B[i+2]),DATA_LIST):
                    if not search(int(B[i+2]),DATA_LIST):
                        DATA_LIST.append(int(B[i+4]))
                    elif search(int(B[i+4]),DATA_LIST):
                        DATA_LIST=DATA_LIST
                DATA_LIST.append(int(B[i+2])>=int(B[i+4]))
                DATA_LIST.append((B[i],search_index(int(B[i+2])>=int(B[i+4]),DATA_LIST)))
                return DATA_LIST
            elif B[i + 3] == '==':
                if not search(int(B[i+2]), DATA_LIST):
                    if not search(int(B[i+4]), DATA_LIST):
                        DATA_LIST.append(int(B[i+2]))
                        DATA_LIST.append(int(B[i+4]))
                    elif search(int(B[i+4]), DATA_LIST):
                        DATA_LIST.append(int(B[i+2]))
                elif search(int(B[i+2]), DATA_LIST):
                    if not search(int(B[i+4]), DATA_LIST):
                        DATA_LIST.append(int(B[i+4]))
                    elif search(int(B[i+4]), DATA_LIST):
                        DATA_LIST = DATA_LIST
                DATA_LIST.append(int(B[i+2]))
                DATA_LIST.append(int(B[i+4]))
                DATA_LIST.append(int(B[i+2]) == int(B[i+4]))
                DATA_LIST.append((B[i], search_index(int(B[i+2]) == int(B[i+4]), DATA_LIST)))
                return DATA_LIST
            elif B[i+3]=='!=':
                if not search(int(B[i+2]),DATA_LIST):
                    if not search(int(B[i+4]),DATA_LIST):
                        DATA_LIST.append(int(B[i+2]))
                        DATA_LIST.append(int(B[i+4]))
                    elif search(int(B[i+4]),DATA_LIST):
                        DATA_LIST.append(int(B[i+2]))
                elif search(int(B[i+2]),DATA_LIST):
                    if not search(int(B[i+4]),DATA_LIST):
                        DATA_LIST.append(int(B[i+4]))
                    elif search(int(B[i+4]),DATA_LIST):
                        DATA_LIST=DATA_LIST
                DATA_LIST.append(int(B[i+2]))
                DATA_LIST.append(int(B[i+4]))
                DATA_LIST.append(int(B[i+2])!=int(B[i+4]))
                DATA_LIST.append((B[i],search_index(int(B[i+2])!=int(B[i+4]),DATA_LIST)))
                return DATA_LIST
        elif (i + 4) < len(B) and element_type(B[i+2])=='variable' and element_type(B[i+4])=='integer_constant':
            c=DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]
            if B[i+3]=='<':
                if not search(int(B[i+4]),DATA_LIST):
                    DATA_LIST.append(int(B[i+4]))
                elif search(int(B[i+4]),DATA_LIST):
                    DATA_LIST=DATA_LIST
                DATA_LIST.append(c<int(B[i+4]))
                DATA_LIST.append((B[i],search_index(c<int(B[i+4]),DATA_LIST)))
                return DATA_LIST
            elif B[i+3]=='<=':
                if not search(int(B[i+4]),DATA_LIST):
                    DATA_LIST.append(int(B[i+4]))
                elif search(int(B[i+4]),DATA_LIST):
                    DATA_LIST=DATA_LIST
                DATA_LIST.append(c<=int(B[i+4]))
                DATA_LIST.append((B[i],search_index(c<=int(B[i+4]),DATA_LIST)))
                return DATA_LIST
            elif B[i+3]=='>':
                if not search(int(B[i+4]),DATA_LIST):
                    DATA_LIST.append(int(B[i+4]))
                elif search(int(B[i+4]),DATA_LIST):
                    DATA_LIST=DATA_LIST
                DATA_LIST.append(c>int(B[i+4]))
                DATA_LIST.append((B[i],search_index(c>int(B[i+4]),DATA_LIST)))
                return DATA_LIST
            elif B[i + 3] == '>=':
                if not search(int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+4]))
                elif search(int(B[i+4]), DATA_LIST):
                    DATA_LIST = DATA_LIST
                DATA_LIST.append(c >= int(B[i+4]))
                DATA_LIST.append((B[i], search_index(c >= int(B[i+4]), DATA_LIST)))
                return DATA_LIST
            elif B[i + 3] == '==':
                if not search(int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+4]))
                elif search(int(B[i+4]), DATA_LIST):
                    DATA_LIST = DATA_LIST
                DATA_LIST.append(c == int(B[i+4]))
                DATA_LIST.append((B[i], search_index(c == int(B[i+4]), DATA_LIST)))
                return DATA_LIST
            elif B[i + 3] == '!=':
                if not search(int(B[i+4]), DATA_LIST):
                    DATA_LIST.append(int(B[i+4]))
                elif search(int(B[i+4]), DATA_LIST):
                    DATA_LIST = DATA_LIST
                DATA_LIST.append(c != int(B[i+4]))
                DATA_LIST.append((B[i], search_index(c != int(B[i+4]), DATA_LIST)))
                return DATA_LIST

        elif (i + 4) < len(B) and element_type(B[i+2])=='integer_constant' and element_type(B[i+4])=='variable':
            c=DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]]
            if B[i+3]=='<':
                if not search(int(B[i+2]),DATA_LIST):
                    DATA_LIST.append(int(B[i+2]))
                elif search(int(B[i+2]),DATA_LIST):
                    DATA_LIST=DATA_LIST
                DATA_LIST.append(int(B[i+2])<c)
                DATA_LIST.append((B[i],search_index(c>int(B[i+2]),DATA_LIST)))
                return DATA_LIST
            elif B[i+3]=='<=':
                if not search(int(B[i+2]),DATA_LIST):
                    DATA_LIST.append(int(B[i+2]))
                elif search(int(B[i+2]),DATA_LIST):
                    DATA_LIST=DATA_LIST
                DATA_LIST.append(c>=int(B[i+2]))
                DATA_LIST.append((B[i],search_index(c>=int(B[i+2]),DATA_LIST)))
                return DATA_LIST
            elif B[i + 3] == '>':
                if not search(int(B[i+2]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]))
                elif search(int(B[i+2]), DATA_LIST):
                    DATA_LIST = DATA_LIST
                DATA_LIST.append(c < int(B[i+2]))
                DATA_LIST.append((B[i], search_index(c < int(B[i+2]), DATA_LIST)))
                return DATA_LIST
            elif B[i + 3] == '>=':
                if not search(int(B[i+2]), DATA_LIST):
                    DATA_LIST.append(int(B[i+2]))
                elif search(int(B[i+2]), DATA_LIST):
                    DATA_LIST = DATA_LIST
                DATA_LIST.append(c <= int(B[i+2]))
                DATA_LIST.append((B[i], search_index(c <= int(B[i+2]), DATA_LIST)))
                return DATA_LIST
            elif B[i+3]=='==':
                if not search(int(B[i+2]),DATA_LIST):
                    DATA_LIST.append(int(B[i+2]))
                elif search(int(B[i+2]),DATA_LIST):
                    DATA_LIST=DATA_LIST
                DATA_LIST.append(c==int(B[i+2]))
                DATA_LIST.append((B[i],search_index(c==int(B[i+2]),DATA_LIST)))
                return DATA_LIST
            elif B[i+3]=='!=':
                if not search(int(B[i+2]),DATA_LIST):
                    DATA_LIST.append(int(B[i+2]))
                elif search(int(B[i+2]),DATA_LIST):
                    DATA_LIST=DATA_LIST
                DATA_LIST.append(c!=int(B[i+2]))
                DATA_LIST.append((B[i],search_index(c!=int(B[i+2]),DATA_LIST)))
                return DATA_LIST
        elif (i + 4) < len(B) and element_type(B[i+2])=='variable' and element_type(B[i+4])=='variable':
            c=DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]
            d=DATA_LIST[DATA_LIST[search_index(B[i+4],DATA_LIST)][1]]
            if B[i+3]=='<':

                DATA_LIST.append(c<d)
                DATA_LIST.append((B[i],search_index(c<d,DATA_LIST)))
                return DATA_LIST
            elif B[i + 3] == '<=':

                DATA_LIST.append(c <= d)
                DATA_LIST.append((B[i], search_index(c <= d, DATA_LIST)))
                return DATA_LIST
            elif B[i + 3] == '>':

                DATA_LIST.append(c > d)
                DATA_LIST.append((B[i], search_index(c > d, DATA_LIST)))
                return DATA_LIST
            elif B[i + 3] == '>=':

                DATA_LIST.append(c >= d)
                DATA_LIST.append((B[i], search_index(c >= d, DATA_LIST)))
                return DATA_LIST
            elif B[i + 3] == '==':

                DATA_LIST.append(c == d)
                DATA_LIST.append((B[i], search_index(c == d, DATA_LIST)))
                return DATA_LIST
            elif B[i + 3] == '!=':

                DATA_LIST.append(c != d)
                DATA_LIST.append((B[i], search_index(c != d, DATA_LIST)))
                return DATA_LIST

        # Unary operator part.
        if (i+2)<len(B) and element_type(B[i+2])=='integer_constant':
            if B[i+1]=='-':
                if search(-int(B[i+2]),DATA_LIST):
                    DATA_LIST=DATA_LIST
                elif not search(-int(B[i+2]),DATA_LIST):
                    DATA_LIST.append(-int(B[i+2]))
                DATA_LIST.append((B[i],search_index(-int(B[i+2]),DATA_LIST)))
                return DATA_LIST
        elif (i+2)<len(B) and element_type(B[i+2])=='variable' and element_type(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]])=='integer_constant':
            c=DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]
            if B[i + 1] == '-':
                if search(-DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]], DATA_LIST):
                    DATA_LIST = DATA_LIST
                elif not search(-DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]], DATA_LIST):
                    DATA_LIST.append(-DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]])
                DATA_LIST.append((B[i], search_index(-DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]], DATA_LIST)))
                return DATA_LIST
        elif (i+2)<len(B) and element_type(B[i+2])=='boolean':
            if B[i+1]=='not':
                if search(not eval(B[i+2]),DATA_LIST):
                    DATA_LIST=DATA_LIST
                elif not search(not eval(B[i+2]),DATA_LIST):
                    DATA_LIST.append( not eval(B[i+2]))
                DATA_LIST.append((B[i],search_index(not eval(B[i+2]),DATA_LIST)))
                return DATA_LIST
        elif (i+2)<len(B) and element_type(B[i+2])=='variable' and element_type(DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]])=='boolean':
            c=DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]]
            if B[i + 1] == 'not':
                if search(not DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]], DATA_LIST):
                    DATA_LIST = DATA_LIST
                elif not search( not DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]], DATA_LIST):
                    DATA_LIST.append(not DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]])
                DATA_LIST.append((B[i], search_index(not DATA_LIST[DATA_LIST[search_index(B[i+2],DATA_LIST)][1]], DATA_LIST)))
                return DATA_LIST


def subtraction_of_sets(A,B):
    l=len(A)
    i = 0
    L=[]
    while i<len(A):
        j = 0
        k=len(B)
        while j < len(B):
            if A[i] == B[j]:
                A.remove(A[i])
                j += 1
            else:
                j += 1
        i += 1
    return A



lines = []      # initialise to empty list
with open('C:/Users/Abdhesh Dash/OneDrive/Desktop/IITD/COL100/After Minor/Ass.5/input_file.txt') as f:
    lines = lines + f.readlines()       #It will read all lines into a list of strings
    print(lines)

OUTPUT=[]
for statement in lines:     # each statement is on a separate line
    token_list = statement.split()      # It splits a statement into a list of tokens.
    print(token_list)
    OUTPUT = OUTPUT + interpret(token_list)
    print(OUTPUT)

def output1():
    FINAL_OUTPUT_LIST= subtraction_of_sets(OUTPUT, GARBAGE_LIST)
    return print('Output is: ', FINAL_OUTPUT_LIST)

def output2():
    return print('Garbage is: ', GARBAGE_LIST)









