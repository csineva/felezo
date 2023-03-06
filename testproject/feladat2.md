# 2. Feladat: Sales tax applikáció funkcióinak automatizálása

Készíts egy python applikációt (egy darab python file) ami selenium-ot használ. 

A program töltse be a sales tax app-ot az [https://svtesztelovizsga.blob.core.windows.net/$web/felezo-vizsga/salestax.html](https://svtesztelovizsga.blob.core.windows.net/$web/felezo-vizsga/salestax.html) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a sales tax kalkulátort.

# Az alábbi teszteseteket fedd le:

## TC01: üres kitöltés helyessége
* Nem kell ellenőrizni, hogy üresek-e a mezők, csak azt, hogy alapból a "Subtotal" feliratú gomb megnyomásakor a "Subtotal" feliratú beviteli mezőbe 0.00 érték kerül.
* Illetve a "Calculate Order" gomb megnyomására a "Total" feliratú beviteli mező 4.95 értéket kell mutasson.

## TC02: 6" x 6" Volkanik Ice kitöltés helyessége
* Válasszuk ki a Product Item feliratú mezőből a `6" x 6" Volkanik Ice` értéket.
* A Quantity feliratú mezőbe írjunk 1-et.
* A californiai rendelésekre vonatkozó checkbox legyen bepipálva.
* Ellenőrizzük, hogy a a "Calculate Order" gomb megnyomására a `salestax` azonosítójú mező 0.43 értéket mutat-e.
* Illetve ellenőrizzük, hogy a "Total" feliratú beviteli mező pedig 10.33 értéket mutat-e.

Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!
** Az input mezők értékének kinyeréséhez a mező "value" attribútumát használd!

### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `feladat2_salestax.py` néven
* a lokálisan kidolgozott megoldásodat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a legjobb szintaktikai praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne teljesen biztos, mert részpontokat ér a tárgyhoz kötődő mindennemű kód beadása
* a megoldás fájlba írjál kommenteket, amiben magyarázod a megírt kódodat (ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod)
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(
