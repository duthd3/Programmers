import Foundation

func solution(_ my_string:String, _ n:Int) -> String {
    var new_array :[Character] = []
    for char in my_string{
        for i in 0..<n{
            new_array.append(char)
        }
    }
    return String(new_array)
}
