Problema: Avem o matrice 3x3 cu 8 dintre celule numerotate de la 1 la 8 și una goală. Știind că poziția inițială a celulelor este aleatoare și că putem muta o celulă doar în locul celulei goale și doar dacă este adiacentă acesteia, să se găsească, dacă există, o secvență de mutări ale celulelor astfel încât toate să fie plasate în ordine crescătoare în matrice. După mutarea unei celule, ea nu mai poate fi mutată din nou decât după ce unul din vecinii săi a fost mutat. Poziția celulei goale nu contează pentru validarea stării finale.

Folosiți pentru testarea implementărilor instanțele: [8, 6, 7, 2, 5, 4, 0, 3, 1], [2, 5, 3, 1, 0, 6, 4, 7, 8] și [2, 7, 5, 0, 8, 4, 3, 1, 6].

Etape de rezolvare: 
(0.2) Alegeți o reprezentare a unei stări a problemei. Reprezentarea trebuie să fie suficient de explicită pentru a conține toate informaţiile necesare pentru continuarea găsirii unei soluții dar trebuie să fie și suficient de formalizată pentru a fi ușor de prelucrat/memorat. 
(0.2) Identificați stările speciale (inițială și finală) și implementați funcția de inițializare (primește ca parametri instanța problemei, întoarce starea inițială) și funcția booleană care verifică dacă o stare primită ca parametru este finală.
(0.2) Implementați tranzițiile ca funcții care primesc parametri o stare și parametrii tranziției și întoarce starea rezultată în urma aplicării tranziției. Validarea tranzițiilor se face în una sau mai multe  funcții booleană, cu aceeași parametri. 
(0.4) Implementați strategia IDDFS.
(0.5) Implementați strategia Greedy și testați cel puțin trei euristici: distanța Manhattann, distanța Hamming, plus cel puțin încă o euristică diferită.
(0.5) Implementați un program care rulează toate cele 4 strategii (IDDFS și Greedy cu cele trei euristici) pentru cele trei instanțe și afișează soluția (dacă e găsită), lungimea sa (numărul de mutări) și durata execuției pentru fiecare din cele 4 strategii.
(Bonus: 0.1) Implementați strategia A* cu o euristică admisibilă. Includeți strategia în afișările de la punctul 6.

Pentru rezolvarea incompletă a unei etape se acordă cel mult 0.1 puncte.

Partea 1 (predare săptămâna 3): punctele 1-4.
Partea 2 (predare săptămâna 4): punctele 5 și 6. 

Resurse utile: 
https://deniz.co/8-puzzle-solver/ 
https://www.geeksforgeeks.org/iterative-deepening-searchids-iterative-deepening-depth-first-searchiddfs/ 
http://www.ieee.ma/uaesb/pdf/distances-in-classification.pdf 
