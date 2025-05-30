import argparse
from face_recognition.detector import detect_faces
from social_search.searcher import search_social_media

def main(image_path):
    print("Detecting faces...")
    faces = detect_faces(image_path)
    if not faces:
        print("No faces detected.")
        return
    print(f"Detected {len(faces)} face(s). Searching social media...")
    for idx, face_encoding in enumerate(faces):
        print(f"Searching for face {idx + 1}...")
        results = search_social_media(face_encoding)
        print(f"Results for face {idx + 1}:")
        for result in results:
            print(f"  - {result}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True, help="Path to the input image")
    args = parser.parse_args()
    main(args.image)
