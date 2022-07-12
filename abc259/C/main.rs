use proconio::input;

fn main() {
    input! {
        s: String,
        t: String,
    }

    let _s = run_length_encode(s.chars().collect());
    let _t = run_length_encode(t.chars().collect());

    let mut ans = "Yes";
    if _s.len() != _t.len() {
        ans = "No";
    }
    for (s, t) in _s.iter().zip(_t.iter()) {
        if s.0 != t.0 {
            ans = "No";
        }
        if s.1 > t.1 {
            ans = "No";
        }
        if s.1 < t.1 && s.1 < 2 {
            ans = "No";
        }
    }
    println!("{}", ans);
}

fn run_length_encode<T: Eq + Copy>(s: Vec<T>) -> Vec<(T, usize)> {
    let mut res = vec![];
    let mut i = 0;
    while i < s.len() {
        let mut j = i + 1;
        while j < s.len() && s[i] == s[j] {
            j += 1;
        }
        res.push((s[i], j - i));
        i = j;
    }
    res
}
