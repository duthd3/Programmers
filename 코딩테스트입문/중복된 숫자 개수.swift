import Foundation

func solution(_ array:[Int], _ n:Int) -> Int {
    let count = array.count
    var result = 0
    for i in 0..<count{
        if n == array[i]{
            result += 1
        }
    }
    return result
}
