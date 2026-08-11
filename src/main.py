import processor as p

def main():
    data = p.load_file('data/data.json')
    if p.validate_data('data/data.json'):
        print("Data is valid")
        most_plays = p.get_most_plays(data)
        print(f"Song with the most plays: {most_plays['name']} by {', '.join(most_plays['artist'])}")
    else:
        print("Data is invalid")

if __name__ == "__main__":
    main()