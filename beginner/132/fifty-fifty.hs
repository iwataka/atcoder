import           Data.List

main = do
    s <- getLine
    let a:b:c:d:rest = sort s
    let result = a == b && a /= c && c == d
    let str = if result then "Yes" else "No"
    putStrLn str
