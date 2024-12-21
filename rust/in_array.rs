//https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/rust

fn in_array(arr_a: &[&str], arr_b: &[&str]) -> Vec<String> {
    let mut r: Vec<String> = Vec::new();
    for substring in arr_a.into_iter(){
        for string in arr_b.into_iter(){
            if string.contains(substring) && !r.contains(&substring.to_string()){
                r.push(substring.to_string());
                break;
            }
        }
    }
    r.sort();
    return r;
}

