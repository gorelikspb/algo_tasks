# Python code to find frequency of each word 
def metrics(str): 
  
    # break the string into list of words  
    str = str.split()          
    freqs = dict()
    lens = dict()
    for word in str:
        if word in freqs:
            freqs[word]+=1
        else:
            freqs[word]=1
            lens[word]=len(word)


    return freqs, lens

text = input()

freqs, lens = metrics(text)

max_key = max(lens, key=lens.get)
max_len = (lens[max_key])

max_freq_word = max(freqs, key=freqs.get)
max_freq = (freqs[max_freq_word])

coef = 10/max_freq

freqs_sorted = {k: v for k, v in sorted(freqs.items(), key=lambda item: item[1])}

for word in freqs_sorted:
    freqs_sorted[word]*=coef
    freqs_sorted[word]=round(freqs_sorted[word])


#output
for word in freqs_sorted:
    print ((max_len-lens[word])*'_' + word, '.'*freqs_sorted[word])

