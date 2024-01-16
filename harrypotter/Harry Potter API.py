import tkinter as tk
from PIL import Image, ImageTk
import requests
import io
import random

def fetch_potions():
    response = requests.get('https://api.potterdb.com/v1/potions')
    if response.status_code == 200:
        return response.json()['data']
    else:
        return []

def fetch_characters():
    response = requests.get('https://api.potterdb.com/v1/characters')
    if response.status_code == 200:
        return response.json()['data']
    else:
        return []

def fetch_books():
    response = requests.get('https://api.potterdb.com/v1/books')
    if response.status_code == 200:
        return response.json()['data']
    else:
        return []

def fetch_spells():
    response = requests.get('https://api.potterdb.com/v1/spells')
    if response.status_code == 200:
        return response.json()['data']
    else:
        return []

def fetch_movies():
    response = requests.get('https://api.potterdb.com/v1/movies')
    if response.status_code == 200:
        return response.json()['data']
    else:
        return []

def fetch_and_display_image(image_url, image_label):
    if image_url:
        try:
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                image_data = Image.open(io.BytesIO(image_response.content))
                image_data.thumbnail((200, 200))
                image = ImageTk.PhotoImage(image_data)
                image_label.config(image=image, bg="lightblue")
                image_label.image = image  
        except Exception as e:
            print(f"An error occurred: {e}")
            image_label.config(image='', text='Image not available')
    else:
        image_label.config(image='', text='No image URL provided')

def display_potion(potion, image_label, details_label):
    potion_attributes = potion['attributes']
    potion_details = f"Name: {potion_attributes['name']}\n" \
                     f"Ingredients: {potion_attributes['ingredients']}\n" \
                     f"Slug Name: {potion_attributes['slug']}\n" \
                     f"Characteristics: {potion_attributes['characteristics']}\n" \
                     f"Effects: {potion_attributes['effect']}"

    details_label.config(text=potion_details)
    image_url = potion_attributes.get('image')
    fetch_and_display_image(image_url, image_label)

def fetch_random_potion(image_label, details_label):
    potions = fetch_potions()
    if potions:
        random_potion = random.choice(potions)
        display_potion(random_potion, image_label, details_label)

def display_character(character, image_label, details_label):
    character_attributes = character['attributes']
    character_details = f"Name: {character_attributes.get('name', 'N/A')}\n" \
                        f"House: {character_attributes.get('house', 'N/A')}\n" \
                        f"Role: {character_attributes.get('role', 'N/A')}\n" \
                        f"Blood Status: {character_attributes.get('bloodStatus', 'N/A')}"

    details_label.config(text=character_details)
    image_url = character_attributes.get('image')
    fetch_and_display_image(image_url, image_label)

def fetch_random_character(image_label, details_label):
    characters = fetch_characters()
    if characters:
        random_character = random.choice(characters)
        display_character(random_character, image_label, details_label)

def display_book(book, image_label, details_label):
    book_attributes = book['attributes']
    book_details = f"Title: {book_attributes.get('title', 'Unknown Title')}\n" \
                   f"ISBN: {book_attributes.get('isbn13', 'N/A')}\n" \
                   f"Number of Pages: {book_attributes.get('numberOfPages', 'N/A')}\n" \
                   f"Description: {book_attributes.get('description', 'No description available.')}"

    details_label.config(text=book_details)
    image_url = book_attributes.get('cover')

    fetch_and_display_image(image_url, image_label)

def fetch_random_book(image_label, details_label):
    books = fetch_books()
    if books:
        random_book = random.choice(books)
        display_book(random_book, image_label, details_label)

def display_spell(spell, image_label, details_label):
    spell_attributes = spell['attributes']
    spell_details = f"Name: {spell_attributes['name']}\n" \
                    f"Type: {spell_attributes.get('type', 'N/A')}\n" \
                    f"Effect: {spell_attributes.get('effect', 'N/A')}"

    details_label.config(text=spell_details)
    image_url = spell_attributes.get('image')
    fetch_and_display_image(image_url, image_label)

