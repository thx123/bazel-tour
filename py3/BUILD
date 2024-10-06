load("@pypi_dev//:requirements.bzl", req_dev = "requirement")
load("@rules_python//python:defs.bzl", "py_binary", "py_library", "py_test")

py_library(
    name = "greeter_lib",
    srcs = ["greeter.py"],
)

py_binary(
    name = "hello_world",
    srcs = ["hello_world.py"],
    deps = [
        ":greeter_lib",
    ],
)

py_test(
    name = "hello_world_test",
    srcs = ["hello_world_test.py"],
    deps = [
        ":hello_world",
        req_dev("pytest"),
    ],
    size = "small",
)
