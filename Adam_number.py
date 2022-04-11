n=int(input())
sq=n*n

revn=str(n)
revn=list(revn)
revn.reverse()
revn=''.join(revn)

revn=int(revn)
sqrev=revn*revn

sqrevn=str(sqrev)
sqrevn=list(sqrevn)
sqrevn.reverse()
sqrevn=''.join(sqrevn)
sqrevn=int(sqrevn)
if sq==sqrevn:
    print('True')
else:
    print('False')