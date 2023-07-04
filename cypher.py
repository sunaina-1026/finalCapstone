# This is a cypher program to convert a message into a coded language!
# This will allow user to input their message

in_text = input('Please provide your input text: ')

# Following function will convert the input message by adding 15 places to existing place in alphabet cycle.
# English alphabet consists of 26 letters. Hence, if we go back by 11 places we will reach to the desired
# place in the alphabet cycle


def cypher_conv(in_text):
    output_text = ''
    for i in in_text:
        if ord(i) in range(97, 108):
            i = ord(i) + 15
        elif ord(i) in range(108, 123):
            i = ord(i) - 11

            # Here it will take a reverse gear to complete the alphabet cycle.
            # Perhaps, an unique reverse gear which completes a cycle :)

        elif ord(i) in range(65, 76):
            i = ord(i) + 15
        elif ord(i) in range(76, 91):
            i = ord(i) - 11
        else:       # This section will not convert anything except english alphabets
            i = ord(i)
        output_text += chr(i)
    print(output_text)


cypher_conv(in_text)
