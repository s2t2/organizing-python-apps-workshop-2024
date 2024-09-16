from flask import Flask, render_template_string, request

from app.rps import determine_outcome, generate_computer_choice


app = Flask(__name__)


@app.route('/')
def home():
    # NOTE: we would usually have this template in its own .html file
    # ... but it is included as an HTML string here for simplicity
    home_template = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Rock-Paper-Scissors</title>
        </head>
        <body>
            <h1>Rock-Paper-Scissors Game</h1>

            <form action="/determine_winner" method="POST">
                <label for="user_choice">Choose your move:</label>
                <select name="user_choice" id="user_choice">
                    <option value="rock">Rock</option>
                    <option value="paper">Paper</option>
                    <option value="scissors">Scissors</option>
                </select>

                <button type="submit">Submit</button>
            </form>
        </body>
    </html>
    """
    return render_template_string(home_template)


@app.route('/determine_winner', methods=['POST'])
def determine_winner():
    # Get the user's choice from the form data
    user_choice = request.form.get('user_choice')

    computer_choice = generate_computer_choice()

    outcome = determine_outcome(user_choice, computer_choice)

    # NOTE: we would usually have this template in its own .html file
    # ... but it is included as an HTML string here for simplicity
    # NOTE: the curly braces are jinja syntax (not a format string)
    # ... they use whatever variables are passed via the render_template function
    result_template = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Game Result</title>
        </head>
        <body>
            <h1>Game Result</h1>
            <p><b>User</b>: {{ user_choice.upper() }}</p>
            <p><b>Computer</b>: {{ computer_choice.upper() }}</p>
            <p><b>Outcome</b>: {{ outcome.upper() }}</p>

            <a href="/">Play again</a>
        </body>
    </html>
    """
    return render_template_string(result_template,
        user_choice=user_choice,
        computer_choice=computer_choice,
        outcome=outcome
    )


if __name__ == '__main__':

    app.run(debug=True)
