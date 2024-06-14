import os
# import firebase_admin
# from firebase_admin import firestore, credentials
from django.shortcuts import render
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# def initialize_firebase():
#     """
#     Initializes the Firebase Admin app using the service account key path from the environment variable.
#     """
#     service_account_key_path = os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY")
#     if not service_account_key_path:
#         raise ValueError("Missing environment variable: FIREBASE_SERVICE_ACCOUNT_KEY")
#     cred = credentials.Certificate(service_account_key_path)
#     firebase_admin.initialize_app(cred)

# # Call the initialization function outside the view
# initialize_firebase()

def data(request):
    return render(request,'pages/home.html')
    # try:
    #     db = firestore.client()
    #     users_ref = db.collection('sensordata')
    #     docs = users_ref.limit(1000).get()  # Limit to 1000 entries

    #     data = {}  # Initialize an empty dictionary to hold the data
    #     for doc in docs:
    #         data[doc.id] = doc.to_dict()

    #     return render(request, 'pages/data.html', {'data': data})  # Pass data to the template
    # except firestore.exceptions.NotFound:
    #     return render(request, 'pages/error.html', context={'message': "No data found at the specified path."})
    # except Exception as e:
    #     # Handle exceptions appropriately
    #     return render(request, 'pages/error.html', context={'message': f"An error occurred: {e}"})


def home(request):
    return render(request, 'pages/home.html')
