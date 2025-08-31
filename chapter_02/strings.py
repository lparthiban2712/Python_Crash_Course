print('This is a string')
print("This is also a string")
name="parthiban"
print(name.title())
print(name.upper())
print(name.lower())
print(f"Hi {name.title()}, How are you!")
f_name="parthiban"
l_name="lakshmanan"
full_name=f"{f_name.title()} {l_name.title()}"
print(full_name)
print(f"HI {full_name}, How are you!")
print("I love Python\tJava")
print("I love Python\nJava")
lang=" python "
print(lang,len(lang))
print(lang.rstrip(),len(lang.rstrip()))
print(lang.lstrip(),len(lang.lstrip()))
print(lang.strip(),len(lang.strip()))
url="https://nostarch.com"
simpled_url=url.removeprefix("https://")
print(simpled_url)
print("Hi, This is Parthi's mobile")
print('Hi, This is Parthi"s mobile')
# print('Hi, This is Parthi's mobile') Syntax Error: unterminated string literal
# print("Hi, This is Parthi"s mobile") Syntax Error: unterminated string literal
