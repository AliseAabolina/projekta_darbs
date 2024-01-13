# projekta_darbs
## Darba uzdevuma apraksts
Ik dienu tūkstošiem cilvēku visā pasaulē iepērkas interneta veikalos, tādā veidā ietaupot savu laiku un resursus. Es bieži arī izvēlos iepirkties interneta veikalos, it īpaši apģērbu veikalos. Tomēr bieži vien pavadu vairākas stundas pie datora, meklējot piemēroto mājaslapu, kur varu atrast sev tīkamo apģērbu. 

  Šajā projektā esmu izvēlējusies tīmekļa pārlūkprogrammu automatizēšanu, ar kuras palīdzību es varu iegūt datus no interneta veikaliem par sev nepieciešamajām precēm un iegūt datus pārskatāmā veidā.
  
   Programmas mērķis ir sniegt lietotājiem iespēju ievadīt produkta nosaukumu un maksimālo cenu (budžetu), pēc kuras tiek meklēts un salīdzināts šī produkta piedāvājumus divās interneta veikala platformās "About You" un "Zalando". Rezultāti tiek saglabāti Excel datnē.


## Python bibliotēku apraksts
* import Selenium- šī ir galvenā bibliotēka programmā, tā ļauj automatizēt tīmekļa pārlūkprogrammas darbības. Selenium ir daudzas pakotnes, kuras ir arī plaši izmantotas veiktajā darbā.
  
* from selenium.webdriver.support.ui import WebDriverWait - ir viena no pakotnēm, kas liek programmai "uzgaidīt", kamēr tiek ielādēts viss lapas satur un tad tiek veiktas nākamās darbības.

* from selenium.webdriver.common.keys import Keys - šī Selenium pakotne atļauj programmai piespiest taustiņus uz klavietūras, piemēram backspace, enter u.tml.

* ActionChains no selenium.webdriver.common.action_chains: - ar šo paktoni līdzīgi kā ar "Keys", šeit var simulēt peles klikšķu darbību, piemēram, man mājaslapā bija nepieciešams lapā uzspiest uz objekta "double-click", lai objekts tiktu "iezīmēts."

* from selenium.webdriver.common.by import By - šī pakotne nodrošina, ka tiek meklēti elementi pēc kaut kādām elementa unikālajām īpašībām (HTML vidē).

* from openpyxl import Workbook, load_workbook - ar šo bibliotēku tiek veikta Excel failu nolasīšana un sagatavošana, lai ar Excel formāta failiem varētu darboties python.

* import pandas as pd - pandas tiek izmantotas, lai kodā veiktu datu vizualizāciju Excel tabulā.


## Metožu apraksts
**1. WebDriver inicializācija** 

-Šajā koda daļā tiek importēta lielākā daļa no nepieciešajām bibliotēkām un to pakotnēm.

-Kā arī tiek veikta lietotāja ievade, kurā tiks ievadīts vēlamās preces nosaukums un tās budžets.

**2.Mājaslapas atvēršana un elementu meklēšana**
Šajā un turpmākajās sadaļās kods tiek viedots divās daļās. Pirmā daļa, kur tiek automatizēta "About You" vietne un otrā daļa (kodā atzīmēta) ir vietne "Zalando". 

- Tiek veikta mājaslapas atvēršana, izmantojot "driver.get.url()"

- Abās vietnēs tiek apstiprināti "cookies" jeb sīkdatņu apstiprināšana.

- Tiek atrasts meklēšanas lauks un tajā ievadīta lietotāja ievade.

- Tiek atrasts un uzspiests cenu filtrs un piešķirta maksimālā vērtība precei, kuru lietotājs vēlas iegādāties.

- Meklēšanai tika izmantoti gan klases nosaukumi ("CLASS_NAME"), gan "CSS_SELECTORS", gan "XPATH", identifikators "ID."

- Man bija svarīgi iegūt preces nosaukumu un tās cenu.

**3.Datu iegūšana un apstrāde**
- Izmantojot maksimālo cenu, kas norādīta lietotāja ievadē, programma filtrē produktus, kas atbilst šim kritērijam.
  
- Tiek izvadīti produktu nosaukumi

- Nepieciešamie dati tiek ievietoti sarakstā
  
- Izmantojot pandas, dati tiek sakārtoti pārskatāmā veidā, tiek arī filtrēts datu saturs un atbrīvošanās no nevajadzīgiem elementiem.

**4.Datu pārveide uz Excel**
- Izmantojot Openpyxl, tiek izveidota jauna Excel datne, kurā tiks ievietoti dati

- Tiek izveidots datu formatējums tabulā (tabulas kollonu nosaukumi)

**5.Programmas beigas**
- tiek aizvērts selenium webdriver.

-  tiek izvadīts paziņojums par veiksmīgu datu pārnesi uz Excel datni.




