vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

fact("This is my first Degree in Saveetha School of Engineering").

count_vowels(Fact, Count) :-
    atom_chars(Fact, Chars),
    count_vowels(Chars, 0, Count).

count_vowels([], Count, Count).
count_vowels([H|T], Acc, Count) :-
    (vowel(H) -> NewAcc is Acc + 1 ; NewAcc is Acc),
    count_vowels(T, NewAcc, Count).
