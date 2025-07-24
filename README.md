# Coinflip over the phone

### Projektbeschreibung
Das Projektziel besteht darin, eine faire und sichere Methode für das Durchführen eines Münzwurfs zu entwickeln, bei der die beteiligten Personen sich nicht gegenseitig beobachten können.

Problem:
- Alice und Bob wollen beide die selbe Aufgabe machen
- Jedoch kann die Aufgabe nur von maximal einer Person gewählt werden
- Alice und Bob einigen sich darauf eine Münze zu werfen
- Durch Corona-Beschränkungen dürfen Alice und Bob sich nicht treffen


### Ansatz
Unser Ansatz sieht vor, eine Hashfunktion mit einem zweistufigen zufälligen Padding zu verwenden, um ein Zero-Knowledge-Protokoll zu implementieren.
Dafür werden auf der Clientseite zwei Python-Skripte verwendet, und die Kommunikation zwischen den Clients soll per E-Mail erfolgen. Eine grafische Benutzeroberfläche (UI) wird den Benutzern die erforderlichen Interaktionen ermöglichen und eine einfache sowie schnelle Nutzererfahrung bieten. Zusätzlich zu den eigentlichen Daten für den Münzwurf werden auch Logdaten/Protokolldaten erhoben und ausgetauscht, um den Nutzern eine gewisse Transparenz zu gewährleisten.


### Arbeitspakete:
- **AP1:** Festlegung eines Vorgehens und Aufgabenverteilung
- **AP2:** Dokumentation: Erstellung und Pflege von Präsentation, GitHub usw.
- **AP3:** Entwicklung der Benutzeroberfläche (UI)
- **AP4:** Implementierung der Hashfunktion
- **AP5:** Implementierung der E-Mail-Übertragung
- **AP6:** Implementierung von Logdaten
- **AP7:** Integration der Bausteine
- **AP8:** Durchführung von Anwendungstests
- **AP9:** Erstellung eines Benutzerhandbuchs
- **AP10:** Durchführung der Abschlusspräsentation



### Tools
- Sprache: Python
- Übertragung: E-Mails (smtplib + MIMEText)


### Zeitplan/Meilensteine
Meetings Sonntag 16 Uhr Zoom

| Datum  | Aufgabe                                               |
|--------|-------------------------------------------------------|
| 26.5.  | Gruppenorganisation / Neuorganisation                 |
| 28.5.  | Präsentation mit Anwendungsdiagramm                     |
| 9.6.   | AP3, AP4, AP5, AP6                 |
| 16.6.  | Arbeitspakete zusammenfügen (AP7)                  |
| 23.6.  | Qualitätssicherung (QA) (AP8)                          |
| 30.6.  | Puffer                                                |


## Libraries

smtplib + MIMEText

## Informationen und Links
Folien: 
https://docs.google.com/presentation/d/1jhJto1Lg3mN5KdeO4-RpBr2azkh84hl-BWB__PQs9D4/edit?usp=sharing

Abschlusspräsentation:
https://docs.google.com/presentation/d/1wrlrA9bhwajSp36e3IZHWxsz65wk13IxhTzA7fFNfXE/edit?usp=sharing


  
## Vorlesungsfolien:
- Zero Knowledge Proofs: https://iuk.one/1033-1211.pdf
- Aufgabenstellung: https://iuk.one/1033-2023.pdf
