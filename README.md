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
