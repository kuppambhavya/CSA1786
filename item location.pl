location(desk, office).
location(apple, kitchen).
location(flashlight, desk).

find_location(Item, Location) :- location(Item, Location).fact(mortal(socrates)).
fact(mortal(einstein)).
fact(mortal(alexander)).

is_mortal(Person) :- mortal(Person), write(Person), write(' is mortal.'), nl.
is_not_mortal(Person) :- not(mortal(Person)), write(Person), write(' is not mortal.'), nl.

check_mortality(Person) :-
    (is_mortal(Person); is_not_mortal(Person)).
