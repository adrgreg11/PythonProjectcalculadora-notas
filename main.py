def media(notas):
    """Devuelve la media aritmética de una lista de notas."""
    return sum(notas) / len(notas)


def calificacion(nota):
    """Devuelve la calificación en texto de una nota numérica."""
    if nota < 5:
        return "Insuficiente"
    elif nota < 6:
        return "Suficiente"
    elif nota < 7:
        return "Bien"
    elif nota < 9:
        return "Notable"
    return "Sobresaliente"


if __name__ == "__main__":
    notas = [6.5, 7, 8.25, 5]
    m = media(notas)
    print(f"Nota media del grupo: {m:.2f}")
    print(f"Calificación: {calificacion(m)}")

    def media_ponderada(notas, pesos):
        """Media ponderada: cada nota se multiplica por su peso."""
        return sum(n * p for n, p in zip(notas, pesos)) / sum(pesos)
    pesos = [0.2, 0.2, 0.4, 0.2]
    print(f"Media ponderada: {media_ponderada(notas, pesos):.2f}")

def nota_maxima(notas):
    return max(notas)


def nota_minima(notas):
    return min(notas)
print(f"Nota más alta: {nota_maxima(notas)}")
print(f"Nota más baja: {nota_minima(notas)}")

def nota_maxima(notas):
    """Devuelve la nota más alta de una lista."""
    return max(notas)


def nota_minima(notas):
    """Devuelve la nota más baja de una lista."""
    return min(notas)