
import torch
from torchvision import transforms
from torchvision.models import VGG19_BN_Weights, vgg19_bn

model =torch.load('assets/skin.pth')
#print(torch.load('assets/weights.pth'))
# model=vgg19_bn()
# print(torch.load('assets/model.pth'))
# model.load_state_dict(torch.load('assets/skin_cancer.pth'))
# print(model)
# torch.save(model.state_dict(), 'assets/skin_cancer.pth')
skin_map={0:'Добро',1:'Зло'}
def get_evil(img):
    
    transform = transforms.Compose([
            transforms.Resize((224, 224)),  # Размер, ожидаемый VGG19_bn
            transforms.ToTensor(),
        ])
    
    input_image = transform(img).unsqueeze(0) # Добавьте размерность пакета (batch dimension)
    
    device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')
    model.to(device)
    model.eval()
    input_image = input_image.to(device)
    #model.to(device)
    with torch.no_grad():
        res=model(input_image).item()
    return f'Степень злобы: {res}\n\n Т.е. опухоль: {skin_map[round(res)]}'