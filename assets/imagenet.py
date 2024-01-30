import torch
from torchvision import transforms

import json
#import matplotlib.pyplot as plt

from torchvision.models import inception_v3,Inception_V3_Weights
model = inception_v3(weights=Inception_V3_Weights.DEFAULT)


with open('assets/imagenet_classes.json', 'r') as f:
    class_labels = json.load(f)
class_labels=[value for _,value in class_labels.items()]
def img_class(img):
    transform = transforms.Compose([
        transforms.Resize((299, 299)),  # Размер, ожидаемый Inception_v3
        transforms.ToTensor(),
    ])
    
    input_image = transform(img).unsqueeze(0) # Добавьте размерность пакета (batch dimension)
    
    device = torch.device("cuda" if torch.cuda.is_available() else 'mps')
    model.to(device)
    model.eval()
    input_image = input_image.to(device)
    with torch.no_grad():
        output = model(input_image)
    return class_labels[torch.argmax(output).item()]
