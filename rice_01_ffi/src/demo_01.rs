#[diplomat::bridge]
mod ffi {
    use diplomat_runtime::{DiplomatStr, DiplomatWrite};
    use std::fmt::Write;

    #[diplomat::opaque]
    struct Demo01;
    
    impl Demo01 {
        pub fn greeting(name: &DiplomatStr, write: &mut DiplomatWrite) {
            write!(write, "hello, {}", String::from_utf8(name.to_vec()).unwrap()).unwrap();
        }
    }

}