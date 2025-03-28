# HelpNDoc TOC Generator from Microsoft HTML Workshop (.hhc)

Dieses Projekt zeigt, wie man aus einer Microsoft HTML Help Workshop `.hhc`-Datei ein automatisch einlesbares Inhaltsverzeichnis (TOC) für [HelpNDoc](https://www.helpndoc.com) erzeugt. Es besteht aus einem getesteten Workflow zur Erstellung eines Pascal-Skripts, das direkt im HelpNDoc-Skript-Editor verwendet werden kann.

---

## 🎓 Ziel

- Automatisches Parsen einer `.hhc`-Datei (HTML Help Contents)
- Extraktion von Themen-Titeln und ihrer Hierarchieebene
- Automatische Generierung eines Pascal-Skripts für HelpNDoc
- Einrückung der Themen gemäß Ebenentiefe (Level)
- Einbindung einer HTML-Vorlagendatei in jedes erstellte Thema

---

## 🔧 Projektstruktur

| Datei                | Beschreibung |
|----------------------|--------------|
| `toc.hhc`            | Ursprüngliche HTML Help Workshop Inhaltsverzeichnisdatei |
| `template.htm`       | HTML-Vorlagendatei, die als Inhalt in jedes HelpNDoc-Thema eingefügt wird |
| `hhc_to_helpndoc.py` | Python-Skript, das `toc.hhc` parst und ein Pascal-Skript erzeugt |
| `helpndoc.pas`       | Generiertes HelpNDoc-Pascal-Skript zur Ausführung im Skript-Editor |

---

## 💡 Funktionsweise

1. `hhc_to_helpndoc.py` liest die `.hhc`-Datei mit **BeautifulSoup** ein
2. Alle `<object>`-Elemente mit `param name="Name"` werden extrahiert
3. Die Tiefe wird durch Zählen der Nummerierung (z. B. `1.1.1`) erkannt
4. Ein Pascal-Skript wird erzeugt, das:
   - Themen via `HndTopics.CreateTopic` erstellt
   - Titel via `HndTopics.SetTopicCaption` setzt
   - Inhalte aus `template.htm` einbindet
   - Themen per `HndTopics.MoveTopicRight` korrekt einrückt

---

## 📄 Beispiel eines generierten Themas (Pascal)

```pascal
Thema.TopicID := HndTopics.CreateTopic;
HndTopics.SetTopicCaption(Thema.TopicID, 'Kapitel 1.1.2');
for j := 1 to Thema.Level do
  HndTopics.MoveTopicRight(Thema.TopicID);
HndTopics.SetTopicContent(Thema.TopicID, Editor.Text);
```

---

## ⚖️ Voraussetzungen

- Python 3.x
- `beautifulsoup4` (installierbar per `pip install beautifulsoup4`)
- [HelpNDoc](https://www.helpndoc.com) ab Version 9.7 mit Pascal-Skript-Editor

---

## 🌐 Veröffentlichung / Lizenz

Dieses Projekt wurde von einem Entwickler getestet und freigegeben, um anderen HelpNDoc-Anwendern das schnelle Generieren von TOC-Strukturen zu ermöglichen. Es kann gerne weitergegeben, angepasst und verbessert werden.

> Autor: paule32  
> E-Mail: paule32.jk@gmail.com  
> Lizenz: MIT License

---

## 🚀 Nächste Schritte

- Integration in CI-Tools oder als Build-Script
- Anbindung an bestehende Dokumentationsgeneratoren
- Verwendung mehrerer Templates je nach Themenebene

---

## 💬 Hinweis zu HelpNDoc-Versionen

Die Ultimate-Version von HelpNDoc bietet sogenannte **BuiltActions**, mit denen zusätzliche Automatisierungen möglich sind. Damit können z. B. externe Programme oder Skripte vor oder nach dem Build ausgeführt werden. Das ermöglicht eine sehr flexible Preprocessing- oder Postprocessing-Strategie – besonders in komplexen Dokumentationspipelines.

Leider sind **BuiltActions nur in der Ultimate-Version** verfügbar. Die **freie** sowie die **professionelle Version** bieten diesen Komfort nicht. In diesen Versionen müssen viele Schritte manuell oder über eigene Skriptstrukturen wie dieses Projekt umgesetzt werden.

Die **freie Version von HelpNDoc** ist uneingeschränkt für Evaluierungs- und Testzwecke nutzbar. Es werden dabei jedoch **dezente Banner** in den generierten Dokumentationen eingefügt. Diese Banner können je nach Layout kleine Darstellungsprobleme verursachen, was ein Upgrade auf die kostenpflichtigen Varianten (Professional oder Ultimate) sinnvoll macht.

HelpNDoc bietet ein gutes Preis-Leistungs-Verhältnis und ein sehr freundliches Support-Team. Mit guten Argumenten sind auch **Rabatte von bis zu 50 %** auf kostenpflichtige Versionen möglich. Für Dokumentationsautoren – besonders jene mit Microsoft-Word-Hintergrund – ist HelpNDoc absolut empfehlenswert.

---

Bei Fragen oder Vorschlägen: gerne melden!
