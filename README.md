# Função print e variáveis
Depois de abrir o interpretador Python, podemos acessar um terminal à parte com a ajuda da linguagem. Basta chamarmos a função `help()`:

```
PS D:\alura\python-comecando> python
Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> help()

Welcome to Python 3.11's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.11/tutorial/. 

Enter the name of any module, keyword, or topic to get help on writing  
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help>
```

Chamando a ajuda para a função `print`:
```
help> print
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

help>
```

Usando separadores na função `print`:
```python
>>> print(1,2,3, sep='; ') # Repare no parâmetro nomeado "sep" e a string '; ' separando cada valor.
1; 2; 3
```

Modificando o fim da linha exibida pela função `print`:
```python
>>> print(1, 2, 3, end=' <câmbio>\n\n') # Repare no parâmetro "end" e a saída. A saída tem duas quebras de linha.
1 2 3 <câmbio>

>>>
```
Comando com a atribuição de variáveis para uso posterior na função `print`.
```python
>>> pais = 'Italia'
>>> type(pais)
<class 'str'>
>>> quantidade = 4
>>> type(quantidade)                            
<class 'int'>
>>> print(pais, "ganhou", quantidade, "titulos mundiais")
Italia ganhou 4 titulos mundiais
>>>
```
# Tipagem do Python
A tipagem do Python é dinâmica: uma variável pode guardar uma string agora e guardar um inteiro depois. O tipo em Python é definido na execução, não na compilação.

# Comparando variáveis
```python
numero_secreto = 43                     # Inteiro.
chute = input("Digite o seu número: ")  # Lê a entrada como string.

print(numero_secreto == chute)      ## Imprime false: compara inteiro com string.
print(numero_secreto == int(chute)) ## Imprime true: compara inteiro com inteiro.
```

# Diferenças entre o Python 2 e o Python 3
A chamda da função no Python 2 admite que a função `print` dispense parênteses.
```python
print('Funciona nas duas versões do Python, 2 e 3')
print "Só funciona no Python 2" # Erro de interpretação no Python 3.
```
Fornecer uma lista como parâmetro no Python 3 resulta em uma única string;
```python
>>> print("ola", "mundo")
# No Python 2, o resultado é => ("ola", "mundo")
# No Python 3, o resultado é => "ola mundo"
```

O comando `print` no Python 2 não tem o parâmetro `sep`
```python
>>> print("ola", "mundo", sep=', ', end='\r\n') # Erro de compilação no Python 2.
```

A função `input` no Python 2 infere o tipo de dados; no Python 3 o tipo é sempre string.
```python
>>> var = input('Digite')
Digite 3
>>> type(var)
# No Python 2, imprime <type 'int'>. A função raw_input sempre lê string.
# No Python 3, imprime <type 'str'>. A função raw_input não existe na versão nova do Python.
```

# A condição elif
`elif` é o mesmo que `else if` no Python.

Código do arquivo `adivinhacao.py`:
```python
print("*******************************")
print("Bem vindo ao jogo de avinhação!")
print("*******************************")

numero_secreto = 43

chute_str = input("Digite o seu número: ")

print("Você digitou", chute_str)
chute = int(chute_str)

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if (acertou):
    print("Você acertou.")
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")
    
print("Fim do jogo.")
```

# O laço com while

Atualização do código do arquivo `adivinhacao.py`:
```python
print("*******************************")
print("Bem vindo ao jogo de avinhação!")
print("*******************************")

numero_secreto = 43
total_tentativas = 3
rodada = 1

while (rodada <= total_tentativas):
    print ('Tentativa', rodada, 'de', total_tentativas)
    chute_str = input("Digite o seu número: ")
    if (chute_str == 'FIM'):
        exit()

    print("Você digitou", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você acertou.")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

    rodada = rodada + 1
    
print("Fim do jogo.")
```

# Formatação de strings

Atualização do código do arquivo `adivinhacao.py`:

```python
print("*******************************")
print("Bem vindo ao jogo de avinhação!")
print("*******************************")

numero_secreto = 43
total_tentativas = 3
rodada = 1

while (rodada <= total_tentativas):
    # Interpolação da string com a função .format(...)
    print ('Tentativa {} de {}'.format(rodada, total_tentativas))
    # print (f'Tentativa {rodada} de {total_tentativas}') # Usando as f-strings.
    chute_str = input("Digite o seu número: ")
    if (chute_str == 'FIM'):
        exit()

    print("Você digitou", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você acertou.")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

    rodada = rodada + 1
    
print("Fim do jogo.")
```
> Você pode usar f-strings também: 
> ```python
> variavel = 10
> print(f'Conteúdo da variavel: {variavel}.')
> # Imprime: Conteúdo da variavel: 10.
> ```

# O laço com for
Sintaxe de um laço com for:
```python
for i in [1,2,3]:
    print(f'Número {i}')
# Resultado (o número 10 não está incluído no range):
# Número 1
# Número 2
# Número 3
```
> Note que no loop com `for` não se usa parenteses, como no `while` ou no `if`.

