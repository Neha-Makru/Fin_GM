import pandas as pd
import numpy as np

# Load your dataset
df = pd.read_excel("ml_training_dataset.xlsx", sheet_name="Sheet1")

# Define a base mix percentage per Dealer Tier
# Premium tiers (Platinum/Gold) get higher averages
tier_map = {
    "Platinum": 0.75,
    "Gold": 0.55,
    "Silver": 0.35,
    "Bronze": 0.20
}

# Apply the base mix, then add some noise so it's not perfectly deterministic
np.random.seed(42)
df["Premium Product Mix %"] = df["Dealer Tier"].map(tier_map)

# Add random noise (0.0 to 0.15) to create realistic variation within tiers
noise = np.random.uniform(0, 0.15, len(df))
df["Premium Product Mix %"] = (df["Premium Product Mix %"] + noise).clip(0, 1)

# Convert to percentage format (0 to 100)
df["Premium Product Mix %"] = (df["Premium Product Mix %"] * 100).round(2)

# Save back to the file
with pd.ExcelWriter("ml_training_dataset.xlsx", engine="openpyxl", mode="w") as writer:
    df.to_excel(writer, sheet_name="Sheet1", index=False)

print("Premium Product Mix % added successfully!")