# Analiza danych złożonych - projekt - zadanie 1: Klasyfikacja kolektywna

Przedmiotem zadania 1 jest zaproponowanie algorytmu klasyfikacji kolektywnej radzącego sobie w kwestii klasyfikacji etykiet 
węzłów w udostępnionym zbiorze danych. 
Zbiór danych to komunikacja e-mailowa w firmie produkcyjnej oraz dane o tym kto do kogo raportuje (struktura organizacyjna). 
Zaproponowany algorytm klasyfikacji kolektywnej powinien decydować jakie węzły odkryć i jak propagować wiedzę dot. 
ich etykiet aby klasyfikacja była jak najtrafniejsza

## Zbiór danych

Udostępniony jest on pod tym adresem:
https://doi.org/10.7910/DVN/6Z3CGX

W udostępnionym zbiorze danych można przyjąć, że węzły z następującymi identyfikatorami należą do następujących grup pracowników:

* wyższy poziom zarządzania: 86, 7, 27, 36, 69, 70, 85, 104, 121, 148, 156, 163
*	średni poziom zarządzania: 76, 90, 136, 137, 143, 152, 47, 162
*	regularni pracownicy: pozostałe węzły

## Zadania (15 pkt)
1. Implementacja i ewaluacja wybranego algorytmu klasyfikacji kolektywnej dla zadania klasyfikacji etykiet węzłów **(7.5 pkt)**
2. Przeprowadzanie badań dotyczących wyboru węzłów początkowych do odkrycia etykiet (metoda wyboru i procent odkrytych etykiet) **(5.5 pkt)**
3. Porównanie zaimplementowanego algorytmu z innym np. losowym (średniowym) **(2 pkt)**

Proszę mieć na uwadze niezbalansowanie klas. Z tego względu do pomiaru skuteczności klasyfikacji proszę użyć miary F1.

## Referencje:
[1] Sen, P., Namata, G., Bilgic, M., Getoor, L., Galligher, B., & Eliassi-Rad, T. (2008). Collective classification in network data. AI magazine, 29(3), 93-93.  
[2] Musial, K., Kajdanowicz, T., Michalski, R., & Kazienko, P. (2016). Learning in Unlabelled Networks–An Active Learning and Inference Approach. AI Communications: the European journal on artificial intelligence, 29(1).  
[3] N Nurek M, Michalski R. Combining Machine Learning and Social Network Analysis to Reveal the Organizational Structures. Applied Sciences. 2020; 10(5):1699.
