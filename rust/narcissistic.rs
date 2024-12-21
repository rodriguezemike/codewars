// https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/rust

fn narcissistic(num: u64) -> bool {
    const RADIX: u32 = 10;
    let mut total = 0 as u64;
    let exp = num.to_string().len();
    for c in num.to_string().chars(){
        total += u64::pow(c.to_digit(RADIX).unwrap() as u64, exp as u32);
    }
    total as u64 == num
}

fn narcissistic_functional(num: u64) -> bool {
    num.to_string()
        .chars()
        .fold (0, |mut total, c| {
            total += u64::pow(c.to_digit(10).unwrap() as u64, num.to_string().len() as u32);
            total
        }) as u64 == num
}
