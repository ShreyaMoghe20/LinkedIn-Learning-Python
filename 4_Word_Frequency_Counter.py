text = '''Life is about choices. Every day we're faced with hundreds of choices, and this speech by Tony Robbins will help you see that 
it’s the choices, not the conditions, which shape our lives.Take a moment during this speech to pause and reflect on some choices 
you have made in the past, and really think about the direction your life took because of them, both good and bad. 
Tony Robbins explains in his inimitable way that we have the choice to focus on what we want, and that when we focus, we can achieve 
whatever we want.'''

print(len(text))
len_text = len(text.split())

word_count = {}

for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count) 
