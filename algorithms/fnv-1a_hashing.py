OFFSET_BASIS = 2166136261
FNV_PRIME = 16777619


def fnv1a(text: str) -> int:

    hash = OFFSET_BASIS

    # convert text into bytes using UTF-8
    text_as_bytes = text.encode("utf-8")

    for byte in text_as_bytes:

        hash = hash ^ byte
        # diffusion
        hash = hash * FNV_PRIME
        # cut out the values higher than 32 bits
        hash = hash & 0xFFFFFFFF

    return hash


print(fnv1a("Aziz"))
print(fnv1a("Aziz1"))
print(fnv1a("Kasis"))
