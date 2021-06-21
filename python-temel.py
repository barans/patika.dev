def duzlestir(liste):
    duz_liste = []
    for eleman in liste:
        if type(eleman) == list:
            [duz_liste.append(i) for i in duzlestir(eleman)]
        else:
            duz_liste.append(eleman)
    return duz_liste
    
def ters_cevir(liste):
    liste.reverse()
    for eleman in liste:
        if type(eleman) == list:
            ters_cevir(eleman)
    return liste
