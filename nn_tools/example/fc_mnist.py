import torch as t
import torch.nn as nn
import torch.functional as F
import torchvision.datasets
import torch.utils.data.dataloader
import torchvision.transforms as transforms


class My_fc(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = t.nn.Sequential(t.nn.Linear(784, 500), t.nn.LeakyReLU())
        self.fc2 = t.nn.Sequential(t.nn.Linear(500, 200), t.nn.LeakyReLU())
        self.fc3 = t.nn.Sequential(t.nn.Linear(200, 50), t.nn.LeakyReLU())
        self.fc4 = t.nn.Linear(50, 10)

    def forward(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        x = self.fc4(x)
        return x


if __name__ == "__main__":
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    learning_rate = 0.001

    train_dataset = torchvision.datasets.MNIST("./",
                                               train=True,
                                               transform=transforms.ToTensor(),
                                               download=True)
    test_dataset = torchvision.datasets.MNIST("./",
                                              train=False,
                                              transform=transforms.ToTensor())
    image, label = train_dataset[0]
    print(image.size)
    print(label)
    train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                               batch_size=8,
                                               shuffle=True)
    test_loader = torch.utils.data.DataLoader(dataset=test_dataset)
    model = My_fc().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    total_step = len(train_loader)
    print(total_step)
    for i, [images, labels] in enumerate(train_loader):
        images = images.view(-1, 28 * 28).to(device)
        labels = labels.to(device)
        outputs = model(images)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if (i + 1) % 100 == 0:
            print('Step [{}/{}], Loss: {:.4f}'
                  .format(i + 1, total_step, loss.item()))

    with torch.no_grad():
        correct = 0
        total = 0
        for images, labels in test_loader:
            images = images.view(-1, 28 * 28).to(device)
            labels = labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        print('Accuracy of the network on the 10000 test images: {} %'.format(100 * correct / total))
