module RunLength (decode, encode) where

import Text.Regex ( matchRegex, mkRegex )
import Text.Regex.Posix 
import Data.List (intercalate)

decode :: String -> String
decode cs = cc . getAllTextMatches $ cs =~ "[0-9]*[[:alpha:]]" 

encode :: String -> String
encode = error "You need to implement this function."

cc :: [ String ] -> String
cc s = intercalate "" $ ep s

ep :: [ String ] -> [ String ]
ep s = map f s

f :: String -> String
f cp = case length cp of
		1 -> cp
		_ -> duplicate (read $ init cp :: Int) (cts $ last cp)

duplicate :: Int -> String -> String
duplicate n sl = concat $ replicate n sl

cts :: Char -> String
cts = (:[])
