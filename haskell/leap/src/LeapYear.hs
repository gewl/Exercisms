module LeapYear (isLeapYear) where

isLeapYear :: Integer -> Bool
isLeapYear year = if (rem year 400 == 0) || (rem year 4 == 0 && rem year 100 /= 0)
					then True
					else False
