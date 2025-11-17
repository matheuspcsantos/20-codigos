def eh_palindromo(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(eh_palindromo("Ame a Ema"))
