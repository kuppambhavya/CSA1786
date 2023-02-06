fact(passed(X, history) :- studied(X), lucky(X)).
fact(passed(X, history) :- studied(X)).
fact(passed(X, history) :- lucky(X)).
fact(happy(X) :- passed(X, history), won_lottery(X)).
fact(won_lottery(X) :- lucky(X)).
fact(not_studied(john)).
fact(lucky(john)).

resolve(not_studied(john), not(studied(john))).
resolve(not(studied(john)), passed(john, history)).
resolve(passed(john, history), happy(john)).

prove(Goal) :-
    resolve(Goal, Proved),
    write(Proved), nl,
    (Goal == Proved -> true ; prove(Proved)).
