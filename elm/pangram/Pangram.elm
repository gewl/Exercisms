module Pangram exposing (..)
import Char

isPangram_ : String -> String -> Bool
isPangram_ s l =
    case String.uncons s of
        Nothing -> String.isEmpty l
        Just (head, tail) ->
            isPangram_ tail (String.filter (isNot (Char.toLower head)) l)

isPangram : String -> Bool
isPangram s = isPangram_ s "abcdefghijklmnopqrstuvwxyz"

isNot : Char -> Char -> Bool
isNot a b =
    a /= b


-- isPangram takes string and list. if string is empty,
-- return whether list is empty. if string isn't empty,
-- call isPangram on tail string, list -= head string

-- function takes char and list and returns list without char
