from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Customer
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os
import base64
# sales_prediction/views.py
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import io
import base64
import nltk
import nltk
nltk.download('averaged_perceptron_tagger')
import random
from django.http import JsonResponse
import razorpay
from django.conf import settings

from nltk.tokenize import word_tokenize
from django.shortcuts import render
from django.http import JsonResponse
import cv2
from pyzbar.pyzbar import decode
import time

def scan_barcode(request):
    print('Initialising Camera')
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Camera Feed', cv2.WINDOW_NORMAL)
    start_time = time.time()
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Camera Feed', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            decoded_objects = decode(gray)
            if decoded_objects:
                barcode_data = decoded_objects[0].data.decode('utf-8')
                cv2.destroyAllWindows()
                cap.release()  # Release the camera
                return barcode_data
        if time.time() - start_time > timeout:
            print('Timeout: Unable to read barcode')
            cv2.destroyAllWindows()
            cap.release()  # Release the camera
            return None


def start_scan(request):
    barcode_data = scan_barcode(request)
    if barcode_data:
        return JsonResponse({'barcode': barcode_data})
    else:
        return JsonResponse({'error': 'Barcode not found within timeout period'})


# Download NLTK resources (run once)
nltk.download('punkt')
def suggest_order(request):
    if request.method == 'POST':
        user_mood = request.POST.get('mood')
        suggested_order = process_mood(user_mood)
        return JsonResponse({'suggested_order': suggested_order})
    return render(request, 'chatbot.html')

