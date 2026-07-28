# Jorge Guillermo Farfan Zapata


def es_entero(valor):
    return isinstance(valor, int) and not isinstance(valor, bool)


def es_numero(valor):
    return isinstance(valor, (int, float)) and not isinstance(valor, bool)


def validar_entero_no_negativo(valor, nombre):
    if not es_entero(valor):
        raise TypeError(
            f"'{nombre}' must be an integer, but {type(valor).__name__} "
            f"was received ({valor!r})."
        )
    if valor < 0:
        raise ValueError(
            f"'{nombre}' must be >= 0, but {valor} was received."
        )


def _recursiva(n):
    if n == 0:
        return "Done!"
    print(n)
    return _recursiva(n - 1)


def recursiva(n):
    try:
        validar_entero_no_negativo(n, "n")
        return _recursiva(n)
    except (TypeError, ValueError) as error:
        print(f"[ERROR] recursiva: {error}")
        return None
    except RecursionError:
        print("[ERROR] recursiva: recursion limit reached.")
        return None


def _fibonacci(n, memoria):
    if n in memoria:
        return memoria[n]
    if n == 0 or n == 1:
        return n
    resultado = _fibonacci(n - 1, memoria) + _fibonacci(n - 2, memoria)
    memoria[n] = resultado
    return resultado


def fibonacci(n):
    try:
        validar_entero_no_negativo(n, "n")
        return _fibonacci(n, {})
    except (TypeError, ValueError) as error:
        print(f"[ERROR] fibonacci: {error}")
        return None
    except RecursionError:
        print("[ERROR] fibonacci: recursion limit reached.")
        return None


def _factorial(n):
    if n == 0 or n == 1:
        return 1
    return _factorial(n - 1) * n


def factorial(n):
    try:
        validar_entero_no_negativo(n, "n")
        return _factorial(n)
    except (TypeError, ValueError) as error:
        print(f"[ERROR] factorial: {error}")
        return None
    except RecursionError:
        print("[ERROR] factorial: recursion limit reached.")
        return None


def _multiplicacion_recursiva(n, m):
    if m == 0:
        return 0
    return _multiplicacion_recursiva(n, m - 1) + n


def multiplicacion_recursiva(n, m):
    try:
        if not es_numero(n):
            raise TypeError(
                f"'n' must be a number, {type(n).__name__} received ({n!r})."
            )
        if not es_entero(m):
            raise TypeError(
                f"'m' must be an integer, {type(m).__name__} received ({m!r})."
            )
        if m < 0:
            return -_multiplicacion_recursiva(n, -m)
        return _multiplicacion_recursiva(n, m)
    except TypeError as error:
        print(f"[ERROR] multiplicacion_recursiva: {error}")
        return None
    except RecursionError:
        print("[ERROR] multiplicacion_recursiva: 'm' is too large.")
        return None


def _division_entera_recursiva(dividendo, divisor):
    if dividendo - divisor < 0:
        return 0
    return _division_entera_recursiva(dividendo - divisor, divisor) + 1


def division_entera_recursiva(dividendo, divisor):
    try:
        if not es_entero(dividendo):
            raise TypeError(
                f"'dividendo' must be an integer, "
                f"{type(dividendo).__name__} received ({dividendo!r})."
            )
        if not es_entero(divisor):
            raise TypeError(
                f"'divisor' must be an integer, "
                f"{type(divisor).__name__} received ({divisor!r})."
            )
        if divisor == 0:
            raise ZeroDivisionError("cannot divide by zero.")
        negativo = (dividendo < 0) != (divisor < 0)
        cociente = _division_entera_recursiva(abs(dividendo), abs(divisor))
        return -cociente if negativo else cociente
    except (TypeError, ZeroDivisionError) as error:
        print(f"[ERROR] division_entera_recursiva: {error}")
        return None
    except RecursionError:
        print("[ERROR] division_entera_recursiva: quotient too large.")
        return None


def _potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    return _potencia_recursiva(base, exponente - 1) * base


def potencia_recursiva(base, exponente):
    try:
        if not es_numero(base):
            raise TypeError(
                f"'base' must be a number, "
                f"{type(base).__name__} received ({base!r})."
            )
        if not es_entero(exponente):
            raise TypeError(
                f"'exponente' must be an integer, "
                f"{type(exponente).__name__} received ({exponente!r})."
            )
        if exponente < 0:
            if base == 0:
                raise ZeroDivisionError(
                    "0 raised to a negative exponent is undefined."
                )
            return 1 / _potencia_recursiva(base, -exponente)
        return _potencia_recursiva(base, exponente)
    except (TypeError, ZeroDivisionError) as error:
        print(f"[ERROR] potencia_recursiva: {error}")
        return None
    except RecursionError:
        print("[ERROR] potencia_recursiva: 'exponente' is too large.")
        return None
    except OverflowError:
        print("[ERROR] potencia_recursiva: result too large.")
        return None


