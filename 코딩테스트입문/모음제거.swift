import Foundation

func solution(_ my_string:String) -> String {
    var string = my_string
    let result = string.components(separatedBy: ["u","a","e","i","o"]).joined()
    return result
}
