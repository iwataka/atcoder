main = do
    _ <- getLine
    s <- getLine
    let ps = map read $ words s :: [Int]
    let ans = count ps
    print ans

count :: [Int] -> Int
count ps
    | length ps < 3 = 0
    | otherwise = do
        let countup = (p1 < p2 && p2 < p3) || (p1 > p2 && p2 > p3)
        let base = if countup then 1 else 0
        base + count (p2:p3:rest)
    where
        p1:p2:p3:rest = ps