def fetch_random_spell(image_label, details_label):
    spells = fetch_spells()
    if spells:
        random_spell = random.choice(spells)
        display_spell(random_spell, image_label, details_label)

def display_movie(movie, image_label, details_label):
    movie_attributes = movie['attributes']
    movie_details = f"Title: {movie_attributes.get('title', 'N/A')}\n" \
                    f"Year: {movie_attributes.get('year', 'N/A')}\n" \
                    f"Director: {movie_attributes.get('director', 'N/A')}\n"

    details_label.config(text=movie_details)
    image_url = movie_attributes.get('poster')
    fetch_and_display_image(image_url, image_label)

def fetch_random_movie(image_label, details_label):
    movies = fetch_movies()
    if movies:
        random_movie = random.choice(movies)
        display_movie(random_movie, image_label, details_label)

def main(root):
    main_window = tk.Toplevel(root)
    main_window.title("Harry Potter Random Information Generator")

    background_color = "#7391B5"
    text_color = "#F8F8FF"
    button_color = "#7391B5"

    main_window.configure(bg="#d2d5f1")

    details_frame = tk.Frame(main_window, borderwidth=2, relief="groove", bg=background_color)
    details_frame.pack(pady=20, padx=20, fill="both", expand=True)

    image_label = tk.Label(details_frame, bg=background_color)
    image_label.grid(row=0, column=0, padx=10, pady=10)

    details_label = tk.Label(details_frame, text="", justify=tk.LEFT, anchor="w", bg=background_color, fg=text_color)
    details_label.grid(row=0, column=1, sticky="nsew")

    # Buttons at the top in one line
    top_buttons_frame = tk.Frame(main_window ,bg="#d2d5f1")
    top_buttons_frame.pack(fill="both")

    potion_button = tk.Button(top_buttons_frame, text="Generate Random Potion", command=lambda: fetch_random_potion(image_label, details_label), bg=button_color, fg=text_color)
    potion_button.pack(side=tk.LEFT, padx=10, pady=20)

    character_button = tk.Button(top_buttons_frame, text="Generate Random Character", command=lambda: fetch_random_character(image_label, details_label), bg=button_color, fg=text_color)
    character_button.pack(side=tk.LEFT, padx=10, pady=20)

    spell_button = tk.Button(top_buttons_frame, text="Generate Random Spell", command=lambda: fetch_random_spell(image_label, details_label), bg=button_color, fg=text_color)
    spell_button.pack(side=tk.LEFT, padx=10, pady=20)

    bottom_buttons_frame = tk.Frame(main_window ,bg="#d2d5f1")
    bottom_buttons_frame.pack(fill="both", side=tk.BOTTOM) 

    # Buttons at the bottom
    book_button = tk.Button(bottom_buttons_frame, text="Generate Random Book", command=lambda: fetch_random_book(image_label, details_label), bg=button_color, fg=text_color)
    book_button.pack(side=tk.LEFT, padx=(100, 5), pady=20)

    movie_button = tk.Button(bottom_buttons_frame, text="Generate Random Movie", command=lambda: fetch_random_movie(image_label, details_label), bg=button_color, fg=text_color)
    movie_button.pack(side=tk.RIGHT, padx=(5, 90), pady=20)

    main_window.mainloop()


def create_welcome_window():
    root = tk.Tk()
    root.title("Welcome")
    root.geometry("350x400")

    background_image = Image.open("harrypotter/bg1.jpg")  
    # Resize the image using Image.resize(width, height)
    background_image = background_image.resize((350, 400))
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a label with the background image
    background_label = tk.Label(root, image=background_photo)
    background_label.place(relwidth=1, relheight=1)

    welcome_label = tk.Label(root, text="Harry Potter Random Information Generator", font=("Helvetica", 12), bg="#7391B5", fg="black")
    welcome_label.pack(pady=20)

    start_button = tk.Button(root, text="Start App", command=lambda: open_main(root))
    start_button.pack(pady=(150, 10))

    root.mainloop()

def open_main(root):
    root.withdraw()
   
    main(root)

if __name__ == "__main__":
    create_welcome_window()