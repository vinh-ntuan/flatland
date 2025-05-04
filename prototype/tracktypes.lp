track(1025). % =
track(32800). %||
track(33825). % + crossing

% trains can stop on any type of track
{action(train(ID), wait, T)} :- train(ID), time(T).

{action(train(ID), move_forward, T)} :- train(ID), coord(ID, T, (X, Y)), cell((X,Y), 1025), dir(ID, T, e).
{action(train(ID), move_forward, T)} :- train(ID), coord(ID, T, (X, Y)), cell((X,Y), 1025), dir(ID, T, w).

{action(train(ID), move_forward, T)} :- train(ID), coord(ID, T, (X, Y)), cell((X,Y), 32800), dir(ID, T, n).
{action(train(ID), move_forward, T)} :- train(ID), coord(ID, T, (X, Y)), cell((X,Y), 32800), dir(ID, T, s).

{action(train(ID), move_forward, T)} :- train(ID), coord(ID, T, (X, Y)), cell((X,Y), 33825), dir(ID, T, n).
{action(train(ID), move_forward, T)} :- train(ID), coord(ID, T, (X, Y)), cell((X,Y), 33825), dir(ID, T, e).
{action(train(ID), move_forward, T)} :- train(ID), coord(ID, T, (X, Y)), cell((X,Y), 33825), dir(ID, T, s).
{action(train(ID), move_forward, T)} :- train(ID), coord(ID, T, (X, Y)), cell((X,Y), 33825), dir(ID, T, w).


