#Import necessary libraries
from flask import Flask, render_template, request

import numpy as np
import os

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = 'model.h5'

model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

def pred_tomato_dieas(tomato_plant):
  test_image = load_img(tomato_plant, target_size = (128, 128)) # load image 
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
  result = model.predict(test_image) # predict diseased palnt or not
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result, axis=1)
  print(pred)
  #if pred==0:
     # return "corn-healthy",'corn-healthy.html'
  if pred==0:
      return "Cherry - Powdery Mildew", 'Cherry - Powdery_mildew.html'
  elif pred==1:
      return "Cherry - Healthy", 'Cherry - Healthy.html'
  elif pred==2:
      return "Corn - Ceracospora left spot", 'Corn - Ceracospora_left_spot.html'
  elif pred==3:
      return "Corn - Common rust", 'Corn - Common_rust.html'
  elif pred==4:
      return "Corn - Healthy", 'Corn - Healthy.html'
  elif pred==5:
      return "Grape - Black rot", 'Grape - Black_rot.html'
  elif pred==6:
      return "Grape - Esca(Black Measles)", 'Grape - Esca.html'
  elif pred==7:
      return "Grape - Leaf_Blight", 'Grape - Leaf_Blight.html'
  elif pred==8:
      return "Grape - Healthy", 'Grape - Healthy.html'
  elif pred==9:
      return "Pepperbell - Baterial spot", 'Pepperbell - Baterial_spot.html'
  elif pred==10:
      return "Pepperbell - healthy", 'Pepperbell - healthy.html'
  elif pred==11:
      return "Potato - Early blight", 'Potato - Early_blight.html'
  elif pred==12:
      return "Potato - Late_blight", 'Potato - Late_blight.html'
  elif pred==13:
      return "Potato  - Healthy", 'Potato  - Healthy.html'
  
  elif pred==14:
      return "Tomato - Bacteria Spot Disease", 'Tomato-Bacteria Spot.html'
       
  elif pred==15:
      return "Tomato - Early Blight Disease", 'Tomato-Early_Blight.html'
        
  elif pred==16:
      return "Tomato - Healthy and Fresh", 'Tomato-Healthy.html'
        
  elif pred==17:
      return "Tomato - Late Blight Disease", 'Tomato - Late_blight.html'
       
  elif pred==18:
      return "Tomato - Leaf Mold Disease", 'Tomato - Leaf_Mold.html'
        
  elif pred==19:
      return "Tomato - Septoria Leaf Spot Disease", 'Tomato - Septoria_leaf_spot.html'
        
  elif pred==20:
      return "Tomato - Target Spot Disease", 'Tomato - Target_Spot.html'
        
  elif pred==21:
      return "Tomato - Tomato Yellow Leaf Curl Virus Disease", 'Tomato - Tomato_Yellow_Leaf_Curl_Virus.html'
      
  elif pred==22:
      return "Tomato - Tomato Mosaic Virus Disease", 'Tomato - Tomato_mosaic_virus.html'
    
  elif pred==23:
      return "Tomato - Two Spotted Spider Mite Disease", 'Tomato - Two-spotted_spider_mite.html'

    

# Create flask instance
app = Flask(__name__)

# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')
    
 
# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/upload',filename)
            
        
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = pred_tomato_dieas(tomato_plant=file_path)
              
        return render_template(output_page, pred_output = pred, user_image = file_path)
    
# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False,port=8080) 
    
    
