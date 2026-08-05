# Basic Notes

## Summary
This section covers:
- 

## Reflections
Lessions-learned after every session:
- What did I learn today?
- What still confuses me?
- Which exercises should I revisit later?

2025.11.06:
-Exercise1: how can the line broken if we are working with strings (e.g. print out long strings)
2025.11.16:
- check printing formatting (like in ex9)
- try to run the code from the terminal and not with control+F5

2026.07.24:
- Sync with Lacko

2026.07.24:
- Sync with Lacko is done.

2026.08.04:
Ahhoz, hogy gyorsan átállj először csinálnod kell egy saját branch-et, amit később bemergelünk a fő branch-re. Ez csak egy védelem, hogy ne kerüljön be akármi. A merge-öt először egy pull request fogja megelőzni, ami lényegében a review. Kb ezek a lépések:
- Belépsz a python-practice mappába, amit clone-oztunk múltkor és itt nyitsz egy powershell-t, vagy megnyitod a vs code-dal a projektet.
- Itt a terminálban először nyomatsz egy 'git fetch' vagy 'git fetch origin' parancsot, hogy updateld a git-et és látszódjanak nálad lokálban a changek, amik közben történtek a remote-on.
- Ez után 'git status', hogy lásd, el kell e fogadnod bármilyen commit-ot a nálad levő local repo-ra. Ha igen, tudsz nyomni egy 'git pull' command-ot, amivel ezeket a commitokat le is szeded.
- Mivel még a main branch-en vagy és az most már up-to-date, elágazhatsz innen. Itt egy 'git checkout -b feature/slaccer-tech/exercises_no' jellegű paranccsal leágazol erre a branch-re. Ez még csak lokálban létezik így, viszont itt most el tudod kezdeni a turkálást, ugyanabban a mappában, ahol eddig voltál, egyszerűen innen csak csinálod a changeket izomból.
- Ha megvagy a módosításokkal (ugye valami olyasmit dumáltunk h mondjuk a basic_exercises.py fájlban csak adogatod feladatonként hozzá a függvényeket, feladat nevébe pedig valahogy bevarázsolod az ID-dat), akkor jön a móka. Beteszed ezeket egy commit-ba valamilyen commentel, ezt nyugodtan a VS code-ból.
- Majd jöhet egy 'git push'. Itt ha még csak local-ban van branch-ed (első alkalommal pl), súg valami commandot, hogy hogyan lehet a remote-on is létrehozni a branch-et. Ezt majd csinálhatjuk együtt, de ugyanazzal a 'feature/ID/...' jellegű névvel létre lehet ezeket hozni, majd később ez a remote-on levő kap egy 'origin/' előtagot, ha direktbe ezt kell hivatkozni.
- A github felületén pedig megjelenik ekkor a change, illetve első alkalommal majd a branch-ed. Itt a github felületén lehet nyitni Pull Request-et (PR). Ekkor látod, hogy melyik branch-re kívánod majd bemergelni, illetve azt is látod, hogy hány commit-tal tér az el a tiédtől, amit szeretnél bemergelni.