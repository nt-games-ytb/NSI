# Changelog Filius

## [1.12.5] - 2021-09-01
### Fixed
 * Templates for new applications work now with the new log framework
 
## [1.12.4] - 2021-05-01
### Changed
 * Log can now be enabled for stdout

### Fixed
 * Z layer of components in design mode fixed.
 * Vhosts for web server will be persisted again.
 
## [1.12.3] - 2021-05-01
### Changed
 * Use now SLF4J and Logback for logging

### Fixed
 * Error when reading old Filius files because of non-compliant version strings fixed
 * Fixed wrong data in data exchange detail section caused be shallow frame copies

## [1.12.2] - 2021-04-26
### Fixed
* Fix exception after one node was deleted

## [1.12.1] - 2021-04-25
### Fixed
* Fix command line arg handling (some combinations were not possible)
* Fix spaces in filename when starting via command line under linux
* Ensure that during visual alignment of components in design mode, the dragged component is always in foreground

## [1.12.0] - 2021-04-10
### Added
 * Detailed license information added
 * Report contains now the forwarding table of network nodes and - if available - DNS server configuration
 * Provide an installer with bundled JRE for Windows
 
### Changed
 * IP addresses for router config as well as forwarding table entries are now validated after input
 * SEQ and ACK numbers are now initialized with trailing zeros and formatted as decimal numbers for better readability

### Fixed
 * Version comparison (only visible in log output)
 * Filius can know be installed in directories that contain '+' or '$'
 * SEQ number is now incremented after FIN reception
 * Help contents are now available from the start

## [1.11.0] - 2021-01-23
### Added
 * The personal firewall supports now filtering of UDP traffic.
 * Build and Code Signing with AppVeyor and SignPath.
 
### Changed
 * The default behavior of the firewall is activated UDP traffic filtering, i.e., UDP packets (e.g. DNS) will be discarded.
 * Windows/dialogs are mostly resizable, e.g. application windows on the virtual desktops.
 * Added readme file to be shown at Gitlab.
 
### Fixed
 * When Filius was opened on a secondary monitor that is not available any more, the Filius window will be located onto a visible monitor when starting next time.
 * Within the terminal application the cd command could be used with a file. Now it is only available for directories.
 * Use URI encode and decode for URLs.
 * Do not allow domain names that start with digits.

## [1.10.4] - 2020-11-29
### Fixed
* There was an incompatibility within Report generation on Java 8.
* It was not possible to generate a report of unsaved scenarios.
* The contents of the help dialog were editable.

## [1.10.3] - 2020-08-16
### Fixed
* Manually configured DHCP settings for gateway and dns server were not persisted if they were equal to the os settings.

## [1.10.2] - 2020-07-29
### Fixed
 * Fix bug when loading old project files with documentation elements

### Changed
 * Reduce corner radius of document elements
 * Use secured Filius homepage URL (https)

## [1.10.1] - 2020-07-18
### Fixed
 * Silent Uninstall for Windows
 * Use secured Filius homepage URL (https)

### Changed
 * Default install folder under Windows is now C:\Program Files\Filius

## [1.10.0] - 2020-06-14
### Fixed
 * Uebersetzung zur Simulationsgeschwindigkeit korrigiert
 * Falsche Nummerierung Abschnittsueberschriften im Report behoben
 * Fehlerbehebung zur Erstellung von Kabelverbindungen
 * Korrektur Rechtschreibung in franzoesischer Uebersetzung
 * Korrektur der kaputten Anzeige fuer Terminal-Anwendung
 * Fehlerbehebung im Einfachen Client: Immer auf eingehende Nachrichten warten (auch ohne Versand einer Nachricht)

### Changed
 * Abschnitt zum Nachrichtenaustausch im Report nur, wenn Inhalte vorliegen
 * Redaktionelle Ueberarbeitung der Hilfeseiten 
 * Grundlegende Ueberarbeitung Dokumentationsmodus mit Formatierungsmoeglichkeiten

### Added
 * Möglichkeit, Reiter zum Nachrichtenaustausch zu schliessen
 * Wiederherstellen der angezeigten Fenster bei Wechsel zwischen Anwendungsmodi
 * Hilfeseite für Dokumentationsmodus hinzugefügt

