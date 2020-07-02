n1=int(raw_imput("numero uno"))
n2=int(raw_imput("numero dos"))
while n1 != n2:
    if n1>n2:
        n2=int(raw_imput("elije otro numero dos menor"))
    else:
        n2=int(raw_imput("elije otro numero dos mayor"))

print str("n1=n2")# esta sería la alternativa 1


#la alternativa 2 sería
n1=int(raw_imput("numero uno"))
n2=int(raw_imput("numero dos"))

while n1!=n2:
    if n1>n2:
        n2=int(raw_imput("otro numero dos mayor"))
        continue
        n2=int(raw_imput("otro numero menor"))
print str("n1=n2")#esta sería la otra alternativa, usar continue en vez de else.
