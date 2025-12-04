from plot import heatmap, tanimoto_hist
from similarity import tanimoto_matrix, matrix_length
from welcome import welcome
from network_plot import similarity_network

def ask_yes_no(prompt):
    while True:
        ans = input(prompt + " (y/n): ").strip().lower()
        if ans in ["y", "n"]:
            return ans
        print("❌ Invalid input! Please enter 'y' or 'n'.")

def choose_colormap(colors):
    print("\n🎨 Available colormaps:")
    for idx, name in enumerate(colors):
        print(f"  {idx}: {name}")

    while True:
        choice = input("Enter colormap number: ").strip()
        if choice.isdigit() and int(choice) in range(len(colors)):
            return colors[int(choice)]
        print("❌ Invalid number!")

def main():
    welcome()

    # --- Load file ---
    file_path = input("📁 Enter your file path: ").strip()
    print("⏳ Processing file...")

    data = tanimoto_matrix(file_path)
    length = matrix_length(file_path)

    print(f"✅ File loaded successfully! Matrix size: {length}x{length}")

    # --- HEATMAP ---
    if ask_yes_no("Generate heatmap?") == "y":
        colors = ["plasma","magma","inferno","coolwarm","cividis","Greens","Blues","hot"]
        cmap = choose_colormap(colors)
        heatmap(data, cmap)
        print("🔥 Heatmap generated!")
    else:
        print("⚠ Heatmap skipped.")

    # --- HISTOGRAM ---
    if ask_yes_no("Generate histogram?") == "y":
        name = input("Enter output filename (e.g. hist.png): ").strip()
        tanimoto_hist(data, name)
        print(f"📊 Histogram saved as: {name}")
    else:
        print("⚠ Histogram skipped.")

    # --- NETWORK PLOT ---
    if ask_yes_no("Generate similarity network?") == "y":
        similarity_network(data)
        print("🌐 Network plot generated!")
    else:
        print("⚠ Network plot skipped.")

    print("\n🎉 Done!")

# --- ENTRY POINT ---
if __name__ == "__main__":
    main()
