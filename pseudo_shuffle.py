import numpy as np
import cv2


def cv_show(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def pseudo_shuffle(array, seed=0):
    """
    Pseudo shuffle array or image.
    :param array: array to be shuffled
    :param seed: seed for random number generator
    :return: shuffled array
    """
    # pseudo array initialization
    np.random.seed(seed)
    random_array = np.arange(array.shape[0] * array.shape[1])
    random_array = np.random.permutation(random_array)

    # initialize array to store shuffled values
    shuffle_array = np.zeros_like(array)

    # shuffle
    if array.ndim == 1:
        for i in range(len(array)):
            shuffle_array[i] = array[random_array[i] - 1]
    elif array.ndim >= 2:
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                shuffle_array[i, j] = array[random_array[i * array.shape[1] + j] // array.shape[1], random_array[i * array.shape[1] + j] % array.shape[1]]
    else:
        print('Invalid array dimension')

    return shuffle_array


def pseudo_sort(array, seed=0):
    """
    Pseudo sort array or image.
    :param array: pseudo shuffled array
    :param seed: seed for random number generator
    :return: sorted array
    """
    # pseudo array initialization
    np.random.seed(seed)
    random_array = np.arange(array.shape[0] * array.shape[1])
    random_array = np.random.permutation(random_array)

    # initialize array to store shuffled values
    sort_array = np.zeros_like(array)

    # shuffle
    if array.ndim == 1:
        for i in range(len(array)):
            sort_array[random_array[i]-1] = array[i]
    elif array.ndim >= 2:
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                sort_array[random_array[i * array.shape[1] + j] // array.shape[1], random_array[i * array.shape[1] + j] % array.shape[1]] = array[i, j]
    else:
        print('Invalid array dimension')

    return sort_array


def bytes_shuffle(data, seed=0):
    """
    Pseudo shuffle bytes.
    :param data: origin bytes to be shuffled
    :param seed: seed for random number generator
    :return: shuffled bytes
    """
    data_length = len(data)
    np.random.seed(seed)
    random_array = np.arange(data_length)
    random_array = np.random.permutation(random_array)

    shuffle_data = bytearray(data_length)
    for i in range(data_length):
        shuffle_data[i] = data[random_array[i]]
    return bytes(shuffle_data)


def bytes_sort(data, seed=0):
    """
    Pseudo sort bytes.
    :param data: pseudo shuffled bytes
    :param seed: seed for random number generator
    :return: origin bytes
    """
    data_length = len(data)
    np.random.seed(seed)
    random_array = np.arange(data_length)
    random_array = np.random.permutation(random_array)
    sort_data = bytearray(data_length)
    for i in range(data_length):
        sort_data[random_array[i]] = data[i]
    return bytes(sort_data)


def main():
    """Main function."""
    # test to shuffle image
    array = cv2.imread('lena.png')
    shuffle_array = pseudo_shuffle(array, seed=1)
    recover_array = pseudo_sort(shuffle_array, seed=1)
    cv_show(shuffle_array)
    cv_show(recover_array)

    # test to shuffle bytes
    with open('lena.png', 'rb') as f:
        data = f.read()
    shuffle_data = bytes_shuffle(data, seed=1)
    recover_data = bytes_sort(shuffle_data, seed=1)
    print(data == recover_data)


if __name__ == '__main__':
    main()
