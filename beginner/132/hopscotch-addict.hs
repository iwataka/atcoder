-- incomplete
import           Control.Monad
import           Data.Set      (Set)
import qualified Data.Set      as Set

type Node = (Int, Int)
type Edge = (Node, Node)
type Graph = [Edge]

unableToReach = maxBound :: Int

main = do
    l <- getLine
    let n:m:_ = map read $ words l :: [Int]
    ls <- replicateM m getLine
    let es = map (normalize . words) ls
    let g = buildG es
    l2 <- getLine
    let s:t:_ = map read $ words l2 :: [Int]
    let s' = (s, 0)
    let t' = (t, 0)
    let ans = search s' t' Set.empty g
    let success = ans `mod` 3 == 0
    let out = if success then ans `div` 3 else -1
    print out

normalize :: [String] -> (Int, Int)
normalize xs = do
    let a:b:_ = map read xs :: [Int]
    (a, b)

adjacents n g = do
    let f x = fst x == n
    map snd $ filter f g

search :: Node -> Node -> Set Node -> Graph -> Int
search s t reached g
    | t `elem` adjs = 1
    | null unreached = unableToReach
    | ans == unableToReach = unableToReach
    | otherwise = ans + 1
    where
        adjs = adjacents s g
        unreached = filter (`notElem` reached) adjs
        reached' = foldl (flip Set.insert) reached unreached
        f x = search x t reached' g
        ans = minimum $ map f unreached

buildG :: [(Int, Int)] -> Graph
buildG = concatMap buildE

buildE :: (Int, Int) -> [Edge]
buildE e
    | f == s = error "Self-looped edge"
    | otherwise = do
        let ss = zip (repeat f) [0,1,2]
        let ts = zip (repeat s) [1,2,0]
        zip ss ts
    where
        f = fst e
        s = snd e
