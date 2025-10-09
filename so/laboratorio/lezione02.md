# Interazione tra processi

- I processi possono essre indirettamente a conoscenza l'uno dell'altro (se per esempio hanno un buffre in comune, caso | in bash)
  Il SO deve facilitare la cooperazione fornendo meccanismi di comunicazione

- Direttamente a conoscenza: processi che comunicano direttamente tra di loro (in base al loro id)
  il SO deve facilitare la cooperazione fornendo meccanismi di comunicazione

## memoria condivisa:
- I processi condividono la memoria
  Comunicazione tramite sincronizzazione (Memoria privata)
- I processi non condividono la memoria
  Sincronizzazione tramite comunicazione (mem condivisa)

## Proprietà
Definizione: Una proprietà di un programma concorrente è un attributo che rimane vero per ogni possibile storia di esecuzione del programma stesso
Due proprietà:
- Safety: mostra che il programma non esegue azioni scorrette
- Liveness: il programma avanza, non si ferma (non ha stalling)

### Mutua esclusione (safety)
l'accesso ad una risorsa si dice mutualmente esclusivo se ad ogni istante, al massimo un processo può accedere a quella risorsa
Es: due processi che vogliono accedere contemporaneamente a una stampante, due processi che devono aggiornare la variabile condivisa totale

### Deadlock
La mutua esclusione pernette di risolvere il problema della non interferenza
**ma** può causare il blocco permanente dei processi (l'assenza di deadlock è una proprietà di safety)
Es: processo 1 richiede risorsa A e B, processo 2 richiede B e A, se vengono eseguiti contemporaneamente può avvenire un deadlock

### Starvation
Se un processo non riescere ad accedere ad una risorsa perchè sempre occupata da altri processi
L'assenza di starvation è una proprietà di liveness

### Azione atomica
(atomico = più piccola possibile)
Le azioni atomiche vengono compiute in modo indivisibile (o tutto o niente)
- Nel caso di parallelismo reale: si garantisce che l'azione non interferisca con altri processi durante la sua esecuzione
- Nel caso di parallelismo apparante l'avvicendamento (context switch) fra i processi avviene prima o dopo l'azione, che quindi non può interferire
Es: le singole istruzioni del ling macchina sono atomiche (ovvio!)
- Parallelismo apparente:
  il meccanismo degli interrupt garantisce che un interrupt venga eseguito prima o dopo un'istruzione, mai "durante"
- Parallelismo reale:
  anche se più istruzioni cercano di accedere alla stessa cella di memoria (quella puntata da $t0), la politica di arbitraggio del bus garantisce che una delle due venga servita per prima e l'altra successivamente

#### In C
- a=0; /* int a */
  questo statement è atomico; la variabile a viene definita come un intero di lunghezza "nativa" e inizializzata a 0
- a=0; /* long long a */
  questo statement non è atomico, in quanto si tratta di porre a zero una variabile a 64 bit; questo può richiedere più istruzioni
- a++;
  anche questo statement in generale non è atomico, ma dipende dalle istruzioni disponibili in linguaggio macchina

#### E nei compiti di concorrenza?
Assumiamo che in ogni istante, vi possa essere al massimo un accesso alla memoria alla volta. Questo significa che operazioni tipo:
- aggiornamento di una variabile
- incremento di una variabile
- valutazione di espressioni
non sono atomiche
Operazioni tipo assegnamento di un valore costante ad una variabile sono atomiche

Nel seguito, utilizzeremo la notazione <S>< per indicare che lo statement S deve essere eseguito in modo atomico
Es: < x = x + 1; ><> è da essere eseguito atomicamente
### Non-interferenza
Dobbiamo trovare il modo di specificare che certe parti dei programmi sono "speciali", ovvero devono essere eseguite in modo atomico (senza interruzioni)  Serve la mutua esclusione ma occorre che il meccanismo soddisfi anche altre proprietà...

### Sezioni critiche
La parte del programma che usa una o più risorse condivise viene defiinta sezione critica (critical section, cs) e quindi deve essere eseguita in modo atomico

### Sezioni condivise
Obiettivi:
- Vogliamo garantire che le sezioni critiche siano eseguite in modo mutualmente esclusivo
- Vogliamo evitare situazioni di blocco, sia dovute a deadlock sia dovute a starvation 
- Vogliamo evitare attese non necessarie  Un processo può far attendere altri processi solo se questi ultimi devono usare una sezione critica attualmente occupata dal primo.
#### Sintassi:
- [enter cs] indica il punto di inizio di una sezione critica
- [exit cs] indica il punto di fine di una sezione critica

Es:[enter cs]; x = x+1; [exit cs];

```
process Pi { /* i=1...N */
    while (true) {
        [enter cs]
        critical section
        [exit cs]
        non-critical section
    }
}
```
in modo che valgano le seguenti proprietà:
- Mutua esclusione
- Assenza di deadlock
- Assenza di delay non necessari
- Eventuali entry (assenza di starvation)
Nota: Dobbiamo fare un'assunzione:
Se un processo entra in una critical section, prima o poi ne uscirà. Ovvero, un processo può terminare solo fuori dalla sua sezione critica

#### Possibili approcci:
- Software: responsabilità cade sui processi che vogliono accedere ad un oggetto distribuito (soggetto ad errori)
- Hardware: utilizano istruzioni speciali del linguaggio, progettate apposta (non adatto come soluzioni general-purpose)
- Supporto nel S.O. o nel linguaggio: Es. semafori, monitor, message passing

## Algoritmo di dekker (by Dijkstra)
- sol con variabile globale turn che indica il processo che indica chi può usare la risorsa
  il controllo iterativo su una condizione di accesso viene detto busy waiting
    . Soggetto a delay non necessari

Disabilitazione degli interrupt
Soluzione hw pericolosa (la responsabilità di riattivare gli interrupt, viene passata ai processi), inoltre se ci sono più processori gli interrrupt devono essere bloccati per processore.

### Test & Set


