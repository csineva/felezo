## 3. Feladat: Hogwards express jegyautomata

A Hogwarts express nemrég rájött, hogy érdemes lenne önkiszolgálóvá tenni a jegykiállító rendszert a hallgatók
vasútvonalán. Lehet, hogy drágák a baglyok.

Itt találod az önkiszolgáló webes applikáció prototípusát:
[https://svtesztelovizsga.blob.core.windows.net/$web/felezo-vizsga/hogwards.html](https://svtesztelovizsga.blob.core.windows.net/$web/felezo-vizsga/hogwards.html)
Készíts egy python applikációt (egy darab python file) ami selenium-ot használ.

Teszteld le, hogy az általad megadott adatokkal tölti-e ki a jegyet az applikáció. (Vigyázz, mert elkézpelhető, hogy egyes adatokat egynél több helyen is megjelenít a jegyen az applikáció!)

Nem kell negatív tesztesetet készítened. Egy-egy pozitív teszteset teljesen elég lesz.

Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!


### A megoldás beadása

* a megoldásokat a `testproject` mappába tedd, `feladat3_hogwarts.py` néven
* a lokálisan kidolgozott megoldásodat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a legjobb szintaktikai praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne teljesen biztos, mert részpontokat ér a tárgyhoz kötődő mindennemű kód beadása
* a megoldás fájlba írjál kommenteket, amiben magyarázod a megírt kódodat (ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod)
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(
