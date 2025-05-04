% move_left propagation
coord(ID, T + 1, (X, Y - 1)) :- action(train(ID), move_left, T), coord(ID, T, (X, Y)), dir(ID, T, n), time(T + 1).
dir(ID, T + 1, w) :- action(train(ID), move_left, T), coord(ID, T, (_, _)), dir(ID, T, n), time(T + 1).
coord(ID, T + 1, (X - 1, Y)) :- action(train(ID), move_left, T), coord(ID, T, (X, Y)), dir(ID, T, e), time(T + 1).
dir(ID, T + 1, n) :- action(train(ID), move_left, T), coord(ID, T, (_, _)), dir(ID, T, e), time(T + 1).
coord(ID, T + 1, (X, Y + 1)) :- action(train(ID), move_left, T), coord(ID, T, (X, Y)), dir(ID, T, s), time(T + 1).
dir(ID, T + 1, e) :- action(train(ID), move_left, T), coord(ID, T, (_, _)), dir(ID, T, s), time(T + 1).
coord(ID, T + 1, (X + 1, Y)) :- action(train(ID), move_left, T), coord(ID, T, (X, Y)), dir(ID, T, w), time(T + 1).
dir(ID, T + 1, s) :- action(train(ID), move_left, T), coord(ID, T, (_, _)), dir(ID, T, w), time(T + 1).

% move_right propagation
coord(ID, T + 1, (X, Y + 1)) :- action(train(ID), move_right, T), coord(ID, T, (X, Y)), dir(ID, T, n), time(T + 1).
dir(ID, T + 1, e) :- action(train(ID), move_right, T), coord(ID, T, (_, _)), dir(ID, T, n), time(T + 1).
coord(ID, T + 1, (X + 1, Y)) :- action(train(ID), move_right, T), coord(ID, T, (X, Y)), dir(ID, T, e), time(T + 1).
dir(ID, T + 1, s) :- action(train(ID), move_right, T), coord(ID, T, (_, _)), dir(ID, T, e), time(T + 1).
coord(ID, T + 1, (X, Y - 1)) :- action(train(ID), move_right, T), coord(ID, T, (X, Y)), dir(ID, T, s), time(T + 1).
dir(ID, T + 1, w) :- action(train(ID), move_right, T), coord(ID, T, (_, _)), dir(ID, T, s), time(T + 1).
coord(ID, T + 1, (X - 1, Y)) :- action(train(ID), move_right, T), coord(ID, T, (X, Y)), dir(ID, T, w), time(T + 1).
dir(ID, T + 1, n) :- action(train(ID), move_right, T), coord(ID, T, (_, _)), dir(ID, T, w), time(T + 1).

% move_forward propagation
coord(ID, T + 1, (X - 1, Y)) :- action(train(ID), move_forward, T), coord(ID, T, (X, Y)), dir(ID, T, n), time(T + 1).
dir(ID, T + 1, n) :- action(train(ID), move_forward, T), coord(ID, T, (_, _)), dir(ID, T, n), time(T + 1).
coord(ID, T + 1, (X, Y + 1)) :- action(train(ID), move_forward, T), coord(ID, T, (X, Y)), dir(ID, T, e), time(T + 1).
dir(ID, T + 1, e) :- action(train(ID), move_forward, T), coord(ID, T, (_, _)), dir(ID, T, e), time(T + 1).
coord(ID, T + 1, (X + 1, Y)) :- action(train(ID), move_forward, T), coord(ID, T, (X, Y)), dir(ID, T, s), time(T + 1).
dir(ID, T + 1, s) :- action(train(ID), move_forward, T), coord(ID, T, (_, _)), dir(ID, T, s), time(T + 1).
coord(ID, T + 1, (X, Y - 1)) :- action(train(ID), move_forward, T), coord(ID, T, (X, Y)), dir(ID, T, w), time(T + 1).
dir(ID, T + 1, w) :- action(train(ID), move_forward, T), coord(ID, T, (_, _)), dir(ID, T, w), time(T + 1).

% wait propagation
coord(ID, T + 1, (X, Y)) :- action(train(ID), wait, T), coord(ID, T, (X, Y)), dir(ID, T, _), time(T + 1).
dir(ID, T + 1, D) :- action(train(ID), wait, T), coord(ID, T, (_, _)), dir(ID, T, D), time(T + 1).