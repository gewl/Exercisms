module RunLength (decode, encode) where

import Text.Regex ( matchRegex, mkRegex )
import Text.Regex.Posix 
import Data.List (intercalate)

decode :: String -> String
decode cs = cc ( getAllTextMatches $ cs =~ "[0-9]*[[:alpha:]]" :: [String] )

encode :: String -> String
encode = error "You need to implement this function."

cc :: [ String ] -> String
cc s = intercalate "a " s
