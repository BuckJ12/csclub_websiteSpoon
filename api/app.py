from flask import Flask

app = Flask(__name__)

# noqa: E501
events = [
    {
        'name': 'Interest Meeting 01',
        'description': 'Join us for our upcoming interest meetings! The Computer Science Club is excited to announce that we will be hosting multiple meetings each week, each with a different focus. We want to find the best times for our potential members, so we\'re offering several options. Come and learn more about what our club has to offer and how you can get involved. We hope to see you there!',
        'startDate': '2023-08-28 19:00',
        'endDate': '2023-08-28 20:00',
        'location': 'E281',
    },
    {
        'name': 'Interest Meeting 02',
        'description': 'Join us for our upcoming interest meetings! The Computer Science Club is excited to announce that we will be hosting multiple meetings each week, each with a different focus. We want to find the best times for our potential members, so we\'re offering several options. Come and learn more about what our club has to offer and how you can get involved. We hope to see you there!',
        'startDate': '2023-08-29 19:00',
        'endDate': '2023-08-29 20:00',
        'location': 'E281',
    },
    {
        'name': 'Interest Meeting 03',
        'description': 'Join us for our upcoming interest meetings! The Computer Science Club is excited to announce that we will be hosting multiple meetings each week, each with a different focus. We want to find the best times for our potential members, so we\'re offering several options. Come and learn more about what our club has to offer and how you can get involved. We hope to see you there!',
        'startDate': '2023-08-30 19:00',
        'endDate': '2023-08-30 20:00',
        'location': 'E281',
    },
    {
        'name': 'Interest Meeting 04',
        'description': 'Join us for our upcoming interest meetings! The Computer Science Club is excited to announce that we will be hosting multiple meetings each week, each with a different focus. We want to find the best times for our potential members, so we\'re offering several options. Come and learn more about what our club has to offer and how you can get involved. We hope to see you there!',
        'startDate': '2023-08-31 19:00',
        'endDate': '2023-08-31 20:00',
        'location': 'E281',
    },
    {
        'name': 'First Official Club Meeting',
        'description': 'Join us for our upcoming meeting! The Computer Science Club is excited to kick off the year with our first meeting of the 2023/2024 academic year. At this meeting, we will guide you through setting up the CS Club website on your local machine. We hope to see you there!',
        'startDate': '2023-09-05 19:00',
        'endDate': '2023-09-05 20:00',
        'location': 'E281',
    },
    {
        'name': 'Git & GitHub Workshop',
        'description': 'Join us for our upcoming workshop! Learn the basics of contributing to Git repositories hosted on GitHub. A functional understanding of Git and GitHub will be extremely important for your future projects and career. We hope to see you there!',
        'startDate': '2023-09-07 19:00',
        'endDate': '2023-09-07 20:00',
        'location': 'E281',
    },
]

# define a route like so:
# @app.route(PATH HERE)
# Right below the route, define a function that returns a message
@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)
