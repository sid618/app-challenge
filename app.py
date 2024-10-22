from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for leaderboard and events
leaderboard = [
    {"name": "Alice", "hours": 50},
    {"name": "Bob", "hours": 40},
    {"name": "Charlie", "hours": 30}
]

events = [
    {"name": "Park Cleanup", "date": "2024-10-30", "location": "Central Park"},
    {"name": "Food Drive", "date": "2024-11-12", "location": "Community Center"},
]

@app.route('/')
def home():
    return render_template('home.html', leaderboard=leaderboard, events=events)

@app.route('/get_started')
def get_started():
    return render_template('get_started.html')

@app.route('/tracking')
def tracking():
    user_events = events  # You can modify this to show events specific to users
    return render_template('tracking.html', user_events=user_events)

@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')

@app.route('/fundraising')
def fundraising():
    campaigns = [
        {"name": "School Supplies for Kids", "amount": 2000, "goal": 5000},
        {"name": "Clean Water Initiative", "amount": 1500, "goal": 3000}
    ]
    return render_template('fundraising.html', campaigns=campaigns)

if __name__ == '__main__':
    app.run(debug=True)