def _serie_collatz(n):
    if n == 1:
        print("END!")
        return 0
    if n % 2 == 0:
        print(n // 2)
        return _serie_collatz(n // 2)
    print(3 * n + 1)
    return _serie_collatz(3 * n + 1)


def serie_collatz(n):
    try:
        if not es_entero(n):
            raise TypeError(
                f"'n' must be an integer, {type(n).__name__} received ({n!r})."
            )
        if n < 1:
            raise ValueError(f"'n' must be >= 1, but {n} was received.")
        return _serie_collatz(n)
    except (TypeError, ValueError) as error:
        print(f"[ERROR] serie_collatz: {error}")
        return None
    except RecursionError:
        print("[ERROR] serie_collatz: recursion limit reached.")
        return None


def _guardar(elementos, clave, valor):
    if clave in elementos:
        contador = 2
        nueva = f"{clave}#{contador}"
        while nueva in elementos:
            contador += 1
            nueva = f"{clave}#{contador}"
        print(f"[WARNING] aplanar_json: key collision on '{clave}'. "
              f"Saved as '{nueva}'.")
        clave = nueva
    elementos[clave] = valor


def _aplanar_json(estructura, clave_padre, separador, elementos):
    if isinstance(estructura, dict):
        pares = estructura.items()
    elif isinstance(estructura, list):
        pares = enumerate(estructura)
    else:
        pares = None

    if pares is None:
        _guardar(elementos, clave_padre, estructura)
        return elementos

    for clave, valor in pares:
        nueva_llave = (f"{clave_padre}{separador}{clave}"
                       if clave_padre != "" else str(clave))
        if isinstance(valor, (dict, list)):
            _aplanar_json(valor, nueva_llave, separador, elementos)
        else:
            _guardar(elementos, nueva_llave, valor)
    return elementos


def aplanar_json(diccionario, clave_padre="", separador="."):
    try:
        if not isinstance(diccionario, (dict, list)):
            raise TypeError(
                f"a dict or a list was expected, "
                f"{type(diccionario).__name__} received ({diccionario!r})."
            )
        if not isinstance(clave_padre, str):
            raise TypeError("'clave_padre' must be a string.")
        if not isinstance(separador, str) or separador == "":
            raise TypeError("'separador' must be a non empty string.")
        return _aplanar_json(diccionario, clave_padre, separador, {})
    except TypeError as error:
        print(f"[ERROR] aplanar_json: {error}")
        return None
    except RecursionError:
        print("[ERROR] aplanar_json: structure nested too deeply.")
        return None


def titulo(texto):
    print("\n" + "=" * 70)
    print(texto)
    print("=" * 70)


def main():
    titulo("1. recursiva(n)")
    print("recursiva(5)  ->", recursiva(5))
    print("recursiva(0)  ->", recursiva(0))
    print("recursiva(-3) ->", recursiva(-3))
    print("recursiva(3.5)->", recursiva(3.5))
    print('recursiva("5")->', recursiva("5"))

    titulo("2. fibonacci(n)")
    print("fibonacci(0)  ->", fibonacci(0))
    print("fibonacci(7)  ->", fibonacci(7))
    print("fibonacci(40) ->", fibonacci(40))
    print("fibonacci(-1) ->", fibonacci(-1))

    titulo("3. factorial(n)")
    print("factorial(5)  ->", factorial(5))
    print("factorial(0)  ->", factorial(0))
    print("factorial(-2) ->", factorial(-2))
    print("factorial(1.5)->", factorial(1.5))

    titulo("4. multiplicacion_recursiva(n, m)")
    print("multiplicacion_recursiva(4, 3)  ->", multiplicacion_recursiva(4, 3))
    print("multiplicacion_recursiva(7, 0)  ->", multiplicacion_recursiva(7, 0))
    print("multiplicacion_recursiva(4, -3) ->", multiplicacion_recursiva(4, -3))
    print('multiplicacion_recursiva(4,"3")->', multiplicacion_recursiva(4, "3"))

    titulo("5. division_entera_recursiva(dividendo, divisor)")
    print("division_entera_recursiva(17, 5)  ->",
          division_entera_recursiva(17, 5))
    print("division_entera_recursiva(5, 5)   ->",
          division_entera_recursiva(5, 5))
    print("division_entera_recursiva(10, 0)  ->",
          division_entera_recursiva(10, 0))
    print("division_entera_recursiva(-10, 3) ->",
          division_entera_recursiva(-10, 3))

    titulo("6. potencia_recursiva(base, exponente)")
    print("potencia_recursiva(2, 5)  ->", potencia_recursiva(2, 5))
    print("potencia_recursiva(5, 0)  ->", potencia_recursiva(5, 0))
    print("potencia_recursiva(2, -2) ->", potencia_recursiva(2, -2))
    print("potencia_recursiva(0, -2) ->", potencia_recursiva(0, -2))

    titulo("7. serie_collatz(n)")
    print("serie_collatz(6)  ->", serie_collatz(6))
    print("serie_collatz(1)  ->", serie_collatz(1))
    print("serie_collatz(0)  ->", serie_collatz(0))
    print("serie_collatz(-6) ->", serie_collatz(-6))

    titulo("8. aplanar_json(diccionario)")
    print('{"a": 1, "b": {"c": 2}}   ->',
          aplanar_json({"a": 1, "b": {"c": 2}}))
    print('{"a": {"b": {"c": 1}}}    ->',
          aplanar_json({"a": {"b": {"c": 1}}}))
    print('["a", "b", "c"]           ->',
          aplanar_json(["a", "b", "c"]))
    print('{"tags": [1, 2, 3]}       ->',
          aplanar_json({"tags": [1, 2, 3]}))
    print('{"a.b": 1, "a": {"b": 2}} ->',
          aplanar_json({"a.b": 1, "a": {"b": 2}}))
    print("aplanar_json(42)          ->", aplanar_json(42))

    titulo("PROGRAM FINISHED WITHOUT CRASHING")


if __name__ == "__main__":
    main()