from Funcs import FizzBuzzer, HeckerTranslate, isPalindrome
sample_messages = [
"7his所is家4没s4mpl3动m3ss463",
"don7家73ll经4nyon3法7his现m3ss463",
"w3现4r3当b3in6进so好s3cr3t",
"733小h33成h33去nobody看is天on分7o理us",
"w3么will面n3v3r分637理c4u6ht",
"w3事4r3经such没sn34ky天h4ckers"]

print(sample_messages)

heck = HeckerTranslate()

processed = []
print()
for msg in sample_messages:
    msg = heck.replace_3e(msg)
    msg = heck.replace_4a(msg)
    msg = heck.replace_7t(msg)
    msg = heck.replace_6g(msg)
    msg = heck.sub_chinese(msg)
    processed.append(msg)

print(processed)