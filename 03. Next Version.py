version = input().split(".")
version_as_int = int("".join(version)) + 1
new_version = list(str(version_as_int))
print(".".join(new_version))