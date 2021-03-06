# BACKTRACKING

## Install

> run in viertual env

```sh
pip3 install -r requirements.txt
kkbacker --help # to check if everything is allright
```

## Run

```sh
kkbacker --read < example.in
kkbacker --rand=0.50 --vertexes=10
kkbacker --r 0.50 -n 10 --non-hamiltonian
```

## TO-DO [PL]

- [x] Utwórz graf spójny nieskierowany o n wierzchołkach i zadanym nasyceniu grafu (wybierz dowolną reprezentację grafu)
- [x] Współczynnik nasycenia krawędziami w grafach powinien być równy odpowiednio 30% i 70%. Utwórz najpierw cykl Hamiltona w grafie (losując kolejne wierzchołki), a nastepnie dopełnij graf krawędziami wg. współczynnika nasycenia w taki sposób, aby stopień każdego wierzchołka był parzysty (np. poprzez losowanie krótkich cykli złożonych z 3 wierzchołków).
- [x] Utwórz graf nieskierowany nie-hamiltonowski o nasyceniu 50% (można utworzyć graf jak powyżej, a na końcu izolować jeden z wierzchołków)
- [x] Zaimplementuj algorytm znajdowania cyklu Eulera w grafie
- [x] Zaimplementuj algorytm z powracaniem znajdowania cyklu Hamiltona w grafie
- [x] Po utworzeniu grafu (losowo lub z klawiatury) użytkownik może dla tego grafu wykonać dowolne procedury wyświetlania grafu lub znajdowania cykli E i H
