string='''jyothsna puri moahn anil mamu ninna all are close friends!!!'''
wordslist=string.split(' ')
ans=[i for i in wordslist if len(i)<5 ]
print(*ans)
