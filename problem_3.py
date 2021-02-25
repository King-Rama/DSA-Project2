import sys
import heapq

# Let's now build a huffman tree
def makeTree(freqs):
    heap = []
    if msg == "" and freqs == []:
        print("***************************************************************")
        print("Empty String")
        print("***************************************************************")
    # Adding the frequencies in a heap
    for f in freqs:
        heapq.heappush(heap, [f])

    while (len(heap) > 1):
        left = heapq.heappop(heap)  ##Pulling out the left child from the heap
        right = heapq.heappop(heap)  ##Pulling out the right child from the heap
        left_freq, left_char = left[0] ##Inside a tuple we start by labling our character then frequency in the left
        right_freq, right_char = right[0]  ## Taken the frequency that is in the tuple in the right
        frequency = left_freq + right_freq ##Adding the two lower frequencies to build an internal node
        ##We have sorted and joined the labels/characters
        char = ''.join((sorted)(left_char + right_char))
        ##Output leaf/node
        node = [(frequency, char), left, right]
        # Returning the joined character/internal node inside the tree
        heapq.heappush(heap, node)
        ##After doing that for every single tree in the element we pop out the last least element
    return None if not heap else heap.pop()


# Let's now map the tree and assign it bits 0 and 1
 # A traverse helper function to be used in assignbits function
def traverse(branch, bitstore, bitvalue):
    if not branch: return None
    if (len(branch) == 1): # If the traverse has reached at the bottom (leaf)
       frequency, char = branch[0]  #printing the first character
       bitstore[char] = bitvalue  # Final bitvalue of a leaf after traversing with 0's and 1's eg. h= 001

    else:
       root, left, right = branch
       traverse(left, bitstore, bitvalue + "0")  # We are walking the tree towards left
       traverse(right, bitstore, bitvalue + "1")  # We are walking the tree towards right



def assignbits(branch):
    if not branch: return None
    bitstore = dict()
    traverse(branch, bitstore, '')
    return bitstore

#Encoding the message function
def encodemessage(msg, freqs):

    if msg == "" and freqs == []:
        print("***************************************************************")
        print("Empty String")
        print("***************************************************************")
    else:
        bitsassigned = assignbits(makeTree(freqs))
        return ''.join([bitsassigned[character] for character in msg])

#Decoding the encoded message
def decodemessage(encmsg, freqs):
   string_decoded = []
   branch = full_traverse = makeTree(freqs)
   if msg == "" and freqs == []:
       print("***************************************************************")
       print("Empty String")
       print("***************************************************************")

   #Traversing through the huffman tree
   for value in encmsg:
        if (value == '0'): branch = branch[1]
        else:
            branch = branch[2]
        if (len(branch) == 1):
            freq, char = branch[0]
            string_decoded.append(char)
            branch = full_traverse
   return ''.join(string_decoded)


freqs = [(1, 'b'), (2, 'd'), (2, 'e'), (2, 'h'), (2, 'i'), (1, 'o'), (2, 'r'), (1, 's'), (1, 'T'), (1, 't'), (1, 'w'), (4, ' ')]
freqs1 = [(1,'a'), (1,'a')]
freqs2 =[(2, 's'), (2, 'a'), (1, 'b'), (3, 'n'), (1, 'h'), (1, 'i'), (1, 'd'), (1, '#'), (1, 'j'), (1, 'k')]
freqs3 =[(1, 'k'), (1, 'j'), (1, 'l'), (1, 'v'), (3, 's'), (1, 'd'), (1, 'r'), (1, '0'), (1, '1'), (1, '?'), (1, '!'), (1, 'o'), (2, 'm'), (1, 'i'), (1, 'f')]
freqs4 = []
freqs5 = [(1,'a'), (1,'a'), (1,'a')]
freqs6 = [(1,'a'), (1,'a'), (1,'a'), (1,'a')]
freqs7 = [(1,'a'), (1,'a'), (1,'a'), (1,'a'), (1,'a')]
freqs8 = [(1,'a'), (1,'a'), (1,'a'), (1,'a'), (1,'a'), (1,'a')]
# freqs = (freq_build('The bird is the word'))
# freqs2 =(freq_build('sabnahisdn#njk'))
# freqs3 =(freq_build('kjlvsdr01?!osmimfs'))