## [1.9.0] - 2020-05-02
### Fixed
 * Fehlerbehebung im Einfachen Client: Auf Serverantworten erst nach Versand einer Nachricht warten
 * Fehlerbehebung TCP-Server: Sockets beim anhalten des Servers gemaess Spezifikation zum Verbindungsabbau schliessen
 * Fehlerbehebung: Sockets im Zustand CLOSED immer aus Socket-Liste entfernen
 * Fehlerbehebung: Versand leerer Nachrichten ermoeglichen (war die Nachricht leer, wurde nichts gesendet)
 * Fehlerbehebung: Netstat zeigt jetzt auch serverseitig die Verbindungen an
 * Fehlerbehebung: Der Befehl cat fuer eine nicht vorhandene Datei fuehrte zu einem Fehler
 * Fehlerbehebung: TCP-Socket-Zeitueberschreitungen wurden nicht korrekt verarbeitet
 * Fehlerbehebung: Die Sequenznummern in TCP wurden falsch hochgezaehlt

### Changed
 * Verbesserung Source Address Table (SAT): Fenster mit SAT werden nicht mehr mehrfach geoeffnet und automatisch aktualisiert
 * Verbesserung: Netstat zeigt jetzt lokale und entfernte Adresse mit IP-Adresse und Port an
 
### Added
 * Verbesserung: Gnutella ermoeglicht jetzt das Zuruecksetzen der bekannten Peers
 * Export der Konfiguration und des Datenaustauschs als PDF-Datei

## [1.8.2] - 2020-04-21
  * Fehlerbehebung Modem: Verklemmung, wenn beide verbundenen Modems in gleicher Filius-Instanz laufen

## [1.8.1] - 2020-02-01
  * Korrekturen zur franzoesischen Typographie
  * Internationalisierung "Netzwerk" in Gnutella
 
## [1.8.0] - 2020-01-20
  * Export aus Dokumentationsmodus als SVG moeglich (zusaetzlich zu PNG)
  * Hinweis/Tooltip zur Einstellung der Simulationsgeschwindigkeit
  * Fehlerbehebung zur Anzeige/Aktualisierung des Modemnamens
  * Verschiedene Fehler im Dokumentationsmodus behoben
  * Korrektur zum Verschieben von mehreren Elementen im Entwurfsmodus 
 
## [1.7.4] - 2019-01-08
  * Sprache Franzoesisch hinzugefuegt (Uebersetzung durch Patrice Treton)
  * Fehlerkorrekturen I18n
  * Software-Assistent wird in Vorgabeeinstellung immer angezeigt

## [1.7.3] - 2018-08-21
  * Abhängigkeit zu Java 8 in Windows-Version korrigiert

## [1.7.2] - 2016-02-07
  * Konfigurierbare Groesse der Arbeitsflaeche zum Aufbau der Rechnernetze (konfigurierbar in filius.ini)
  * Fehlerbehebung: Fenstergroesse fuer E-Mail Verfassen so angepasst, dass es auch unter Mac OS funktioniert
  * Fehlerbehebung: Anhalten einer Server-Anwendung gibt den Port frei, der fuer den Serversocket verwendet wurde

## [1.7.1] - 2016-02-03
  * Fehlerbehebung: Sprachselektion bei erstmaligem Starten wieder aktiviert
 
## [1.7.0] - 2016-01-30
  * Neues Windowsinstallationsprogramm
  * Systemvoraussetzung Java 8
  * Aufrufparameter 'verbose' ergaenzt
  * Grundlegende Ueberarbeitung DHCP
  * DHCP unterstuetzt jetzt statisch zugewiesene IP-Adressen
  * Der Software-Assistent steht jetzt nicht mehr zwingend zur Verfuegung (abhaengig von JDK/JRE und Konfiguration)
  * Im Dateidialog zum Oeffnen eines neuen Projekts ist jetzt das zuletzt verwendete Verzeichnis vorselektiert
  * Webserver erlaubt jetzt auch unbekannte Dateiendungen (Versand als text/plain) und erkennt Endung .htm auch als HTML
  * Fehlerbehebung: Anwendung fuer Dateiaustausch (P2P) und Webserver funktioniert jetzt auch mit Leerzeichen in Dateinamen
  * Fehlerbehebung: Mehrere DHCP-Server können jetzt im gleichen Rechnernetz vorhanden sein
  * Fehlerbehebung: Selektion bei Löschen vorhandener Kabel korrigiert
  * Fehlerbehebung: Validierung E-Mail-Adressen korrigiert (Reg. Ausdruck angepasst)
  * Fehlerbehebung: DHCP funktioniert jetzt auch, wenn zwischendurch das Projekt gewechselt wurde
  * Fehlerbehebung: Wenn ein Projekt ohne Dateiendung gespeichert wird, werden jetzt auch die Textelemente mit gespeichert
  
