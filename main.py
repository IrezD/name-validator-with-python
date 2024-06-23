import re 
def title_except(s, exceptions):
    word_list = re.split(' ', s)       # re.split behaves as expected
    final = [word_list[0].capitalize()]
    for word in word_list[1:]:
        final.append(word if word in exceptions else word.capitalize())
    return " ".join(final)

articles = ['a', 'an', 'of', 'the', 'is', 'and', 'for']

title = title_except(input("Enter Document Title:"), articles)

title_length = (len(title))



if title_length > 20:
    print (f"Character length exceeded! It is {title_length}.")
else:
    print (f"Perfect Character length. It is {title_length}.")

special_characters = ["!", ",", "#", "$", "%", "&", "'", "(", ")", "*", "+", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "\\", "^", "_", "`", "{", "|", "}", "~"]

filename_hyphens = ""

for i in title:

    for check in special_characters:
        if i == check:
            i = ""
    
    if i == ' ':
        i = "-"
        
    filename_hyphens += i

print ("Document Filename: \n", filename_hyphens.title())


print ("Document Title:\n", title)