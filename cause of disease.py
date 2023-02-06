hypothesis(name,disease).
symptom(name,indication).

symptom(amit,fever).
symptom(amit,rash).

disease(measles) :- symptom(amit,fever), symptom(amit,rash).
disease(chickenpox) :- symptom(amit,fever), symptom(amit,rash).

predict_disease(Name, Disease) :- hypothesis(Name, Disease).
