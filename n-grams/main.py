from dataset_parser import remove_punctuation

if __name__ == '__main__':
    sentence = 'esse é um texto escrito em português. será que é possível remover a pontuacão dessa sentença?'
    result = remove_punctuation(sentence)
    print(result)

