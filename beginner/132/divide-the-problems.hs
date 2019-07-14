import           Data.List

main = do
    n' <- getLine
    let n = read n' :: Int
    s <- getLine
    let ds = map read $ words s :: [Int]
    let ds' = sort ds
    let a:b:_ = drop ((n `div` 2) - 1) ds'
    print $ b - a
