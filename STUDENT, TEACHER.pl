studies(charlie).%clauses
studies(olivia).
studies(jack).
studies(arthur).

teaches(kirke).
teaches(collins).
teaches(collins).
teaches(juniper).

subcode(csa135).
subcode(csc135).
subcode(csc131).
subcode(csc134).
subcode(csc135).
subcode(csc131).
subcode(csc171).
subcode(csc134).

studies(charlie, csc135).
studies(olivia, csc135).
studies(jack, csc131).
studies(arthur, csc134).
teaches(kirke, csc135).
teaches(collins, csc131).
teaches(collins, csc171).
teaches(juniper, csc134).

professor(X,Y) :- teaches(X, C),
studies(Y,C).




