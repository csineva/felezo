## 4. Feladat: Bad Word

Készíts egy python függvényt, ami egy string-et vár paraméterként.

Ha a NULLADIK vagy az ELSŐ indextől kezdődően szerepel a "bad" szó akkor irasd ki, hogy "Ez a szó rossz", ha nem
szerepel akkor irasd ki, hogy "Ez a szó jó".

Pl:
badweather -> "Ez a szó rossz",

xbadclown -> "Ez a szó rossz",

yybadweather -> "Ez a szó jó".

Ezekre a szavakra tesztelj:
- badmonkey 
- xbadweather 
- catdog 
- mousebad

### Tanácsok a megoldáshoz:

* Fontos, hogy függvényt használj!
* Fontos, hogy ne triviális megoldást adj be (a fenti szavakra működik csak, de ha egy másik tesztadattal próbáljuk, arra
  nem működik).
* Ne gondold túl!
* Nem kell például szélsőséges paraméter értékekre vizsgálatokat írni. Működjön a példákra és a példákhoz hasonó bemenő
  paraméterekre.
* Bármilyen megoldás, ami a fenti tesztadatokra (és hasonló tesztadatokra) a helyes megoldást adja tökéletesen megfelel.


### A megoldás beadása

* a megoldásokat a `testproject` mappába tedd, `feladat4_bad_word.py` néven
* a lokálisan kidolgozott megoldásodat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a legjobb szintaktikai praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne teljesen biztos, mert részpontokat ér a tárgyhoz kötődő mindennemű kód beadása
* a megoldás fájlba írjál kommenteket, amiben magyarázod a megírt kódodat (ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod)
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(