def duplicate_count(text:str)->int:
    null = ""
    for i in text:
        if i.isalpha() or i.isdigit():
            null += i.lower()
        else:
            print(f" You must input only lphabets (both uppercase and lowercase) and numeric digits")
            return f" You must input only lphabets (both uppercase and lowercase) and numeric digits"
    print(null)
    text = null
    list_one = dict()
    # for i in range(0,len(text)):
    #     if text[i] in text[i+1::]:
    #         list_one.append(text[i])
    # print(list_one)




#     sets = set(text)
#     sets1 = list(sets)
#
#     print(sets1)
#     list_one = [i for i in range(0, len(sets1)) if text.count(sets1[i]) > 1]
#     print(list_one)
#
#

    sets = set(text)
    sets1 = list(sets)
    for i in range(0, len(sets1)):
        if text.count(sets1[i]) >= 2:
            print(text.count(sets1[i]))
            list_one[sets1[i]] = text.count(sets1[i])
    print(list_one)

    keys = list(list_one.keys())

    if keys == []:
        return 0
    else:
        return len(keys)


print(duplicate_count("j2XmZ6iHzEeVBrSmecEjLE4S5poKG3zVFuxMSU8IKghY1fmhrX0pux595R6HZLRinf7vl9Ojf62Oagynok43d"))