A função `range` retorna um vetor com números gerados a partir de um início, exclui o número de fim e se gera um número a partir de um valor de passo.
```python
inicio  = 1     # É incluído na função range.
fim     = 10    # É excluído da função range.
passo   = 3     # Valor que se incrementa a cada passo.
for num in range(inicio, fim, passo):
    print(f'Número {num}')
# Resultado (o número 10 não está incluído no range):
# Número 1
# Número 4
# Número 7
```
# Encerrando a interação e o loop
O comando `break` serve para sair de um laço. O comando `continue` força o próximo loop, sem executar os comandos que vem depois.

```python
print("*******************************")
print("Bem vindo ao jogo de avinhação!")
print("*******************************")

numero_secreto = 43
total_tentativas = 3
rodada = 1

for rodada in range(1, total_tentativas + 1):
    # Interpolação da string com a função .format(...)
    print ('Tentativa {} de {}'.format(rodada, total_tentativas))
    # print (f'Tentativa {rodada} de {total_tentativas}') # Usando as f-strings.
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você acertou.")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
    
print("Fim do jogo.")
```

# Para saber mais: Formatação de strings
```python
"Num. {} de {}.".format(3, 10)      # Resultado: Num. 3 de 10. A ordem dos parms é seguida.
"Num. {0} de {1}.".format(3, 10)    # Resultado: Num. 3 de 10. A base de índice dos parms é zero.
"Num. {1} de {0}.".format(3, 10)    # Resultado: Num. 10 de 3. Invertemos a ordem dentro da string.

"R$ {}".format(1.59)
    # Resultado: R$ 1.59.
"R$ {:f}".format(1.59)
    # Resultado: R$ 1.590000. Por padrão, o formato :f insere seis casas decimais.
"R$ {:2f}".format(1.5)
    # Resultado: R$ 1.50. O formato :2f insere duas casas decimais.
"R$ {:7.2f}".format(1.59)
    # Resultado: R$    1.59. O formato :7.2f acrescenta espaços e alinha casas decimais.
    # O total de dígitos será 7.
"R$ {:07.2f}".format(1.59)
    # Resultado: R$ 0001.59. O formato :07.2f acrescenta espaços e alinha casas decimais.
    # O total de dígitos será 7.

"Int. {:7d}".format(80)
    # Resultado: Int. 0000080. O formato :7d acrescenta espaços e o total de dígitos deve ser sete.
"Int. {:07d}".format(80)
    # Resultado: Int. 0000080. O formato :07d acrescenta zeros e o total de dígitos deve ser sete.

"Data {:2}/{:2}".format(9, 4)
    # Resultado: Data  9/ 4. Repare nos espaços acrescentados ao lado dos dígitos menores que 10.
"Data {:02}/{:02}".format(9, 4)
    # Resultado: Data 09/04. Repare nos zeros acrescentados ao lado dos dígitos menores que 10.
```

> O Python 2 usava uma sintaxe especial, ao invés do `format` era preciso usar o caractere %. Veja o exemplo:
> ```python
> "%d %d" % (1, 2)
> ```

Interpolação de strings com f-strings no Python 3:
```python
>>> nome = 'Matheus'
>>> print(f'Meu nome é {nome.lower()}')
# Resultado: Meu nome é matheus
# Repare na função lower, que retornou o valor da variável em minúsculo antes da saída.
```

# Gerando e arredondando um número aleatório
Invocando a função `random`, que gera números aleatórios. Ela não é uma função built-in: é necessário importá-la do módulo `random`:
```python
>>> import random
>>> random.random()
0.07931856838049844
```

Você pode arredondar números com a funçao built-in `round`:
```python
>>> round(random.random() * 5)
3
```

# Definindo um intervalo para a geração de números aleatórios
A função `random.randrange` retorna um inteiro aleatório entre uma faixa de números:
```python
random.randrange(10) # Números de zero a dez.
random.randrange(1, 10) # Números de um a nove (exclui o dez).
random.randrange(2, 21, 2) # Números pares de 2 a 20 (exclui o 21).
```

`random` é uma função que, dada a mesma entrada, gerará o mesmo número. O truque é oferecer sempre uma entrada diferente para ter números diferentes e exatamente isso que está acontecendo por baixo dos panos.

Essa entrada também é chamada de seed (semente, em português). Entre as chamadas da função `random`, sempre é utilizado um novo seed. Por padrão o Python usa a hora (os milissegundos) como semente, mas nada nos impede de definir o mesmo seed antecipadamente. Para isso, existe a função `seed`!

Por exemplo, no jogo usamos a função `randrange` para gerar um número aleatório entre 1 e 100. Antes do randrange podemos chamar o seed para definir a entrada:

```python
>>> random.seed(100)
>>> random.randrange(1, 101)
19
```

Repare que foi gerado 19 e se usarmos o mesmo seed será gerado o mesmo número:

```python
>>> random.seed(100) # Reinseriu a mesma semente.
>>> random.randrange(1, 101)
19 # Retornou o mesmo número 19.
```
Repare que a biblioteca random é bem previsível e por isso se chama pseudo-random!
