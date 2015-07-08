# GeTwitter-Anwendung des Pojekts

## Nutzung

Die Anwendung muss in einer Server-Umgebung ausgeführt werden, beispielsweise im Verzeichnis eines laufenden Apache-Servers. Im Ordner '/data' wird eine Datei input.json erwartet, welche die zu verarbeitenden Daten enthält. Die Anwendung besteht aus mehreren Anzeigearten, die durch die Navigation angesteuert werden:

Hauptbildschirm - Wird beim Start der Anwendung angezeigt, bietet die Möglichkeit der Auswahl des Sucheinstiegs (Thema/Land)

Zwischenselektion - Abhängig von der Auswahl auf dem Hauptbildschirm wird anschließend eine Liste an Themen oder Ländern angezeigt (bei Auswahl der Suche nach Thema also eine Liste von Themen). 

Endselektion mit Graphen - Abhängig von der Auswahl in der Zwischenselektion wird eine neue Liste mit Daten für das gewählte Land/Thema angezeigt. Bei der Auswahl eines Listenitems wird dieses dem Graphen auf der rechten Seite hinzugefügt, nochmaliges klicken auf den gleichen Term entfernt den Term wieder aus dem Graphen.


### input.json

Die Datenstruktur der JSON-Datei lässt sich wie folgt darstellen.

	[
		{
			'value':'Topic1',
			'content':[
				{
					'value':'Land1',
					'rates':{
						'positive':10,
						'neutral':30,
						'negative':10
					}
				},
				{
					...
				}
			]
		},
		{
			...
		}
	]
	
Hierbei muss jedes Thema die gesammte Auswahl von Ländern umschließen.

## Abhängigkeiten

Alle benötigten Abhängigkeiten sind im Ordner '/lib' hinterlegt. Dies sind AngularJS, Bootstrap-UI, d3.js, nvd3.js und angularjs-nvd3-directives.js

## sentiment.js

Die Datei sentiment.js ist die zentrale Steuerungsdatei für die Anzeige und die Funktionen der Anwendung.
Sie lädt in einem 'run'-Block die bereitgestellte 'input.json' vor dem Start der Anwendung.
In ihrer Controller-Einheit gibt es fünf Funktionen, welche die Darstellung beeinflussen:

### selectView

Diese Funktion steuert die Darstellung einer der drei Anzeigearten, dem Hauptbildschirm mit der Auswahl des Sucheinstiegs, sowie je eine Auswahl ('countries' und 'topics') für die jeweiligen Auswahllisten.
	
### showTopics & showCountries

Diese Funktionen dienen der Darstellung der Listen, aus denen die anzuzeigenden Themen bzw Länder selektiert werden können.

### selectTopic & selectCountry

Diese Funktionen verarbeiten die Auswahl aus einer der Listen und übergibt die selektierten Daten an die eingebundenen Graphen-Templates.

## index.html

Die Datei dient der Browser-Darstellung, deren Anzeige im JavaScript gesteuert wird.
	