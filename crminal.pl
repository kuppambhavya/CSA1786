american(robert).
enemy(countryA).
sells_weapons(robert, countryA).
has_missiles(countryA).

criminal(X) :- american(X), sells_weapons(X, Y), enemy(Y).
Footer