## [1.6.1]
  * Fehlerbehebung: Fehlerhafte Bestimmung von IP-Adressen als Broadcast behoben
  * Fehlerbehebung: TTL wird jetzt nicht mehr fuer lokal adressierte Pakete dekrementiert
  * Verbesserung des Datenaustauschprotokolls als Textdatei

## [1.6]
  * Fehlerbehebung: Robustere Eingabe der Rechnerkonfiguration
  * Fehlerbehebung: Verbindungsherstellung/-trennung mit Modem stabiler realisiert
  * Ausgabe einer Fehlermeldung, wenn ein Broadcast-Ping ausgefuehrt werden soll
  * Fehlerbehebung: Knoten konnten u.U. nicht mehr selektiert werden, wenn sie durch Beschreibungselemente ueberlagert wurden
  * Fehlerbehebung: Ping-Fehler behoben
  * Konfiguration der Knoten als Tooltip in der Netzwerkansicht
  * Export des Nachrichtenaustauschs als einfache Textdatei
  * Maximale Anzahl von Verbindungen zu Switch (von 8) auf 24 erhoeht
  * Fehlerbehebung: TTL wird jetzt korrekt inkrementiert

## [1.5.4]
  * Fehlerbehebung: Inkompatibilität beim Oeffnen von Projektdateien, die mit aelterer Version erstellt wurden, behoben
  * Fehlerbehebung: Kabelwerkzeug wurde an falscher Position angezeigt, wenn Arbeitsbereich per Schieber verschoben wurde
  * Fehlerbehebung: Absender und Empfaenger einer Mail wurde nicht in Projektdatei gespeichert
  * Fehlerbehebung: ARP-Anfrage wurde mehrfach versendet
  * Fehlerbehebung: Dokumentationselemente wurden bei Oeffnen eines neuen Projekts (erstellt mit aelterer Version) nicht immer entfernt
  * Fehlerbehebung: Loeschen gesendeter Mails war nicht mehr moeglich
  * Fehlerbehebung: POP3-Server hat nicht immer geantwortet

## [1.5.3] - 2013-11-07
  * Moeglichkeit, Textfelder und Strukturierungsfelder einzufuegen
  * Exportieren der Netzansicht als PNG moeglich
  * Bounce-Mails bei nicht erreichbaren Empfaengern
  * Reduzierung der Schnittstellen eines Vermittlungsrechners ist jetzt moeglich
  * IP-Adresse der Vermittlungsrechner-Schnittstellen werden jetzt als Reitertitel verwendet
  * Fehlerbehebung: leere Ordner-/Dateinamen möglich -> Datei-Explorer Fehlfunktion
  * Fehlerbehebung: Linux-Startskript ohne 'realpath'
  * Fehlerbehebung: mehrere E-Mail-Benutzerkonten in E-Mail-Anwendung möglich
  * Fehlerbehebung: einzelne Nachrichten wurden bei Wechsel zwischen Entwurfs- und Aktionsmodus wiederholt verarbeitet 

## [1.5.2] - 2013-07-05
  * Umbenennung "Terminal" zu "Befehlszeile"/"Command line"
  * Neue Befehlszeilenwerkzeuge: arp, cat
  * Synchronisation von Dateiinhalten mit Anzeige im Texteditor (insbesondere für E-Mail- und DNS-Server)
  * Validierung von DNS-Server-Konfigurationseingaben und Hinweise bei falscher Eingabe
  * DNS-Server-Konfiguration in Tabellen editierbar

## [1.5.1] - 2013-02-13
  * Kleine Fehlerbehebungen

