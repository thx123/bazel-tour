# Note: Bazel has dropped the support for Python2.
load("@python//3.10:defs.bzl", compile_pip_requirements_3_10 = "compile_pip_requirements")

compile_pip_requirements_3_10(
    name = "requirements_3_10",
    src = "requirements.in",
    requirements_txt = "requirements_lock_3_10.txt",
)

compile_pip_requirements_3_10(
    name = "requirements_dev_3_10",
    src = "requirements-dev.in",
    requirements_txt = "requirements_dev_lock_3_10.txt",
)
