# Skyscrapers

# Task 1
Aceasta masina Turing verifica daca se gaseste vreun numar de mai multe ori, pe fiecare linie. 

## PAS 1
Prima data avanseaza cu starea q0 pana intalneste primele :, unde isi schimba starea in START

## PAS 2
Dupa aceea, din starea START, trece in STAREA START1, START2, START3 sau START4; depinde de numarul pe care il intalneste dupa primul numar de pe aceea linie

## PAS 3
De la linia 4 si pana la ultima linie, acei pasi reprezinta, pe de o parte, pe cate numere s-a verificat conditia din enunt, si pe de alta parte, ce numere au fost supuse verificarii. Spatiile albe, pana la a 5-a coloana si a 17-a linie, semnifica acele cazuri in care se gasesc, de mai multe ori, acelasi numar. 

Ultimul pas, pas3124, ajuta la reinceperea verificarii pentru urmatoarea linie 

# Task 2
Aceasta masina Turing verifica daca se gaseste vreun numar de mai multe ori, pe fiecare coloana

Ideea principala este ca literele A,B,C si D reprezinta notarea tuturor elementelor de pe o anumita coloana, dupa ce aceasta a fost parcursa si verificata, cu litera S este inlocuit primul :, pentru a ajuta la usurarea intelegerii masinii Turing, si la fel ca la task1, toate stariile care au numere de 1,2,3 sau 4 cifre, reprezinta cate si care sunt numerele pe care masina Turing le-a verificat ca sunt valide, conform cerintei problemei. 

In principiu, pentru a trece dintr-un grup de 4 numere in alt grup de 4 numere, luandu-ne dupa input-uri, se vor folosii doua stari ajutatoare: q# si douaPct, iar verific_lit ajuta sa verificam daca numarul ales in aceea pozitie valideaza conditia problemei, si daca da, se afiseaza, in locul acestuia, litera corespunzatoare ei. Am folosit urmatoarele asocieri litera - numar: 
A -> 1, B -> 2, C -> 3, D -> 4.

Am folosit Python si Excel, ajutandu-ma si de site-ul https://web.archive.org/web/20240907093701/https://turingmachinesimulator.com/