## [1.5] - 2013-02-03
  * Firewall grundlegend ueberarbeitet (Firewall-Konfiguration in Projektdateien nicht kompatibel mit aelteren Versionen)
  * Neuer Nachrichtendialog (alter Nachrichtendialog in filius.ini aktivierbar)
  * Im Entwurfsmodus: erstellen mehrerer Kabelverbindungen mit einmaliger Selektion des Kabelwerkzeugs moeglich
  * Anzahl der Pings ueber Kommandozeile wieder auf vier reduziert (Anpassung ueber filius.ini moeglich)
  * Fehlerhafte Anzeige des Icons eines Vermittlungsrechners in Abhaengigkeit des Verbindungsstatus behoben
  
## [1.4.5.3] - 2012-11-25
  * Fehler zu DNS-Server bei schnellem Wechsel Starten/Beenden
  * Fehler zu ICMP (ping/traceroute) behoben

## [1.4.5.2] - 2012-11-12
  * Fehlerbehebung: Ping zu Vermittlungsrechner funktionierte nicht fuer alle Schnittstellen

## [1.4.5.1] - 2012-11-11
  * Fehlerbehebung: Fortschrittsanzeige bei Mail-Abruf wurde nicht mehr ausgeblendet und Mails nicht vollstaendig angezeigt
  * Fehlerbehebung: Durch die rekursive DNS-Namensaufloesung muss die zeitliche Begrenzung des Resolvers auf ein vielfaches der maximalen Round-Trip-Time betragen

## [1.4.5] - 2012-11-04
  * Domainserver unterstuetzen als Option rekursive Domainnamensaufloesung.
  * Re-Integration eines Forks (Dank an pyropeter)
    - erweitertes ICMP
    - im Terminal: Befehlshistorie, Traceroute, Abbruch mit <Strg>+C
    - Vermittlungsrechner koennen jetzt automatisch konfiguriert werden (mit RIP als Routing-Protokoll)
    - Modem: automatischer Wiederaufbau einer unterbrochenen Verbindung
  * Der Webserver des Vermittlungsrechner ermöglicht die Abfrage der aktuellen Weiterleitungstabelle.
  * Vermittlungsrechner-Firewall:
    - kann jetzt alle Versuche eines TCP-Verbindungsaufbaus ablehnen.
    - Absender- und Empfaenger-Regeln gelten nur noch fuer TCP (nicht mehr fuer UPD)
  * Als Rechnername kann jetzt die IP-Adresse verwendet werden.

## [1.4.4] - 2012-03-13
  * Domain Name System: Jetzt kann auch ein Resource Record fuer einen Wurzel-Name-Server konfiguriert werden.
  * Web-Server: Ueberarbeitung des Designs der Vorgabe-Webseite
  * Kleinere Anpassungen der Darstellungen (u.a. Umbenennung des "Echo-Client" zu "Einfacher Client")
  * Programmkonfiguration: 
    - Grundlegende Einstellungen zur Anzeige und Ausfuehrung koennen jetzt als Aufrufparameter oder mit einer Ini-Datei konfiguriert werden.
    - RTT kann jetzt nicht mehr ueber Menue sondern nur noch als Aufrufparameter bzw. per Ini-Datei geaendert werden.
  * Fehlerbehebungen: 
    - Nachrichten des POP3-Servers werden im Log-Fenster angezeigt
    - Flag fuer manuelle Einstellungen des DHCP-Servers wird persistiert
    - Schnittstellenverwaltung der Vermittlungsrechner bei angeschlossenem Switch fuehrte zum Programmabbruch
    - Anzeige des Kontextmenue fuer Kabel im Aktionsmodus wurde nicht unterdrueckt

## [1.4.3] - 2011-11-10
  * Domain Name System: Das DNS erlaubt jetzt rekursive Abfragen zur Aufloesung eines Domainnamens.
  * Webserver: Die optionale Konfiguration der virtuellen Hosts kann jetzt ausgeblendet werden.
  * Firewall: Die Firewall der Vermittlungsrechner kann jetzt dezidiert fuer die Netzwerkschnittstellen aktiviert werden.
  * Kommandozeile: Hier steht jetzt zusaetzlich der Befehl netstat zur Anzeige aktiver Verbindungen zur Verfuegung.
  * In Textfeldern steht jetzt die Tastenfunktion <Strg>+a zur Verfuegung.
  * Fehlerbehebung:
    - Netzwerkschnittstellenkonfiguration Vermittlungsrechner: Jetzt wird die richtige IP-Adresse eines verbundenen Vermittlungsrechners angezeigt.
    - Datenaustausch ueber Vermittlungsrechner: Wenn Standardgateway nicht gesetzt wurde, erfolgt jetzt korrekte Ausnahmebehandlung.

