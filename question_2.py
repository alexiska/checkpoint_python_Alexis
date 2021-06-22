# -- b --

def to_camel_case(text):
    
    new_text = text.lower()
    lst_text = new_text.split()
    
    for i, word in enumerate(lst_text):
        lst_text[i] = word.capitalize()
    return "".join(lst_text)

print(to_camel_case("tHis Is A tesT string"))
print(to_camel_case("hello world"))
print(to_camel_case("My stRiNg"))