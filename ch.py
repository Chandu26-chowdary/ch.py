
import streamlit as st
st.header("Welcome")
import random

# Curated classy color palette
colors = [
    "Royal Blue", "Emerald Green", "Crimson Red",
    "Gold", "Silver", "Violet", "Jet Black", "Pearl White"
]

# Accessories and hairstyles to match outlook
extras = {
    "male": {
        "tall_athletic": ["✔ Tailored blazer", "✔ Short textured hairstyle", "✔ Smart wristwatch"],
        "medium_slim": ["✔ Slim-fit trousers", "✔ Side-part hairstyle", "✔ Minimalist sneakers"],
        "short_stocky": ["✔ Structured jacket", "✔ Buzz cut", "✔ Leather belt"],
    },
    "female": {
        "petite_graceful": ["✔ Flowing scarf", "✔ Bun hairstyle", "✔ Elegant earrings"],
        "tall_curvy": ["✔ Statement necklace", "✔ Wavy hairstyle", "✔ High heels"],
        "medium_professional": ["✔ Blazer", "✔ Straight hair", "✔ Smart handbag"],
    }
}
# Outlook-based styling prompts
styles = {
    "male": {
        "tall_athletic": [
            "Futuristic cyberpunk suit with neon circuitry emphasizing shoulders",
            "Minimalist smart casual with geometric AI motifs elongating frame",
            "Traditional attire reimagined with holographic overlays balancing proportions",
            "Avant-garde streetwear with oversized holographic jacket adding volume",
            "Techno-formal tuxedo with metallic fractal embroidery highlighting physique",
            "Sporty futurism with gradient fabrics enhancing agility"
        ]
    },
    "female": {
        "petite_graceful": [
            "Holographic gown with flowing digital silk layers accentuating height",
            "Smart casual blouse with AI-inspired embroidery elongating lines",
            "Traditional sari with fractal gradient textures adding vertical emphasis",
            "Avant-garde dress with bold geometric patterns balancing proportions",
            "Futuristic business suit with glowing seams for sleek authority",
            "Cropped jacket and holographic pants with neon accents adding presence"
        ]
    }
}

def generate_ai_styles(outlook, gender):
    outlook_styles = styles.get(gender, {}).get(outlook, [])
    outlook_extras = extras.get(gender, {}).get(outlook, [])
    results = []
    
    if not outlook_styles:
        return [f"No styles found for {gender} with outlook '{outlook}'."]
    
    for i, style in enumerate(outlook_styles):
        color = random.choice(colors)
        extra = outlook_extras[i % len(outlook_extras)] if outlook_extras else ""
        results.append(
            f"Outlook: {outlook} | Style: {style} | Color Theme: {color} | {extra}"
        )
    return results