## [1.4.2] - 2011-09-15
  * Fehler bei Aufruf mit Parameter "-wd" zur expliziten Auswahl des Arbeitsverzeichnisses behoben

## [1.4.1] - 2011-09-01
  * Fehler bei Aenderung des Aufbaus behoben
  * TCP-Timeout-Fehlermeldung erfolgt nicht mehr im Konfigurationsmodus
  * Fehlerhafte Modemfunktionalität korrigiert

## [1.4] - 2011-08-07
  * Fehlerbehebung: 
    - Bildbetrachter: Anzeige von Bildern wieder möglich 
    - E-Mail-Programm: Platzhaltergrafik für Nachrichten wird wieder angezeigt
    - Webserver: Anzeige leerer Eingabefelder in Oberfläche (statt "null")
    - DNS-Server: Synchronisation zwischen Oberfläche und Konfigurationstextdatei
    - Gnutella: Fehler bei Dateiübertragung behoben
    - E-Mail-Server: Robustere Verarbeitung von E-Mails durch SMTP-Server
    - Switch: Die Darstellung als Wolke kann auch wieder rückgängig gemacht werden
    - Programmstart: Fehler bei Prüfung der Schreibrechte auf Benutzerverzeichnis unter Windows behoben
    - Info-Dialog: Alle Angaben werden wieder vollständig angezeigt (unter Linux)
    - Nachrichtenansicht: Löschen der Tabelleninhalte korrigiert
  * Echo-Client: Jetzt können hierüber E-Mails versendet (SMTP) und abgerufen (POP3) werden.
  * Rechnerkonfiguration: Jetzt können Gateway- und DNS-Server-Adressen wieder entfernt werden.
  * Nachrichtenansicht: Jetzt steht eine Option "automatisches Scrollen" über Kontextmenü zur Verfügung und das Dialogfenster bleibt immer im Vordergrund.

## [1.3.1.4] - 2011-04-30
  * Verwendung von Java Native Access zur korrekten Ermittlung von Benutzerverzeichnissen unter MS Windows (vgl. Java Bug #4787931: http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=4787931
  * Kontrolle bei Programmstart, ob Arbeitspfad schreibbar ist. Schreibrechte sind notwendig für Dateioperationen wie Speichern/Laden von Szenarien)
  * bei fehlenden Schreibrechten wird sofort Dialog angezeigt zur manuellen Korrektur durch den Benutzer, d.h. Auswahl eines anderen Verzeichnisses

## [1.3.1.3] - 2011-01-30
  * kleine Bugfixes
  * Problem bei Ping-Nachrichten (v.a. Modem betroffen) behoben
  * Darstellungsmöglichkeit von Switches als Netzwerkwolken (identische Funktionalität wie Switch, lediglich Erscheinung aus didaktischen Gründen verändert!) [Rücknahme: - fehlerhaftes Verhalten bei Problemen mit Log-Datei behoben]
 
## [1.3.1.2] - 2010-11-08
  * kleinere Bugfixes
  * verbesserte Log-Daten-Aufzeichnung (aussagekräftigere Auflistung der relevanten hashCodes zur Verfolgung von Aktivitäten)
  * Platzieren der Log-Datei in Arbeitsverzeichnis (.filius) statt in Ort des Startens der Anwendung wegen Rechteproblemen bei Betriebssystem

## [1.3.1.1] - 2010-09-20
  * Bugfix bei IP Adressevaluation; Zahlenbereich war begrenzt durch Fehler in Regulärem Ausdruck

## [1.3.1] - 2010-08-04
  * E-Mail-System überarbeitet; bessere Darstellung im Mailprogramm
  * Antwortfunktion bei Mailprogramm korrigiert
  * Fehler bei Mailverwaltung im Server korrigiert, u.a. beim Löschen abgerufener Mails
  * Scrollpane eingefügt in Mailprogramm (Mailbetrachter) und TextEditor
  * variable Einstellungen für maximale RTT (NOTE: die Simulation wird dadurch nicht verlangsamt, sondern lediglich die Toleranz bzgl. Timeouts wird vergrößert; das ist sinnvoll für langsamere Systeme)
  * Erweiterung des Webservers um virtuelle Hosts
  * Bugfixes z.B. bei Graphikeinbindung
  * Startup-Skript für Mac OS X hinzugefügt; Tests auf Mac OS X erfolgreich

