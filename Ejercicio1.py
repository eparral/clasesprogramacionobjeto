def son_anagramas(a: str, b: str) -> bool:
    def normalizar(cadena: str) -> str:
        return ''.join(c.lower() for c in cadena if not c.isspace())

    a_norm = normalizar(a)
    b_norm = normalizar(b)

    if len(a_norm) != len(b_norm):
        return False

    def contar_letras(cadena: str) -> dict:
        frecuencia = {}
        for letra in cadena:
            frecuencia[letra] = frecuencia.get(letra, 0) + 1
        return frecuencia

    return contar_letras(a_norm) == contar_letras(b_norm)

soy_un_buleano=son_anagramas("Amor","Roma")