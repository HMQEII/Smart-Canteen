# import cv2
# from pyzbar.pyzbar import decode
# import time

# def scan_barcode(timeout=30):
#     print('Initialising Camera')
#     cap = cv2.VideoCapture(0)
#     cv2.namedWindow('Camera Feed', cv2.WINDOW_NORMAL)
#     start_time = time.time()
#     while True:
#         ret, frame = cap.read()
#         if ret:
#             cv2.imshow('Camera Feed', frame)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#             decoded_objects = decode(gray)
#             if decoded_objects:
#                 barcode_data = decoded_objects[0].data.decode('utf-8')
#                 cv2.destroyAllWindows()
#                 cap.release()  # Release the camera
#                 return barcode_data
#         if time.time() - start_time > timeout:
#             print('Timeout: Unable to read barcode')
#             cv2.destroyAllWindows()
#             cap.release()  # Release the camera
#             return None

# if __name__ == '__main__':
#     barcode_data = scan_barcode(timeout=30)  # Set timeout to 30 seconds
#     if barcode_data:
#         print('Barcode Data:', barcode_data)
#     else:
#         print('Barcode not found within timeout period')


from flask import Flask, render_template, jsonify
import cv2
from pyzbar.pyzbar import decode
import time

app = Flask(__name__)

def scan_barcode(timeout=30):
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

# @app.route('/')
# def index():
#     return render_template('try2.html')

@app.route('/scan_barcode')
def start_scan():
    barcode_data = scan_barcode(timeout=30)
    if barcode_data:
        return jsonify({'barcode': barcode_data})
    else:
        return jsonify({'error': 'Barcode not found within timeout period'})

if __name__ == '__main__':
    app.run(debug=True)



# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import cv2
# from pyzbar.pyzbar import decode
# import time

# @csrf_exempt  # Disable CSRF protection for this view
# def scan_barcode(request):
#     if request.method == 'POST':
#         def scan_barcode(timeout=30):
#             print('Initialising Camera')
#             cap = cv2.VideoCapture(0)
#             cv2.namedWindow('Camera Feed', cv2.WINDOW_NORMAL)
#             start_time = time.time()
#             while True:
#                 ret, frame = cap.read()
#                 if ret:
#                     cv2.imshow('Camera Feed', frame)
#                     if cv2.waitKey(1) & 0xFF == ord('q'):
#                         break
#                     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#                     decoded_objects = decode(gray)
#                     if decoded_objects:
#                         barcode_data = decoded_objects[0].data.decode('utf-8')
#                         cv2.destroyAllWindows()
#                         cap.release()  # Release the camera
#                         return barcode_data
#                 if time.time() - start_time > timeout:
#                     print('Timeout: Unable to read barcode')
#                     cv2.destroyAllWindows()
#                     cap.release()  # Release the camera
#                     return None

#         barcode_data = scan_barcode(timeout=30)
#         if barcode_data:
#             return JsonResponse({'barcode': barcode_data})
#         else:
#             return JsonResponse({'error': 'Barcode not found within timeout period'})
#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=405)


