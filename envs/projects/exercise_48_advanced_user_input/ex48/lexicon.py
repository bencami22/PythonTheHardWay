lexicon_list = {"direction":["north","south","east","west","down","up","left","right","back"],
                "verb":["go","stop","kill","eat"],
                "stop":["the","in","of","from","at","it"],
                "noun":["door","bear","princess","cabinet"]}
class lexicon(object):
    def scan(words):
        return_list = []
        words_array = words.split()
        for w in words_array:
            num = convert_number(w)
            if num != None:
                return_list.append(('number', num))
            else:
                found = False
                for k, v in lexicon_list.items():
                    for m in v:
                        if m == w:
                            found = True
                            return_list.append((k, w))
                if found == False:
                    return_list.append(('error', w))

        return return_list

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

#user_input = input(">")
#print(lexicon.scan(user_input))
