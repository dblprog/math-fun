module Goldbach where

import Data.List
import System.IO
import Control.Category hiding ((.))

-- checkPrime checks whether the number is prime.
checkPrime :: Int -> Bool
checkPrime n = n > 1 && islTrue (map (\x -> (n `rem` x) /= 0) [2..(n-1)]) where
   islTrue :: [Bool] -> Bool
   islTrue [] = True
   islTrue (a:as)
      | a == True = islTrue as
      | otherwise = False

-- primes return all possible pairs of prime numbers.
primes :: Int -> [(Int,Int)]
primes n = filter (\x -> x /= (0,0)) (map pjust [1..(n `quot` 2)]) where
   pjust a
      | checkPrime a && checkPrime (n-a) = (a,n-a)
      | otherwise = (0,0)

goldbach :: IO ()
goldbach = do
   getLine >>= (read >>> primes >>> print)