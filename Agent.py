import sys

HOLA_MUNDO = {
    "python": 'print("Hola Mundo")',
    "javascript": 'console.log("Hola Mundo");',
    "java": """
public class Main {
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
    }
}
""",
    "c": """
#include <stdio.h>

int main() {
    printf("Hola Mundo");
    return 0;
}
"""
}

def generar_hola_mundo(lenguaje):
    return HOLA_MUNDO.get(
        lenguaje.lower(),
        f"No conozco el lenguaje: {lenguaje}"
    )

if __name__ == "__main__":
    lenguaje = sys.argv[1]
    print(generar_hola_mundo(lenguaje))
