# esovizgyujtes
Tetőről megérkező esővíz gyűjtés és fogyasztás számolás

Az esővízgyűjtés méretezésénél az éves csapadékmennyiség nem sokat segít, mert van hogy hirtelen esik le sok, máskor meg hónapokig semmi. Ezért inkább historikus napi adatokkal számolom ki, hogy mennyi esőből mennyit tudnék félrerakni.

Megadható adatok:
- MetNet azonosító, hogy melyik város/hely adatai alapján szeretnékn dolgozni (https://www.metnet.hu/napi-adatok?sub=1)
- A gyűjtés kezdetének év-hónapjra. Mert hát ne télen kezdjük el, hiszen a fagyások miatt (azt nem figyeli a rendszer) nem megbízható adatokat kapunk.
- Azzal a tetővel lefedett terület mérete, ahonnan az esővizet gyűjtjök. (Nem a tető felülete maga, hanem amekorra területet lefed.)
- A kiváltani vágyott vízfogyasztásunk. Esővízzel leginkább locsolást és/vagy WC-k lehúzását tudjuk segíteni.
- A vízmegörző kapacitásunkat köbméterbe.
- A kezdő vízkészletet, hogy üresen kezdjük el, vagy előre csapvízzel azért feltöltjük a tartályokat.
- Be lehet állítani, hogy esős nap esetén ne számoljon fogyasztást. Ha öntözésre használjuk a vizet, akkor ez méretezésnél fontos lehetőség.
- Be lehet állítani, hgoy a fogyasztás jelentősebb része hétvégén történjen mindig. Például, ha csak hétvégenként járunk a kiskertbe, akkor ez eltolja a rendszerünket.

Ezek alapján szépen egy grafikonon bemutatja, hogy adott hónaptól egy éven keresztül miyen telítettséggel dolgozott volna a rendszerünk. Hány napon töltődött volna túl, avagy amikor nem sikerült minden vizet megmenteni. Hány száraz napunk lett volna és mekkore a száraznapok leghosszabb sora. És hogy végülis mennyi vizet kellett volna vásárolnunk, avagy mekkora lett volna a megtakarításunk. 

## FIGYELEM!
Jelenleg mivel a metnet.hu nem küld a headerben Access-Control-Allow-Origin részben infót arról, hogy mi használhatjuk, ezért átlag böngészőben nem működik az oldal. Csak akkor, ha ezt a fontos biztonsági funkciót kikapcsoljuk ideigelenesen. Például windows alatt így:
"C:\Program Files\Google\Chrome\Application\chrome.exe" --disable-web-security --user-data-dir="C:\chrome-dev"

