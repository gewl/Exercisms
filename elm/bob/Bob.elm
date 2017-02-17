module Bob exposing (..)
import String
import Char

lowercaseLetters =
    "abcdefghijklmnopqrstuvwxyz"

allLetters =
    String.toUpper lowercaseLetters ++ lowercaseLetters

wordCharacters =
    allLetters ++ "1234567890"

anyLetters : Char -> Bool
anyLetters char =
    String.contains (String.fromChar char) allLetters

anyWordCharacters : Char -> Bool
anyWordCharacters char =
    String.contains (String.fromChar char) wordCharacters

hey : String -> String
hey speech = 
    if String.toUpper speech == speech && String.any anyLetters speech == True then
        "Whoa, chill out!"
    else if String.right 1 speech == "?" then
       "Sure."
    else if String.any anyWordCharacters speech == False then
        "Fine. Be that way!"
    else
        "Whatever."
