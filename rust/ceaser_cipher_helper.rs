//https://www.codewars.com/kata/526d42b6526963598d0004db/train/rust

struct CaesarCipher {
    shift: u32,
    alphabet : Vec<char>
}

impl CaesarCipher {
    fn new(shift: u32) -> CaesarCipher {
        let alphabet = String::from("ABCDEFGHIJKLMNOPQRSTUVWXYZ").chars().collect();
        CaesarCipher { shift, alphabet}
    }

    fn encode(&self, message: &str) -> String {
        message.to_uppercase().as_str().chars()
        .fold(Vec::new(), |mut vector, c| {
            match self.alphabet.iter().position(|&x| x == c) {
                Some(_) => vector.push(self.alphabet[(self.alphabet.iter().position(|&x| x == c).unwrap() + self.shift as usize) % 26]),
                None => vector.push(c)
            }
            vector
        }).iter().collect::<String>()
    }

    fn decode(&self, message: &str) -> String {
        message.to_uppercase().as_str().chars()
        .fold(Vec::new(), |mut vector, c| {
            match self.alphabet.iter().position(|&x| x == c) {
                Some(_) => {
                    if self.alphabet.iter().position(|&x| x == c).unwrap() as isize - (self.shift as isize) < 0 {
                        vector.push(self.alphabet[((self.alphabet.iter().position(|&x| x == c).unwrap() as isize - self.shift as isize) + 26 as isize) as usize]);
                    }
                    else{
                        vector.push(self.alphabet[(self.alphabet.iter().position(|&x| x == c ).unwrap() as isize - self.shift as isize) as usize]);
                    }
                },
                None => vector.push(c)
            }
            vector
        }).iter().collect::<String>()
    }
}


/*
Other Solutions I enjoy

Solution 1 - hashmap based

use std::collections::HashMap;

struct CaesarCipher {
    encrypt_table: HashMap<char, char>,
    decrypt_table: HashMap<char, char>,
}

const ALPHABET: [char; 26] = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
];

impl CaesarCipher {
    fn new(shift: u32) -> CaesarCipher {
        let alphabet = ALPHABET;
        let mut shifted = ALPHABET;
        shifted.rotate_left(shift as usize);
        let enc: HashMap<char, char> = alphabet
            .iter()
            .cloned()
            .zip(shifted.iter().cloned())
            .collect();
        let dec: HashMap<char, char> = shifted
            .iter()
            .cloned()
            .zip(alphabet.iter().cloned())
            .collect();
        CaesarCipher {
            encrypt_table: enc,
            decrypt_table: dec,
        }
    }

    fn encode(&self, message: &str) -> String {
        message
            .to_uppercase()
            .chars()
            .map(|letter| *self.encrypt_table.get(&letter).unwrap_or(&letter))
            .collect()
    }

    fn decode(&self, message: &str) -> String {
        message
            .to_uppercase()
            .chars()
            .map(|letter| *self.decrypt_table.get(&letter).unwrap_or(&letter))
            .collect()
    }
}

Soultion 2 - magic number

struct CaesarCipher {
    shift: u32,
}

impl CaesarCipher {
    fn new(shift: u32) -> Self {
        Self { shift }
    }

    fn encode(&self, s: &str) -> String {
        s.to_uppercase().chars().map(|e| if e>='A' && e<='Z' {(((e as i32-65+self.shift as i32)%26)+65) as u8 as char} else {e}).collect()
    }

    fn decode(&self, s: &str) -> String {
        s.to_uppercase().chars().map(|e| if e>='A' && e<='Z' {((((e as i32-65-self.shift as i32)%26+26)%26)+65) as u8 as char} else {e}).collect()
    }
}

*/
