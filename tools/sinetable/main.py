import math

# --- 設定 ---
ADDR_BITS = 10
DATA_BITS = 24 # Q1.23 (符号付き24bit) として格納
ENTRIES = 2 ** ADDR_BITS     # 1024
MAX_VAL = (2 ** 23) - 1      # Q1.23の最大値 (0x7FFFFF)
FILENAME = "sine_data.txt"

print(f"Generating {FILENAME} ...")

with open(FILENAME, "w") as f:
    for i in range(ENTRIES):
        angle = (i / ENTRIES) * (math.pi / 2)
        val = int(math.sin(angle) * MAX_VAL)

        hex_str = f"{val:06x}"
        suffix = "," if i < ENTRIES - 1 else ""
        f.write(f"24'h{hex_str}{suffix}\n")

print("Done.")
