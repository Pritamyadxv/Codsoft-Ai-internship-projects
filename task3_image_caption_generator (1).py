# task3_image_caption_generator.py
# Simple Image Caption Generator using Dictionary for CodSoft Internship

def generate_caption(image_name):
    captions = {
        "dog.jpg": "A cute dog running in the park.",
        "mountain.jpg": "A beautiful view of snowy mountains.",
        "beach.jpg": "Waves hitting the shore on a sunny beach.",
        "city.jpg": "A busy city street during evening rush hour.",
    }

    return captions.get(image_name.lower(), "No caption available for this image.")

def main():
    print("Image Caption Generator")
    image_name = input("Enter image file name (e.g., dog.jpg): ")
    caption = generate_caption(image_name)
    print("Generated Caption:", caption)

if __name__ == "__main__":
    main()
