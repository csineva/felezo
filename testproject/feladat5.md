## 5. Feladat: Listből List!

Készíts egy Python függvényt, ami egy listát és egy pozitív egész számot vár paraméterként.

Készíts egy új listát, aminek az elemei az eredeti lista azon számai, amik oszthatóak az adott pozitív egész számmal
maradék nélkül.

Az új listával **térjen vissza** a függvény. A Python programod hívja is meg a függvényt a lentebb található
tesztesetekkel és jelenítsd meg a terminálon a visszakapott lista elemeit.

Pl:   
function_name([1, 2, 3, 4, 5, 6], 2) => [2, 4, 6])

function_name([1, 2, 3, 4, 5, 6], 3) => [3,6])

Ezekre tesztelj (legyen meghívva a függvény ezekkel az adatokkal):

- [2,3,4,5,6,7,8], 4 => [4,8]
- [2,3,4,5,6,7,8], 3 => [3,6]
- [2,3,4,5,6,7,8,9,10], 5 => [5,10]

### Tanácsok a megoldáshoz:

* Fontos, hogy függvényt használj!
* Ne gondold túl!
* Nem kell például szélsőséges paraméter értékekre vizsgálatokat írni. Működjön a példákra, és a példákhoz hasonó bemenő
  paraméterekre.
* Bármilyen megoldás, ami a fenti tesztadatokra (és hasonló tesztadatokra) a helyes megoldást adja tökéletesen megfelel


### A megoldás beadása

* a megoldásokat a `testproject` mappába tedd, `feladat5_listcheck.py` néven
* a lokálisan kidolgozott megoldásodat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a legjobb szintaktikai praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne teljesen biztos, mert részpontokat ér a tárgyhoz kötődő mindennemű kód beadása
* a megoldás fájlba írjál kommenteket, amiben magyarázod a megírt kódodat (ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod)
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(