def process_mood(mood):
    tokens = word_tokenize(mood)
    emotions = nltk.pos_tag(tokens)

    # Happy mood
    happy_words = ["happy", "joy", "excited", "content", "pleased",
                "delighted", "elated", "jubilant", "thrilled", "ecstatic",
                "radiant", "cheerful", "exuberant", "blissful", "satisfied"]

    # Sad mood
    sad_words = ["sad", "depressed", "gloomy", "miserable", "despondent",
                "sorrowful", "melancholy", "despairing", "woeful", "dismal",
                "downcast", "heartbroken", "dejected"]

    # Upset mood
    upset_words = ['unhappy', 'upset', 'distressed', 'disheartened', 'agitated',
                'disturbed', 'perturbed', 'discontent', 'frustrated', 'irritated',
                'annoyed', 'dismayed']

    # Relaxed mood
    relaxed_words = ["calm", "serene", "peaceful", "tranquil", "soothing",
                    "unwind", "laid-back", "easygoing", "placid", "mellow"]

    # Energetic mood
    energetic_words = ["dynamic", "vibrant", "enthusiastic", "lively", "spirited",
                    "animated", "zealous", "buoyant", "bubbly", "high-spirited"]

    # Anxious mood
    anxious_words = ["worried", "nervous", "tense", "apprehensive", "uneasy",
                    "agitated", "restless", "jittery", "panicked", "distressed"]

    # Optimistic mood
    optimistic_words = ["hopeful", "positive", "confident", "upbeat", "expectant",
                        "bright", "cheery", "sunny", "encouraged", "buoyant"]

    # Pensive mood
    pensive_words = ["thoughtful", "reflective", "contemplative", "meditative",
                    "introspective", "brooding", "philosophical", "dreamy",
                    "wistful", "absorbed"]

    # Festive mood
    festive_words = ["celebratory", "festive", "merry", "jovial", "festive",
                    "joyful", "gleeful", "reveling", "festal", "rejoicing"]

    # Grateful mood
    grateful_words = ["thankful", "appreciative", "grateful", "acknowledging",
                    "indebted", "recognizing", "gracious", "obliged", "beholden",
                    "graceful"]

    # Creative mood
    creative_words = ["imaginative", "creative", "inspired", "innovative", "artistic",
                    "visionary", "inventive", "expressive", "imagery", "resourceful"]


    happy_food_items = ["pizza", "burger", "frankie", "hotdog", "manchurian", "cutlet", "pakoda", "spring roll", "dabeli", "sev puri", "chapati", "chole bhature", "biryani", "aubergine dish", "fried rice", "noodles", "burger", "hotdogs", "spring rolls", "biryani", "gravy", "fried rice", "noodles"]
    sad_food_items = ["soup", "salad", "smoothie", "cold coffee", "mixed fruit juice", "coffee", "tea", "frooti", "slice", "milkshake"]
    upset_food_items = ['smoothie','coffee','frooti','milkshake']
    # Relaxed mood food items
    relaxed_food_items = ["pizza", "burger", "frankie", "hotdog", "manchurian", "cutlet",
                        "pakoda", "spring roll", "dabeli", "sev puri", "chapati",
                        "chole bhature", "biryani", "aubergine dish", "fried rice",
                        "noodles", "gravy"]

    # Energetic mood food items
    energetic_food_items = ["pizza", "burger", "frankie", "hotdog", "manchurian", "cutlet",
                            "pakoda", "spring roll", "dabeli", "sev puri", "chapati",
                            "chole bhature", "biryani", "aubergine dish", "fried rice",
                            "noodles", "gravy"]

    # Anxious mood food items
    anxious_food_items = ["soup", "salad", "smoothie", "cold coffee", "mixed fruit juice",
                        "coffee", "tea", "frooti", "slice", "milkshake"]

    # Optimistic mood food items
    optimistic_food_items = ["soup", "salad", "smoothie", "cold coffee", "mixed fruit juice",
                            "coffee", "tea", "frooti", "slice", "milkshake"]

    # Pensive mood food items
    pensive_food_items = ["soup", "salad", "smoothie", "cold coffee", "mixed fruit juice",
                        "coffee", "tea", "frooti", "slice", "milkshake"]

    # Festive mood food items
    festive_food_items = ["pizza", "burger", "frankie", "hotdog", "manchurian", "cutlet",
                        "pakoda", "spring roll", "dabeli", "sev puri", "chapati",
                        "chole bhature", "biryani", "aubergine dish", "fried rice",
                        "noodles", "gravy"]

    # Grateful mood food items
    grateful_food_items = ["soup", "salad", "smoothie", "cold coffee", "mixed fruit juice",
                        "coffee", "tea", "frooti", "slice", "milkshake"]

    # Creative mood food items
    creative_food_items = ["soup", "salad", "smoothie", "cold coffee", "mixed fruit juice",
                        "coffee", "tea", "frooti", "slice", "milkshake"]

    veg = ["pizza", "burger", "frankie", "hotdog", "manchurian", "cutlet", "pakoda", "spring roll", "dabeli", "sev puri", "chapati", "chole bhature"]
    nonveg = ["biryani", "gravy", "fried rice", "noodles",'Chicken Curry','Egg masala']
    beverages = ['smoothie','coffee','frooti','milkshake',"cold coffee", "mixed fruit juice","tea",]
    for word, tag in emotions:
        if word.lower() in happy_words:
            ch = random.choice(happy_food_items)
            if ch in beverages:    
                suggested_order = "Since you're feeling "+word+", how about trying " + ch + ",? \n\n You may find it under the Beverages Section."
                return suggested_order
            elif ch in veg:    
                suggested_order = "Since you're feeling "+word+", how about trying " + ch + ",? \n\n You may find it under the Veg Section."
                return suggested_order
            elif ch in nonveg:    
                suggested_order = "Since you're feeling "+word+", how about trying " + ch + ",? \n\n You may find it under the Non Veg Section."
                return suggested_order
            
        elif word.lower() in sad_words:
            ch = random.choice(sad_food_items)
            if ch in beverages:    
                suggested_order = "If you're feeling "+word+", maybe " + ch + ", could lift your spirits. \n\n You may find it under the Beverages Section."
                return suggested_order
            elif ch in veg:
                suggested_order = "If you're feeling "+word+", maybe " + ch + ", could lift your spirits. \n\n You may find it under the Veg Section."
                return suggested_order
            elif ch in nonveg:
                suggested_order = "If you're feeling "+word+", maybe " + ch + ", could lift your spirits. \n\n You may find it under the Non Veg Section."
                return suggested_order
            
        elif word.lower() in upset_words:
            ch = random.choice(upset_food_items)
            if ch in beverages:    
                suggested_order = "Hmm, Since you're feeling "+word+", how about a " + ch + ", could help you cheerup a bit. \n\n You may find it under the Beverages Section."
                return suggested_order
            elif ch in veg:    
                suggested_order = "Hmm, Since you're feeling "+word+", how about a " + ch + ", could help you cheerup a bit. \n\n You may find it under the Veg Section."
                return suggested_order
            elif ch in nonveg:    
                suggested_order = "Hmm, Since you're feeling "+word+", how about a " + ch + ", could help you cheerup a bit. \n\n You may find it under the Non Veg Section."
                return suggested_order
            
        elif word.lower() in relaxed_words:
            ch = random.choice(relaxed_food_items)
            if ch in beverages:
                suggested_order = "Feeling relaxed? How about enjoying " + ch + ",? \n\n You may find it under the Beverages Section."
                return suggested_order
            elif ch in veg:
                suggested_order = "Feeling relaxed? How about enjoying " + ch + ",? \n\n You may find it under the Veg Section."
                return suggested_order
            elif ch in nonveg:
                suggested_order = "Feeling relaxed? How about enjoying " + ch + ",? \n\n You may find it under the Non Veg Section."
                return suggested_order
            
        elif word.lower() in energetic_words:
            ch = random.choice(energetic_food_items)
            if ch in beverages:
                suggested_order = "Feeling energetic? How about grabbing " + ch + ",? \n\n You may find it under the Beverages Section."
                return suggested_order
            elif ch in veg:
                suggested_order = "Feeling energetic? How about grabbing " + ch + ",? \n\n You may find it under the Veg Section."
                return suggested_order
            elif ch in nonveg:
                suggested_order = "Feeling energetic? How about grabbing " + ch + ",? \n\n You may find it under the Non Veg Section."
                return suggested_order
            
        elif word.lower() in anxious_words:
            ch = random.choice(anxious_food_items)
            if ch in beverages:
                suggested_order = "Feeling anxious? Maybe " + ch + ", could help calm your nerves. \n\n You may find it under the Beverages Section."
                return suggested_order
            elif ch in veg:
                suggested_order = "Feeling anxious? Maybe " + ch + ", could help calm your nerves. \n\n You may find it under the Veg Section."
                return suggested_order
            elif ch in nonveg:
                suggested_order = "Feeling anxious? Maybe " + ch + ", could help calm your nerves. \n\n You may find it under the Non Veg Section."
                return suggested_order
            
        elif word.lower() in optimistic_words:
            ch = random.choice(optimistic_food_items)
            if ch in beverages:
                suggested_order = "Feeling optimistic? How about indulging in " + ch + ",? \n\n You may find it under the Beverages Section."
                return suggested_order
            elif ch in veg:
                suggested_order = "Feeling optimistic? How about indulging in " + ch + ",? \n\n You may find it under the Veg Section."
                return suggested_order
            elif ch in nonveg:
                suggested_order = "Feeling optimistic? How about indulging in " + ch + ",? \n\n You may find it under the Non Veg Section."
                return suggested_order
            

    suggested_order = "Sorry, I couldn't understand your mood. Can you please specify if you're feeling happy or sad?"
    return suggested_order

