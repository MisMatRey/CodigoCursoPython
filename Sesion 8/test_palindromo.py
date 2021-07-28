from palindromo import es_palindromo

def test_palabras_simples():
  assert es_palindromo("oso")
  assert es_palindromo("ojo")
  assert not es_palindromo("ola")

def test_frases_completas():
  assert es_palindromo("Dabale arroz a la zorra el abad")
  assert es_palindromo("A Bali su flan anal fusilaba")
  assert es_palindromo("Sometamos o matemos")
  assert es_palindromo("Sera lodo o dolares")
  assert es_palindromo("Lavan esa base naval")