solve :: Double -> Double
solve x = sum $ 1 : [(x**y)/(product [1..y]) | y <- [1..9]]

main :: IO()
main = interact $ unlines . map show . map solve . map read . tail . words
