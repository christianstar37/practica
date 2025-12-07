novios_a = ['Karasuma']
novias_a = ['Kurenai']
novios_irl = ['Oscar Isaac']
novias_irl = ['Cate Blanchett']
novias = novias_a + novias_irl
novios = novios_a + novios_irl
nov_irl = novias_irl + novios_irl
nov_a = novias_a + novios_a
novixs = novias_a + novias_irl + novios_a + novios_irl

elegidos = novixs

print('')

for i in range(len(elegidos))[::-1]:
    for j in range(len(elegidos)):
        if i > j:
            print(f"{elegidos[i]} vs {elegidos[j]}") 

print('')