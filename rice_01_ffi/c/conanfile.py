import os
import subprocess
from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class demo01_runRecipe(ConanFile):
    name = "demo01_run"
    version = "1.0"
    package_type = "application"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of demo01_run package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*"

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        rust_build_args = "--release" if self.settings.build_type == "Release" else "--"
        rust_source_dir = os.path.abspath(os.path.join(self.source_folder, "..", ".."))
        subprocess.run(
            ["cargo", "build", "-p", "rice_01_ffi", rust_build_args],
            check=True,
            cwd=rust_source_dir,
        )
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