msg = "The bird is the word" #encoded data will be 1110000100011011101010100111111001001111101010001000110101101101001111
#Test case 1
msg1 = "aa"  #encoded data
#Test case 2
msg2 = "sabnahisdn#njk" #encoded data will be 111100001101100101111001111010010010011101000
#Test case 3
msg3 = "kjlvsdr01?!osmimfs" #encoded data will be 011001010111110011100101011110110000000111010101011110001001000011111
#Test case 4
msg4 = "" #An empty input string
#Test case 5
msg5 = "aaa"
#Test case 6
msg6 = "aaaa"
#Test case 7
msg7 = "aaaaa"
#Test case 8
msg8 = "aaaaaa"
print("The size of the data of msg1 is: {}\n".format(sys.getsizeof(msg)))
print("The size of the data of msg2 is: {}\n".format(sys.getsizeof(msg2)))
print("The size of the data of msg3 is: {}\n".format(sys.getsizeof(msg3)))
print("The size of the data of msg4 is: {}\n".format(sys.getsizeof(msg4)))
print("The size of the data of msg4 is: {}\n".format(sys.getsizeof(msg5)))
print("The size of the data of msg4 is: {}\n".format(sys.getsizeof(msg6)))
print("The size of the data of msg4 is: {}\n".format(sys.getsizeof(msg7)))
print("The size of the data of msg4 is: {}\n".format(sys.getsizeof(msg8)))
print("The content of the data in msg1 is: {}\n".format(msg))
print("The content of the data in msg2 is: {}\n".format(msg2))
print("The content of the data in msg3 is: {}\n".format(msg3))
print("The content of the data in msg4 is: {}\n".format(msg4))
print("The content of the data in msg4 is: {}\n".format(msg5))
print("The content of the data in msg4 is: {}\n".format(msg6))
print("The content of the data in msg4 is: {}\n".format(msg7))
print("The content of the data in msg4 is: {}\n".format(msg8))
output = encodemessage(msg,freqs)
output1 = encodemessage(msg1,freqs1)
output2 = encodemessage(msg2, freqs2)
output3 = encodemessage(msg3, freqs3)
output5 = encodemessage(msg5, freqs5)
output6 = encodemessage(msg6, freqs6)
output7 = encodemessage(msg7, freqs7)
output8 = encodemessage(msg8, freqs8)
print("The size of the encoded data msg is: {}\n".format(sys.getsizeof(int(output, base=2))))
print("The size of the encoded data msg1 is: {}\n".format(sys.getsizeof(int(output1, base=2))))
print("The size of the encoded data in msg2 is: {}\n".format(sys.getsizeof(int(output2, base=2))))
print("The size of the encoded data in msg3 is: {}\n".format(sys.getsizeof(int(output3, base=2))))
print("The size of the encoded data in msg5 is: {}\n".format(sys.getsizeof(int(output5, base=2))))
print("The size of the encoded data in msg6 is: {}\n".format(sys.getsizeof(int(output6, base=2))))
print("The size of the encoded data in msg7 is: {}\n".format(sys.getsizeof(int(output7, base=2))))
print("The size of the encoded data in msg8 is: {}\n".format(sys.getsizeof(int(output8, base=2))))

print("The content of the encoded data in msg is: {}\n".format(output))
print("The content of the encoded data in msg1 is: {}\n".format(output1))
print("The content of the encoded data in msg2 is: {}\n".format(output2))
print("The content of the encoded data in msg3 is: {}\n".format(output3))
print("The content of the encoded data in msg5 is: {}\n".format(output5))
print("The content of the encoded data in msg6 is: {}\n".format(output6))
print("The content of the encoded data in msg7 is: {}\n".format(output7))
print("The content of the encoded data in msg8 is: {}\n".format(output8))


string_decoded = decodemessage(output, freqs)
string_decoded1 = decodemessage(output1, freqs1)
string_decoded2 = decodemessage(output2, freqs2)
string_decoded3 = decodemessage(output3, freqs3)
string_decoded5 = decodemessage(output5, freqs5)
string_decoded6 = decodemessage(output6, freqs6)
string_decoded7 = decodemessage(output7, freqs7)
string_decoded8 = decodemessage(output8, freqs8)

print("The size of the decoded data in msg is: {}\n".format(sys.getsizeof(string_decoded)))
print("The size of the decoded data in msg1 is: {}\n".format(sys.getsizeof(string_decoded1)))
print("The size of the decoded data in msg2 is: {}\n".format(sys.getsizeof(string_decoded2)))
print("The size of the decoded data in msg3 is: {}\n".format(sys.getsizeof(string_decoded3)))
print("The size of the decoded data in msg5 is: {}\n".format(sys.getsizeof(string_decoded5)))
print("The size of the decoded data in msg6 is: {}\n".format(sys.getsizeof(string_decoded6)))
print("The size of the decoded data in msg7 is: {}\n".format(sys.getsizeof(string_decoded7)))
print("The size of the decoded data in msg8 is: {}\n".format(sys.getsizeof(string_decoded8)))

print("The content of the decoded data in msg1 is: {}\n".format(string_decoded))
print("The content of the decoded data in msg1 is: {}\n".format(string_decoded1))
print("The content of the decoded data in msg2 is: {}\n".format(string_decoded2))
print("The content of the decoded data in msg3 is: {}\n".format(string_decoded3))
print("The content of the decoded data in msg5 is: {}\n".format(string_decoded5))
print("The content of the decoded data in msg6 is: {}\n".format(string_decoded6))
print("The content of the decoded data in msg7 is: {}\n".format(string_decoded7))
print("The content of the decoded data in msg8 is: {}\n".format(string_decoded8))

