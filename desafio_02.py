'''
Desafio
Um supermercado está fazendo uma promoção de venda de refrigerantes. Se um dia você comprar 
refrigerantes e levar os cascos vazios no dia seguinte, ela troca cada conjunto de K garrafas 
vazias  por uma garrafa cheia. Um cliente quer aproveitar ao máximo essa oferta e por isso 
comprou várias garrafas no primeiro dia da promoção. Agora ele quer saber quantas garrafas 
terá ao final do segundo dia da promoção, se usá-la ao máximo.

Faça um programa para calcular isso.

Entrada
A primeira linha de entrada contém inteiro T (1 ≤ T ≤ 10000) , que indica o número de casos de teste.
 Em cada uma das T linhas a seguir vêm dois inteiros N e K (1 ≤ K, N ≤ 10000), 
 respectivamente o número de refrigerantes comprados e o número de garrafas vazias para ganhar uma cheia.

Saída
Para cada caso de teste imprima o número de garrafas que o cliente terá no segundo dia, se aproveitar ao máximo a oferta.
'''

def promo (k, n):
    if n >= k:
        resto = n % k
        novas = n // k
        return resto + novas
    else:
        return n

def input_promo():
    for i in range(int(input())):
        arg = input().split()
        n = int(arg[0])
        k = int(arg[1])
        print(promo(k, n))

    
'''
DESAFIO
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.

'''
dicionario = { "vertebrado" : { 
                "ave" : {
                    "carnivoro" : "aguia",
                    "onivoro" : "pomba"
                }, 
                "mamifero": { 
                    "onivoro" : "homem",
                    "herbivoro" : "vaca"
                }
            },
            "invertebrado" : { 
                "inseto" : {
                    "hematofago" : "pulga",
                    "herbivoro" : "lagarta"
                }, 
                "anelideo": { 
                    "hematofago" : "sanguessuga",
                    "onivoro" : "minhoca"
                }
            }
         }

def desafio_animais():
    a = input() 
    b = input() 
    c = input() 
    print(dicionario[a][b][c])


desafio_animais()