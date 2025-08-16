from app import create_app

app = create_app()

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(port=8000, debug=True)
    print("Flask app has stopped.")
