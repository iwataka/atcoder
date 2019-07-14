import           Control.Monad

denominator = 10^9 + 7

main = do
    l <- getLine
    let n:k:_ = map read $ words l :: [Int]
    forM (solve n k) $ \a -> print $ a `mod` denominator

factorial x = factorials !! x

factorials = 1 : zipWith (*) factorials [1..]

combination n k = do
    let a = factorial n
    let b = factorial k
    let c = factorial (n - k)
    a `div` (b * c)

solve' n k i
    | x < i = 0
    | otherwise = do
        let a = combination x i
        let b = combination (k - 1) (i - 1)
        a * b
    where
        x = n - k + 1

solve n k = do
    let f = solve' n k
    map f [1..k]
