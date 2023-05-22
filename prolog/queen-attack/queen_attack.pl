%! create(+DimTuple)
%
% The create/1 predicate succeeds if the DimTuple contains valid chessboard 
% dimensions, e.g. (0,0) or (2,4).
create((DimX, DimY)) :-
	maplist(between(0, 7), [DimX, DimY]).

%! attack(+FromTuple, +ToTuple)
%
% The attack/2 predicate succeeds if a queen positioned on ToTuple is 
% vulnerable to an attack by another queen positioned on FromTuple.
attack((X, _), (X, _)) :- !.
attack((_, Y), (_, Y)) :- !.
attack((FromX, FromY), (ToX, ToY)) :-
	abs(FromX - ToX) =:= abs(FromY - ToY).