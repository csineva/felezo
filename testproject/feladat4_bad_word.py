# Készíts egy python függvényt, ami egy string-et vár paraméterként.
# Ha a NULLADIK vagy az ELSŐ indextől kezdődően szerepel a "bad" szó akkor irasd ki, hogy "Ez a szó rossz",
# ha nem szerepel akkor irasd ki, hogy "Ez a szó jó".
#
# Pl: badweather -> "Ez a szó rossz",
# xbadclown -> "Ez a szó rossz",
# yybadweather -> "Ez a szó jó".
#
# Ezekre a szavakra tesztelj:
# badmonkey
# xbadweather
# catdog
# mousebad

def bad_word(word: str):
    if word[:3] == 'bad' or word[
                            1:4] == 'bad':  # a string slice segítségével megvizsgáljuk, hogy az adott rész-stringek megegyezek-e a 'bad' stringgel
        print(f'{word} -> Ez a szó rossz')  # majd kiírjuk a konzolra az eredménytől függő üzenetet
    else:
        print(f'{word} -> Ez a szó jó')


bad_word('badmonkey')
bad_word('xbadweather')
bad_word('catdog')
bad_word('mousebad')
