# The Farmer Was Replaced: fazenda automática

Meu código para o [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/),
um jogo em que você programa um drone para cuidar da fazenda numa linguagem
parecida com Python. O objetivo aqui é a fazenda rodar sozinha: o `main.py` sobe a meta
de cada item e o drone vai plantando e colhendo até bater a meta.

## Como roda

`main.py` é um laço infinito. A cada volta a meta é multiplicada por 1,6 e o drone
farma, em ordem, energia, trigo, madeira, cenoura, abóbora, cacto e osso até ter
`meta` unidades de cada. Depois de 10 000 ele começa a trocar de chapéu
(`sort_hat`, escolhido pelo estoque de água, o que dá uma troca meio aleatória).

`basic.farmar(cultura, meta)` usa um catálogo `nome → (função, item)`, então pôr
uma cultura nova é só uma linha no dicionário, sem cadeia de `if`.

## Arquivos

| Arquivo | O que faz |
|---|---|
| `main.py` | laço das metas |
| `basic.py` | catálogo de culturas, preparo do solo (`verificar_solo`), colheita e chapéus |
| `mover.py` | ir até `(x, y)` pelo caminho mais curto (o mundo é um toro: sair por um lado entra pelo outro) e percorrer o campo inteiro |
| `culturas_base.py` | trigo, madeira (árvore nas casas de x e y pares, arbusto no resto) e cenoura |
| `culturas_medias.py` | girassol, abóbora e cacto |
| `culturas_avancadas.py` | dinossauro (osso) e consórcio |
| `__builtins__.py` | tipos das funções do jogo, só para o editor entender (feito pela comunidade no Discord do jogo) |

## Estratégias

- **Girassol (energia):** planta o campo todo e guarda as posições por número de
  pétalas; colhe do que tem mais pétalas para o que tem menos, que é o que dá o bônus.
- **Abóbora:** planta tudo, replanta as que morreram até o campo inteiro estar
  maduro e colhe tudo junto, numa abóbora gigante.
- **Cacto:** ordena o campo trocando vizinhos (`swap`) por linha e por coluna, um
  bubble sort, para colher tudo de uma vez já ordenado.
- **Dinossauro (osso):** com o chapéu de dinossauro, o drone vira uma cobrinha e
  percorre o campo em zigue-zague, coluna por coluna. Esse caminho passa por todas
  as casas sem cruzar o próprio rabo.
- **Consórcio:** pergunta para cada planta qual companheira ela quer
  (`get_companion`) e planta essa onde ela pede. Ainda está meio travado, e foi escrito
  para dar para dividir entre vários drones.
