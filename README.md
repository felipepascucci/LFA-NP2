# Relatório — Atividade: Lema do Bombeamento

Integrantes:

Felipe Rafael Tancredi Pascucci / RA: T895HG3  
Giovanna Santos da Silva / RA: G828HA5  
Leonardo Annunciação Rodrigues / RA: G801873  
Luan Gabriel Melo da Rocha / RA: G7787G0  
Isabelle Rosa Moura Ferreira / RA: N075465  
Kauã da Silva Ferreira / RA: G788486  

Disciplina: Linguagens Formais e Autômatos

Professor(a): Sthephany Oliveira

## Definição da Linguagem

A linguagem escolhida é:  
<br/>L = { aⁿ bⁿ | n ≥ 0 }  
<br/>Essa linguagem contém todas as cadeias compostas por uma sequência de 'a's seguida pela mesma quantidade de 'b's. Exemplos válidos incluem: 'ab', 'aabb', 'aaabbb', etc.

## Objetivo

Aplicar o Lema do Bombeamento para verificar se a linguagem L é ou não regular. Isso é feito dividindo uma cadeia w ∈ L em partes x, y, z, testando se ao repetir y, a cadeia ainda pertence à linguagem.

## Cadeia Testada

Cadeia w: "aaaabbbb"  
Comprimento: 8  
Valor de bombeamento p: 4  
Observa-se que |w| ≥ p, portanto é válida para o teste.

## Print/Output do Teste

Analisando cadeia: aaaabbbb, com p = 4

Testando divisao: x='', y='a', z='aaabbbb'
Com i=0: 'aaabbbb' -> NAO pertence a L
Com i=2: 'aaaaabbbb' -> NAO pertence a L

Testando divisao: x='a', y='a', z='aabbbb'
Com i=0: 'aaabbbb' -> NAO pertence a L
Com i=2: 'aaaaabbbb' -> NAO pertence a L

Testando divisao: x='aa', y='a', z='abbbb'
Com i=0: 'aaabbbb' -> NAO pertence a L
Com i=2: 'aaaaabbbb' -> NAO pertence a L

Testando divisao: x='aaa', y='a', z='bbbb'
Com i=0: 'aaabbbb' -> NAO pertence a L
Com i=2: 'aaaaabbbb' -> NAO pertence a L

QUEBRA DO LEMA: A linguagem NAO é regular

## Conclusão

A partir da simulação do lema do bombeamento:  
<br/>\- Encontramos uma divisão da cadeia w = xyz, com |xy| ≤ p e |y| ≥ 1, tal que, ao repetir y, a nova cadeia resultante não pertence à linguagem.  
\- Isso viola a condição do lema do bombeamento, que só se aplica a linguagens regulares.  
<br/>Portanto, concluímos que a linguagem L = { aⁿ bⁿ | n ≥ 0 } não é regular.

## Link do Código

https://github.com/felipepascucci/LFA-NP2
