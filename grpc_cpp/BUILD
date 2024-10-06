cc_binary(
    name = "greeter_client",
    srcs = ["greeter_client.cc"],
    # static linking to overcome the version mismatch problem of
    # libc.so.6 and libstdc++.so.6 between host and target environments.
    # linkopts = ["-static"],
    deps = [
        "@grpc//:grpc++",
        "//protos:helloworld_cpp_grpc",
        "@abseil-cpp//absl/flags:flag",
        "@abseil-cpp//absl/flags:parse",
    ],
)

cc_binary(
    name = "greeter_server",
    srcs = ["greeter_server.cc"],
    # static linking to overcome the version mismatch problem of
    # libc.so.6 and libstdc++.so.6 between host and target environments.
    # linkopts = ["-static"],
    deps = [
        "@grpc//:grpc++",
        "@grpc//:grpc++_reflection",
        "//protos:helloworld_cpp_grpc",
        "@abseil-cpp//absl/flags:flag",
        "@abseil-cpp//absl/flags:parse",
        "@abseil-cpp//absl/strings:str_format",
    ],
)
