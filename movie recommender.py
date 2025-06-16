import pandas as pd
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import io, requests

# ── Data ──────────────────────────────────────────────────────────────────────
df = pd.read_csv(r"C:\Users\anton\OneDrive\Documents\bhaves\imdb_top_1000.csv")
df = df.dropna(subset=["Series_Title", "Genre", "Released_Year", "IMDB_Rating", "Poster_Link"])
df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")
df["IMDB_Rating"] = pd.to_numeric(df["IMDB_Rating"], errors="coerce")

# ── Theme colors ─────────────────────────────────────────────────────────────
BG_MAIN      = "#0d0d16"   # deep charcoal
BG_PANEL     = "#1a1a28"
BG_CARD      = "#222233"
FG_TEXT      = "#e5e5e5"
NEON_GREEN   = "#39ff14"
NEON_CYAN    = "#00e5ff"
NEON_PINK    = "#ff41ff"

FONT_SANS = ("Segoe UI", 10)
FONT_BOLD = ("Segoe UI", 10, "bold")

# ── GUI root & style ─────────────────────────────────────────────────────────
root = tk.Tk()
root.title("🎬 Movie Recommender")
root.geometry("750x620")
root.configure(bg=BG_MAIN)

style = ttk.Style()
style.theme_use("clam")  # neutral base

style.configure(".", background=BG_MAIN, foreground=FG_TEXT, font=FONT_SANS)

style.configure("Accent.TButton",
                background=NEON_CYAN,
                foreground=BG_MAIN,
                font=FONT_BOLD,
                padding=6,
                borderwidth=0)
style.map("Accent.TButton",
          background=[("active", NEON_PINK), ("pressed", NEON_GREEN)])

style.configure("TLabel", background=BG_MAIN, foreground=FG_TEXT)
style.configure("Card.TLabel", background=BG_CARD, foreground=FG_TEXT, anchor="w")

style.configure("Custom.TEntry",
                fieldbackground=BG_PANEL,
                foreground=FG_TEXT,
                padding=4,
                relief="flat")

# ── State vars ───────────────────────────────────────────────────────────────
genre_var  = tk.StringVar()
year_var   = tk.StringVar()
rating_var = tk.StringVar()
filtered_df = pd.DataFrame()
recommend_index = 0

# ── Auto suggest helpers ─────────────────────────────────────────────────────
def update_suggestions(var, suggestion_box, column):
    value = var.get().lower()
    suggestions = sorted(set(df[column].dropna()))
    matches = [s for s in suggestions if value in str(s).lower()]
    suggestion_box.delete(0, tk.END)
    for m in matches[:10]:
        suggestion_box.insert(tk.END, m)

def on_select_suggestion(var, box):
    var.set(box.get(tk.ACTIVE))
    box.pack_forget()

def suggest_entry(frame, label_text, var, column):
    ttk.Label(frame, text=label_text + ":").pack(anchor="w", pady=(4,0))
    entry = ttk.Entry(frame, textvariable=var, style="Custom.TEntry")
    entry.pack(fill="x")
    box = tk.Listbox(frame, height=5, bg=BG_PANEL, fg=FG_TEXT,
                     selectbackground=NEON_CYAN, activestyle="none",
                     borderwidth=0, highlightthickness=0)
    box.pack(fill="x")
    box.pack_forget()

    entry.bind("<KeyRelease>",
               lambda e: (box.pack(fill="x"),
                          update_suggestions(var, box, column)))
    box.bind("<<ListboxSelect>>",
             lambda e: on_select_suggestion(var, box))

# ── Recommendation logic ─────────────────────────────────────────────────────
def recommend_movies():
    global filtered_df, recommend_index
    genre  = genre_var.get().lower()
    rating = rating_var.get()
    year_input = year_var.get()

    try:
        rating = float(rating)
    except:
        rating = 0

    if "-" in year_input:
        y_start, y_end = map(int, year_input.split("-"))
    else:
        try:
            y_start = y_end = int(year_input)
        except:
            y_start, y_end = 1900, 2100

    filtered_df = df[
        df["Genre"].str.lower().str.contains(genre) &
        (df["IMDB_Rating"] >= rating) &
        (df["Released_Year"].between(y_start, y_end))
    ]

    recommend_index = 0
    show_next_movies()

def show_next_movies():
    global recommend_index
    for widget in result_frame.winfo_children():
        widget.destroy()

    batch = filtered_df.iloc[recommend_index:recommend_index + 3]
    if batch.empty:
        ttk.Label(result_frame, text="No more recommendations!", style="Card.TLabel",
                  font=FONT_BOLD).pack(pady=10)
        return

    for _, row in batch.iterrows():
        card = tk.Frame(result_frame, bg=BG_CARD, bd=0, pady=6, padx=6)
        card.pack(fill="x", padx=10, pady=8)

        # Poster
        try:
            response = requests.get(row["Poster_Link"])
            img_data = response.content
            img = Image.open(io.BytesIO(img_data)).resize((90, 135))
            photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(card, image=photo, bg=BG_CARD)
            img_label.image = photo
            img_label.pack(side="left", padx=(0, 10))
        except:
            pass

        # Details
        info = (f"{row['Series_Title']} ({int(row['Released_Year'])})\n"
                f"Genre:  {row['Genre']}\n"
                f"Rating: {row['IMDB_Rating']}")
        ttk.Label(card, text=info, style="Card.TLabel", justify="left").pack(anchor="w")

    recommend_index += 3

# ── Layout ───────────────────────────────────────────────────────────────────
top_frame = tk.Frame(root, bg=BG_MAIN, padx=12, pady=12)
top_frame.pack(fill="x")

suggest_entry(top_frame, "Genre", genre_var, "Genre")
suggest_entry(top_frame, "Release Year (e.g., 2000 or 1990 2010)", year_var, "Released_Year")
suggest_entry(top_frame, "Min IMDB Rating", rating_var, "IMDB_Rating")

ttk.Button(top_frame, text="🎯 Recommend", style="Accent.TButton",
           command=recommend_movies).pack(pady=8, fill="x")
ttk.Button(top_frame, text="📩 More Suggestions", style="Accent.TButton",
           command=show_next_movies).pack(fill="x")

result_frame = tk.Frame(root, bg=BG_PANEL)
result_frame.pack(fill="both", expand=True, padx=12, pady=12)

root.mainloop()

