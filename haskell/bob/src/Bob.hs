module Bob (responseFor) where

import Data.Char
import Data.List
trim = dropWhileEnd isSpace . dropWhile isSpace

responseFor :: String -> String
responseFor xs = 
	case length sxs == 0 of
		True -> "Fine. Be that way!"
		False -> case sxs == map toUpper sxs && sxs /= map toLower sxs of
			True -> "Whoa, chill out!"
			False -> case last sxs == '?' of
				True -> "Sure."
				False -> "Whatever."
	where sxs = trim xs
