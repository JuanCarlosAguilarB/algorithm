/*
Problem 

En una lengua alienígena también utilizan las letras del español, pero posiblemente en un orden diferente. Es una permutación de nuestro alfabeto.

Tu desafío es, dada una secuencia de palabras escritas en el idioma extranjero y el orden del alfabeto alienígena, devolver verdadero si 
y solo si las palabras dadas están ordenadas lexicográficamente según el orden de letras del alfabeto alienígena dado.

*/

function isAlienSorted(palabras, orden) {
  let index = 0;
  while (index < palabras.length - 1) {
    if (palabras[index][0] == palabras[index + 1][0]) {
      if (
        palabras[index].startsWith(
          palabras[index + 1] || palabras[index + 1].startsWith(palabras[index])
        )
      ) {
        if (!(palabras[index].length <= palabras[index + 1].length))
          return false;
      } else {
        let secondIndex = 1;
        while (secondIndex <= Math.min(palabras[index], palabras[index + 1])) {
          let firstletter = palabras[index][secondIndex];
          let secondletter = palabras[index][secondIndex + 1];

          if (firstletter != secondletter) {
            if (!(orden.indexOf(firstletter) <= orden.indexOf(secondletter)))
              return false;
            break;
          }
          secondIndex += 1;
        }
      }
    } else {
      let firstletter = palabras[index][0];
      let secondletter = palabras[index + 1][0];

      if (!(orden.indexOf(firstletter) <= orden.indexOf(secondletter)))
        return false;
    }

    index += 1;
  }
  return true;
}

// example 1
// Input
const words1 = ["habito", "hacer", "lectura", "sonreir"];
const order1 = "hlabcdfgijkmnopqrstuvwxyz";
//    isAlienSorted(words1, order1);
console.log(isAlienSorted(words1, order1), "Output True");
// Output
// true

// Input 1
const words2 = ["habito", "hacer", "sonreir", "lectura"];
const order2 = "hlabcdfgijkmnopqrstuvwxyz";
//    isAlienSorted(words2, order2);
console.log(isAlienSorted(words2, order2), "Output false");
// Output 2
// false

const words3 = ["conocer", "cono"];
const order3 = "abcdefghijkmnopqrstuvwxyz";
//    isAlienSorted(words3, order3);
console.log(isAlienSorted(words3, order3), "Output falseds");
// Output:
// false

// _________________________________________________________________________________________________________________________
// another version of solution

var isAlienSorted = function (palabras, orden) {
  // Crear mapa del diccionario alienigena
  mapa_diccionario = new Map();
  for (let i = 0; i < orden.length; i++) {
    mapa_diccionario[orden[i]] = i;
  }

  // Revisar el orden de las palabras
  for (let i = 1; i < palabras.length; i++) {
    // T = 0(n)   S = 0(m)
    if (comparar(palabras[i - 1], palabras[i]) === false) {
      return false;
    }
  }
  return true;
};

// O(longitud de la palabra mÃ¡s larga)
var comparar = function (palabra1, palabra2) {
  const longitud = Math.min(palabra1.length, palabra2.length);
  for (let i = 0; i < longitud; i++) {
    if (mapa_diccionario[palabra1[i]] < mapa_diccionario[palabra2[i]]) {
      return true;
    }
    if (mapa_diccionario[palabra1[i]] > mapa_diccionario[palabra2[i]]) {
      return false;
    }
  }
  return palabra1.length <= palabra2.length;
};
