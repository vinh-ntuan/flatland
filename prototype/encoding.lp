#include "instance.lp".
#include "propagation.lp".
#include "tracktypes.lp".

command(move_left).
command(move_right).
command(wait).
command(move_forward).
direction(n).
direction(e).
direction(s).
direction(w).
time(0..GT) :- global(GT).

% generator
1 = {action(train(ID), A, T) : command(A)} :- train(ID), time(T).

% testers

% for each timestep at the spawning timestep and after, for each train, there is exactly one coordinate and one direction
% TODO: set this so train can be spawned later
1 = {coord(ID, T1, (X, Y)) : cell((X, Y), _)} :- train(ID), time(T1), start(ID, (_, _), T2, _), T1 >= T2.
1 = {dir(ID, T, D) : direction(D)} :- train(ID), time(T).

% initialize starting coordinate and direction of each train
startTime(ID, TT) :- TT = #min {T: coord(ID, T, (_, _))}, train(ID).
coord(ID, T, (X, Y)) :- startTime(ID, T), start(ID, (X, Y), _, _), train(ID).
dir(ID, T, D) :- startTime(ID, T), start(ID, (_, _), _, D), train(ID).

% it must not be that the coordinate of the train is not the same as the end coordinate
:- train(ID), coord(ID, ET, (X1, Y1)), end(ID, (X2, Y2), ET), X1 != X2.
:- train(ID), coord(ID, ET, (X1, Y1)), end(ID, (X2, Y2), ET), Y1 != Y2.

% two trains cannot be at the same coordinate at the same time

% two trains cannot swap coordinates (passing through each other)

#show action/3.