module Pangram exposing (..)
import List
import String

isPangram : String -> String
isPangram line =
    String.join "" (List.sort (String.split "" line))
