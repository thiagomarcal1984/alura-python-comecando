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
