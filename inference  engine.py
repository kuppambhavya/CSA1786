interpret(true) :- !.
interpret((GoalA,GoalB)) :- !,
    interpret(GoalA),
    interpret(GoalB).

goal_succeeds(Goal) :-
    interpret(Goal),
    write("Goal Succeeds: "), write(Goal), nl.
goal_fails(Goal) :-
    \+ interpret(Goal),
    write("Goal Fails: "), write(Goal), nl.
