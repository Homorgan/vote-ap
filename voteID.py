import random

test = 0
data = []
counter = 0
count = 0

#while test = 0:
for x in range(10):
    data.append(hex(random.getrandbits(64))[2:-1])

#for pkt in data:
#    print pkt


while test == 0:
    voteID = hex(random.getrandbits(64))[2:-1]
    test_vote = data.count(voteID)
    if test_vote == 1:
        # data.append(voteID)
        test = 1
        print 'The new Id is {}'.format(voteID)
    else:
        data.append(voteID)
        counter = counter + 1
        count = count + 1

    if count == 100:
        print 'The count is {}'.format(counter)
        test = 1
        for pkt in data:
            print pkt

print 'The database has {} records'.format(counter)
