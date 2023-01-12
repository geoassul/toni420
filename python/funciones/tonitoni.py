while True: 
    palabra = input('> ')
    if palabra == 'fin':
        break
    if palabra < 'banana':
        print('Tu palabra, ' + palabra + ', está antes de banana.')
    elif palabra > 'banana':
        print('Tu palabra, ' + palabra + ', está después de banana.')
    else:
        print('Muy bien, bananas.')
    print(palabra.capitalize())
    print(palabra.center(100))
    print(palabra.count('o',0,5))
    #print(palabra.encode()) - no entiendo bien para que sirve este metodo del string
    print(palabra.endswith('mojo',0,5))
    print(palabra.expandtabs())
    print(palabra.find('je'))
    #print(palabra.index('je',0,5))
    print(palabra.isalnum())
    print(palabra.isalpha())
    print(palabra.isdigit())
    print(palabra.islower())
    print(palabra.isspace())
    print(palabra.istitle())
    print(palabra.isupper())
    print(palabra.join('palabra'))
    print(palabra.ljust(10000))
    print(palabra.lower())
    print(palabra.lstrip())
    print(palabra.replace('joder','no molestes'))
    print(palabra.rfind('j'))
    print(palabra.find('j'))#no encuentro la diferencia entre find y rfind
    print(palabra.rjust(50))
    print(palabra.rstrip())
    print(palabra.split(None,23))
    print(palabra.rfind('jo'))
    print(palabra.splitlines(True))
    print(palabra.startswith('esto'))
    print(palabra.strip())
    print(palabra.swapcase())
    print(palabra.title())
    print(palabra.translate('a'))
    print(palabra.upper())