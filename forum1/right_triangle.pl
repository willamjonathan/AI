forum6(A1, A2, A3) :-

    %check sum
    %check it has to be greater than 0
    A1 > 0,
    A2 > 0,
    A3 > 0,
    A1 + A2 + A3 =:= 180,
        %no angle can be 0
        %1 have to be 90
    (A1 =:= 90 ; A2 =:= 90 ; A3 =:= 90).