def sales_prediction_view(request):
    # Read DataFrame from CSV file
    # df = pd.read_csv(r'../canteen/static/MP_B15_train_data - Sheet1.csv') # Replace 'your_dataset.csv' with your actual file path
    file_path = os.path.join(settings.BASE_DIR, 'canteen', 'static', 'MP_B15_train_data - Sheet1.csv')
    
    # Read DataFrame
    df = pd.read_csv(file_path)
    # One-hot encoding categorical variables
    df_encoded = pd.get_dummies(df, columns=['time_of_day', 'day_of_week', 'weather', 'food_item'])

    # Features for prediction
    features = ['time_of_day_morning', 'time_of_day_afternoon', 'time_of_day_evening', 
                'day_of_week_Monday', 'day_of_week_Tuesday', 'day_of_week_Wednesday',
                'weather_cloudy', 'weather_rainy', 'weather_sunny',
                'special_event'] + [col for col in df_encoded.columns if col.startswith('food_item_')]

    # Feature Engineering
    df_encoded['time_weather_interaction'] = df_encoded['time_of_day_evening'] * df_encoded['weather_sunny']
    additional_features = ['time_weather_interaction']
    features_updated = features + additional_features

    # Creating and fitting the linear regression model with updated features
    X_updated = df_encoded[features_updated]
    y = df_encoded['demand']
    model_updated = LinearRegression()
    model_updated.fit(X_updated, y)

    # Fetching current time of day
    current_time = pd.Timestamp.now().hour
    if current_time < 12:
        time_of_day = 'morning'
    elif current_time < 17:
        time_of_day = 'afternoon'
    elif current_time < 21:
        time_of_day = 'evening'
    else:
        time_of_day = 'night'

    # Fetching current day of the week
    current_day = pd.Timestamp.now().day_name()

    #
    weather="cloudy"
    # Assume no special event for simplicity
    special_event = 0

    # Create input features dictionary
    input_features = {
        'time_of_day_' + time_of_day: 1,
        'day_of_week_' + current_day: 1,
        'weather_condition_' + weather: 1,
        'special_event': special_event
    }

    # Predict demand for each food item using the updated model
    predicted_demand_updated = {}
    for food_item in df['food_item'].unique():
        food_item_features = input_features.copy()
        food_item_features['food_item_' + food_item] = 1

        # Create DataFrame with input features for the food item
        input_df = pd.DataFrame([food_item_features], columns=features_updated).fillna(0)

        # Predict demand for the food item using the updated model
        predicted_demand_updated[food_item] = model_updated.predict(input_df)[0]

    # Plotting predicted demand for the top 5 selling items using the updated model
    plt.figure(figsize=(10, 6))
    plt.bar(predicted_demand_updated.keys(), predicted_demand_updated.values(), color='skyblue')
    plt.xlabel('Food Item')
    plt.ylabel('Predicted Demand')
    plt.title('Predicted Demand for Top Selling Items (Updated Model)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Save plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data_uri = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    # Render the template with the plot
    return render(request, 'Home.html', {'plot_data_uri': plot_data_uri})


# def home(request):
#   template = loader.get_template('home.html')
#   return HttpResponse(template.render())


def login(request):
    if request.method == 'POST':
        pid = request.POST.get('email')  # Assuming PID is entered in the 'email' field
        password = request.POST.get('password')
        print("PID:", pid)
        print("Password:", password)

        # Check if a user with the given PID exists in the database
        try:
            user = Customer.objects.get(pid=pid)
            # If a user is found, check if the password matches
            if user.password == password:
                # Authentication successful
                # return JsonResponse({'success': True, 'message': 'Login Successful'})
                return JsonResponse({'success': True, 'username': user.username, 'pid': user.pid, 'message': 'Login Successful'})
            else:
                # Password doesn't match
                return JsonResponse({'success': False, 'message': 'Invalid Credentials'})
        except Customer.DoesNotExist:
            # User with the given PID doesn't exist
            return JsonResponse({'success': False, 'message': 'Invalid Credentials'})
    else:
        return render(request, 'login.html')
    
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('rusername')
#         pid = request.POST.get('remail')
#         password = request.POST.get('rpassword')
#         print("Username:", username)
#         print("PID:", pid)
#         print("Password:", password)
#         # Create and save the user object
#         user = Customer(pid=pid, username=username, password=password)
#         user.save()

#         # Return a JsonResponse indicating success
#         return JsonResponse({'message': 'User registered successfully'})
#     else:
#         return render(request, 'login.html')
from django.shortcuts import render
from django.http import JsonResponse
from .models import Customer

def register(request):
    if request.method == 'POST':
        username = request.POST.get('rusername')
        pid = request.POST.get('remail')
        password = request.POST.get('rpassword')
        print("Username:", username)
        print("PID:", pid)
        print("Password:", password)
        
        # Check if user with provided PID already exists
        if Customer.objects.filter(pid=pid).exists():
            return JsonResponse({'success': False, 'message': 'User already exists. Kindly login.'})
        
        # Create and save the user object
        user = Customer.objects.create(pid=pid, username=username, password=password)
        return JsonResponse({'success': True, 'message': 'User registered successfully'})
    else:
        return render(request, 'login.html')

def Veg(request):
  template = loader.get_template('c1.html')
  return HttpResponse(template.render())

def NVeg(request):
  template = loader.get_template('c2.html')
  return HttpResponse(template.render())

def Wallet(request):
  template = loader.get_template('Wallet.html')
  return HttpResponse(template.render())



def Beverage(request):
  template = loader.get_template('c3.html')
  return HttpResponse(template.render())


from django.http import JsonResponse
import cv2
from pyzbar.pyzbar import decode
import time

def scan_barcode(request):
    if request.method == 'POST':
        def scan_barcode(timeout=30):
            # Barcode scanning logic
            # ...
            pass

        barcode_data = scan_barcode(timeout=30)
        if barcode_data:
            return JsonResponse({'barcode': barcode_data})
        else:
            return JsonResponse({'error': 'Barcode not found within timeout period'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)



from django.http import JsonResponse
from .models import CartItem
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def addtocart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # id = data['id']
        userid = data['userid']
        category = data['shopName']
        itemName = data['itemName']
        Image = data['Image']
        price = data['price']
        
        # print('views was called')
        
        # Save data to the database
        cart_item = CartItem.objects.create(
            # id=id,
            userid=userid,
            category=category,
            Itemname=itemName,
            image=Image,
            price=price

        )
        
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


def get_cart_items(request):
    pid = request.GET.get('pid')
    # Retrieve cart items based on the provided PID
    cart_items = CartItem.objects.filter(userid=pid).values()
    return JsonResponse(list(cart_items), safe=False)

@csrf_exempt
def delete_cart_item(request, pid, item_name):
    if request.method == 'DELETE':
        try:
            # Search for the cart item based on PID and item name
            cart_item = CartItem.objects.get(userid=pid, Itemname=item_name)
            cart_item.delete()
            return JsonResponse({'success': True})
        except CartItem.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'Cart item does not exist'}, status=404)
        except Exception as e:
                print(e)  # Log the error message
                return JsonResponse({'success': False, 'message': 'Internal Server Error'}, status=500)
    else:
        return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)
    

