module RunLength (decode, encode) where

import Data.List (intercalate)
import Text.Regex.PCRE

decode :: String -> String
decode cs = cc f ( getAllTextMatches $ cs =~ "[0-9]*[[:alpha:]]|[[:blank:]]" ) 

cc :: (String -> String) -> [ String ] -> String
cc x s = intercalate "" $ ep x s

ep :: (String -> String) -> [ String ] -> [ String ]
ep x s = map x s

f :: String -> String
f cp = case length cp of
		1 -> cp
		_ -> duplicate (read $ init cp :: Int) (cts $ last cp)

duplicate :: Int -> String -> String
duplicate n sl = concat $ replicate n sl

cts :: Char -> String
cts = (:[])

-- Oh my god, Haskell doesn't have backreferencing.
encode :: String -> String
encode fs = cc g ( getAllTextMatches $ fs =~ "[[:blank:]]|A*|B*|C*|D*|E*|F*|G*|H*|I*|J*|K*|L*|M*|N*|O*|P*|Q*|R*|S*|T*|U*|V*|W*|X*|Y*|Z*|a*|b*|c*|d*|e*|f*|g*|h*|i*|j*|k*|l*|m*|n*|o*|p*|q*|r*|s*|t*|u*|v*|w*|x*|y*|z*" )

g :: String -> String
g cp = case length cp of
		0 -> ""
		1 -> cp
		len -> ( show len ) ++ (cts $ head cp)
