maca = int(input("As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. "
                 "Quantas maças você deseja comprar?"))
maca1 = 1.30
maca2 = 1

total = int(maca * maca1)
total2 = int(maca * maca2)

if maca <= 11:
    print(f'Você comprou {maca} maças, pagou R$ 1,30 por unidade e o valor total foi R$ {total},00. Obrigado e volte sempre!')

elif maca >= 12:
    print(f'Você comprou {maca} maças, pagou R$ 1,00 por unidade e o valor total foi R$ {total2},00. Obrigado e volte sempre!')