from backend.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY

# def checkout(request):
#     template = loader.get_template('checkout.html')
#     # return HttpResponse(template.render())
#     client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

#     DATA = {
#         "amount": 850,
#         "currency": "INR",
#         "payment_capture":"1",
#     }
#     payment_order = client.order.create(data=DATA)
#     payment_order_id = payment_order['id']
#     context = {
#         'api_key':RAZORPAY_API_KEY, 'order_id': payment_order_id,
#     }
#     return render(request, 'checkout.html', context)


import razorpay
from django.shortcuts import render
from .models import Customer

from backend.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY

def checkout(request):
    template = loader.get_template('checkout.html')
    return HttpResponse(template.render())

from django.http import JsonResponse

from django.http import JsonResponse
import json

def process_payment(request):
    client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

    # Extract the amount from the request body
    data = json.loads(request.body)
    amount = data.get('amount')

    # Validate the amount (you may need to add additional validation logic here
    if not amount:
        return JsonResponse({'error': 'Amount is required'}, status=400)

    # Convert the amount to the required format (assuming it's in paisa)
    amount_in_paisa = int(amount) * 100  # Assuming the amount is in rupees, convert it to paisa

    # Create the payment order with the extracted amount
    DATA = {
        "amount": amount_in_paisa,
        "currency": "INR",
        "payment_capture": "1",
    }
    payment_order = client.order.create(data=DATA)
    payment_order_id = payment_order['id']

    # Return the required data as a JSON response
    return JsonResponse({
        'api_key': RAZORPAY_API_KEY,
        'order_id': payment_order_id,
        'success': True,
    })




from django.http import JsonResponse
from .models import CartItem  # Import your CartItem model
from django.core.exceptions import ObjectDoesNotExist
def delete_cart_aftersuccess(request):
    if request.method == 'POST':
        try:
            # Assuming 'pid' is passed in the POST request body
            data = json.loads(request.body.decode('utf-8'))
            pid = data.get('upid')

            # Filter CartItem objects by pid and delete them
            try:
                cart_item = CartItem.objects.get(userid=pid)
            except ObjectDoesNotExist:
                # If no CartItem object is found, return a JsonResponse indicating the error
                return JsonResponse({'error': 'CartItem with the given pid does not exist'}, status=404)

            # If CartItem object exists, delete it
            cart_item.delete()
            
            return JsonResponse({'success': True})
        except Exception as e:
            print("Error:", e)
            return JsonResponse({'error': str(e)}, status=500)
    else:
        # If request method is not POST, return method not allowed
        return JsonResponse({'error': 'Method not allowed'}, status=405)








    