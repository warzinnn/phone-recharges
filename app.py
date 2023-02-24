from src import create_app

app = create_app()

if __name__ == "__main__":
    # Run flask on port 5001
    app.run(port=5001)
