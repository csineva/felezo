## 1. Feladat: Kalkulátor automatizálása

Készíts egy python applikációt (egy darab python file) ami selenium-ot használ. 

A program töltse be a bmi kalkulátor app-ot az [https://svtesztelovizsga.blob.core.windows.net/$web/felezo-vizsga/bmi.html](https://svtesztelovizsga.blob.core.windows.net/$web/felezo-vizsga/bmi.html) oldalról. 

Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a kalkulátorban:

Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!

Underweight:
* height: 171 cm
* weight: 45 kg
* Elvárt értékek:
    * Your BMI is: 15
    * This means you are: Underweight

Normal:
* height: 185 cm
* weight: 65 kg
* Elvárt értékek:
    * Your BMI is: 19
    * This means you are: Normal


### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `feladat1_bmi.py` néven
* a lokálisan kidolgozott megoldásodat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a legjobb szintaktikai praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne teljesen biztos, mert részpontokat ér a tárgyhoz kötődő mindennemű kód beadása
* a megoldás fájlba írjál kommenteket, amiben magyarázod a megírt kódodat (ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod)
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(
