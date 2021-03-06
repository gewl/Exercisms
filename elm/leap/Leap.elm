module Leap exposing (..)

isLeapYear : Int -> Bool

isLeapYear year =
    if year % 400 == 0 || (year % 4 == 0 && year % 100 /= 0) then
        True
    else
        False
