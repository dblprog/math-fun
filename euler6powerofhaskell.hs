module Main where 

import Data.List
import System.Environment
import Prelude

main :: IO ()
main = do print result
--(dif $ last list)  

list = [1..100]

sumSq :: [Integer] -> Integer
sumSq = sum . map (^2) 

sqSum :: [Integer] -> Integer
sqSum = (^2) . sum 

--res :: [Integer] -> Integer
res x = (sumSq x) - (sqSum x)

result :: Integer
result = abs . res $ list


