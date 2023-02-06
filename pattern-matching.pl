first_name(tonyblair, tony).
first_name(georgebush, georgedubya).
second_name(tonyblair, blair).
second_name(georgebush, bush).

full_name(First, Last, Name) :- first_name(Name, First), second_name(Name, Last).
