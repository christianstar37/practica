def spin_words(sentence):
    # Your code goes here
    words = sentence.split()
    reverse = ''
    for word in words:
        if len(word) >= 5:
            reverse += word[::-1]
        reverse += word
    return reverse 
print(spin_words('holaaaa'))