## [1.3.0.4] - 2010-07-07
  * Hinzufügen eines Startup-Skripts für UNIX-basierte Systeme (Filius.sh)
  * Parameterunterstützung zur Verlegung des Arbeitsverzeichnisses ".filius": '-wd <path>'
  * Überprüfung der DNS-Einträge; falls URL leer wird Eintrag nicht übernommen/gespeichert
  * Fehlplatzierung bei Kabel behoben
  * Kontextmenü zum Löschen von Kabeln an engeren Kollisionsbereich gebunden
  * Kontextmenü zum Löschen von Kabeln nur angezeigt, falls keine Kabelvorschau aktiv

## [1.3.0.3] - 2010-04-19
  * Fehler bei der direkten Bearbeitung von DNS-Einträgen in der Tabelle korrigiert
  * Daten werden nun getrennt nach A bzw. MX Einträgen verarbeitet (JTableEditable)
  * Pfadunstimmigkeiten bei Hilfe-Dateien (bei Aufruf der Jar-Datei aus anderem Verzeichnis) beseitigt

## [1.3.0.2] - 2010-04-15
  * Bilder in JAR-Datei integriert
  * Korrektur der Pfadzuweisungen, um Dateien innerhalb der JAR-Datei zu finden
  * Fehler bei Suche von FLS-Datei als Parameter beseitigt
  * Fehler bei Pfadbestimmung korrigiert, damit Filius von beliebiger Stelle aus aufgerufen werden kann (betrifft JAR und EXE!)

## [1.3.0.1] - 2010-04-09
  * Datei-Explorer importiert beliebige Dateien bis zu einer Größe von 150KB
  * bei fehlgeschlagener DHCP-Anfrage werden Zeroconf-Adressen zugewiesen (169.254.x.x)
  * ping-Befehl wurde in Befehlsliste bei Terminal aufgenommen
  * Überschrift für Tabellenausgabe bei route-Befehl

## [1.3.0] - 2010-03-31
  * Terminal-Funktionen implementiert (move, copy, dir, help, ...)
  * Hilfeseite zur Auflistung aller unterstützter Terminal-Befehle
  * Ping-Befehl implementiert in Terminal
  * Tool zur Namensauflösung direkt über Terminal ('host')
  * Tastenkombinationen zur Steurung der Menüfunktionen (Strg+<?>) + Auswahl Kabel (Alt-1)
  * konsequentes Loggen in Datei möglich für Fehlersuche; Debug-Ausgaben vereinheitlicht
  * DHCP kann DNS/Gateway abweichend von Server-Einstellungen vergeben
  * DNS-Einträge auch änderbar in DNS-Server (statt nur Löschen/Neuanlegen)
  * einzelne Kabel können entfernt werden
  * Fehler durch sich blockierende nebenläufige Prozesse beseitigt (Threads haben aufeinander gewartet; Race Conditions bei Prüfung von Queues)
  * deutliche Reduktion von Ausnahmefehlern (Exceptions oftmals für Testzwecke auf mögliche Probleme genutzt. Lässt sich jedoch durch vorherige Prüfung fast durchgängig vermeiden!)
  * Terminal-Funktionen waren nur angedeutet, jedoch nicht implementiert
  * Knoten können nun nicht mehr aus Arbeitsfläche herausgezogen werden (war vorher möglich; leider dann aber keine Möglichkeit mehr, diese in den Sichtbereich zurückzuholen)
  * manche Dialoge wurden zu Singleton umfunktioniert (nur noch ein Dialog)
  * Darstellung/Einsehen der MAC-Adressen einfacher möglich
  * MX Eintrag bei DNS-Server unterstützt nun auch IP-Adressen, statt nur URLs
  * Ethernet akzeptiert nun nur noch Pakete, wenn Kabel physisch mit betrachteter Netzwerkkarte verbunden ist (vorher: bei Vermittlungsrechner Pakete aller NICs verarbeitet)
  * warten auf DHCP Server bei Wechsel zu Simulationsmodus, erst dann DHCP Anfragen möglich
  * Überschriften in diversen Dialogen zur besseren Usability
  * fehlerhafte Pattern für IP-Adressen korrigiert
  * Sprache bei Buttons in Dialogen korrigiert