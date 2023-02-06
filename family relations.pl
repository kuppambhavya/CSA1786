female(sarah).
female(rebekah).
female(hagar_concubine).
female(milcah).
female(bashemath).
female(mahalath).
female(first_daughter).
female(rachel).
female(labans_wife).

male(terah).
male(abraham).
male(nahor).
male(haran).
male(isaac).
male(ismael).
male(uz).
male(kemuel).

parent(terah, abraham).
parent(terah, haran).
parent(haran, ishmael).
parent(abraham, isaac).
parent(abraham, ishmael).
parent(sarah, isaac).
parent(rebekah, jacob).
parent(isaac, jacob).
parent(jacob, first_daughter).

father(Father, Child) :- male(Father), parent(Father, Child).
mother(Mother, Child) :- female(Mother), parent(Mother, Child).
