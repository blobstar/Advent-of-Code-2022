#read in the input
with open('input.txt') as f:
    packet = f.read()
f.close()
packet2 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
#print(packet)
arrayPacket = list(packet.strip())
arrayPacket2 = list(packet2.strip())

#print(arrayPacket)

# finds the spm given an input array
def packetCount(signal):
    count = 0
    for i in range(len(signal)-14):
        spm = signal[i:i+14]
        #print(spm)
        setpm = set(spm)
        #print(setpm)
        if (len(setpm) < 14):
            count += 1
        else:
            return count + 14



print(packetCount(arrayPacket))