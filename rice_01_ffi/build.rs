fn main() {
    diplomat_tool::gen(
        std::path::Path::new("src/lib.rs"),
        "c",
        std::path::Path::new("c/include/"),
        &Default::default(),
        None,
        false,
    )
    .unwrap();
}
