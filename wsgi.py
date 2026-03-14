from src import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
    # app.run(host="127.0.0.1", port=5000)                        # for TestingConfig
    # app.run(debug=True, host="127.0.0.1", port=5000)
    # app.run(debug=True, host="0.0.0.0")                       # for Dockerfile.dev
