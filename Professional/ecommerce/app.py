from flask import Flask, render_template, request
import stripe

app = Flask(__name__)

# Set your Stripe API keys
stripe.api_key = 'YOUR_STRIPE_SECRET_KEY'
stripe.publishable_key = 'YOUR_STRIPE_PUBLISHABLE_KEY'

@app.route('/')
def index():
    return render_template('payment_form.html', key=stripe.publishable_key)

@app.route('/charge', methods=['POST'])
def charge():
    # Get the payment details from the form
    amount = request.form['amount']
    token = request.form['stripeToken']

    try:
        # Create a charge using the Stripe API
        charge = stripe.Charge.create(
            amount=int(amount),
            currency='usd',
            source=token
        )

        # If the charge is successful, display a success message
        return render_template('success.html', amount=amount)
    except stripe.error.CardError as e:
        # If there's an error with the payment, display an error message
        return render_template('error.html', error_message=e.user_message)
