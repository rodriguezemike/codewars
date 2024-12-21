//https://www.codewars.com/kata/5262119038c0985a5b00029f/train/rust

fn is_prime(x: i64) -> bool {
    x > 1 && (2..(x as f64).sqrt() as i64 + 1).filter(|y| x % y == 0).collect::<Vec<i64>>().is_empty()
}
