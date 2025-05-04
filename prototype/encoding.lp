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
%TODO: how to combine generating with above commands, directions + limit actions by tracktypes

% generator in tracktypes

% define
% initialize starting coordinate and direction of each train
coord(ID, T, (X,Y)) :- start(ID, (X,Y), T, _).
dir(ID, T, D) :- start(ID, _, T, D).


% testers

% for each timestep at the spawning timestep and after, for each train, there is exactly one coordinate and one direction
% TODO: set this so train can be spawned later
:- train(ID), time(T1), start(ID, (_, _), T2, _), T1 >= T2,
    {coord(ID, T1, (X, Y))} != 1.
:- train(ID), time(T),
    {dir(ID, T, D) } != 1.


% it must not be that the coordinate of the train is not the same as the end coordinate
:- train(ID), coord(ID, ET, (X1, Y1)), end(ID, (X2, Y2), ET), X1 != X2.
:- train(ID), coord(ID, ET, (X1, Y1)), end(ID, (X2, Y2), ET), Y1 != Y2.


% two trains cannot be at the same coordinate at the same time

% two trains cannot swap coordinates (passing through each other)
#show action/3.