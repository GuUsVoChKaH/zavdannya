def r_duplicate(*a):
    list(a)
    element = []
    for item in a:
        if item in element:
            pass
        elif type(item) == str:
            for letters in item:
                if letters in element:
                    pass
                else:
                    element.append(letters)
        else:
            element.append(item)
    return element


def sortingg(sorting_element):
    number = []
    strings = []
    for item in sorting_element:
        if type(item) == int or type(item) == float:
            number.append(item)
        elif type(item) == str:
            strings.append(item)
    number.sort()
    strings.sort()
    return number + strings

    
uniq_list_element = (r_duplicate(2,3,4,5,6,5,1,3,7,4,2,3,5,6,7,5,7,8,9,1,0,7,6,4,4,3 'допобачення', 'перепідвиверт'))
uniq_list_element_sort = (sortingg(uniq_list_element))
print (f'uniq list {uniq_list_element} \n\n sort_uniq_list {uniq_list_element_sort} ' )
