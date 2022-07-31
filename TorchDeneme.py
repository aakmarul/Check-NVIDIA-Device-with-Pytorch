import torch 

print ("Hello Ubuntu, i'm working!")

print ("IS Torch Cuda is available ? \n", torch.cuda.is_available())

print ("Device Count :", torch.cuda.device_count())

print ("Device name is :", torch.cuda.get_device_name(torch.cuda.current_device()))


