# этот классификатор
# был изобретён дурачком
# взятый, буквально с боем
# но он работает
# но с костылём
# но работает
# перед работай убидитесь, что библиотеки установлены
# и данные лежат в нужных папках

import numpy as np
from keras.models import load_model
from keras.utils import load_img
from keras.utils import img_to_array


# загрузка обученой нейросети
loaded_model = load_model('saved_models/contour_dense.hdf5')

# компиляция нейросети
loaded_model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# записываем данные классов в подходящие переменные
class1 = 2
class2 = 1
class3 = 0

# преобразуем данные для элемента, который ходим классифицировать
img_path = 'images/output/elements0.jpg'
img = load_img(img_path, target_size=(150, 150))

y = img_to_array(img)
y = y/255
y = np.expand_dims(y, axis=0)

prediction = loaded_model.predict(y)

for value in range(len(prediction)):
    prediction = prediction[value]

prediction = np.argmax(prediction)

# классификация
if prediction == class1:
    print('окно')
else:
    if prediction == class2:
        print('стена')
    else:
        if prediction == class3:
            print('дверь')
        else:
            print('ошибка!')
