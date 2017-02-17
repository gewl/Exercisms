module Raindrops exposing (..)

raindrops : Int -> String
raindrops num =
    case (num%3, num%5, num%7) of
        (0, 0, 0) -> "PlingPlangPlong"
        (0, 0, _) -> "PlingPlang"
        (0, _, 0) -> "PlingPlong"
        (_, 0, 0) -> "PlangPlong"
        (0, _, _) -> "Pling"
        (_, 0, _) -> "Plang"
        (_, _, 0) -> "Plong"
        _ -> toString num
