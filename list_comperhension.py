words = "Why sometimes I have believed as " \
        "many as six impossible things before breakfast".split()

word_count = [len(word) for word in words]
print(word_count)

# The above code is the same as:
# lengths = []
# for word in words:
#    lengths.append(len(word))